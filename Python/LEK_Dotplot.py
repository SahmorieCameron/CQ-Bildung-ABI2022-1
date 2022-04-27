import numpy as np
import pylab as pl

window = 2
Count = 0
Error = 0
seq1 = "AGTTGT"
seq2 = "AGTTTGG"
x = []
y = []

for i in range(len(seq1)):
    for j in range(
        len(seq2)
    ):  # Loops over each letter of the first sequence, then all the letters of the second sequence

        if seq1[i : i + 2] == seq2[j : j + 2]:
            for k in range(len(seq1[i : i + window])):
                if i + k < len(seq1) and j + k < len(seq2):
                    if seq1[i + k] == seq2[j + k]:
                        Count += 1
            if window - Count <= Error:
                x.append(i)
                y.append(j)
# compares bp to one another. If they match they are appended to the lists.

pl.plot(x, y, ".k")  # .k = black dots
pl.title("Sequence comparison dotplot")
pl.xlabel("base [sequence 1]")
pl.xticks(np.arange(len(seq1)), seq1)
pl.xlim(left=-1, right=len(seq1))
pl.ylabel("base [sequence 2]")
pl.yticks(np.arange(len(seq2)), seq2)
pl.ylim(bottom=-1, top=len(seq2))
pl.gca().invert_yaxis()
pl.gca().xaxis.tick_top()
pl.gca().xaxis.set_label_position("top")
pl.show()
print(x)
print(y)
