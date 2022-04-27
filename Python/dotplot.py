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

# Exercise 6 - Dotplots in Python

# myfile = open("/home/cq/CQ-Bildung-ABI2022-1/Python/Unknown.fasta.txt", "r")
# lines = myfile.readlines()
# myfile.close()
# # print(len(lines))
# # print(lines)
#
# print(lines[1])
# print(lines[3])
#
# seq1 = lines[1]
# seq2 = lines[3]
#
# x = []
# y = []
#
# for i in range(len(seq1)):
#     for j in range(
#         len(seq2)
#     ):  # Loops over each letter of the first sequence, then all the letters of the second sequence
#         if (
#             seq1[i] == seq2[j]
#         ):  # compares bp to one another. If they match they are appended to the lists.
#             x.append(i)
#             y.append(j)
#
# pl.figure(figsize=[11, 6])
# pl.plot(x, y, ".k")  # .k = black dots
# pl.title("Sequence comparison dotplot")
# pl.xlabel("base [sequence 1]")
# pl.xticks(np.arange(len(seq1)), seq1)
# pl.xlim(left=-1, right=len(seq1))
# pl.ylabel("base [sequence 2]")
# pl.yticks(np.arange(len(seq2)), seq2)
# pl.ylim(bottom=-1, top=len(seq2))
# pl.gca().invert_yaxis()
# pl.gca().xaxis.tick_top()
# pl.gca().xaxis.set_label_position("top")
# # pl.savefig("Dotplot.png")
# pl.show()
# print(x)
# print(y)

# Exercise 7 -

# Exercise 8 -

# ▪ In the two previous exercises you worked with nucleotide
# sequences for your Dotplots
# ▪ Now adapt your program so that it can work on the protein
# sequences from your zip-file
# ▪ Keep in mind that these sequences have different lengths.

myfile1 = open(
    "/home/cq/CQ-Bildung-ABI2022-1/Python/Mystery_Proteins/Mystery Protein1.txt.txt",
    "r",
)
myfile2 = open(
    "/home/cq/CQ-Bildung-ABI2022-1/Python/Mystery_Proteins/Mystery Protein2.txt.txt",
    "r",
)
myfile3 = open(
    "/home/cq/CQ-Bildung-ABI2022-1/Python/Mystery_Proteins/Mystery Protein3.txt.txt",
    "r",
)
myfile4 = open(
    "/home/cq/CQ-Bildung-ABI2022-1/Python/Mystery_Proteins/Mystery Protein4.txt.txt",
    "r",
)
myfile5 = open(
    "/home/cq/CQ-Bildung-ABI2022-1/Python/Mystery_Proteins/Mystery Protein5.txt.txt",
    "r",
)
myfile6 = open(
    "/home/cq/CQ-Bildung-ABI2022-1/Python/Mystery_Proteins/Mystery Protein6.txt.txt",
    "r",
)

lines1 = myfile1.readlines()
seqlist1 = []
for line in lines1:
    if line[0] != ">":
        seqlist1.append(line.replace("\n", ""))

lines2 = myfile2.readlines()
seqlist2 = []
for line2 in lines2:
    if line2[0] != ">":
        seqlist2.append(line2.replace("\n", ""))

myfile1.close()
myfile2.close()
print()
print(seqlist1)
print()
print(seqlist2)
print()


seq1 = seqlist1[0]
seq2 = seqlist2[0]
#
x = []
y = []

for i in range(len(seq1)):
    for j in range(
        len(seq2)
    ):  # Loops over each letter of the first sequence, then all the letters of the second sequence
        if (
            seq1[i] == seq2[j]
        ):  # compares bp to one another. If they match they are appended to the lists.
            x.append(i)
            y.append(j)

pl.figure(figsize=[11, 6])
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
# pl.savefig("Dotplot.png")
pl.show()


# Exercise 9 -

# Add the parameter E (or S) for the number of allowed Errors in your Window, to the dotplot program you generated in Exercise 8


