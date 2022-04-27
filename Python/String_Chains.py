#### Working with string chains in Python
#
# Applications
#
# Need to know how to work with string chains for numerous applications
# e.g. Dot Plots, Alignments, Searching databanks
#
#### Contents
#
# -How to work with strings
# -Homology - the phylogenetic tree of genes
# -Dotplots - simple graphical similarity searches
#
#### Definitions
#
# Alphabets
#    Σdna = {A,G,C,T} ; for nucleotides
#    Σamino = {A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y}; for amino acids.

# Each Element E of an alphabet is named symbol or letter.
# String S is a juxtaposition of symbols from the alphabet.
# Sigma
#   S = (EΣ) (An order of symbols is defined)
#   e.g. S = "ATGGAATGCTAATAG"
#
# Definitions (cont)
#
# Position Si is the letter E on position i in the string (strats at position 0!)
#
# Substring Sij are the letters from position Si to Sj
#
# Length N of a string is the number of letters
#
# Split Spliti is the splitting of a string in two substring at position i.
# Two new strings S0i and SiN are created.
#
# Split SplitDelimitor is the splitting of a string multiple substrings divided at the delimitor.
# The number of substrings is equal to the number of occurences of the delimitor +1
#
# Prefix is a substring of a string with which the string starts.
# Suffix is a substring of a string with which the string ends.
#
#### Python Position Si
#
# S = "Examplestring"
#
# S[0] = "E"
#
# S[1] = "x"
#
# S[2] = "a"
#
# etc...

#### Python Substring Sij

# S = "Examplestring"
#
# Sub = S[2:5] = "amp"
# Sub = S[:5] = "Examp"
# Sub = S[2:] = "amplestring"

#### Python Length N
#
# s = "Examplestring"
# Length = len(s)  # length = 13
#
# #### Python Prefix
#
# s = "Examplestring"
# prefixone = s[:0]  # prefixone = ""
# prefixtwo = s[:1]  # prefixtwo = "E"
# prefixthree = s[:2]  # prefixthree = "x"
# # etc
# S1 = "This string is an example"
# print(S1[:0])
# print(S1[:1])
# print(S1[:2])
# print(S1[:3])
# print(S1[:4])
# print("")
#
# #### Python Split SplitDelimitor
#
# S = "This is a test"
# List = s.split()  # list = ["This","is","a","test"]
# List = s.split(",")  # list = ["This is a test"]
#
# S = "This,is,a,test"
# List = s.split(",")  # list = ("This","is","a","test")
#
# S1 = "This string is an example"
# S2 = "Another example for a long string"
# S3 = " A third example for a string, this time with punctuation!"
#
# Sp1 = S1.split()
# Sp2 = S2.split()
# Sp3 = S3.split()
# print(Sp1)
# print(Sp2)
# print(Sp3)
# print("")
#
# Sp4 = S1.split(",")
# Sp5 = S2.split(",")
# Sp6 = S3.split(",")
# print(Sp4)
# print(Sp5)
# print(Sp6)
# print("")
#
# #### Python find occurences
# # Case sensitive
# print("Find occurences")
#
# S = "This is a test"
# F = S.find("s")  # F = 3
#
# S1 = "This string is an example"
# S2 = "Another example for a long string"
# S3 = " A third example for a string, this time with punctuation!"
#
# print(S1.find("a"))
# print(S2.find("a"))
# print(S3.find("a"))
# print("")
#
# # If your find finds no result, the output = -1
#
# #### The module re
#
# import re
#
# S1 = "This string is an example"
# S2 = "Another example for a long string"
# S3 = " A third example for a string, this time with punctuation!"
#
# Sp7 = re.split(" |,|;", S1)
# Sp8 = re.split(" |,|;", S2)
# Sp9 = re.split(" |,|;|!", S3)
# print(Sp7)
# print(Sp8)
# print(Sp9)
# print("")
#
# #
#
# I1 = [m.start() for m in re.finditer("a", S1)]
# I2 = [m.start() for m in re.finditer("a", S2)]
# I3 = [m.start() for m in re.finditer("a", S3)]
# print(I1)
# print(I2)
# print(I3)
#
# #### Is something in a string
#
# print("Is something in a string?")
# # True or false statement, doesn't give positional information.
#
# s3 = " "
#
# S1 = "This string is an example"
# S2 = "Another example for a long string"
# S3 = " A third example for a string, this time with punctuation!"
#
# print("string" in S1)
# print("string" in S2)
# print("string" in S3)
# print("")
#
# if "string" in S1:
#     print("This word is in your first string, brilliant")
# if "string" in S2:
#     print("This word is in your second string, brilliant")
# if "string" in S2:
#     print("This word is in your third string, brilliant")
#
# # Another example
#
# print("an ex" in S1)
# if "an ex" in S1:
#     print("This word is in your string, brilliant")

