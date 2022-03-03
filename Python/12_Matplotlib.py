import pickle, random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  # alias for matplot, so you don't have to keep typing the full name out

(Gammas, Dists, Dia) = pickle.load(open("New.pickle", "rb"))

Dir2 = "MBD"

#### Histograms
plt.figure(figsize=[11, 6])  # opens a simple canvas on which we can create our plot
plt.hist(
    Gammas, range=[0, 180], bins=90, facecolor="0.75", edgecolor="k"
)  # creates a histogram, define the range, everything out of the range isn't included on the histogram
plt.xticks(
    [0, 30, 60, 90, 120, 150, 180], fontsize=25, rotation=90
)  # from this line of code, everything is for aesthetic purposes
plt.xlim([0, 180])
plt.yticks(fontsize=25)
plt.grid(axis="y")  # adding grid lines (here only for the y axis.)
plt.xlabel(r"$\gamma$-Winkel [Â°]", fontsize=25)
plt.ylabel("Anzahl", fontsize=25)
plt.title((r"$\gamma$-Winkel Kation-$\pi$ " + Dir2), y=1.02, fontsize=25)
plt.tight_layout()
plt.savefig(("Gamma_" + Dir2 + ".png"))
plt.close()

plt.figure(figsize=[11, 6])
plt.hist(Dists, range=[3.4, 6], bins=27, facecolor="0.75", edgecolor="k")
plt.xticks([3.4, 4.05, 4.7, 5.35, 6], fontsize=25, rotation=90)
plt.xlim([3.4, 6])
plt.yticks(fontsize=25)
plt.grid(axis="y")
plt.xlabel("Abstand Aromat Kation [Ã…]", fontsize=25)
plt.ylabel("Anzahl", fontsize=25)
plt.title(("AbstÃ¤nde Aromat Kation " + Dir2), y=1.02, fontsize=25)
plt.tight_layout()
plt.savefig(("Distance_" + Dir2 + ".png"))
plt.close()


#####Scatterplot
plt.figure(figsize=[11, 6])
plt.plot(Dia["DG"][0], Dia["DG"][1], "k.")
plt.yticks([0, 30, 60, 90, 120, 150, 180], fontsize=25)
plt.ylim([0, 180])
plt.xticks([3.4, 4.05, 4.7, 5.35, 6], fontsize=25, rotation=90)
plt.xlim([3.4, 6])
plt.grid()
plt.ylabel(r"$\gamma$-Winkel [Â°]", fontsize=25)
plt.xlabel("Abstand Aromat Kation [Ã…]", fontsize=25)
plt.title((r"Abstand gegen $\gamma$-Winkel " + Dir2), y=1.02, fontsize=25)
plt.tight_layout()
plt.savefig(("Distance_Gamma_" + Dir2 + ".png"))
plt.close()

Values = np.ones(20)
Values2 = np.ones(20)
Values3 = np.ones(20)
for i in range(len(Values)):
    Values[i] = Values[i] * random.randint(1, 8) * random.random()
    Values2[i] = Values2[i] * random.randint(1, 8) * random.random()
    Values3[i] = Values3[i] * random.randint(1, 8) * random.random()
plt.figure(figsize=[10, 10])
plt.bar(np.arange(20), Values)
plt.title("Example Barplot", fontsize=25)
plt.xlabel("Contesdant Nr", fontsize=25)
plt.ylabel("Mark", fontsize=25)
plt.xlim([-1, 20])
plt.ylim([0, 8])
plt.yticks(np.arange(9), fontsize=25)
plt.xticks(np.arange(20), fontsize=20, rotation=45)
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("Barplot_Example.png")
plt.close()

Values.sort()
Values2.sort()
Values3.sort()

plt.figure(figsize=[10, 10])
plt.plot(np.arange(20), Values)
plt.plot(np.arange(20), Values2, "r.", markersize=15)
plt.plot(np.arange(20), Values3, "*g--", markersize=15)
plt.title("Example Scatterplot", fontsize=25)
plt.xlabel("Contesdant Nr", fontsize=25)
plt.ylabel("Mark", fontsize=25)
plt.xlim([-1, 20])
plt.ylim([0, 8])
plt.yticks(np.arange(9), fontsize=25)
plt.xticks(np.arange(20), fontsize=20, rotation=45)
plt.grid()
plt.tight_layout()
plt.savefig("Example_Plot.png")
plt.close()
