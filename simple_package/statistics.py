###
## Module for basic statistics
###

## Here I need functions to take in data
## and do the following:
##
## 1. Calculate mean. Calculate median. Calculate 
##    standard deviation.
##
## 2. Display the result with a nice print statement.
##
## 3. Plot a histogram of the data, with the mean and median 
##    marked on the plot. This should be part of a new Python
##    file in the package, called graphics.py.
##
## 4. Remember to provide a mechanism for checking that the input
##    is a numpy array or a list (if a list, you must convert it
##    to a numpy array).
##
## 5. Also, do something and/or throw an exception/message if the
##    numpy and matplotlib packages are not installed.


import numpy as np

def calculate_mean(data):
    """Calculate the mean of a numpy array."""
    if isinstance(data,(list)):
        data = np.array(data)
    elif isinstance(data,(np.ndarray)):
        pass
    else:
        raise ValueError("Data must be a list or numpy array.")
    
    res = data.mean()
    print(f"The mean of the data is {res}")
    return res

def calculate_median(data):
    """Calculate the median of a numpy array."""
    if isinstance(data,(list)):
        data = np.array(data)
    elif isinstance(data,(np.ndarray)):
        pass
    else:
        raise ValueError("Data must be a list or numpy array.")
    
    res = np.median(data)
    print(f"The median of the data is {res}")
    return res

def calculate_std(data):
    """Calculate the standard deviation of a numpy array."""
    if isinstance(data,(list)):
        data = np.array(data)
    elif isinstance(data,(np.ndarray)):
        pass
    else:
        raise ValueError("Data must be a list or numpy array.")
    
    res = data.sd()
    print(f"The median of the data is {res}")
    return res