# S1 = "This string is an example"
# S2 = "Another example for a long string"
# S3 = " A third example for a string, this time with punctuation!"
#
# print(len(S1))
# print(len(S2))
# print(len(S3))
# print("")
#
# for i in range(len(S1)):
#     print(S1[i], S2[i], S3[i])
# print("")
#
# print(S1[5:20])
# print(S2[5:20])
# print(S3[5:20])
# print("")

#### Exercise 1 - Working with Strings

# print("Exercise 1")

# Take the “lorem ipsum” String from down below and use it as a variable in Python. Complete
# the following tasks:
# 1. How long is this text?
# 2. How many words are in this text? (split and len)
# 3. How often does each letter of the alphabet occur in this text? (re, len and a loop)
# 4. Are the words minim, anim, caesar, brutus and duis in the string?

# SE = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
#
# # 1.
# print(f"This text is {len(SE)} long")
#
# # 2.
# SpE = SE.split()
# print(f"This text has {len(SpE)} words")
#
# # 3.
# out = {x: SE.count(x) for x in set(SE)}
# print("Occurrence of all characters in our text is :\n " + str(out))
#
# # 4.
#
# I1 = [m.start() for m in re.finditer("minim", SE, re.IGNORECASE)]
# print(I1)
# I2 = [m.start() for m in re.finditer("anim", SE, re.IGNORECASE)]
# print(I2)
# I3 = [m.start() for m in re.finditer("caesar", SE, re.IGNORECASE)]
# print(I3)
# I4 = [m.start() for m in re.finditer("brutus", SE, re.IGNORECASE)]
# print(I4)
# I5 = [m.start() for m in re.finditer("duis", SE, re.IGNORECASE)]
# print(I5)

#### Modifying strings

# upper() returns the string in upper case
# lower() returns the string in lower case
# strip() removes whitespaces at the beginning or the end of the string
# replace(„H“,“J“) replaces a string with another strin

#### Concatenating Strings

#  We can combine strings simply by using a „+“ operator
# S1 = "This string is an example"
# S2 = "Another example for a long string„
# S4 = S1 + S2
# S4  "This string is an exampleAnother
# example for a long string"

#### Adding numbers to strings

#  We can combine strings simply by using a „+“ operator
# S1 = "This string is an example"
# S2 = "Another example for a long string„
# S4 = S1 + S2
# S4  "This string is an exampleAnother
# example for a long string"

# I1 = 4
# S5 = „This string contains „ + str(I1) + „ words“
# S6 = „This string contains {} words“
# print(S6.format(I1)
#
# I1 = 4
# S7 = "This string contains {} words"
# print(S7.format(I1))
# I2 = 3
# I3 = 567
# F1 = 49.95
# S8 = "I want {} pieces of item {} for {} dollars."
# print(S8.format(I2, I3, F1))
# S9 = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(S9.format(I2, I3, F1))
# print("")


#### Exercise 2 - A bit more about strings

# Take the “lorem ipsum” string from Exercise 01 – Working with Strings and complete the
# following tasks:

# 1. Replace the strings et, in and eu with at, on and au.
# 2. Create a all lower case and a all upper case variant of it.
# 3. Split the text in it’s words and concatenate them together again. (split and a loop)

# SE2 = str(SE)
#
# # 1.
# print(SE2.replace("et", "at"))
# print(SE2.replace("in", "on"))
# print(SE2.replace("eu", "au"))
# print("")
#
# # 2.
# print(SE2.upper())
# print(SE2.lower())
#
# # 3.
# SpE2 = SE2.split()
# print(SpE2)
# S4 = S1 + S2
#
# # 4.
# Xstring = ""
# for string in SpE2:
#     Xstring = Xstring + " " + string
#
# print(Xstring)
#

#### Parsing a file

# Inputs of bioinformatics programs are often from text files or similar things
# Not all information contained in the file are always necessary for the handling of the problem
# You want to pick only the information you really need
# This process is called parsing
# Parsing requires the file to follow a specific format

#### Example: Fasta file

