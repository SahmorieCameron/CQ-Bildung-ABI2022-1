import Bio.Entrez as ez
ez.email = "christoph-knorr@gmx.de"
handle = ez.egquery(term="biopython")
record = ez.read(handle)
for row in record["eGQueryResult"]:
    print(row["DbName"], row["Count"])