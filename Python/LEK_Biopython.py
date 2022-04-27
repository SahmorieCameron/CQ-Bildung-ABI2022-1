#### LEK Biopython

#### Einfo
import Bio.Entrez as ez

ez.email = "sjkconline@gmail.com"
with ez.einfo() as query:
    parse_dict = ez.read(query)
print("These are the available databases:\n", parse_dict["DbList"])

#### ESearch

import Bio.Entrez as ez

ez.email = "sjkconline@gmail.com"
with ez.esearch(db="nucleotide", term="Caretta caretta[title]", retmax="40") as query:
    record_nuc = ez.read(query)
print("The result of the nucleotide search looks like this:\n", record_nuc)

#### ESummary


import Bio.Entrez as ez

ez.email = "sjkconline@gmail.com"
id_list = ["32080298", "34438892", "31988720"]
for ids in id_list:
    with ez.esummary(db="pubmed", id=ids) as handle:
        record = ez.read(handle)
    print("Journal info\nid:", record[0]["Id"], "\nTitle: ", record[0]["Title"])

#### EFetch

from Bio import SeqIO
import Bio.Entrez as ez

ez.email = "sjkconline@gmail.com"
handle = ez.efetch(db="pubmed", id="32080298", rettype="gb", retmode="text")
print(handle.read())
print("")

#### ELink
import Bio.Entrez as ez

ez.email = "sjkconline@gmail.com"
pmid = "32080298"
record = ez.read(ez.elink(db="pubmed", dbgrom="pubmed", id=pmid))
print("The links for our first search are:\n", record[0]["LinkSetDb"])
print("")
