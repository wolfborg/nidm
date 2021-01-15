import os
import codecs
import collections
import sys
import glob
from nidmresults.owl.owl_reader import OwlReader
from nidmresults.objects.constants_rdflib import *
import markdown2
import shlex

RELPATH = os.path.dirname(os.path.abspath(__file__))

#NIDM_ROOT = os.path.dirname(RELPATH)
NIDM_ROOT = RELPATH
DOC_FOLDER = os.path.join(NIDM_ROOT, 'docs')
INCLUDE_FOLDER = os.path.join(DOC_FOLDER, "include")

#NIDM_EXPE_PATH = os.path.dirname(RELPATH)
NIDM_EXPE_PATH = RELPATH
TERMS_FOLDER = os.path.join(NIDM_EXPE_PATH, 'terms')
RELEASED_TERMS_FOLDER = os.path.join(TERMS_FOLDER, "releases")

class OwlNidmHtml:
    def __init__(self, owl_file, import_files, spec_name, subcomponents=None,
                 used_by=None, generated_by=None, derived_from=None,
                 attributed_to=None, prefix=None, commentable=False,
                 intro=None):
        self.owl = OwlReader(owl_file, import_files)
        self.owl.graph.bind('dct', 'http://purl.org/dc/terms/')
        self.owl.graph.bind('dicom', 'http://purl.org/nidash/dicom#')
        self.owl.graph.bind('nidm', 'http://purl.org/nidash/nidm#')
        self.owl.graph.bind('bids', 'http://purl.org/nidash/bids#')
        self.owl.graph.bind('onli', 'http://neurolog.unice.fr/ontoneurolog/v3.0/instrument.owl#')
        self.owl.graph.bind('pato', 'http://purl.obolibrary.org/obo/pato#')
        self.owl.graph.bind('prov', 'http://www.w3.org/ns/prov')
        self.owl.graph.bind('qibo', 'http://www.owl-ontologies.com/Ontology1298855822.owl')
        self.owl.graph.bind('sio', 'http://semanticscience.org/resource/')
        self.name = spec_name
        self.component = self.name.lower().replace("-", "_")
        self.section_open = 0
        self.already_defined_classes = list()
        self.commentable = commentable

        self.attributes_done = set()
        self.text = "--- layout: default ---\n"
        self.create_specification(subcomponents, used_by, generated_by,
                                  derived_from, attributed_to, prefix, intro)
    
    def create_specification(self, subcomponents, used_by, generated_by,
                             derived_from, attributed_to, prefix, intro=None):
        self.create_title(self.name+": Types and relations", "definitions")

        if intro is not None:
            self.text += intro

        #table_num = 3
        for subcomponent_name, classes in subcomponents.items():
            classes_by_types = self.owl.get_class_names_by_prov_type(
                classes, prefix=prefix, but=self.already_defined_classes)
            self.already_defined_classes += classes

            #self.create_subcomponent_table(classes_by_types, table_num,
            #                               subcomponent_name)
            #table_num = table_num + 1
            all_classes = \
                classes_by_types[PROV['Activity']] + \
                classes_by_types[PROV['Entity']] + \
                classes_by_types[PROV['Agent']] + \
                classes_by_types[None]

            for class_name in all_classes:
                self.create_class_section(
                    class_name,
                    self.owl.get_definition(class_name),
                    self.owl.attributes.setdefault(class_name, None),
                    used_by, generated_by, derived_from, attributed_to,
                    children=not (
                        self.owl.get_prov_class(class_name) == PROV['Entity']))

            if subcomponent_name:
                self.text += """
            </section>"""

        self.close_sections()
    
    def create_subcomponent_table(self, classes, table_num,
                                  subcomponent_name=None):
        if subcomponent_name:
            self.text += """
        <section><h1>"""+subcomponent_name+"""</h1>"""
            # Check if there is a header file to include here
            fname = os.path.join(
                INCLUDE_FOLDER,
                self.component+"_" +
                subcomponent_name.split(" ")[0].lower()+".html")
            if os.path.isfile(fname):
                fid = open(fname, "r")
                self.text += fid.read()
                fid.close()

        else:
            subcomponent_name = ""

        # Did not find how to handle table numbering and ids with Respec as we
        # did for figures?
        table_id = "prov-mapping-"""+subcomponent_name.lower()
        self.text += """
        <div style="text-align: left;">
            <table class="thinborder">
                <caption id=\""""+table_id+"""\">
                    <a class="internalDFN" href=\"#"""+table_id+"""\">Table """+str(table_num)+"""</a>:"""+self.name+subcomponent_name + """ Concepts
                </caption>
                <tbody>
                    <tr>
                        <th align="center"><b>"""+self.name+""" Concept</b></th>
                        <th align="center"><b>PROV type</b></th>
                        <th align="center"><b>Identifier</b></th>
                    </tr>
        """

        self.text += """
        <!-- HERE ------------- Beginning of PROV Entities ------------- -->
        """

        for prov_class in list([
                PROV['Activity'],
                PROV['Entity'],
                PROV['Agent']]):
            sorted_classes = classes[prov_class]
            for class_uri in sorted_classes:
                self.text += """
                        <tr>
                            <td>"""+self.term_link(class_uri)+"""
                            </td>
                    """

                # First iteration
                if class_uri is sorted_classes[0]:
                    self.text += """
                                <td rowspan=\""""+str(len(sorted_classes)) + \
                        """\" style="text-align: center;"> """ + \
                        self.owl.get_label(prov_class) + \
                        """</td>
                        """

                self.text += """
                                <td>"""+self.owl.graph.qname(class_uri) + \
                             """</td>
                            </tr>
                """

        self.text += """
                </tbody>
                </table>
            </div>"""
    
    def create_title(self, title, id=None):

        #print "into create_title"

        if id is None:
            self.text += """
        <section>
        """
        else:
            self.text += """
        <section id=\""""+id+"""\">
        """
        self.text += """
            <h1>"""+title+"""</h1>
        """
        self.section_open += 1
    
    def _format_markdown(self, text):

        #print "into _format_markdown"

        # Replace links specified in markdown by html
        text = markdown2.markdown(text).replace("<p>", "").replace("</p>", "")
        # Remove trailing new line
        text = text[0:-1]
        return text

    def format_definition(self, definition):

        #print "into format_definition"

        # Capitalize first letter, format markdown and end with dot
        if definition:
            definition = definition[0].upper() + definition[1:]
            definition = self._format_markdown(definition)
            definition += "."

        return definition

    def linked_listing(self, uri_list, prefix="", suffix="", sort=True):

        #print "into linked_listing"

        linked_listing = prefix

        if sort:
            uri_list = self.owl.sorted_by_labels(uri_list)

        for i, uri in enumerate(uri_list):
            if i == 0:
                sep = ""
            elif i == len(uri_list):
                sep = " and "
            else:
                sep = ", "
            linked_listing += sep+self.term_link(uri)

        return linked_listing+suffix

    def term_link(self, term_uri, tag="a", text=None):
        href = ""
        if self.owl.is_external_namespace(term_uri):
            href = " href =\""+str(term_uri)+"\""
        else: #target link fix
            href = " href =\"#dfn-"+self.owl.get_name(term_uri).lower()+"\""
            if tag is "dfn":
                href += " id=\"dfn-"+self.owl.get_name(term_uri).lower()+"\""
        
        if text is None:
            text = self.owl.get_label(term_uri)

        term_link = "<" + tag + " title=\"" + self.owl.get_name(term_uri) + \
                    "\"" + href + ">" + text+"</"+tag+">"

        if tag is "dfn":
            issue_url = "https://github.com/incf-nidash/nidm/issues"

            # Add link to current definition
            term_link = self.term_link(term_uri, text=term_link)

            if self.commentable:
                term_link = term_link + \
                    " <a href=\""+issue_url+"?&q=is%3Aopen+'" + text + \
                    "'\"\"><sup>&#9734;</sup></a>" + \
                    "<a href=\""+issue_url+"/new\";\"><sup>+</sup></a>"

        return term_link

    def create_class_section(self, class_uri, definition, attributes,
                             used_by=None, generated_by=None,
                             derived_from=None, attributed_to=None,
                             children=False,
                             is_range=False):
        class_label = self.owl.get_label(class_uri)
        class_name = self.owl.get_name(class_uri)

        definition = self.format_definition(definition)

        self.text += """
            <!-- """+class_label+""" ("""+class_name+""")"""+""" -->
            <section id="section-"""+class_label+"""">
                <h1 label=\""""+class_name+"""\">"""+class_label+"""</h1>
                <div class="glossary-ref">
                    """+self.term_link(class_uri, "dfn") + ": " + definition

        self.text += "<p> "+self.term_link(class_uri)+" is"

        nidm_class = self.owl.get_nidm_parent(class_uri)
        if nidm_class:
            self.text += " a "+self.term_link(nidm_class)
        else:
            prov_class = self.owl.get_prov_class(class_uri)
            if prov_class:
                self.text += " a "+self.owl.get_label(prov_class)

        found_used_by = False
        if used_by:
            if class_uri in used_by:
                self.text += self.linked_listing(used_by[class_uri],
                                                 " used by ")
                found_used_by = True
            used_entities = list()

            for used_entity, used_activities in used_by.items():
                for used_act in used_activities:
                    if used_act == class_uri:
                        used_entities.append(used_entity)
            if used_entities:
                self.text += self.linked_listing(used_entities,
                                                 " that uses ",
                                                 " entities")

        found_attr_to = False
        if attributed_to:
            if class_uri in attributed_to:
                if found_used_by:
                    self.text += " and "
                self.text += self.linked_listing(attributed_to[class_uri],
                                                 " attributed to ")
                found_attr_to = True

        found_generated_by = False
        if generated_by:
            if class_uri in generated_by:
                if found_used_by or found_generated_by:
                    self.text += " and "

                self.text += self.linked_listing(
                    list([generated_by[class_uri]]), " generated by ")

                found_generated_by = True

            if class_uri in generated_by.values():
                generated_entities = list()
                for generated_entity, generated_act in generated_by.items():
                    if generated_act == class_uri:
                        generated_entities.append(generated_entity)

                if generated_entities:
                    self.text += self.linked_listing(
                        generated_entities,
                        ". This activity generates ", " entities")

        if derived_from:
            if class_uri in derived_from:
                if found_used_by or found_generated_by or found_attr_to:
                    self.text += " and "

                self.text += self.linked_listing(
                    list([derived_from[class_uri]]), " derived from ")

        class_children = self.owl.get_direct_children(class_uri)
        if class_children:
            if found_used_by or found_generated_by or found_attr_to:
                self.text += ". It "
            else:
                self.text += " and "
            self.text += " has the following child"
            if len(class_children) > 1:
                self.text += "ren"
            self.text += ": " + \
                         self.linked_listing(class_children)

        self.text += "."
        self.text += "</p>"

        range_classes = list()

        self.text += """
                </div>"""

        if attributes and (attributes != set([CRYPTO['sha512']])):
            self.text += """
                <p></p>
                <div class="attributes" id="attributes-"""+class_label + \
                """"> A """ + \
                self.term_link(class_uri)+""" has attributes:
                <ul>
                    <li><span class="attribute" id=\"""" + \
                class_label+""".label">rdfs:label</span>: \
                    (<em class="rfc2119" title="OPTIONAL">OPTIONAL</em>) """\
            """Human readable description of the """ + \
                self.term_link(class_uri)+""".</li>"""

            for att in sorted(attributes):

                # Do not display prov relations as attributes
                # (except prov:atLocation...)
                if not self.owl.is_prov(att) or (att == PROV['atLocation']):
                    if att not in self.attributes_done:
                        # First definition of this attribute
                        att_tag = "dfn"
                    else:
                        att_tag = "a"

                    self.attributes_done.add(att)

                    # if att_label.startswith("nidm:"):
                    att_def = self.owl.get_definition(att)
                    self.text += """
                        <li>"""+self.term_link(att, att_tag) + \
                        '</span>: (<em class="rfc2119" title="OPTIONAL">' + \
                        'OPTIONAL</em>) ' + self.format_definition(att_def)

                    if att in self.owl.parent_ranges:
                        child_ranges = list()
                        for parent_range in self.owl.parent_ranges[att]:
                            child_ranges += self.owl.get_direct_children(
                                parent_range)
                            if self.owl.get_label(parent_range).\
                                    startswith('nidm'):
                                range_classes.append(parent_range)
                        child_ranges = sorted(child_ranges)

                        # if nidm_namespace:
                        child_range_txt = ""
                        if child_ranges:
                            # Get all child ranges
                            child_range_txt = self.linked_listing(
                                child_ranges, " such as ")

                        self.text += self.linked_listing(
                            self.owl.parent_ranges[att],
                            " (range ", child_range_txt+")")
                        self.text += "."

                        self.text += "</li>"

            self.text += """
                </ul>
                </div>"""

        BASE_REPOSITORY = "https://raw.githubusercontent.com/" + \
            "incf-nidash/nidm/master/"
        for title, example in self.owl.get_example(class_uri, BASE_REPOSITORY):
            self.text += """
                </ul>
                </div>
                <pre class='example highlight' title=\""""+title+"""\">""" + \
                cgi.escape(example) + """</pre>"""

        # For object property list also children (in sub-sections)
        if children:
            direct_children = self.owl.sorted_by_labels(
                self.owl.get_direct_children(class_uri))
            for child in direct_children:
                if not child in self.already_defined_classes:
                    self.create_class_section(
                        child,
                        self.owl.get_definition(child),
                        self.owl.attributes.setdefault(child, None),
                        children=True)
                    self.already_defined_classes.append(child)

        # Display individuals
        individuals = self.owl.sorted_by_labels(
            self.owl.get_individuals(class_uri))
        if individuals:
            self.text += \
                " Examples of "+self.term_link(class_uri)+" includes " + \
                "<ul>"

            for indiv in individuals:
                self.text += "<li>" + self.term_link(indiv, "dfn") + ": " + \
                             self.format_definition(
                                 self.owl.get_definition(indiv)) + \
                             "</li>"

            self.text += "</ul>"

        if is_range:
            self.text += """
                </section>"""

        for range_name in self.owl.sorted_by_labels(range_classes):
            if not range_name in self.already_defined_classes:
                self.already_defined_classes.append(range_name)
                self.create_class_section(
                    range_name,
                    self.owl.get_definition(range_name),
                    self.owl.attributes.setdefault(range_name, None),
                    children=True, is_range=True)

        if not is_range:
            self.text += """
                </section>"""

    def close_sections(self):

        #print "into close_sections"

        for x in range(0, self.section_open):
            self.text += "\t"*x+"</section>\n"
    
    # Write out specification
    def write_specification(self, spec_file=None, component=None,
                            version=None):

        spec_file = "index.html"
        spec_open = codecs.open(spec_file, 'w', "utf-8")
        spec_open.write(self.text)
        spec_open.close()

    def _header_footer(self, prev_file=None, follow_file=None, component=None,
                       version=None):

        #print "into _header_footer"

        release_notes = None
        
        if component:
            prev_file = os.path.join(
                INCLUDE_FOLDER, component+"_"+version+"_head.html")
            if not os.path.isfile(prev_file):
                prev_file = os.path.join(
                    INCLUDE_FOLDER, component+"_head.html")
            follow_file = os.path.join(
                INCLUDE_FOLDER, component+"_"+version+"_foot.html")
            if not os.path.isfile(follow_file):
                follow_file = os.path.join(
                    INCLUDE_FOLDER, component+"_foot.html")
            if version:
                release_notes = os.path.join(
                    os.path.dirname(self.owl.file),
                    component+"_"+version+"_notes.html")
                if not os.path.isfile(release_notes):
                    release_notes = None

        if prev_file is not None:
            prev_file_open = open(prev_file, 'r')
            self.text = prev_file_open.read().decode('utf-8')+self.text
            prev_file_open.close()
        if release_notes is not None:
            release_note_open = open(release_notes, 'r')
            self.text = self.text+release_note_open.read()
            release_note_open.close()
        if follow_file is not None:
            follow_file_open = open(follow_file, 'r')
            self.text = self.text+follow_file_open.read()
            follow_file_open.close()

    def owl_process():
        owl = OwlReader(owlTest)
        owl.graph.bind('dct', 'http://purl.org/dc/terms/')
        owl.graph.bind('dicom', 'http://purl.org/nidash/dicom#')
        owl.graph.bind('nidm', 'http://purl.org/nidash/nidm#')
        owl.graph.bind('bids', 'http://purl.org/nidash/bids#')
        owl.graph.bind('onli', 'http://neurolog.unice.fr/ontoneurolog/v3.0/instrument.owl#')
        owl.graph.bind('pato', 'http://purl.obolibrary.org/obo/pato#')
        owl.graph.bind('prov', 'http://www.w3.org/ns/prov')
        owl.graph.bind('qibo', 'http://www.owl-ontologies.com/Ontology1298855822.owl')
        owl.graph.bind('sio', 'http://semanticscience.org/resource/')

        html = "---\nlayout: default\n---\n"

        terms = owl.get_class_names()
        terms = owl.sorted_by_labels(terms)
        
        props = owl.get_property_names()
        props = owl.sorted_by_labels(props)
        for x in props:
            print(x)

        print('==========')
        print(owl.get_prov_class(terms[0]))
        print(owl.get_prov_class(terms[1]))

        for i in range(0,10):
            term = terms[i]
            name = owl.get_label(term)
            html += "<div id='" + name + "'>\n"
            html += "<b>"
            html += "<a href='#" + name + "'>"
            html += name
            html += "</a>"
            html += "</b>: "
            html += owl.get_definition(term)
            html += "\n<br/><br/>\n"

        html_file = open("index.html", "w")
        html_file.write(html)
        html_file.close()
            
        return



    def split_process():
        #older version without owl_reader
        f = open(owlTest, "r")
        lines = f.readlines()
        f.close()

        prefixes = []
        subject = ""
        html = "---\nlayout: default\n---\n"

        for x in lines:
            #print(x)
            x = x.strip()
            if x != "" and x[0] != "#" and x[0] != "@" and x[0] != "[":
                x = shlex.split(x)
                if len(x)<3 or x[0] == "owl:imports":
                    continue
                
                if subject == "":
                    subject = x[0]
                    html += "<div id='" + subject + "'>\n"
                    html += "<h2>"
                    html += "<a href='#" + subject + "'>"
                    html += subject
                    html += "</a>"
                    html += "</h2>\n"
                    continue
                end = x[-1]
                vo = " ".join(x[:-1])
                verb = x[0]
                obj = x[1]
                html += "<b>" + verb + "</b> "
                html += obj + "</br>\n"
                if end == ".":
                    subject = ""
                    html += "</div></br>\n"

        html_file = open("index.html", "w")
        html_file.write(html)
        html_file.close()

        #print(html)
        return