#  Fasta files are used to save and relay raw sequences
#  Have the ending .fasta
#  Are built very easily:
#  In one line stand either the name of the sequence or the sequence itself
#  If the line contains the name of the sequence it starts with “>”
#  The next line contains the sequence

#### Example FASTA

# >Sequence1
# THISISASEQUENCE
# >Sequence2
# THISISANOTHERSEQUENCE

#### Input operations Python

#  You have to read a file before you can use the data
#  File = open(“Test.txt”, “r”)
#  Opens the file and outputs an object of the type file
#  The first argument is always the filename
#  The second argument defines in what modus the file should
# be opened
#  “r”: read
#  “w”: write – contents are overwritten
#  “a”: append – contents are appended

#### Create a list from a file

# Lines = File.readlines()
# File:
#     >Sequence1
#     THISISASEQUENCE
# Lines:
#     [“>Sequence1”,” THISISASEQUENCE”]

#### HOW-TO PARSING

# Read the file
# Generate a list with the rows
# Iterate over the list
# Disassemble the rows according to format so that only the necessary information is retained – Know the format

#### Exercise 03 – Create a Suffix array
# 1. Read the file “Unknown.fasta”
# 2. Generate a list of the rows of this file
# 3. Read out only the sequences and save them in a list “sequences”
# 4. For each sequence create a list which contains all suffixes
# 5. Sort this lists

"""
The program consists of three blocks of code, i want to explain here in the
beginning so that the comments don't split up the program too much.
In the first block we open our file and than use the readlines() method to
create a list that contains all lines of our file. So each entry in our list
is on line of our file. That means our list contains 1000 entries. Don't forget
to close the file afterwards.
"""

# # 1.
# myfile = open("/home/cq/CQ-Bildung-ABI2022-1/Python/Unknown.fasta.txt", "r")
# lines = myfile.readlines()
# myfile.close()
# print(len(lines))

"""
In the second block we loop over all lines and filter for lines that don't
contain a ">" at the first position. Since we know we are working with a fasta
file we know that sequences are only in lines that start with a letter and not
with the ">" symbol. The result is a list called seqlist with 500 entries, one
for each sequence.
"""

# seqlist = []
# for line in lines:
#     if line[0] != ">":
#         seqlist.append(line.replace("\n", ""))
# print(len(seqlist))
# print(seqlist)

"""
In the last block we create our suffix array. We loop over our seqlist to work
on each sequence in order. I used an Array in which I collect my output, so I
have to create an empty list inside my dictionary for each sequence. Than I can
initialize a second loop inside the first one, that loops over the length of the
sequence. I append my empty list with the suffixes by using the statement
seqlist[i][-j:]. This statement takes the current sequence seqlist[i] and slices
it from the position -j (so -1, -2, -3 and so on) until the end. By appending
these slices to my suffix array I can collect all suffixes. I even added a
version in which I collect all suffixes of all sequences in one list, to check
if I run into any problems with my RAM.
"""

# Sufarray = {}
# Test = []
# for i in range(len(seqlist)):
#     Sufarray[i] = []
#     for j in range(len(seqlist[i])):
#         Sufarray[i].append(seqlist[i][-j:])
#         Test.append(seqlist[i][-j:])
#     Sufarray[i].sort()
# Test.sort()
# print(len(Test))
#
#
# #### Exercise 4 - Protein sequences
#
# # Until now we only looked at nucleotide sequences. You got a zip file that contains 6 files with
# # amino acid sequences.
# # Applied Bioinformatics
# # 1. How long is each sequence?
# # 2. How often does each of the 20 canonic amino acids appear in each sequence?
# # 3. What is the percentage distribution for the 20 canonic amino acids in these sequences?
# # 4. Search for repeating amino acids in the sequences, e:g. EE or LL.
#
# Prot1 = open(
#     "/home/cq/CQ-Bildung-ABI2022-1/Python/Mystery_Proteins/Mystery Protein1.txt.txt",
#     "r",
# )
# Prot2 = open(
#     "/home/cq/CQ-Bildung-ABI2022-1/Python/Mystery_Proteins/Mystery Protein2.txt.txt",
#     "r",
# )
# Prot3 = open(
#     "/home/cq/CQ-Bildung-ABI2022-1/Python/Mystery_Proteins/Mystery Protein3.txt.txt",
#     "r",
# )
# Prot4 = open(
#     "/home/cq/CQ-Bildung-ABI2022-1/Python/Mystery_Proteins/Mystery Protein4.txt.txt",
#     "r",
# )
# Prot5 = open(
#     "/home/cq/CQ-Bildung-ABI2022-1/Python/Mystery_Proteins/Mystery Protein5.txt.txt",
#     "r",
# )
# Prot6 = open(
#     "/home/cq/CQ-Bildung-ABI2022-1/Python/Mystery_Proteins/Mystery Protein6.txt.txt",
#     "r",
# )
#
# Prot1liens = Prot1.readlines()
# print(Prot1liens)
#
#
# # 2.
#
#
# out = {x: str(Prot1liens).count(x) for x in set(str(Prot1liens))}
# print("Occurrence of all characters in our text is :\n " + str(out))


