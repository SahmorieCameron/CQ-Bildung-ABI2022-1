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
# Now I used a list of PubMed IDs which I can than use to loop over them and
# create my summaries later on
id_list = ["19304878", "18606172", "16403221", "16377612", "14871861", "14630660"]
# Now I initiate a loop over all of my IDs so that I can send queries to the
# Entrez system.
for ids in id_list:
    # For each ID I create a query to the Entrez system with the help of the
    # esummary method. We have to hand over the database we want to use and the
    # corresponding ID so that we can get the summary back
    with ez.esummary(db="pubmed", id=ids) as handle:
        # We use the ez.read() method again here, but this time we have to keep
        # in mind that the resulting dictionary is encapsulated inside a list
        record = ez.read(handle)
    # So now we can print out some information from our summary. To access the
    # values of our dictionary, we have to remember that we are dealing with a
    # list in which our dicitionary was saved. So to access a specific value,
    # we have to use the syntax below record[0] to first be able to access our
    # dictionary and than we add the key, e.g. record[0]["Id"] allows us to
    # access the ID of the database entry whose summary we're currently looking
    # at. It's possible that if you use Esummary in combination with Epost,
    # that the list would than contain dictionaries for all of your entries in
    # the list you handed over to Epost.
    print("Journal info\nid:", record[0]["Id"], "\nTitle: ", record[0]["Title"])

#### EFetch

"""
This is the example script for fetching data from the NCBI databases with the
help of Biopython. There are at least three different ways to get data from
these databases. I wuill explain all three of them here, but I personally
prefer using the last one, which creates a dictionary.
"""

from Bio import SeqIO
import Bio.Entrez as ez

ez.email = "christoph-knorr@gmx.de"

handle = ez.efetch(db="nucleotide", id="EU490707", rettype="gb", retmode="text")

print(handle.read())
print("")

with ez.efetch(db="nucleotide", id="EU490707", rettype="gb", retmode="text") as handle:

    record1 = SeqIO.read(handle, "genbank")
print("Our Seqreader object looks like this:\n", record1)

print("The ID of our entry is:", record1.id)
print("The Sequence of our entry is:\n", record1.seq)
print("")

with ez.efetch(db="nucleotide", id="NM_006852", retmode="xml") as handle:
    record2 = ez.read(handle)
print("The definition for this entry is:\n", record2[0]["GBSeq_definition"])
print("This entry stems from:", record2[0]["GBSeq_source"])
print("The sequence for this Entry is:\n", record2[0]["GBSeq_sequence"])


#### ELink

"""
This is the exampl program for the Elink method, to show you how you can find
related entries in different databases. I included two examples one for PubMed
and one for a specific nucleotide entry
"""
# First we import Entrez
import Bio.Entrez as ez

# Now we hand over our E-Mail again.
ez.email = "christoph-knorr@gmx.de"
# Now I define a specific PubMed ID I want ot use for finding crosslinks
pmid = "19304878"
# To find cross links I need the elink method which I give the database I want
# to search in (db), the database my id stems from (dbfrom) and the ID (id)
# I want to search for. per default db and dbfrom are set to pubmed, so you
# could run the example below without specifying anything. So in the Example
# below we only search in the PDB for related entries to our Paper.
record = ez.read(ez.elink(db="pubmed", dbgrom="pubmed", id=pmid))
# The Key "LinkSetDb" contains all the IDs of entries that are linked to our
# handed over ID. So we can look at all the cross links with this key. The IDs
# you can see are other PubMed IDs so you can access the different papers with
# them later on.
print("The links for our first search are:\n", record[0]["LinkSetDb"])
print("")
# The second exampel I prepared searches for cross links in the PubMed by using
# an ID from nucleotide. So now we get citations that are related to our
# nucleotide entry.
record2 = ez.read(ez.elink(db="pubmed", dbfrom="nucleotide", id="NM_006852"))
print("The links for our second search are:\n", record2[0]["LinkSetDb"])
