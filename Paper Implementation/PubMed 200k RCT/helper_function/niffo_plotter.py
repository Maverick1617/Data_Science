import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt


def plot_histogram(data, bins=5, xlabel="", ylabel="", title="", figsize=(12, 6)):

    sns.set_style("darkgrid")
    matplotlib.rcParams["font.size"] = 14
    matplotlib.rcParams["figure.figsize"] = figsize

    plt.figure(facecolor="#F6F6F6")
    plt.axes().set_facecolor("#EEEEEE")

    plt.hist(data, bins=bins, color="#DD4A48")
    plt.xlabel(xlabel=xlabel)
    plt.ylabel(ylabel=ylabel)
    plt.title(title, weight="bold", fontname="monospace", fontsize=20)
    plt.show()