"""
This is the script I created ot show you some examples of working with
Matplotlib in Python. I will comment on the specific methods only the first time
they appear in the program, because the logic stays true independent of the type
of plot you're creating. I included a simple unpickling of variables here, so I
will also upload the corresponding pickle File to the BSCW, so make sure that
the pickle file and the python script are in the same directory before you start
the script.
""" """
This is the script I created ot show you some examples of working with
Matplotlib in Python. I will comment on the specific methods only the first time
they appear in the program, because the logic stays true independent of the type
of plot you're creating. I included a simple unpickling of variables here, so I
will also upload the corresponding pickle File to the BSCW, so make sure that
the pickle file and the python script are in the same directory before you start
the script.
"""
# First we have to import our modules. For this example I need pickle, to get
# the data for my diagrams and random later on to generate some example values
# for the line and bar plots.
# import pickle, random
#
# # I need numpy to generate some ranges as ticks for my plots
# import numpy as np
#
# # Last but not least I need to import matplotlib.pyplot, we have to import the
# # class pyplot here because matplotlib stands for Mathematical Plot Library and
# # can be used in other programming languages as well and to be able to use it in
# # Python we need the pyplot class that is designed for the use in Python. The
# # alias of plt we set here is a convention that was chosen by the creators of
# # Matplotlib and is used by nearly all working groups.
# import matplotlib.pyplot as plt
#
# # Now I can unpickle the values I need for my examples. These three variables
# # are two numpy Arrays (Gammas and Dists) and a Dictionary that contains
# # multtiple two dimensional numpy arrays.
# (Gammas, Dists, Dia) = pickle.load(open("New.pickle", "rb"))
# # This is just a small String variable I need to use in the creation of my plots
# # I could've changed the set ups later on to be able to run this program without
# # this variable, but i decided not to, so that I can show you how to puzzle
# # together titles and Savenames from strings and variables.
# Dir2 = "MBD"
# # If you want to create a plot you have to open a figure to be able to draw on
# # it. There asre more complex options by defining a variable as our figure, but
# # for this example it's enough to just initiate the figure with the plt.figure()
# # command. By defining the attribute figsize, you can set up the size of your
# # plot (in the case below 1100pixels x 600pixels). The first value represents
# # the width and the second the height of our plot.
# plt.figure(figsize=[11, 6])
# # This plot generates a histogram of our calculated values. The neat thing about
# # this is, that we can use an unsorted list and the values are sorted according
# # to the given range autoomatically by matplotlib. To use this type of plot we
# # have to hand over our values in an iterable element (list, array and so on),
# # than we have to define over which range we want the histogram to be contructed
# # (in our case, since I work with angles here a range from 0 to 180 is totally
# # fine). After our range we have to define how many bars (or bins) our histogram
# # should contain. Here I decided to generate 90 bins, so the first bin contains
# # values betwen 0 and 2, the second one value sbetween 2 and 4, and so on until
# # the last bin which contains values from 178 to 180. If I chose a smaller
# # number of bins (e.g 30), the size of the bins would change as well (1: 0-6,
# # 2_6-12 and so on until 30: 174-180). The plot works fine without anything else
# # but you can adjust the color of your bars and the color of the borde of your
# # bars with the facecolor and edgecolor attributes. Bot take color words as
# # strings, e.g "red", "green", "black", shortcuts as string, e.g. "k" for
# # black or "r" for red or "g" for green, floating point numbers, e.g "0.75" for
# # grey, a RGB tuple, a html color name or a hexstring from hatml coloring. This
# # is true for all color option throughout the whole matplotlib.pyplot module.
# plt.hist(Gammas, range=[0, 180], bins=90, facecolor="0.75", edgecolor="k")
# # After we created our histogram we want to adjust the axes of our plot, so that
# # they are to our liking. There are several methods for this I want to show you.
# # The first one xticks allows us to specify on which positions on the x axis we
# # want to have our tick marks or the value of our data points. We have to hand
# # over an iterable argument to xticks so that these can be set by matplotlib.
# # Afterwards we can adjust the desing of the text that is written below our axis
# # Here I adjusted the fontsize to 25 so that the text is bigger and easier to
# # read. I also rotated the text counter-clockwise (mathematical positive) to
# # create a better design.
# plt.xticks([0, 30, 60, 90, 120, 150, 180], fontsize=25, rotation=90)
# # Now we define the dimensions of our x axis by using the xlim method. This
# # method needs a tuple that contains the start and the end point of your axis.
# # This is only a cosmetic change so the bins you created beforehand with the
# # hist method are still on the plot if you would use smaller limits.
# plt.xlim((0, 180))
# # Now we can adjust the ticks for our y-axis. This is done similiar to the way
# # we did it with the x-axis, but this time I let Matplotlib decide were to put
# # the ticks since, I don't know the counts of my histogram. So I only set a
# # bigger fontsize here. All methods that are available for one axis are always
# # also accessible for the other axis. You just have to change the name of the
# # axis form x to y in this example.
# plt.yticks(fontsize=25)
# # Now we want to set up grid lines in our plot. By using hte method without any
# # arguments we get a grid that is created from both axes. So for each tick on
# # any of the axes a small grey line is drawn in our plot to indicate the grid.
# # In the example below I want the grid to be only drawn from the ticks of the
# # y-axis, so I hand over the attribute axis="y" to tell matplotlib from which
# # axis the grid should be drawn.
# plt.grid(axis="y")
# # Now I set uup the names (or labels) of our two axis. Since I want to use
# # special characters like the greek gamma I use the r before my string to be
# # able to use escape caracters $\ to set up the corresponding special characters
# # in my string. In the example below $\gamma$ produces the greek letter gamma in
# # the string that is shown beneath my x-axis. You can use this for other greek
# # letters as well and for pther special characters. I again increased the size
# # of my text so that it's easier to read.
# plt.xlabel(r"$\gamma$-Winkel [Â°]", fontsize=25)
# # Now I set the label for my y-axis as you can see you cna use a similiar syntax
# # as we did with our x-axis.
# plt.ylabel("Anzahl", fontsize=25)
# # Now I set up a title for my whole plot. I use again the r to have access to
# # the special characters (in this case the gamma and the pi). Since I have to
# # puzzle together a string and a variable here, I have to use a separate pair of
# # brackets. The attribute y allows me to specify a height above the border of my
# # canvas so that the title isn't sutck directly to the black border on the top
# # of this canvas.
# plt.title((r"$\gamma$-Winkel Kation-$\pi$ " + Dir2), y=1.02, fontsize=25)
# # Now I use the tight_layout() method to crop everything in a way, that the
# # resulting image has no unenecassary white areas.
# plt.tight_layout()
# # Now I can save my Plot as an image. You always have to do this if you want to
# # be able to look at your plot after the run of your program. If you don't use
# # this the plot is only accessable during the run of the program and not saved
# # on your harddisk. So keep in mind to always use the savefig method. You can
# # handover different images formats but I prefer to use png, since I know that
# # matplotlib can generate pngs. If you want another format you would have to
# # look it up online (The URL at point 16 at the end of the presentation).
# plt.savefig(("Gamma_" + Dir2 + ".png"))
# # Before we go on we have to close our current plot Otherwise we would draw on
# # the same canvas as before if we want ot create multiple plots. Furthermore
# # stays the plot in your memeory as long as you didn't close the window, so you
# # it's better to close it after you're finished.
# plt.close()
# # Here I create another histogram, so the set up is nearly identical to our
# # firts plot.
# plt.figure(figsize=[11, 6])
# plt.hist(Dists, range=[3.4, 6], bins=27, facecolor="0.75", edgecolor="k")
# plt.xticks([3.4, 4.05, 4.7, 5.35, 6], fontsize=25, rotation=90)
# plt.xlim([3.4, 6])
# plt.yticks(fontsize=25)
# plt.grid(axis="y")
# plt.xlabel("Abstand Aromat Kation [Ã…]", fontsize=25)
# plt.ylabel("Anzahl", fontsize=25)
# plt.title(("AbstÃ¤nde Aromat Kation " + Dir2), y=1.02, fontsize=25)
# plt.tight_layout()
# plt.savefig(("Distance_" + Dir2 + ".png"))
# plt.close()
# # Now I want ot show you a Scatter plot using Matplotlib.
# plt.figure(figsize=[11, 6])
# # This line is the main difference in comparison to our histogram, since we now
# # use th eplot method and not the hist method. The plot method needs first
# # x-Values and than the cporresponding y-Values. Both have to be iterable and of
# # the same length. Afterwards you can specify how you want the data to be
# # plotted. You can simply hand over some shortcuts to tell matplotlib the color,
# # the form of the marker and the type of line you want to use. In the example
# # here we use black dots. You can look up all htese shortcuts also in the
# # documentary I wrote in my presentation. There are a lot of different options
# # so it's very difficult ot remember everything.
# plt.plot(Dia["DG"][0], Dia["DG"][1], "k.")
# plt.yticks([0, 30, 60, 90, 120, 150, 180], fontsize=25)
# plt.ylim([0, 180])
# plt.xticks([3.4, 4.05, 4.7, 5.35, 6], fontsize=25, rotation=90)
# plt.xlim([3.4, 6])
# # For this example I use the default grid, so now we get grid lines from both
# # axes at the same time.
# plt.grid()
# plt.ylabel(r"$\gamma$-Winkel [Â°]", fontsize=25)
# plt.xlabel("Abstand Aromat Kation [Ã…]", fontsize=25)
# plt.title((r"Abstand gegen $\gamma$-Winkel " + Dir2), y=1.02, fontsize=25)
# plt.tight_layout()
# plt.savefig(("Distance_Gamma_" + Dir2 + ".png"))
# plt.close()
# # For the bar-plot and the second Scatter- or Line-plot I need some values, so
# # I created four numpy arrays containing only 20 ones and adjusted them with
# # the help of some random numbers in the loop shown below. The array Values4 is
# # used for displaying some standard deviations or errors in our Bar-plot.
# Values = np.ones(20)
# Values2 = np.ones(20)
# Values3 = np.ones(20)
# Values4 = np.ones(20)
# for i in range(len(Values)):
#     Values[i] = Values[i] * random.randint(1, 8) * random.random()
#     Values2[i] = Values2[i] * random.randint(1, 8) * random.random()
#     Values3[i] = Values3[i] * random.randint(1, 8) * random.random()
#     Values4[i] = Values4[i] * random.random()
# plt.figure(figsize=[10, 10])
# # With this example we are creating a simple bar plot with the help of our
# # random values from before. We have to hand over the values for our x-axis, in
# # this example the numbers from 0 to 19, and the heights of the different bars,
# # so the y-Values or our random numbers in the case here. This is enough to
# # create a simple bar-plot. Yu can add the standard-deviation by using the
# # attribute yerr (which stands for error on y-axis). Of course all elements you
# # hand over until this point have to be iterable and of the same size. You can
# # adjust your plot with a multitude of attributes for the filling color of your
# # bars, the color of the broders of your bars, the padding between the bars and
# # so on. There are many examples all over the internet, so if you want to create
# # more complex plots look them up.
# plt.bar(np.arange(20), Values, yerr=Values4)
# plt.title("Example Barplot", y=1.02, fontsize=25)
# plt.xlabel("Contesdant Nr", fontsize=25)
# plt.ylabel("Mark", fontsize=25)
# plt.xlim([-1, 20])
# plt.ylim([0, 8])
# plt.yticks(np.arange(9), fontsize=25)
# plt.xticks(np.arange(20), fontsize=20, rotation=45)
# plt.grid(axis="y")
# plt.tight_layout()
# plt.savefig("Barplot_Example.png")
# plt.close()
# # Now I sort my random values so that the Line- and Scatter-plots below look
# # at least somewhat ok.
# Values.sort()
# Values2.sort()
# Values3.sort()
#
# plt.figure(figsize=[10, 10])
# # This example shows you how to create Line- or Scatter-plots. We saw the use
# # of plot earlier. If you use plot without any attribue beside the two lists
# # of values, you create a plot that contains a simple blue line.
# plt.plot(np.arange(20), Values)
# # If we now use plot again with a different set of y-Values we can draw another
# # "line" in our plot. But this time we only want to mark the values with red
# # dots. By also handing over the attribute markersize we can define the size of
# # our points.
# plt.plot(np.arange(20), Values2, "r.", markersize=15)
# # Now we want to add a dashed line to our plot, again with a different set of
# # values. The data points should be marked with an asterisk in addition, so we
# # can use the shortcuts as shown below, first the markertype, than the color and
# # last but not least the line type. "--" stands for a dashed line, I know that
# # there are at least three different modes "-" for a normal line, "-." for a mix
# # of dashes and dots in the line and ":" for a dotted line. I added a second
# # optional attribute here the linewidth. This attribute allows you to define the
# # thickness of your drawn line.
# plt.plot(np.arange(20), Values3, "*g--", markersize=15, linewidth=5)
# # As you can see in the examples above you can combine multiple pairs of values
# # in one plot. But to get the best results the different y-values should be
# # associated witht he same x-values, to make sure that the definition range of
# # your plot is ok.
# plt.title("Example Scatterplot", y=1.02, fontsize=25)
# plt.xlabel("Contesdant Nr", fontsize=25)
# plt.ylabel("Mark", fontsize=25)
# plt.xlim([-1, 20])
# plt.ylim([0, 8])
# plt.yticks(np.arange(9), fontsize=25)
# plt.xticks(np.arange(20), fontsize=20, rotation=45)
# plt.grid()
# plt.tight_layout()
# plt.savefig("Example_Plot.png")
# plt.close()
# # First we have to import our modules. For this example I need pickle, to get
# # the data for my diagrams and random later on to generate some example values
# # for the line and bar plots.
# import pickle, random
#
# # I need numpy to generate some ranges as ticks for my plots
#
# """
# This is the script I created ot show you some examples of working with
# Matplotlib in Python. I will comment on the specific methods only the first time
# they appear in the program, because the logic stays true independent of the type
# of plot you're creating. I included a simple unpickling of variables here, so I
# will also upload the corresponding pickle File to the BSCW, so make sure that
# the pickle file and the python script are in the same directory before you start
# the script.
# """
# # First we have to import our modules. For this example I need pickle, to get
# # the data for my diagrams and random later on to generate some example values
# # for the line and bar plots.
# import pickle, random
#
# # I need numpy to generate some ranges as ticks for my plots
# import numpy as np
#
# # Last but not least I need to import matplotlib.pyplot, we have to import the
# # class pyplot here because matplotlib stands for Mathematical Plot Library and
# # can be used in other programming languages as well and to be able to use it in
# # Python we need the pyplot class that is designed for the use in Python. The
# # alias of plt we set here is a convention that was chosen by the creators of
# # Matplotlib and is used by nearly all working groups.
# import matplotlib.pyplot as plt
#
# # Now I can unpickle the values I need for my examples. These three variables
# # are two numpy Arrays (Gammas and Dists) and a Dictionary that contains
# # multtiple two dimensional numpy arrays.
# (Gammas, Dists, Dia) = pickle.load(open("New.pickle", "rb"))
# # This is just a small String variable I need to use in the creation of my plots
# # I could've changed the set ups later on to be able to run this program without
# # this variable, but i decided not to, so that I can show you how to puzzle
# # together titles and Savenames from strings and variables.
# Dir2 = "MBD"
# # If you want to create a plot you have to open a figure to be able to draw on
# # it. There asre more complex options by defining a variable as our figure, but
# # for this example it's enough to just initiate the figure with the plt.figure()
# # command. By defining the attribute figsize, you can set up the size of your
# # plot (in the case below 1100pixels x 600pixels). The first value represents
# # the width and the second the height of our plot.
# plt.figure(figsize=[11, 6])
# # This plot generates a histogram of our calculated values. The neat thing about
# # this is, that we can use an unsorted list and the values are sorted according
# # to the given range autoomatically by matplotlib. To use this type of plot we
# # have to hand over our values in an iterable element (list, array and so on),
# # than we have to define over which range we want the histogram to be contructed
# # (in our case, since I work with angles here a range from 0 to 180 is totally
# # fine). After our range we have to define how many bars (or bins) our histogram
# # should contain. Here I decided to generate 90 bins, so the first bin contains
# # values betwen 0 and 2, the second one value sbetween 2 and 4, and so on until
# # the last bin which contains values from 178 to 180. If I chose a smaller
# # number of bins (e.g 30), the size of the bins would change as well (1: 0-6,
# # 2_6-12 and so on until 30: 174-180). The plot works fine without anything else
# # but you can adjust the color of your bars and the color of the borde of your
# # bars with the facecolor and edgecolor attributes. Bot take color words as
# # strings, e.g "red", "green", "black", shortcuts as string, e.g. "k" for
# # black or "r" for red or "g" for green, floating point numbers, e.g "0.75" for
# # grey, a RGB tuple, a html color name or a hexstring from hatml coloring. This
# # is true for all color option throughout the whole matplotlib.pyplot module.
# plt.hist(Gammas, range=[0, 180], bins=90, facecolor="0.75", edgecolor="k")
# # After we created our histogram we want to adjust the axes of our plot, so that
# # they are to our liking. There are several methods for this I want to show you.
# # The first one xticks allows us to specify on which positions on the x axis we
# # want to have our tick marks or the value of our data points. We have to hand
# # over an iterable argument to xticks so that these can be set by matplotlib.
# # Afterwards we can adjust the desing of the text that is written below our axis
# # Here I adjusted the fontsize to 25 so that the text is bigger and easier to
# # read. I also rotated the text counter-clockwise (mathematical positive) to
# # create a better design.
# plt.xticks([0, 30, 60, 90, 120, 150, 180], fontsize=25, rotation=90)
# # Now we define the dimensions of our x axis by using the xlim method. This
# # method needs a tuple that contains the start and the end point of your axis.
# # This is only a cosmetic change so the bins you created beforehand with the
# # hist method are still on the plot if you would use smaller limits.
# plt.xlim((0, 180))
# # Now we can adjust the ticks for our y-axis. This is done similiar to the way
# # we did it with the x-axis, but this time I let Matplotlib decide were to put
# # the ticks since, I don't know the counts of my histogram. So I only set a
# # bigger fontsize here. All methods that are available for one axis are always
# # also accessible for the other axis. You just have to change the name of the
# # axis form x to y in this example.
# plt.yticks(fontsize=25)
# # Now we want to set up grid lines in our plot. By using hte method without any
# # arguments we get a grid that is created from both axes. So for each tick on
# # any of the axes a small grey line is drawn in our plot to indicate the grid.
# # In the example below I want the grid to be only drawn from the ticks of the
# # y-axis, so I hand over the attribute axis="y" to tell matplotlib from which
# # axis the grid should be drawn.
# plt.grid(axis="y")
# # Now I set uup the names (or labels) of our two axis. Since I want to use
# # special characters like the greek gamma I use the r before my string to be
# # able to use escape caracters $\ to set up the corresponding special characters
# # in my string. In the example below $\gamma$ produces the greek letter gamma in
# # the string that is shown beneath my x-axis. You can use this for other greek
# # letters as well and for pther special characters. I again increased the size
# # of my text so that it's easier to read.
# plt.xlabel(r"$\gamma$-Winkel [Â°]", fontsize=25)
# # Now I set the label for my y-axis as you can see you cna use a similiar syntax
# # as we did with our x-axis.
# plt.ylabel("Anzahl", fontsize=25)
# # Now I set up a title for my whole plot. I use again the r to have access to
# # the special characters (in this case the gamma and the pi). Since I have to
# # puzzle together a string and a variable here, I have to use a separate pair of
# # brackets. The attribute y allows me to specify a height above the border of my
# # canvas so that the title isn't sutck directly to the black border on the top
# # of this canvas.
# plt.title((r"$\gamma$-Winkel Kation-$\pi$ " + Dir2), y=1.02, fontsize=25)
# # Now I use the tight_layout() method to crop everything in a way, that the
# # resulting image has no unenecassary white areas.
# plt.tight_layout()
# # Now I can save my Plot as an image. You always have to do this if you want to
# # be able to look at your plot after the run of your program. If you don't use
# # this the plot is only accessable during the run of the program and not saved
# # on your harddisk. So keep in mind to always use the savefig method. You can
# # handover different images formats but I prefer to use png, since I know that
# # matplotlib can generate pngs. If you want another format you would have to
# # look it up online (The URL at point 16 at the end of the presentation).
# plt.savefig(("Gamma_" + Dir2 + ".png"))
# # Before we go on we have to close our current plot Otherwise we would draw on
# # the same canvas as before if we want ot create multiple plots. Furthermore
# # stays the plot in your memeory as long as you didn't close the window, so you
# # it's better to close it after you're finished.
# plt.close()
# # Here I create another histogram, so the set up is nearly identical to our
# # firts plot.
# plt.figure(figsize=[11, 6])
# plt.hist(Dists, range=[3.4, 6], bins=27, facecolor="0.75", edgecolor="k")
# plt.xticks([3.4, 4.05, 4.7, 5.35, 6], fontsize=25, rotation=90)
# plt.xlim([3.4, 6])
# plt.yticks(fontsize=25)
# plt.grid(axis="y")
# plt.xlabel("Abstand Aromat Kation [Ã…]", fontsize=25)
# plt.ylabel("Anzahl", fontsize=25)
# plt.title(("AbstÃ¤nde Aromat Kation " + Dir2), y=1.02, fontsize=25)
# plt.tight_layout()
# plt.savefig(("Distance_" + Dir2 + ".png"))
# plt.close()
# # Now I want ot show you a Scatter plot using Matplotlib.
# plt.figure(figsize=[11, 6])
# # This line is the main difference in comparison to our histogram, since we now
# # use th eplot method and not the hist method. The plot method needs first
# # x-Values and than the cporresponding y-Values. Both have to be iterable and of
# # the same length. Afterwards you can specify how you want the data to be
# # plotted. You can simply hand over some shortcuts to tell matplotlib the color,
# # the form of the marker and the type of line you want to use. In the example
# # here we use black dots. You can look up all htese shortcuts also in the
# # documentary I wrote in my presentation. There are a lot of different options
# # so it's very difficult ot remember everything.
# plt.plot(Dia["DG"][0], Dia["DG"][1], "k.")
# plt.yticks([0, 30, 60, 90, 120, 150, 180], fontsize=25)
# plt.ylim([0, 180])
# plt.xticks([3.4, 4.05, 4.7, 5.35, 6], fontsize=25, rotation=90)
# plt.xlim([3.4, 6])
# # For this example I use the default grid, so now we get grid lines from both
# # axes at the same time.
# plt.grid()
# plt.ylabel(r"$\gamma$-Winkel [Â°]", fontsize=25)
# plt.xlabel("Abstand Aromat Kation [Ã…]", fontsize=25)
# plt.title((r"Abstand gegen $\gamma$-Winkel " + Dir2), y=1.02, fontsize=25)
# plt.tight_layout()
# plt.savefig(("Distance_Gamma_" + Dir2 + ".png"))
# plt.close()
# # For the bar-plot and the second Scatter- or Line-plot I need some values, so
# # I created four numpy arrays containing only 20 ones and adjusted them with
# # the help of some random numbers in the loop shown below. The array Values4 is
# # used for displaying some standard deviations or errors in our Bar-plot.
# Values = np.ones(20)
# Values2 = np.ones(20)
# Values3 = np.ones(20)
# Values4 = np.ones(20)
# for i in range(len(Values)):
#     Values[i] = Values[i] * random.randint(1, 8) * random.random()
#     Values2[i] = Values2[i] * random.randint(1, 8) * random.random()
#     Values3[i] = Values3[i] * random.randint(1, 8) * random.random()
#     Values4[i] = Values4[i] * random.random()
# plt.figure(figsize=[10, 10])
# # With this example we are creating a simple bar plot with the help of our
# # random values from before. We have to hand over the values for our x-axis, in
# # this example the numbers from 0 to 19, and the heights of the different bars,
# # so the y-Values or our random numbers in the case here. This is enough to
# # create a simple bar-plot. Yu can add the standard-deviation by using the
# # attribute yerr (which stands for error on y-axis). Of course all elements you
# # hand over until this point have to be iterable and of the same size. You can
# # adjust your plot with a multitude of attributes for the filling color of your
# # bars, the color of the broders of your bars, the padding between the bars and
# # so on. There are many examples all over the internet, so if you want to create
# # more complex plots look them up.
# plt.bar(np.arange(20), Values, yerr=Values4)
# plt.title("Example Barplot", y=1.02, fontsize=25)
# plt.xlabel("Contesdant Nr", fontsize=25)
# plt.ylabel("Mark", fontsize=25)
# plt.xlim([-1, 20])
# plt.ylim([0, 8])
# plt.yticks(np.arange(9), fontsize=25)
# plt.xticks(np.arange(20), fontsize=20, rotation=45)
# plt.grid(axis="y")
# plt.tight_layout()
# plt.savefig("Barplot_Example.png")
# plt.close()
# # Now I sort my random values so that the Line- and Scatter-plots below look
# # at least somewhat ok.
# Values.sort()
# Values2.sort()
# Values3.sort()
#
# plt.figure(figsize=[10, 10])
# # This example shows you how to create Line- or Scatter-plots. We saw the use
# # of plot earlier. If you use plot without any attribue beside the two lists
# # of values, you create a plot that contains a simple blue line.
# plt.plot(np.arange(20), Values)
# # If we now use plot again with a different set of y-Values we can draw another
# # "line" in our plot. But this time we only want to mark the values with red
# # dots. By also handing over the attribute markersize we can define the size of
# # our points.
# plt.plot(np.arange(20), Values2, "r.", markersize=15)
# # Now we want to add a dashed line to our plot, again with a different set of
# # values. The data points should be marked with an asterisk in addition, so we
# # can use the shortcuts as shown below, first the markertype, than the color and
# # last but not least the line type. "--" stands for a dashed line, I know that
# # there are at least three different modes "-" for a normal line, "-." for a mix
# # of dashes and dots in the line and ":" for a dotted line. I added a second
# # optional attribute here the linewidth. This attribute allows you to define the
# # thickness of your drawn line.
# plt.plot(np.arange(20), Values3, "*g--", markersize=15, linewidth=5)
# # As you can see in the examples above you can combine multiple pairs of values
# # in one plot. But to get the best results the different y-values should be
# # associated witht he same x-values, to make sure that the definition range of
# # your plot is ok.
# plt.title("Example Scatterplot", y=1.02, fontsize=25)
# plt.xlabel("Contesdant Nr", fontsize=25)
# plt.ylabel("Mark", fontsize=25)
# plt.xlim([-1, 20])
# plt.ylim([0, 8])
# plt.yticks(np.arange(9), fontsize=25)
# plt.xticks(np.arange(20), fontsize=20, rotation=45)
# plt.grid()
# plt.tight_layout()
# plt.savefig("Example_Plot.png")
# plt.close()
# import numpy as np
#
# # Last but not least I need to import matplotlib.pyplot, we have to import the
# # class pyplot here because matplotlib stands for Mathematical Plot Library and
# # can be used in other programming languages as well and to be able to use it in
# # Python we need the pyplot class that is designed for the use in Python. The
# # alias of plt we set here is a convention that was chosen by the creators of
# # Matplotlib and is used by nearly all working groups.
# import matplotlib.pyplot as plt
#
# # Now I can unpickle the values I need for my examples. These three variables
# # are two numpy Arrays (Gammas and Dists) and a Dictionary that contains
# # multtiple two dimensional numpy arrays.
# (Gammas, Dists, Dia) = pickle.load(open("New.pickle", "rb"))
# # This is just a small String variable I need to use in the creation of my plots
# # I could've changed the set ups later on to be able to run this program without
# # this variable, but i decided not to, so that I can show you how to puzzle
# # together titles and Savenames from strings and variables.
# Dir2 = "MBD"
# # If you want to create a plot you have to open a figure to be able to draw on
# # it. There are more complex options by defining a variable as our figure, but
# # for this example it's enough to just initiate the figure with the plt.figure()
# # command. By defining the attribute figsize, you can set up the size of your
# # plot (in the case below 1100pixels x 600pixels). The first value represents
# # the width and the second the height of our plot.
# plt.figure(figsize=[11, 6])
# # This plot generates a histogram of our calculated values. The neat thing about
# # this is, that we can use an unsorted list and the values are sorted according
# # to the given range autoomatically by matplotlib. To use this type of plot we
# # have to hand over our values in an iterable element (list, array and so on),
# # than we have to define over which range we want the histogram to be contructed
# # (in our case, since I work with angles here a range from 0 to 180 is totally
# # fine). After our range we have to define how many bars (or bins) our histogram
# # should contain. Here I decided to generate 90 bins, so the first bin contains
# # values betwen 0 and 2, the second one value sbetween 2 and 4, and so on until
# # the last bin which contains values from 178 to 180. If I chose a smaller
# # number of bins (e.g 30), the size of the bins would change as well (1: 0-6,
# # 2_6-12 and so on until 30: 174-180). The plot works fine without anything else
# # but you can adjust the color of your bars and the color of the borde of your
# # bars with the facecolor and edgecolor attributes. Bot take color words as
# # strings, e.g "red", "green", "black", shortcuts as string, e.g. "k" for
# # black or "r" for red or "g" for green, floating point numbers, e.g "0.75" for
# # grey, a RGB tuple, a html color name or a hexstring from hatml coloring. This
# # is true for all color option throughout the whole matplotlib.pyplot module.
# plt.hist(Gammas, range=[0, 180], bins=90, facecolor="0.75", edgecolor="k")
# # After we created our histogram we want to adjust the axes of our plot, so that
# # they are to our liking. There are several methods for this I want to show you.
# # The first one xticks allows us to specify on which positions on the x axis we
# # want to have our tick marks or the value of our data points. We have to hand
# # over an iterable argument to xticks so that these can be set by matplotlib.
# # Afterwards we can adjust the desing of the text that is written below our axis
# # Here I adjusted the fontsize to 25 so that the text is bigger and easier to
# # read. I also rotated the text counter-clockwise (mathematical positive) to
# # create a better design.
# plt.xticks([0, 30, 60, 90, 120, 150, 180], fontsize=25, rotation=90)
# # Now we define the dimensions of our x axis by using the xlim method. This
# # method needs a tuple that contains the start and the end point of your axis.
# # This is only a cosmetic change so the bins you created beforehand with the
# # hist method are still on the plot if you would use smaller limits.
# plt.xlim((0, 180))
# # Now we can adjust the ticks for our y-axis. This is done similiar to the way
# # we did it with the x-axis, but this time I let Matplotlib decide were to put
# # the ticks since, I don't know the counts of my histogram. So I only set a
# # bigger fontsize here. All methods that are available for one axis are always
# # also accessible for the other axis. You just have to change the name of the
# # axis form x to y in this example.
# plt.yticks(fontsize=25)
# # Now we want to set up grid lines in our plot. By using hte method without any
# # arguments we get a grid that is created from both axes. So for each tick on
# # any of the axes a small grey line is drawn in our plot to indicate the grid.
# # In the example below I want the grid to be only drawn from the ticks of the
# # y-axis, so I hand over the attribute axis="y" to tell matplotlib from which
# # axis the grid should be drawn.
# plt.grid(axis="y")
# # Now I set uup the names (or labels) of our two axis. Since I want to use
# # special characters like the greek gamma I use the r before my string to be
# # able to use escape caracters $\ to set up the corresponding special characters
# # in my string. In the example below $\gamma$ produces the greek letter gamma in
# # the string that is shown beneath my x-axis. You can use this for other greek
# # letters as well and for pther special characters. I again increased the size
# # of my text so that it's easier to read.
# plt.xlabel(r"$\gamma$-Winkel [Â°]", fontsize=25)
# # Now I set the label for my y-axis as you can see you cna use a similiar syntax
# # as we did with our x-axis.
# plt.ylabel("Anzahl", fontsize=25)
# # Now I set up a title for my whole plot. I use again the r to have access to
# # the special characters (in this case the gamma and the pi). Since I have to
# # puzzle together a string and a variable here, I have to use a separate pair of
# # brackets. The attribute y allows me to specify a height above the border of my
# # canvas so that the title isn't sutck directly to the black border on the top
# # of this canvas.
# plt.title((r"$\gamma$-Winkel Kation-$\pi$ " + Dir2), y=1.02, fontsize=25)
# # Now I use the tight_layout() method to crop everything in a way, that the
# # resulting image has no unenecassary white areas.
# plt.tight_layout()
# # Now I can save my Plot as an image. You always have to do this if you want to
# # be able to look at your plot after the run of your program. If you don't use
# # this the plot is only accessable during the run of the program and not saved
# # on your harddisk. So keep in mind to always use the savefig method. You can
# # handover different images formats but I prefer to use png, since I know that
# # matplotlib can generate pngs. If you want another format you would have to
# # look it up online (The URL at point 16 at the end of the presentation).
# plt.savefig(("Gamma_" + Dir2 + ".png"))
# # Before we go on we have to close our current plot Otherwise we would draw on
# # the same canvas as before if we want ot create multiple plots. Furthermore
# # stays the plot in your memeory as long as you didn't close the window, so you
# # it's better to close it after you're finished.
# plt.close()
# # Here I create another histogram, so the set up is nearly identical to our
# # firts plot.
# plt.figure(figsize=[11, 6])
# plt.hist(Dists, range=[3.4, 6], bins=27, facecolor="0.75", edgecolor="k")
# plt.xticks([3.4, 4.05, 4.7, 5.35, 6], fontsize=25, rotation=90)
# plt.xlim([3.4, 6])
# plt.yticks(fontsize=25)
# plt.grid(axis="y")
# plt.xlabel("Abstand Aromat Kation [Ãi…]", fontsize=25)
# plt.ylabel("Anzahl", fontsize=25)
# plt.title(("AbstÃ¤nde Aromat Kation " + Dir2), y=1.02, fontsize=25)
# plt.tight_layout()
# plt.savefig(("Distance_" + Dir2 + ".png"))
# plt.close()

