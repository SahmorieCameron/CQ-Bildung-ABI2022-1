#### XML

# ▪ Extensible Mashup language
# ▪ Similar to HTML, but without predefined tags to use
# ▪ A powerful way to store data in a format that can be stored,
# searched and shared
# ▪ The fundamental format is standardized so it can be parsed
# on any system

#### XML Example
<?xml version="1.0" encoding="UTF-8"?>
<message>
    <warning>
        Hello World
    </warning>
</message>

XML Elements

▪ Value
 Data to be saved
 In XML atomic (not separable)
 Text
▪ Tag
 Structure element for values or other tags

#### XML Tags
<name>Christoph Knorr </name>

<GivenName>Christoph</GivenName><LastName>Knorr</LastName>
Or
<GivenName>Christoph</GivenName>
<LastName>Knorr</LastName>

<person>
    <GivenName>Christoph</GivenName>
    <LastName>Knorr</LastName>
</person>

#### XML Tag Rules

One tag can contain as many under tags as you want or
exactly one value!

#### Example (Music)

▪ We want to safe information about Beethoven‘s 10th
symphony and Let it Be from the Beatles
▪ For each track we want safe the title, the length in seconds,
the genre and the name of the componist (given and last)
▪ We will do it in XML

<tracks>
</tracks>

<tracks>
    <track>
    </track>
</tracks>

<tracks>
    <track>
        <Length>666</Length>
        <title>Beethoven‘s 10th symphony</title>
        <genre>Classic</genre>
        <componist></componist>
    </track>
</tracks>

<tracks>
    <track>
        <Length>666</Length>
        <title>Beethoven‘s 10th symphony</title>
        <genre>Classic</genre>
        <componist>
            <name>
                <Given>Ludwig</Given>
                <Last>Beethoven</Last>
                <title>von</title>
            </name>
        </componist>
    </track>
</tracks>

#### Empty Tags

# ▪ You can include empty tags in you XML documents
# ▪ There is a short listing for this
# ▪ <tagname/>

#### Exercise 2 – Music Albums

# ▪ You want to categorize your music albums
# ▪ For each album you want to write down the title, the artist,
# the runtime and a list of tracks
# ▪ For each track you want to safe the name, the runtime and
# the number of stars you would give it (0 to 5)
# ▪ Do this for two albums

#### Attributes

# ▪ Additions in attribute names to supplement the tag
# ▪ Standard form: attribute name = value
# ▪ For example you should hand over the units as a an
# attribute <Length unit=„s“>
# ▪ Are written in the opening tag, you can add as many as you
# want there

#### Exercise 3 - Book catalog

# ▪ A publisher wants to safe his book list
# ▪ The list should contain the title of the book, the MSRP
# (UVP), the ISBN, the author, a chapter list with short
# descriptions of the chapters and the genre
# ▪ The saved file should also include the day on which it was
# saved
# ▪ Create the general structure of this XML file with the
# corresponding tags and attributes
# ▪ Write down the details for at least two books

#### Exercise 4 – Protein structures

# ▪ Create an XML structure for saving information about the
# structure of different proteins
# ▪ It should include the isoelectric point, the molecular weight,
# the name and its synonyms as well as the sequences
# ▪ Furthermore it should tell on which positions in the structure
# secondary structure elements (α-Helix and β-Strand) can be
# found

#### Parsing XML

# ▪ SAX ➔ Simple Api for XML
#  Standard parser for all XML files
# ▪ DOM ➔ Document object model
#  Standard parser for XML files
#  Standard parser for XML manipulation
# ▪ Parsing by hand with String manipulation
#  Possible for all XML files
#  Has to be developed by us
# ▪ Specialised Parser
#  Only usable for special XML-files (Bio.Entrez for NCBI files)

#### Dom

# ▪ The XML DOM (Document Object Model) class is an inmemory representation of an XML document
# ▪ Allows you to programmatically read, manipulate, and
# modify an XML document
# ▪ Editing is the primary function

#### TBC...
