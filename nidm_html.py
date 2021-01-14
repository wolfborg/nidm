from nidmresults.owl.owl_reader import OwlReader

import shlex

#owlTest = "test.owl"
owlTest = "nidm-experiment.owl"

def main():
    #owl_process()
    split_process()

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

    html = "---\nlayout: default\n---"

    terms = owl.get_class_names()
    terms = owl.sorted_by_labels(terms)
    for term in terms:
        name = owl.get_label(term)
        html += "<div id='" + name + "'>\n"
        html += "<h2>"
        html += name
        html += "</a>"
        html += "</h2>\n"
        html += owl.get_definition(term)

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
    main()