# # Now I want ot show you a Scatter plot using Matplotlib.
# plt.figure(figsize=[11, 6])
# # This line is the main difference in comparison to our histogram, since we now
# # use th eplot method and not the hist method. The plot method needs first
# # x-Values and than the cporresponding y-Values. Both have to be iterable and of
# # the same length. Afterwards you can specify how you want the data to be
# # plotted. You can simply hand over some shortcuts to tell matplotlib the color,
# # the form of the marker and the type of line you want to use. In the example
# # here we use black dots. You can look up all htese shortcuts also in the
# # documentary I wrote in my presentation. There are a lot of different options
# # so it's very difficult ot remember everything.
# plt.plot(Dia["DG"][0], Dia["DG"][1], "k.")
# plt.yticks([0, 30, 60, 90, 120, 150, 180], fontsize=25)
# plt.ylim([0, 180])
# plt.xticks([3.4, 4.05, 4.7, 5.35, 6], fontsize=25, rotation=90)
# plt.xlim([3.4, 6])
# # For this example I use the default grid, so now we get grid lines from both
# # axes at the same time.
# plt.grid()
# plt.ylabel(r"$\gamma$-Winkel [Â°]", fontsize=25)
# plt.xlabel("Abstand Aromat Kation [Ã…]", fontsize=25)
# plt.title((r"Abstand gegen $\gamma$-Winkel " + Dir2), y=1.02, fontsize=25)
# plt.tight_layout()
# plt.savefig(("Distance_Gamma_" + Dir2 + ".png"))
# plt.close()
# # For the bar-plot and the second Scatter- or Line-plot I need some values, so
# # I created four numpy arrays containing only 20 ones and adjusted them with
# # the help of some random numbers in the loop shown below. The array Values4 is
# # used for displaying some standard deviations or errors in our Bar-plot.
# Values = np.ones(20)
# Values2 = np.ones(20)
# Values3 = np.ones(20)
# Values4 = np.ones(20)
# for i in range(len(Values)):
#     Values[i] = Values[i] * random.randint(1, 8) * random.random()
#     Values2[i] = Values2[i] * random.randint(1, 8) * random.random()
#     Values3[i] = Values3[i] * random.randint(1, 8) * random.random()
#     Values4[i] = Values4[i] * random.random()
# plt.figure(figsize=[10, 10])
# # With this example we are creating a simple bar plot with the help of our
# # random values from before. We have to hand over the values for our x-axis, in
# # this example the numbers from 0 to 19, and the heights of the different bars,
# # so the y-Values or our random numbers in the case here. This is enough to
# # create a simple bar-plot. Yu can add the standard-deviation by using the
# # attribute yerr (which stands for error on y-axis). Of course all elements you
# # hand over until this point have to be iterable and of the same size. You can
# # adjust your plot with a multitude of attributes for the filling color of your
# # bars, the color of the broders of your bars, the padding between the bars and
# # so on. There are many examples all over the internet, so if you want to create
# # more complex plots look them up.
# plt.bar(np.arange(20), Values, yerr=Values4)
# plt.title("Example Barplot", y=1.02, fontsize=25)
# plt.xlabel("Contesdant Nr", fontsize=25)
# plt.ylabel("Mark", fontsize=25)
# plt.xlim([-1, 20])
# plt.ylim([0, 8])
# plt.yticks(np.arange(9), fontsize=25)
# plt.xticks(np.arange(20), fontsize=20, rotation=45)
# plt.grid(axis="y")
# plt.tight_layout()
# plt.savefig("Barplot_Example.png")
# plt.close()
# # Now I sort my random values so that the Line- and Scatter-plots below look
# # at least somewhat ok.
# Values.sort()
# Values2.sort()
# Values3.sort()
#
# plt.figure(figsize=[10, 10])
# # This example shows you how to create Line- or Scatter-plots. We saw the use
# # of plot earlier. If you use plot without any attribue beside the two lists
# # of values, you create a plot that contains a simple blue line.
# plt.plot(np.arange(20), Values)
# # If we now use plot again with a different set of y-Values we can draw another
# # "line" in our plot. But this time we only want to mark the values with red
# # dots. By also handing over the attribute markersize we can define the size of
# # our points.
# plt.plot(np.arange(20), Values2, "r.", markersize=15)
# # Now we want to add a dashed line to our plot, again with a different set of
# # values. The data points should be marked with an asterisk in addition, so we
# # can use the shortcuts as shown below, first the markertype, than the color and
# # last but not least the line type. "--" stands for a dashed line, I know that
# # there are at least three different modes "-" for a normal line, "-." for a mix
# # of dashes and dots in the line and ":" for a dotted line. I added a second
# # optional attribute here the linewidth. This attribute allows you to define the
# # thickness of your drawn line.
# plt.plot(np.arange(20), Values3, "*g--", markersize=15, linewidth=5)
# # As you can see in the examples above you can combine multiple pairs of values
# # in one plot. But to get the best results the different y-values should be
# # associated witht he same x-values, to make sure that the definition range of
# # your plot is ok.
# plt.title("Example Scatterplot", y=1.02, fontsize=25)
# plt.xlabel("Contesdant Nr", fontsize=25)
# plt.ylabel("Mark", fontsize=25)
# plt.xlim([-1, 20])
# plt.ylim([0, 8])
# plt.yticks(np.arange(9), fontsize=25)
# plt.xticks(np.arange(20), fontsize=20, rotation=45)
# plt.grid()
# plt.tight_layout()
# plt.savefig("Example_Plot.png")
# plt.close()
