#### Biopython

# A set of freely available tools for biological computation
# It is a distributed collaborative effort to develop Python
# libraries and applications which address the needs of
# current and future work in bioinformatics


# Parse bioinformatics files into Python utilizable data:
# Blast output -
# ClustalW
# FASTA
# GenBank
# PubMed and Medline
# ExPASy files, like Enzyme and Prosite
# SCOP, including 'dom' and 'lin' files
# UniGene
# SwissProt

# Files in the supported formats can be iterated over, record by record, or indexed and accessed via a Dictionary interface.

# Code to deal with popular online bioinformatics destinations such as:
# NCBI – Blast, Entrez and PubMed services
# ExPASy - Swiss-Prot and Prosite entries, as well as Prosite
# searches

# Interfaces to common bioinformatics programs such as:
# Standalone BLAST from NCBI
# Clustalw Alignment programs

# A standard sequence class that deals with sequences, ids on sequences, and sequence features.
# Tools for performing common operations on sequences, such as translation, transcription and weight calculations.

# Code to perform classification of data using k Nearest Neighbors, Naive Bayes or Support Vector Machines

# Code for dealing with alignments, including a standard way to create and deal with substitution matrices.

# Code making it easy to split up parallel tasks in to separate processes.

# GUI-based programs to do basic sequence manipulations, translations, BLASTing, etc.
# Extensive documentation and help with using the modules, including this file, online wiki documentation, the website and the mailing list.
# Integration with BioSQL, a sequence database schema..

# Biopython with Entrez

# We will focus on using the web services of the Biopython module in combination with Entrez the NCBI database.
# To be able to use these functions we need the following import:

# import Bio.Entrez as ez
# ez.email = "christoph-knorr@gmx.de"
#
# # with ez.einfo we can get info regarding the databases.
#
# # with ez.einfo() as query:
# #     xml_string = query.read() #
# # with ez.einfo() as query:
# #     parse_dict = ez.read(query)
# #
# # print(xml_string)
# # print(parse_dict["DbList"])
# #
# # with ez.einfo(db="pubmed") as query:
# #     PubMedDict = ez.read(query)
# #
# #
# #
# # print(PubMedDict["DbInfo"].keys())
# # for field in PubMedDict["DbInfo"]["FieldList"]:
# #     print("%(Name)s, %(FullName)s, %(Description)s" % field)
#
# #### Exercise 8 - using ez.einfo
# # Use ez.einfo to make ten different queries about different databases to the NCBI Entrez system
# # Remember you can get a list of databases by using ez.einfo without any parameters to get a list of potential databases.
# # Loop through Dict["DbInfo"]["FieldList"] to see what fields are available to you for searching in these databases
#
# import Bio.Entrez as ez
# ez.email = "christoph-knorr@gmx.de"
#
# with ez.einfo() as query:
#     xml_string = query.read()
#
# with ez.einfo() as query:
#     parse_dict = ez.read(query)
#
# print(xml_string)
# print()
# print(parse_dict["DbList"])
#
# with ez.einfo(db="pubmed") as query:
#     PubMedDict = ez.read(query)
# print()
# print(PubMedDict["DbInfo"].keys())
# print()
# for field in PubMedDict["DbInfo"]["FieldList"]:
#     print("%(Name)s, %(FullName)s, %(Description)s" % field)
#
# with ez.einfo(db="nucleotide") as query:
#     Nucleotide = ez.read(query)
# print(Nucleotide)
#
# print()
# for field in Nucleotide["DbInfo"]["FieldList"]:
#     print("%(Name)s, %(FullName)s, %(Description)s" % field)
#

#### Biopython ESearch

# Biopython allows you to search in the NCBI databases with the ESearch method.

# You can use this method like this:
# import Bio.Entrez as ez
#
# with ez.esearch(db="pubmed", term="biopython[title]", retmax="40" ) as query:
#     record_pub = ez.read(query)
#
# #This term is the search query and you have to add the field you want to be searched (here the title (advanced search option e.g. FieldList or something))
#
#
# import Bio.Entrez as ez
# ez.email = "christoph-knorr@gmx.de"
# with ez.esearch(db="pubmed", term="biopython[title]", retmax="40" ) as query:
#     record_pub = ez.read(query)
# #just returns IDs
# print()
# print(record_pub)
# #with search, just obtain an overview of results
# print()
# if "19304878" in record_pub["IdList"]:
#     print("Your article was found")
# #IdList every article has a specific public id
#
# with ez.esearch(db="nucleotide", term="Cypripedioideae[Orgn] AND matK[Gene]", idtype="acc") as query:
#     record_nuc = ez.read(query)
#
# #idtype = acc (ACCESSIBLE)
#
# print("Here is the Count number: " + str(record_nuc["Count"]))
# print(record_nuc["IdList"])
#
# with ez.esearch(db="nlmcatalog", term="computational[Journal]", retmax="20") as handle:
#     record_jou = ez.read(handle)
#
# print(record_jou["Count"],"computational journals found")
# print("The first 20 are\n",record_jou["IdList"])

#### Exercise 9
#
# import Bio.Entrez as ez
# ez.email = "sjkconline@gmail.com"
#
# with ez.einfo() as query:
#     parse_dict = ez.read(query)
# print(parse_dict["DbList"])
#
#
# list = []
# for db in (parse_dict["DbList"]):
#     with ez.esearch(db=db, term="Vulpes vulpes[title]", retmax="20", idtype="acc") as query:
#         record_nuc = ez.read(query)
#         print("Here is the Count number for " + db + ": " + str(record_nuc["Count"]))
#         list.append("Database " db + ":" + str(record_nuc["Count"]))
# print(list)

#### EPost

