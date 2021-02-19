---
title: BIDS
layout: template
filename: bids
---
    <section id='abstract'>
        <p>
            This document provides an intuitive introduction to the NIDASH Data Model for neuroimaging data
            sharing. NIDASH defines a core vocabulary that extends the PROV Data Model for provenance with terms that
            capture information about neuroimaging research, from data acquisition to analysis and results. This primer
            explains the fundamental NIDASH concepts and provides examples of its use. The primer is intended as a
            starting point for neuroimaging scientists or developers interested in using or creating apps with NIDM.
        </p>
    </section>

    <section id="sodt">
        <p>

        </p>
    </section>

    <section class="introductory">
        <h2>Overview</h2>
        This section provides an overview of the NIDASH Family of Documents and suggestions to the neuroimaging community
        for implementing these standards to support data sharing activities, as well as in reporting issues or comments.
        <section>
        <h4>NIDASH Family of Documents</h4>
            <p>
                This document is part of the NIDASH Family of Documents, a set of documents defining various aspects of
                neuroimaging research that are necessary to achieve the vision of inter-operable interchange of information in
                heterogeneous environments such as the Web, research consortia, and laboratories. A list of current <abbr
                title="Neuroimaging Data Sharing">NIDASH</abbr> documents and the latest revision of this specification can be
                found in the <a href="http://nidm.nidash.org/specs"><abbr title="NIDASH Data Model">NIDM </abbr>specification
                index</a>. These documents are listed below.
            </p>
            <ul>
                <li><a href="http://nidm.nidash.org/specs/nidm-overview.html">NIDM-OVERVIEW</a> (Draft), an overview of the
                    NIDASH Model Specificatin Suite (this document);
                </li>
                <li><a href="http://nidm.nidash.org/specs/nidm-primer.html">NIDM-PRIMER</a> (Draft), a primer for the NIDASH
                    data model [[!NIDM-Primer]];
                </li>
                <li><a href="http://nidm.nidash.org/specs/nidm-descriptor.html">NIDM-DESCRIPTOR</a> (Draft), the NIDM Dataset
                    Descriptor is a high level description of neuroimaging data modeled using NIDM [[!NIDM-Descriptor]];
                </li>
                <li><a href="http://nidm.nidash.org/specs/nidm-experiment.html">NIDM-EXPERIMENT</a> (Draft), a data model for
                    describing the organization of raw neuroimaging experiment data [[!NIDM-Experiment]];
                </li>
                <li><a href="http://nidm.nidash.org/specs/nidm-results.html">NIDM-RESULTS</a> (Draft), a data model for
                    describing the results of neuroimaging analyses.[[!NIDM-Results]].
                </li>
            </ul>
        </section>

        <section>
            <h4>Implementations Encouraged</h4>
            <p>
                The NIDASH Working Group encourages implementation of the specifications presented in this document. Work on
                this document by the NIDASH Working Group is active and ongoing. Errors and suggestions may be reported in the <a
                href="https://github.com/ni-/ni-dm/issues">issue tracker</a> and these may be addressed in future revisions.
            </p>
        </section>

        <section>
            <h4>Please Send Comments</h4>
            <p>
                This document was published by the NIDASH Working Group as a Working Draft. If you wish to make comments
                regarding this document, please report using the <a href="https://github.com/ni-/ni-dm/issues">NIDM issue
                tracker</a>. You can also ask questions at <a href="http://neurostars.org/">Neurostars Q&A.</a> All comments
                and questions are welcome.
            </p>
        </section>
    </section>

    <section>
        <h2>Introduction</h2>
        <p>
            This primer document provides information on the NIDM-Experiment specification. The goal of NIDM-Experiment is to 
            provide terms that describe entities and activities for general scientific experiments with a focus on those 
            specific to 
            neuroscience. It is meant to work with NIDM-Workflow, which describes the processing and analysis of data and NIDM-Results
            that describes the results of workflows in the fMRI domain. It also provides terms used in PyNIDM, which can be 
            used to annotate data.
        </p>
    </section>

    <section>
        <h2>Overview of the NIDM Experiment Component</h2>
        <p>
            This section provides an explanation of NIDM-Experiment, which is based on the  <a href="https://www.w3.org/TR/prov-o/">
            W3C PROV ontology (Prov-O)</a> that has as it basic elements Entities, Activities, and Agents.  In constructing 
            NIDM-Experiment, we have reused terms from existing terminologies and ontologies where possible. Terms that are 
            reused from other ontologies are imported into the main NIDM-Experiment OWL file and can be found in the /imports  
            directory.  The most extensive 
            modality coverage is for MRI, but there are also terms useful for electrophysiology experiments.  Extensions to 
            other modalities and expansions of existing modalities are ongoing and requests for the inclusion of terms for 
            specific experiments are encouraged.   
            <figure id="Small_imaging_example">
                <img src="img/Small_imaging_example.png" width=800px/>
                <figcaption>A MR imaging experiment modeled using NIDM-experiment.</figcaption>
            </figure>
        </p>
        <p>
           NIDM-Experiment will be integrated into PyNIDM  <a href="https://github.com/incf-nidash/PyNIDM">
            PyNIDM</a>in the future.  PyNIDM will include a mechanism by which users can 
           search for terms necessary to annotate their specific dataset.  It will also provide a mechanism by which 
           users can request needed missing terms to be included in future NIDM-Experiment releases.
        </p>

        <section id="definitions">
        
            <h1>BIDS: Types and relations</h1>
        
            <!-- bids:'Acquisition' (Acquisition) -->
            <section id="acquisition">
                <h1 label="Acquisition">bids:'Acquisition'</h1>
                <div class="glossary-ref">
                    <a title="Acquisition" href ="#acquisition"><dfn title="Acquisition" href ="#acquisition">bids:'Acquisition'</dfn></a>: <p> <a title="Acquisition" href ="#acquisition">bids:'Acquisition'</a> is a <a title="BIDSEntity" href ="#bidsentity">bids:'BIDS Entity'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'BIDS Data Type' (BIDSDataType) -->
            <section id="bidsdatatype">
                <h1 label="BIDSDataType">bids:'BIDS Data Type'</h1>
                <div class="glossary-ref">
                    <a title="BIDSDataType" href ="#bidsdatatype"><dfn title="BIDSDataType" href ="#bidsdatatype">bids:'BIDS Data Type'</dfn></a>: <p> <a title="BIDSDataType" href ="#bidsdatatype">bids:'BIDS Data Type'</a> is and  has the following children: <a title="anat" href ="#anat">bids:'anat'</a>, <a title="dwi" href ="#dwi">bids:'dwi'</a>, <a title="eeg" href ="#eeg">bids:'eeg'</a>, <a title="fmap" href ="#fmap">bids:'fmap'</a>, <a title="func" href ="#func">bids:'func'</a>, <a title="ieeg" href ="#ieeg">bids:'ieeg'</a>, <a title="meg" href ="#meg">bids:'meg'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'BIDS Entity' (BIDSEntity) -->
            <section id="bidsentity">
                <h1 label="BIDSEntity">bids:'BIDS Entity'</h1>
                <div class="glossary-ref">
                    <a title="BIDSEntity" href ="#bidsentity"><dfn title="BIDSEntity" href ="#bidsentity">bids:'BIDS Entity'</dfn></a>: <p> <a title="BIDSEntity" href ="#bidsentity">bids:'BIDS Entity'</a> is and  has the following children: <a title="Acquisition" href ="#acquisition">bids:'Acquisition'</a>, <a title="ContrastEnhancingAgent" href ="#contrastenhancingagent">bids:'Contrast Enhancing Agent'</a>, <a title="CorrespondingModality" href ="#correspondingmodality">bids:'Corresponding Modality'</a>, <a title="Echo" href ="#echo">bids:'Echo'</a>, <a title="PhaseEncodingDirection" href ="#phaseencodingdirection">bids:'Phase-Encoding Direction'</a>, <a title="Processed" href ="#processed">bids:'Processed'</a>, <a title="Reconstruction" href ="#reconstruction">bids:'Reconstruction'</a>, <a title="Recording" href ="#recording">bids:'Recording'</a>, <a title="Run" href ="#run">bids:'Run'</a>, <a title="Session" href ="#session">bids:'Session'</a>, <a title="Space" href ="#space">bids:'Space'</a>, <a title="Split" href ="#split">bids:'Split'</a>, <a title="Subject" href ="#subject">bids:'Subject'</a>, <a title="Task" href ="#task">bids:'Task'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'BIDS Folder' (BIDSFolder) -->
            <section id="bidsfolder">
                <h1 label="BIDSFolder">bids:'BIDS Folder'</h1>
                <div class="glossary-ref">
                    <a title="BIDSFolder" href ="#bidsfolder"><dfn title="BIDSFolder" href ="#bidsfolder">bids:'BIDS Folder'</dfn></a>: <p> <a title="BIDSFolder" href ="#bidsfolder">bids:'BIDS Folder'</a> is and  has the following children: <a title="code" href ="#code">bids:'code'</a>, <a title="derivatives" href ="#derivatives">bids:'derivatives'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'BIDS Suffix' (BIDSSuffix) -->
            <section id="bidssuffix">
                <h1 label="BIDSSuffix">bids:'BIDS Suffix'</h1>
                <div class="glossary-ref">
                    <a title="BIDSSuffix" href ="#bidssuffix"><dfn title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</dfn></a>: <p> <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a> is and  has the following children: <a title="FLAIR" href ="#flair">bids:'FLAIR'</a>, <a title="FLASH" href ="#flash">bids:'FLASH'</a>, <a title="PD" href ="#pd">bids:'PD'</a>, <a title="PDT2" href ="#pdt2">bids:'PDT2'</a>, <a title="PDmap" href ="#pdmap">bids:'PDmap'</a>, <a title="T1map" href ="#t1map">bids:'T1map'</a>, <a title="T1rho" href ="#t1rho">bids:'T1rho'</a>, <a title="T1w" href ="#t1w">bids:'T1w'</a>, <a title="T2map" href ="#t2map">bids:'T2map'</a>, <a title="T2star" href ="#t2star">bids:'T2star'</a>, <a title="T2w" href ="#t2w">bids:'T2w'</a>, <a title="angio" href ="#angio">bids:'angio'</a>, <a title="bold" href ="#bold">bids:'bold'</a>, <a title="cbv" href ="#cbv">bids:'cbv'</a>, <a title="defacemask" href ="#defacemask">bids:'defacemask'</a>, <a title="epi" href ="#epi">bids:'epi'</a>, <a title="events" href ="#events">bids:'events'</a>, <a title="fieldmap" href ="#fieldmap">bids:'fieldmap'</a>, <a title="inplaneT1" href ="#inplanet1">bids:'inplaneT1'</a>, <a title="inplaneT2" href ="#inplanet2">bids:'inplaneT2'</a>, <a title="magnitude" href ="#magnitude">bids:'magnitude'</a>, <a title="magnitude1" href ="#magnitude1">bids:'magnitude1'</a>, <a title="magnitude2" href ="#magnitude2">bids:'magnitude2'</a>, <a title="phase1" href ="#phase1">bids:'phase1'</a>, <a title="phase2" href ="#phase2">bids:'phase2'</a>, <a title="phasediff" href ="#phasediff">bids:'phasediff'</a>, <a title="sbref" href ="#sbref">bids:'sbref'</a>, <a title="stim" href ="#stim">bids:'stim'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'Contrast Enhancing Agent' (ContrastEnhancingAgent) -->
            <section id="contrastenhancingagent">
                <h1 label="ContrastEnhancingAgent">bids:'Contrast Enhancing Agent'</h1>
                <div class="glossary-ref">
                    <a title="ContrastEnhancingAgent" href ="#contrastenhancingagent"><dfn title="ContrastEnhancingAgent" href ="#contrastenhancingagent">bids:'Contrast Enhancing Agent'</dfn></a>: <p> <a title="ContrastEnhancingAgent" href ="#contrastenhancingagent">bids:'Contrast Enhancing Agent'</a> is a <a title="BIDSEntity" href ="#bidsentity">bids:'BIDS Entity'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'Corresponding Modality' (CorrespondingModality) -->
            <section id="correspondingmodality">
                <h1 label="CorrespondingModality">bids:'Corresponding Modality'</h1>
                <div class="glossary-ref">
                    <a title="CorrespondingModality" href ="#correspondingmodality"><dfn title="CorrespondingModality" href ="#correspondingmodality">bids:'Corresponding Modality'</dfn></a>: <p> <a title="CorrespondingModality" href ="#correspondingmodality">bids:'Corresponding Modality'</a> is a <a title="BIDSEntity" href ="#bidsentity">bids:'BIDS Entity'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'Echo' (Echo) -->
            <section id="echo">
                <h1 label="Echo">bids:'Echo'</h1>
                <div class="glossary-ref">
                    <a title="Echo" href ="#echo"><dfn title="Echo" href ="#echo">bids:'Echo'</dfn></a>: <p> <a title="Echo" href ="#echo">bids:'Echo'</a> is a <a title="BIDSEntity" href ="#bidsentity">bids:'BIDS Entity'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'FLAIR' (FLAIR) -->
            <section id="flair">
                <h1 label="FLAIR">bids:'FLAIR'</h1>
                <div class="glossary-ref">
                    <a title="FLAIR" href ="#flair"><dfn title="FLAIR" href ="#flair">bids:'FLAIR'</dfn></a>: <p> <a title="FLAIR" href ="#flair">bids:'FLAIR'</a> is a <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'FLASH' (FLASH) -->
            <section id="flash">
                <h1 label="FLASH">bids:'FLASH'</h1>
                <div class="glossary-ref">
                    <a title="FLASH" href ="#flash"><dfn title="FLASH" href ="#flash">bids:'FLASH'</dfn></a>: <p> <a title="FLASH" href ="#flash">bids:'FLASH'</a> is a <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'PD' (PD) -->
            <section id="pd">
                <h1 label="PD">bids:'PD'</h1>
                <div class="glossary-ref">
                    <a title="PD" href ="#pd"><dfn title="PD" href ="#pd">bids:'PD'</dfn></a>: <p> <a title="PD" href ="#pd">bids:'PD'</a> is a <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'PDT2' (PDT2) -->
            <section id="pdt2">
                <h1 label="PDT2">bids:'PDT2'</h1>
                <div class="glossary-ref">
                    <a title="PDT2" href ="#pdt2"><dfn title="PDT2" href ="#pdt2">bids:'PDT2'</dfn></a>: <p> <a title="PDT2" href ="#pdt2">bids:'PDT2'</a> is a <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'PDmap' (PDmap) -->
            <section id="pdmap">
                <h1 label="PDmap">bids:'PDmap'</h1>
                <div class="glossary-ref">
                    <a title="PDmap" href ="#pdmap"><dfn title="PDmap" href ="#pdmap">bids:'PDmap'</dfn></a>: <p> <a title="PDmap" href ="#pdmap">bids:'PDmap'</a> is a <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'Phase-Encoding Direction' (PhaseEncodingDirection) -->
            <section id="phaseencodingdirection">
                <h1 label="PhaseEncodingDirection">bids:'Phase-Encoding Direction'</h1>
                <div class="glossary-ref">
                    <a title="PhaseEncodingDirection" href ="#phaseencodingdirection"><dfn title="PhaseEncodingDirection" href ="#phaseencodingdirection">bids:'Phase-Encoding Direction'</dfn></a>: <p> <a title="PhaseEncodingDirection" href ="#phaseencodingdirection">bids:'Phase-Encoding Direction'</a> is a <a title="BIDSEntity" href ="#bidsentity">bids:'BIDS Entity'</a>.</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'Processed' (Processed) -->
            <section id="processed">
                <h1 label="Processed">bids:'Processed'</h1>
                <div class="glossary-ref">
                    <a title="Processed" href ="#processed"><dfn title="Processed" href ="#processed">bids:'Processed'</dfn></a>: <p> <a title="Processed" href ="#processed">bids:'Processed'</a> is a <a title="BIDSEntity" href ="#bidsentity">bids:'BIDS Entity'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'Reconstruction' (Reconstruction) -->
            <section id="reconstruction">
                <h1 label="Reconstruction">bids:'Reconstruction'</h1>
                <div class="glossary-ref">
                    <a title="Reconstruction" href ="#reconstruction"><dfn title="Reconstruction" href ="#reconstruction">bids:'Reconstruction'</dfn></a>: <p> <a title="Reconstruction" href ="#reconstruction">bids:'Reconstruction'</a> is a <a title="BIDSEntity" href ="#bidsentity">bids:'BIDS Entity'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'Recording' (Recording) -->
            <section id="recording">
                <h1 label="Recording">bids:'Recording'</h1>
                <div class="glossary-ref">
                    <a title="Recording" href ="#recording"><dfn title="Recording" href ="#recording">bids:'Recording'</dfn></a>: <p> <a title="Recording" href ="#recording">bids:'Recording'</a> is a <a title="BIDSEntity" href ="#bidsentity">bids:'BIDS Entity'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'Run' (Run) -->
            <section id="run">
                <h1 label="Run">bids:'Run'</h1>
                <div class="glossary-ref">
                    <a title="Run" href ="#run"><dfn title="Run" href ="#run">bids:'Run'</dfn></a>: <p> <a title="Run" href ="#run">bids:'Run'</a> is a <a title="BIDSEntity" href ="#bidsentity">bids:'BIDS Entity'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'Session' (Session) -->
            <section id="session">
                <h1 label="Session">bids:'Session'</h1>
                <div class="glossary-ref">
                    <a title="Session" href ="#session"><dfn title="Session" href ="#session">bids:'Session'</dfn></a>: <p> <a title="Session" href ="#session">bids:'Session'</a> is a <a title="BIDSEntity" href ="#bidsentity">bids:'BIDS Entity'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'Space' (Space) -->
            <section id="space">
                <h1 label="Space">bids:'Space'</h1>
                <div class="glossary-ref">
                    <a title="Space" href ="#space"><dfn title="Space" href ="#space">bids:'Space'</dfn></a>: <p> <a title="Space" href ="#space">bids:'Space'</a> is a <a title="BIDSEntity" href ="#bidsentity">bids:'BIDS Entity'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'Split' (Split) -->
            <section id="split">
                <h1 label="Split">bids:'Split'</h1>
                <div class="glossary-ref">
                    <a title="Split" href ="#split"><dfn title="Split" href ="#split">bids:'Split'</dfn></a>: <p> <a title="Split" href ="#split">bids:'Split'</a> is a <a title="BIDSEntity" href ="#bidsentity">bids:'BIDS Entity'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'Subject' (Subject) -->
            <section id="subject">
                <h1 label="Subject">bids:'Subject'</h1>
                <div class="glossary-ref">
                    <a title="Subject" href ="#subject"><dfn title="Subject" href ="#subject">bids:'Subject'</dfn></a>: <p> <a title="Subject" href ="#subject">bids:'Subject'</a> is a <a title="BIDSEntity" href ="#bidsentity">bids:'BIDS Entity'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'T1map' (T1map) -->
            <section id="t1map">
                <h1 label="T1map">bids:'T1map'</h1>
                <div class="glossary-ref">
                    <a title="T1map" href ="#t1map"><dfn title="T1map" href ="#t1map">bids:'T1map'</dfn></a>: <p> <a title="T1map" href ="#t1map">bids:'T1map'</a> is a <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'T1rho' (T1rho) -->
            <section id="t1rho">
                <h1 label="T1rho">bids:'T1rho'</h1>
                <div class="glossary-ref">
                    <a title="T1rho" href ="#t1rho"><dfn title="T1rho" href ="#t1rho">bids:'T1rho'</dfn></a>: <p> <a title="T1rho" href ="#t1rho">bids:'T1rho'</a> is a <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'T1w' (T1w) -->
            <section id="t1w">
                <h1 label="T1w">bids:'T1w'</h1>
                <div class="glossary-ref">
                    <a title="T1w" href ="#t1w"><dfn title="T1w" href ="#t1w">bids:'T1w'</dfn></a>: <p> <a title="T1w" href ="#t1w">bids:'T1w'</a> is a <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'T2map' (T2map) -->
            <section id="t2map">
                <h1 label="T2map">bids:'T2map'</h1>
                <div class="glossary-ref">
                    <a title="T2map" href ="#t2map"><dfn title="T2map" href ="#t2map">bids:'T2map'</dfn></a>: <p> <a title="T2map" href ="#t2map">bids:'T2map'</a> is a <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'T2star' (T2star) -->
            <section id="t2star">
                <h1 label="T2star">bids:'T2star'</h1>
                <div class="glossary-ref">
                    <a title="T2star" href ="#t2star"><dfn title="T2star" href ="#t2star">bids:'T2star'</dfn></a>: <p> <a title="T2star" href ="#t2star">bids:'T2star'</a> is a <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'T2w' (T2w) -->
            <section id="t2w">
                <h1 label="T2w">bids:'T2w'</h1>
                <div class="glossary-ref">
                    <a title="T2w" href ="#t2w"><dfn title="T2w" href ="#t2w">bids:'T2w'</dfn></a>: <p> <a title="T2w" href ="#t2w">bids:'T2w'</a> is a <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'Task' (Task) -->
            <section id="task">
                <h1 label="Task">bids:'Task'</h1>
                <div class="glossary-ref">
                    <a title="Task" href ="#task"><dfn title="Task" href ="#task">bids:'Task'</dfn></a>: <p> <a title="Task" href ="#task">bids:'Task'</a> is a <a title="BIDSEntity" href ="#bidsentity">bids:'BIDS Entity'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'anat' (anat) -->
            <section id="anat">
                <h1 label="anat">bids:'anat'</h1>
                <div class="glossary-ref">
                    <a title="anat" href ="#anat"><dfn title="anat" href ="#anat">bids:'anat'</dfn></a>: <p> <a title="anat" href ="#anat">bids:'anat'</a> is a <a title="BIDSDataType" href ="#bidsdatatype">bids:'BIDS Data Type'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'angio' (angio) -->
            <section id="angio">
                <h1 label="angio">bids:'angio'</h1>
                <div class="glossary-ref">
                    <a title="angio" href ="#angio"><dfn title="angio" href ="#angio">bids:'angio'</dfn></a>: <p> <a title="angio" href ="#angio">bids:'angio'</a> is a <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'bold' (bold) -->
            <section id="bold">
                <h1 label="bold">bids:'bold'</h1>
                <div class="glossary-ref">
                    <a title="bold" href ="#bold"><dfn title="bold" href ="#bold">bids:'bold'</dfn></a>: <p> <a title="bold" href ="#bold">bids:'bold'</a> is a <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'cbv' (cbv) -->
            <section id="cbv">
                <h1 label="cbv">bids:'cbv'</h1>
                <div class="glossary-ref">
                    <a title="cbv" href ="#cbv"><dfn title="cbv" href ="#cbv">bids:'cbv'</dfn></a>: <p> <a title="cbv" href ="#cbv">bids:'cbv'</a> is a <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'code' (code) -->
            <section id="code">
                <h1 label="code">bids:'code'</h1>
                <div class="glossary-ref">
                    <a title="code" href ="#code"><dfn title="code" href ="#code">bids:'code'</dfn></a>: <p> <a title="code" href ="#code">bids:'code'</a> is a <a title="BIDSFolder" href ="#bidsfolder">bids:'BIDS Folder'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'defacemask' (defacemask) -->
            <section id="defacemask">
                <h1 label="defacemask">bids:'defacemask'</h1>
                <div class="glossary-ref">
                    <a title="defacemask" href ="#defacemask"><dfn title="defacemask" href ="#defacemask">bids:'defacemask'</dfn></a>: <p> <a title="defacemask" href ="#defacemask">bids:'defacemask'</a> is a <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'derivatives' (derivatives) -->
            <section id="derivatives">
                <h1 label="derivatives">bids:'derivatives'</h1>
                <div class="glossary-ref">
                    <a title="derivatives" href ="#derivatives"><dfn title="derivatives" href ="#derivatives">bids:'derivatives'</dfn></a>: <p> <a title="derivatives" href ="#derivatives">bids:'derivatives'</a> is a <a title="BIDSFolder" href ="#bidsfolder">bids:'BIDS Folder'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'dwi' (dwi) -->
            <section id="dwi">
                <h1 label="dwi">bids:'dwi'</h1>
                <div class="glossary-ref">
                    <a title="dwi" href ="#dwi"><dfn title="dwi" href ="#dwi">bids:'dwi'</dfn></a>: <p> <a title="dwi" href ="#dwi">bids:'dwi'</a> is a <a title="BIDSDataType" href ="#bidsdatatype">bids:'BIDS Data Type'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'eeg' (eeg) -->
            <section id="eeg">
                <h1 label="eeg">bids:'eeg'</h1>
                <div class="glossary-ref">
                    <a title="eeg" href ="#eeg"><dfn title="eeg" href ="#eeg">bids:'eeg'</dfn></a>: <p> <a title="eeg" href ="#eeg">bids:'eeg'</a> is a <a title="BIDSDataType" href ="#bidsdatatype">bids:'BIDS Data Type'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'epi' (epi) -->
            <section id="epi">
                <h1 label="epi">bids:'epi'</h1>
                <div class="glossary-ref">
                    <a title="epi" href ="#epi"><dfn title="epi" href ="#epi">bids:'epi'</dfn></a>: <p> <a title="epi" href ="#epi">bids:'epi'</a> is a <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'events' (events) -->
            <section id="events">
                <h1 label="events">bids:'events'</h1>
                <div class="glossary-ref">
                    <a title="events" href ="#events"><dfn title="events" href ="#events">bids:'events'</dfn></a>: <p> <a title="events" href ="#events">bids:'events'</a> is a <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'fieldmap' (fieldmap) -->
            <section id="fieldmap">
                <h1 label="fieldmap">bids:'fieldmap'</h1>
                <div class="glossary-ref">
                    <a title="fieldmap" href ="#fieldmap"><dfn title="fieldmap" href ="#fieldmap">bids:'fieldmap'</dfn></a>: <p> <a title="fieldmap" href ="#fieldmap">bids:'fieldmap'</a> is a <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'fmap' (fmap) -->
            <section id="fmap">
                <h1 label="fmap">bids:'fmap'</h1>
                <div class="glossary-ref">
                    <a title="fmap" href ="#fmap"><dfn title="fmap" href ="#fmap">bids:'fmap'</dfn></a>: <p> <a title="fmap" href ="#fmap">bids:'fmap'</a> is a <a title="BIDSDataType" href ="#bidsdatatype">bids:'BIDS Data Type'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'func' (func) -->
            <section id="func">
                <h1 label="func">bids:'func'</h1>
                <div class="glossary-ref">
                    <a title="func" href ="#func"><dfn title="func" href ="#func">bids:'func'</dfn></a>: <p> <a title="func" href ="#func">bids:'func'</a> is a <a title="BIDSDataType" href ="#bidsdatatype">bids:'BIDS Data Type'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'ieeg' (ieeg) -->
            <section id="ieeg">
                <h1 label="ieeg">bids:'ieeg'</h1>
                <div class="glossary-ref">
                    <a title="ieeg" href ="#ieeg"><dfn title="ieeg" href ="#ieeg">bids:'ieeg'</dfn></a>: <p> <a title="ieeg" href ="#ieeg">bids:'ieeg'</a> is a <a title="BIDSDataType" href ="#bidsdatatype">bids:'BIDS Data Type'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'inplaneT1' (inplaneT1) -->
            <section id="inplanet1">
                <h1 label="inplaneT1">bids:'inplaneT1'</h1>
                <div class="glossary-ref">
                    <a title="inplaneT1" href ="#inplanet1"><dfn title="inplaneT1" href ="#inplanet1">bids:'inplaneT1'</dfn></a>: <p> <a title="inplaneT1" href ="#inplanet1">bids:'inplaneT1'</a> is a <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'inplaneT2' (inplaneT2) -->
            <section id="inplanet2">
                <h1 label="inplaneT2">bids:'inplaneT2'</h1>
                <div class="glossary-ref">
                    <a title="inplaneT2" href ="#inplanet2"><dfn title="inplaneT2" href ="#inplanet2">bids:'inplaneT2'</dfn></a>: <p> <a title="inplaneT2" href ="#inplanet2">bids:'inplaneT2'</a> is a <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'magnitude' (magnitude) -->
            <section id="magnitude">
                <h1 label="magnitude">bids:'magnitude'</h1>
                <div class="glossary-ref">
                    <a title="magnitude" href ="#magnitude"><dfn title="magnitude" href ="#magnitude">bids:'magnitude'</dfn></a>: <p> <a title="magnitude" href ="#magnitude">bids:'magnitude'</a> is a <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'magnitude1' (magnitude1) -->
            <section id="magnitude1">
                <h1 label="magnitude1">bids:'magnitude1'</h1>
                <div class="glossary-ref">
                    <a title="magnitude1" href ="#magnitude1"><dfn title="magnitude1" href ="#magnitude1">bids:'magnitude1'</dfn></a>: <p> <a title="magnitude1" href ="#magnitude1">bids:'magnitude1'</a> is a <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'magnitude2' (magnitude2) -->
            <section id="magnitude2">
                <h1 label="magnitude2">bids:'magnitude2'</h1>
                <div class="glossary-ref">
                    <a title="magnitude2" href ="#magnitude2"><dfn title="magnitude2" href ="#magnitude2">bids:'magnitude2'</dfn></a>: <p> <a title="magnitude2" href ="#magnitude2">bids:'magnitude2'</a> is a <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'meg' (meg) -->
            <section id="meg">
                <h1 label="meg">bids:'meg'</h1>
                <div class="glossary-ref">
                    <a title="meg" href ="#meg"><dfn title="meg" href ="#meg">bids:'meg'</dfn></a>: <p> <a title="meg" href ="#meg">bids:'meg'</a> is a <a title="BIDSDataType" href ="#bidsdatatype">bids:'BIDS Data Type'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'phase1' (phase1) -->
            <section id="phase1">
                <h1 label="phase1">bids:'phase1'</h1>
                <div class="glossary-ref">
                    <a title="phase1" href ="#phase1"><dfn title="phase1" href ="#phase1">bids:'phase1'</dfn></a>: <p> <a title="phase1" href ="#phase1">bids:'phase1'</a> is a <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'phase2' (phase2) -->
            <section id="phase2">
                <h1 label="phase2">bids:'phase2'</h1>
                <div class="glossary-ref">
                    <a title="phase2" href ="#phase2"><dfn title="phase2" href ="#phase2">bids:'phase2'</dfn></a>: <p> <a title="phase2" href ="#phase2">bids:'phase2'</a> is a <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'phasediff' (phasediff) -->
            <section id="phasediff">
                <h1 label="phasediff">bids:'phasediff'</h1>
                <div class="glossary-ref">
                    <a title="phasediff" href ="#phasediff"><dfn title="phasediff" href ="#phasediff">bids:'phasediff'</dfn></a>: <p> <a title="phasediff" href ="#phasediff">bids:'phasediff'</a> is a <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'sbref' (sbref) -->
            <section id="sbref">
                <h1 label="sbref">bids:'sbref'</h1>
                <div class="glossary-ref">
                    <a title="sbref" href ="#sbref"><dfn title="sbref" href ="#sbref">bids:'sbref'</dfn></a>: <p> <a title="sbref" href ="#sbref">bids:'sbref'</a> is a <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
            <!-- bids:'stim' (stim) -->
            <section id="stim">
                <h1 label="stim">bids:'stim'</h1>
                <div class="glossary-ref">
                    <a title="stim" href ="#stim"><dfn title="stim" href ="#stim">bids:'stim'</dfn></a>: <p> <a title="stim" href ="#stim">bids:'stim'</a> is a <a title="BIDSSuffix" href ="#bidssuffix">bids:'BIDS Suffix'</a>.</p><p>Type: Class</p><p>Curation Status: obo:IAO_0000124</p><p>Editor Note: To be discussed</p>
                </div>
            </section>
	</section>
