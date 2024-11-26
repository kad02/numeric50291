###
## test package
###

import simple_package as sp

if __name__ == '__main__':
    ## Define two numbers
    a = 1;
    b = 2;
    
    ## Print their sum with a nice message.
    print(f"The sum of {a} and {b} is {sp.add(a,b)}")

    ## Now do the same for the function in sp
    print(f"The product of {a} and {b} is {sp.multiply(a,b)}")

    ## Run the interface function
    sp.which_operation()

    ## Define some data
    data = [1,2,3,4,5,6,7,8,9,10]

    data = 5
    sp.plotData(data, sp.calculate_mean(data), sp.calculate_median(data))