# EPost uploads a list of UIs for use in subsequent search strategies, suppose you have a long list of IDs you want to download using EFetch.
# When you make a request with EFetch your list of IDs, the database etc, are all turned into a long URL.
# If your list of IDs is long, this URL gets long, and long URLs can break.
# Instead, you can break this up into two steps, first uploading the list of IDs using EPost
# With the history support, you can then refer to this long list of IDs, and download the associated data with EFetch.

# import Bio.Entrez as ez
# ez.email = "sjkconline@gmail.com"
#
# id_list = ["19304878", "18606172", "16403221", "16377612", "14871861", "14630660"]
# print(ez.epost("pubmed", id=",".join(id_list)).read())
#
# search_results = ez.read(ez.epost("pubmed", id=",".join(id_list)))
# webenv = search_results["WebEnv"]
# query_key = search_results["QueryKey"]
#
#
# #### ESummary
#
# #Retrieves document summaries from a list of primary IDs
# #What kind of information is available to you in the summary depends on the database you are using.
#
# #### Exercise 10 - Creating summaries
# #Use ESummary to create at least 15 different summaries of entries in at least six different databases of the NCBI. What keys are identical and what keys are unique to specific database?
#
#
# import Bio.Entrez as ez
# ez.email = "sjkconline@gmail.com"
#
# id_list = ["19304878", "18606172", "16403221", "16377612", "14871861", "14630660", "79001"]
#
# with ez.einfo() as query:
#     parse_dict = ez.read(query)
# print(parse_dict["DbList"])
#
# for id in id_list:
#     for db in (parse_dict["DbList"]):
#         with ez.esummary(db=db, id=id_list) as handle:
#             record = ez.read(handle)
#
#     print("Journal info\nid:",record[0]["Id"],"\nTitle: ",record[0]["Title"])


#### EGQuery

# e
#
#
#

# import Bio.Entrez as ez
# ez.email = "sjkconline@gmail.com"
# handle = ez.egquery(term="biopython")
# record = ez.read(handle)
# print(record)
# for row in record["eGQueryResult"]:
#     print(row["DbName"], row["Count"])


# import Bio.Entrez as ez
# ez.email = "sjkconline@gmail.com"
# handle = ez.egquery(term="Olfactory Receptor")
# record = ez.read(handle)
# print(record)
# for row in record["eGQueryResult"]:
#     print(row["DbName"], row["Count"])
#
#
# #Eparse
#
# #
# #100
# #
# #
#
# import Bio.Entrez as ez
# ez.email = "christoph-eknorr@gmx.de"
# handle = open("E_coli.xml", "b")
# records = ez.parse(handle)
# for record in records:
#     status = record["Entrezgene_track-info"]["Gene-track"]["Gene-track_status"]
#     if status.attributes["value"]=="discontinued":
#         continue
#     geneid = record["Entrezgene_track-info"]["Gene-track"]["Gene-track_geneid"]
#     genename = record["Entrezgene_gene"]["Gene-ref"]["Gene-ref_locus"]
#     print(geneid, genename)
#

# Exercise 15 - A pipeline

# Create a Pipeline that gives you access to data from one organism.
# Need: PubMed IDsparse_dict
# Sequence Data from protein,nucleotide and gene
#

# E search -  Fetch - Parse results of the fetch methods - save out the ids - create datastructures

import Bio.Entrez as ez

ez.email = "sjkconline@gmail.com"

# Check the list of databases (we are looking for PubMed, protein, nucleotide and gene)
with ez.einfo() as query:
    parse_dict = ez.read(query)
print(parse_dict["DbList"])

with ez.esearch(db="pubmed", term="Vulpes vulpes[title]", retmax="20") as query:
    idealist = ez.read(query)
print(idealist)

seqlist = []
for id in idealist["IdList"]:
    handle = ez.efetch(db="pubmed", id=id, rettype="gb", retmode="text")
    seqlist.append(handle)
print(seqlist)


# with ez.esearch(db="protein", term="Vulpes vulpes[title]", retmax="20") as query:
#      record_pro = ez.read(query)
# print(record_pro)
#
# with ez.esearch(db="nucleotide", term="Vulpes vulpes[title]", retmax="20") as query:
#      record_nuc = ez.read(query)
# print(record_nuc)
#
# with ez.esearch(db="gene", term="Vulpes vulpes[title]", retmax="20") as query:
#      record_gene = ez.read(query)
# print(record_gene["DbInfo"].keys())

#
# print(record_pubmed["DbInfo"].keys())
# print()
# print(protein["DbInfo"].keys())
# print()
# print(nucleotide["DbInfo"].keys())
# print()
# print(gene["DbInfo"].keys())
# print()

# print()
# print("The first 20 are\n",record_pubmed["IdList"])
# print("The first 20 are\n",record_pro["sequence"])
# print("The first 20 are\n",record_nuc["sequence"])
# print("The first 20 are\n",record_gene["sequence"])


# from Bio import SeqIOimport Bio.Entrez as ez
# ez.email = "billyasser@hotmail.co.uk"
# handle = ez.efetch(db="nucleotide", id="NG_042186.1", rettype="gb", retmode="text")
# print(handle.read())
#
# with ez.efetch(db="nucleotide", id="NG_042186.1", rettype="gb", retmode="text") as handle:    record1 = SeqIO.read(handle, "genbank")
# print(record1.id)
#
# with ez.efetch(db="nucleotide", id="NG_042186.1", retmode="xml") as handle:    record2 = ez.read(handle)print(record2[0]["GBSeq_definition"])
#
# print(record2[0]["GBSeq_source"])handle2 = ez.efetch(db="protein", id="NP_002500.1", rettype="fasta", retmode="text")
#
# print(handle2.read())