# if "string" in S1:
#     print("This word is in your String, Genius")
# if "string" in S2:
#     print("This word is in your String, Genius")
# if "string" in S3:
#     print("This word is in your String, Genius")
# print("")
#
# print(S1.upper())
# print(S2.upper())
# print(S3.upper())
# print("")
#
# print(S1.lower())
# print(S2.lower())
# print(S3.lower())
# print("")
#
# print(S3.strip())
# print("")
#
# print(S1.replace("s", "W"))
# print(S2.replace("s", "W"))
# print(S3.replace("s", "W"))
# print("")
#
# S4 = S1 + S2
# S5 = S1 + S3
# S6 = S2 + S3
# print(S4)
# print(S5)
# print(S6)
# print("")


#### Exercise 5 - Bioinformatic files

# with open("455373.gb", "r") as file:
#     lines = file.readlines()
#     for row in file:
#         print(row)
#
# print(lines)

import re

Proteinbank = {}
Proteinbank["C-alpha"] = {}
seqsum = []
alphasum = []

with open("1kim.pdb", "r") as proteindb:
    lines = proteindb.readlines()
    for line in lines:
        if line[0:6] == "SEQRES":
            seqsum.append(line)
            Proteinbank["Sequence"] = seqsum
        if line[13:15] == "CA":
            if line[21] not in Proteinbank["C-alpha"]:
                alphasum = []
            alphasum.append(line[23:26])
            Proteinbank["C-alpha"][line[21]] = alphasum

print(Proteinbank)


####################

ResultsPDB = {}
ResultsGB = {}

with open("1kim.pdb", "r") as file:
    for row in file:
        if row.find("ATOM") == 0:
            Entries = row.split()
            if Entries[4] not in ResultsPDB:
                ResultsPDB[Entries[4]] = {}
            if Entries[2] == "CA":
                ResultsPDB[Entries[4]][Entries[5]] = Entries[3]

with open("455373.gb", "r") as file:
    Lines = file.readlines()
    for i in range(len(Lines)):
        if Lines[i].find("ACCESSION") == 0:
            ResultsGB["Accession"] = Lines[i].split()[1]
        if Lines[i].find("DBSOURCE") == 0:
            Entries = Lines[i].split()
            String = ""
            for elem in Entries[1::]:
                String += elem + " "
            ResultsGB["Database"] = String
        if Lines[i].find("AUTHORS") == 2:
            ResultsGB["Authors"] = Lines[i][9::].strip()
            j = 1
            while Lines[i + j].find("TITLE") != 2:
                ResultsGB["Authors"] += " " + Lines[i + j][9::].strip()
                j += 1
        if Lines[i].find("TITLE") == 2:
            ResultsGB["Title"] = Lines[i][9::].strip()
            j = 1
            while Lines[i + j].find("JOURNAL") != 2:
                ResultsGB["Title"] += " " + Lines[i + j][9::].strip()
                j += 1
        if Lines[i].find("JOURNAL") == 2:
            ResultsGB["Journal"] = Lines[i][9::].strip()
            j = 1
            while Lines[i + j].find("PUBMED") != 3:
                ResultsGB["Journal"] += " " + Lines[i + j][9::].strip()
                j += 1
        if Lines[i].find("PUBMED") == 3:
            ResultsGB["Pubmed"] = Lines[i][9::].strip()
        if Lines[i].find("ORIGIN") == 0:
            ResultsGB["Sequence"] = ""
            j = 1
            while Lines[i + j].find("//") != 0:
                for elem in Lines[i + j].split()[1:]:
                    ResultsGB["Sequence"] += elem.upper()
                j += 1

print(ResultsPDB)
print(ResultsGB)
