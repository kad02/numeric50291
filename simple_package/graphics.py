import numpy as np
import matplotlib.pyplot as plt

def plotData(data, mean, median):
    """Plot a histogram of the data with mean and median."""
    try:
        if isinstance(data,(list)):
            data = np.array(data)
        elif isinstance(data,(np.ndarray)):
            pass
        else:
            raise ValueError("Error plotting data: Data must be a list or numpy array.")
    except ValueError as e:
        print(e)
        return None
    plt.hist(data, bins=30)
    plt.axvline(mean, color='r', linestyle='dashed', linewidth=1)
    plt.axvline(median, color='g', linestyle='dashed', linewidth=1)
    plt.show()
    return None