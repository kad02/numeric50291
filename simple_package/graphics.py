import matplotlib.pyplot as plt

def plotData(data, mean, median):
    """Plot a histogram of the data with mean and median."""
    plt.hist(data, bins=30)
    plt.axvline(mean, color='r', linestyle='dashed', linewidth=1)
    plt.axvline(median, color='g', linestyle='dashed', linewidth=1)
    plt.show()
    return None