if __name__ == "__main__":
    if len(sys.argv) > 1:
        nidm_original_version = sys.argv[1]
        nidm_version = nidm_original_version.replace(".", "")
    else:
        nidm_original_version = "dev"
        nidm_version = 'dev'

    # Retrieve owl file for NIDM-Results
    if nidm_version == "dev":
        owl_file = os.path.join(TERMS_FOLDER, 'nidm-experiment.owl')
        import_files = glob.glob(os.path.join(NIDM_EXPE_PATH, "imports", '*.ttl'))
    else:
        owl_file = os.path.join(RELEASED_TERMS_FOLDER, \
            'nidm-experiment_'+nidm_version+'.owl')
        # For released version of the ontology imports are embedded
        import_files = None

    # check the file exists
    assert os.path.exists(owl_file)

    subcomponents =  collections.OrderedDict()

    subcomponents['Project'] = [
        NIDM['CoInvestigator'], NIDM['Gender'],NIDM['Group'], NIDM['ModelDesigner'], 
        NIDM['ModelSpecification'], NIDM['PrincipalInvestigator'], NIDM['Project'],
        NIDM['Protocol'], NIDM['ResearchAssistant'], NIDM['SpecifiedPlan'], NIDM['Subject']
    ]
    subcomponents['Acquisition'] = [
        NIDM['Acquisition'],NIDM['AcquisitionDeviceOperator'], NIDM['AcquisitionMethod'],
        NIDM['AcquisitionModality'], NIDM['AcquisitionObject'], NIDM['AcquisitionObjectQuality'],
        NIDM['AcquisitionUsageType'], NIDM['AuxiliaryFile'], NIDM['AuxiliaryFileCollection'],
        NIDM['CalculatedParameter'], NIDM['Magnitude'], NIDM['PerformedPlan'], NIDM['Phase'],
        NIDM['PresentationSoftware'], NIDM['ProcessedAcquisitionObject'], NIDM['RawAcquisitionObject'],
        NIDM['ReconstructedAcquisitionObject'], NIDM['Series'], NIDM['Session'], NIDM['SessionObject'],
        NIDM['StimulusPresentationFile'], NIDM['StimulusResponseFile'], NIDM['Task']
    ]
    subcomponents['Assessment Instrument'] = [
        NIDM['BehavioralInstrument'],  NIDM['DemographicsInstrument'],
        NIDM['InformedConsentInstrument'], NIDM['InstrumentAdministrator'], NIDM['InstrumentUsageType']
    ]
    subcomponents['Magnetic Resonance Imaging'] = [
        NIDM['Anatomical'], NIDM['Angiography'], NIDM['ArterialSpinLabeling'], NIDM['BloodOxygenLevelDependent'], 
        NIDM['Cartesian'], NIDM['CerebralBloodFlow'], NIDM['CerebralBloodVolume'], 
        NIDM['DICOMTagCollection'], NIDM['DiffusionTensor'],NIDM['DiffusionWeighted'], 
        NIDM['DynamicContrastEnhanced'], NIDM['DynamicSusceptibilityContrast'],
        NIDM['EchoPlanar'], NIDM['FlowWeighted'],NIDM['FluidAttenuatedInversionRecovery'], 
        NIDM['Functional'], NIDM['ImageContrastType'],
        NIDM['ImageDataReconstruction'], NIDM['ImageUsageType'], NIDM['Inside-outSpiral'], 
        NIDM['MagneticResonanceImaging'], NIDM['MagneticResonanceImagingScanner'], 
        NIDM['NuclearMagneticResonanceSpectroscopy'],
        NIDM['NuclearMagneticResonanceSpectroscopicImaging'],NIDM['Outside-inSpiral'], NIDM['ParallelImaging'], 
        NIDM['ProtonDensityWeighted'],NIDM['PulseSequence'],NIDM['QuantitativeSusceptibilityMapping'],
        NIDM['Rectilinear'],NIDM['SimultaneousMultisliceMethod'], NIDM['SteadyStateFreePrecession'], NIDM['Structural'], 
        NIDM['SusceptibilityWeighted'],NIDM['SusceptibilityWeightedImaging'],
        NIDM['T1Weighted'], NIDM['T2StarWeighted'], NIDM['T2Weighted'],NIDM['b-ValueFile'],
        NIDM['b-VectorFile'], NIDM['k-spaceTraversalScheme'], NIDM['NIDM_0000152'], NIDM['NIDM_0000153'],
        NIDM['NIDM_0000154'], NIDM['NIDM_0000155']
    ]
    subcomponents['Electrophysiology'] = [
        NIDM['Amperometry'],  NIDM['CurrentClamp'], 
        NIDM['Electrocorticography'], NIDM['ElectrophysiologyRecording'],
        NIDM['ExtracellularElectrophysiologyRecording'],NIDM['FieldPotential'],
        NIDM['IntracellularElectrophysiologyRecording'],
        NIDM['MultiUnitReccording'],  NIDM['SharpElectrode'], NIDM['SingleUnitReccording'], 
        NIDM['PatchClamp'], NIDM['VoltageClamp']
    ]
    subcomponents['Devices'] = [
        NIDM['Attenuator'], NIDM['BandpassFilter'], NIDM['CurrentAmplifier'],
        NIDM['DataAcquisitionDevice'], NIDM['DataProcessingDevice'], NIDM['Electrode'],
        NIDM['ElectroencephalographyAcquisitionDevice'], NIDM['EyeTrackingDevice'],
        NIDM['HeartRateMonitor'], NIDM['HighPassFilter'], NIDM['ImageAcquisitionDevice'],
        NIDM['LowPassFilter'], NIDM['MultielectrodeArray'], NIDM['ReceiveCoil'], 
        NIDM['RespirationRateMonitor'], NIDM['SignalFilter'], NIDM['SignalGenerator'],
        NIDM['StimulusGenerator'], NIDM['StimulusIsolator'], NIDM['TransmitCoil'],
        NIDM['VoltageAmplifier']
    ]
    subcomponents['Positron Emission Tomography'] = [
        NIDM['PositronEmissionTomography'],
        NIDM['PositronEmissionTomographyScanner']
    ]
    subcomponents['X-ray Computed Tomography'] = [
        NIDM['X-rayComputedTomography'],
        NIDM['X-rayComputedTomographyAcquisitionDevice']
    ]
    subcomponents['Magnetoencephalography'] = [
        NIDM['Magnetoencephalography'],
        NIDM['MagnetoencephalographyAcquisitionDevice'],
        NIDM['NoiseMeasurement'] 
    ]
    subcomponents['Electroencephalography'] = [
        NIDM['Electroencephalography'],
        NIDM['ElectroencephalographyAcquisitionDevice']
    ]
    subcomponents['SinglePhotonEmissionComputedTomography'] = [
        NIDM['SinglePhotonEmissionComputedTomography'],
        NIDM['SinglePhotonEmissionComputedTomographyScanner']
    ]

    # Add manually used and wasDerivedFrom because these are not stored in the
    # owl file (no relations yet!)
    used_by = {}
    generated_by = {}
    derived_from = {}

    owlspec = OwlNidmHtml(owl_file, import_files, "NIDM-Experiment", subcomponents, used_by, generated_by, derived_from, prefix=str(NIDM))
    
    if not nidm_version == "dev":
        owlspec.text = owlspec.text.replace("(under development)", nidm_original_version)
        owlspec.text = owlspec.text.replace("img/", "img/nidm-results_"+nidm_version+"/") #where versions are included

    component_name = "nidm-experiment"
    #owlspec._header_footer(component=component_name, version=nidm_version)
    owlspec.write_specification(component=component_name, version=nidm_version)
    
    #owlspec.write_specification()
    #owlspec.owl_process()
    #split_process()
