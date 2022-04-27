from Bio import pairwise2
from Bio import SeqIO
from Bio import Align
from Bio.Align import substitution_matrices

seq1 = SeqIO.read("/home/cq/CQ-Bildung-ABI2022-1/Python/Fasta/alpha.faa", "fasta")
seq2 = SeqIO.read("/home/cq/CQ-Bildung-ABI2022-1/Python/Fasta/beta.faa", "fasta")
seq3 = SeqIO.read("/home/cq/CQ-Bildung-ABI2022-1/Python/Fasta/delta.faa", "fasta")
seq4 = SeqIO.read("/home/cq/CQ-Bildung-ABI2022-1/Python/Fasta/epsilon.faa", "fasta")
seq5 = SeqIO.read("/home/cq/CQ-Bildung-ABI2022-1/Python/Fasta/gamma.faa", "fasta")
seq6 = SeqIO.read("/home/cq/CQ-Bildung-ABI2022-1/Python/Fasta/zeta.faa", "fasta")

mpseq1 = SeqIO.read(
    "/home/cq/CQ-Bildung-ABI2022-1/Python/Mystery_Proteins/Mystery Protein1.txt.txt",
    "fasta",
)
mpseq2 = SeqIO.read(
    "/home/cq/CQ-Bildung-ABI2022-1/Python/Mystery_Proteins/Mystery Protein2.txt.txt",
    "fasta",
)
mpseq3 = SeqIO.read(
    "/home/cq/CQ-Bildung-ABI2022-1/Python/Mystery_Proteins/Mystery Protein3.txt.txt",
    "fasta",
)
mpseq4 = SeqIO.read(
    "/home/cq/CQ-Bildung-ABI2022-1/Python/Mystery_Proteins/Mystery Protein4.txt.txt",
    "fasta",
)
mpseq5 = SeqIO.read(
    "/home/cq/CQ-Bildung-ABI2022-1/Python/Mystery_Proteins/Mystery Protein5.txt.txt",
    "fasta",
)
mpseq6 = SeqIO.read(
    "/home/cq/CQ-Bildung-ABI2022-1/Python/Mystery_Proteins/Mystery Protein6.txt.txt",
    "fasta",
)

alignments1 = pairwise2.align.globalxx(seq1.seq, seq2.seq)
alignments2 = pairwise2.align.globalxx(seq1.seq, seq3.seq)
alignments3 = pairwise2.align.globalxx(seq1.seq, seq4.seq)

mpalignments1 = pairwise2.align.globalxx(mpseq1.seq, mpseq2.seq)
mpalignments2 = pairwise2.align.globalxx(mpseq1.seq, mpseq3.seq)
mpalignments3 = pairwise2.align.globalxx(mpseq1.seq, mpseq4.seq)

print(max([elem.score for elem in alignments1]))
print(max([elem.score for elem in alignments2]))
print(max([elem.score for elem in alignments3]))

print(max([elem.score for elem in mpalignments1]))
print(max([elem.score for elem in mpalignments2]))
print(max([elem.score for elem in mpalignments3]))

print(len(alignments1))
print(len(alignments1))
print(len(alignments1))

print(alignments1)
print(alignments1)
print(alignments1)

print(alignments1[0])
print(alignments1[0])
print(alignments1[0])

blosum62 = substitution_matrices.load("BLOSUM62")
alignments4 = pairwise2.align.globalds(seq1.seq, seq2.seq, blosum62, -10, -0.5)

print(len(alignments4))
print(alignments4)
print(alignments4[0])
#
alignments5 = pairwise2.align.localds("LSPADKTNVKAA", "PEEKSAV", blosum62, -10, -1)
print(pairwise2.format_alignment(*alignments5[0]))
print(pairwise2.format_alignment(*alignments5[0], full_sequences=True))

aligner = Align.PairwiseAligner()
aligner = Align.PairwiseAligner(match_score=1.0)


alignments6 = aligner.align(seq1.seq, seq2.seq)
print(len(alignments6))

for alignment in alignments6:
    print(alignment)
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
score = aligner.score(seq1.seq, seq2.seq)
print(score)

alignments7 = aligner.align(seq1.seq, seq2.seq)
print(len(alignments7))
