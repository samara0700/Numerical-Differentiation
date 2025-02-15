#------------------------------------------------------------------#
# Samara Overvaag
# MATH374 - Project 1
# Numerical computation of the derivative of:
# f(x) = sinx at x = 1
# as h -> 0
#------------------------------------------------------------------#
# we consider and compare two numerical differentiation formulas:
# f'(x) = (f(x+h)-f(x))/h
#
# f'(x) = (f(x+h)-f(x-h))/2h
#
# referencing the Numerical Mathematics and Computing Textbook pseudocode
# google helped a lot with numpy and matplotlib
# To save graphs as .png files, please see lines 192 and 205.
#------------------------------------------------------------------#

import math
# stuff for plotting:
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# integers
n = 30; # 30 iterations 

# real numbers
x = 1.0 # x = 1
h = 1.0 # "step size"

# truncation error vars 
te_min1 = 1 # minimum t. error for eq. 1, initialize at 1
te_min2 = 1 # minimum t. error for eq. 2
te_max1 = 0 # maximum t. error for eq. 1, initialize at zero
te_max2 = 0 # maximum t. error for eq. 2

# rounding error vars
e = 2.22*10**(-16) # machine epsilon
re_min = 1 # minimum r. error
re_max = 0 # maximum r. error

# total error vars
total_min1 = 1
total_min2 = 1
total_max1 = 0
total_max2 = 0

# error arrays used for plotting
trunc_array1 = []
trunc_array2 = []
round_array = []
total_array1 = []
total_array2 = []
h_array = []

# factorial values because things were looking messy, so I just assigned variables to each
tfact = math.factorial(3) # 3! = 6
ffact = math.factorial(5) # 5! = 120
sfact = math.factorial(7) # 7! = 5040
nfact = math.factorial(9) # 9! = 362880

#-----------------------------------------------#
# Begin procedure:

# n iterations (n = 30)
# for each iteration, the function is approximated with a Taylor Series,
#   then the derivatives and error are calcualted. Max and min error
#   are determined, and everything is stored in an array for graph use

for i in range(n):

    xph = x + h # use in f(x+h) = f(xph), x = 1 and h decreases with each iteration
    xmh = x - h # use in f(x-h) = f(xmh), same deal

    # taylor series expansions for f(x), f(x+h), and f(x-h) using 5 terms:
    fx = x - ((x**3)/tfact) + ((x**5)/ffact) - ((x**7)/sfact) + ((x**9)/nfact) # sin(x) 
    fxph = (xph) - ((xph**3)/tfact) + ((xph**5)/ffact) - ((xph**7)/sfact) + ((xph**9)/nfact) # sin(x+h)
    fxmh = (xmh) - ((xmh**3)/tfact) + ((xmh**5)/ffact) - ((xmh**7)/sfact) + ((xmh**9)/nfact) # sin(x-h)
    
    #-------------------------------------------#
    #        Numerical Differentiation:         #
    
    # calculation of f'(x) = (f(x+h)-f(x))/h
    fprime1 = (fxph - fx)/h
    
    # calculation of f'(x) = (f(x+h)-f(x-h))/2h
    fprime2 = (fxph - fxmh)/(2*h)    
    #-------------------------------------------#


    #-------------------------------------------#
    #       Truncation Error Calculations       #
    t_error1 = abs(math.cos(x) - fprime1) # error = |cosx - f'(x)|
    t_error2 = abs(math.cos(x) - fprime2) # error = |cosx - f'(x)|
    t_error3 = abs(math.sin(x) - fx) # error = |sinx - f(x)|, just curious about to see
    
    # to-do: I want to plot the error per iteration so we can see it
    # minimum error calculations
    if t_error1 < te_min1: # check to see if error has decreased
        te_min1 = t_error1 # if so, save it
        imin1 = i # track the iteration number for later results
    
    if t_error2 < te_min2:
        te_min2 = t_error2
        imin2 = i

    # maximum error calculations, same process as min error
    if t_error1 > te_max1:
        te_max1 = t_error1
        imax1 = i

    if t_error2 > te_max2:
        te_max2 = t_error2
        imax2 = i
    #-------------------------------------------#


    #-------------------------------------------#
    #       Rounding Error Calculations         #

    round_error = e/h # machine epsilon divided by h

    if round_error > re_max: # check to see if error has increased
        re_max = round_error # if so, keep it
        imax = i # track the it. number for later results

    if round_error < re_min: # check to see if error has decreased
        re_min = round_error # if so, keep it
        imin = i # track the it. number for later results
    #-------------------------------------------#


    #-------------------------------------------#
    #         Total Error Calculations          #

    total_error1 = t_error1 + round_error # trunc + round
    total_error2 = t_error2 + round_error # trunc + round

    # Looking for max and min vals
    if total_error1 < total_min1: # check to see if error has decreased
        total_min1 = total_error1 # if so, keep it
        total_imin1 = i # track the it. number for later results
        total_opth1 = h
    
    if total_error2 < total_min2:
        te_min2 = total_error2
        total_imin2 = i
        total_opth2 = h

    # maximum error calculations, same process as min error
    if total_error1 > total_max1:
        total_max1 = total_error1
        total_imax1 = i

    if total_error2 > total_max2:
        total_max2 = total_error2
        total_imax2 = i

    #-------------------------------------------#
    #        Store values to be plotted         #
    trunc_array1.append(t_error1) # eq. 1 trunc error
    trunc_array2.append(t_error2) # eq. 2 trunc error
    total_array1.append(total_error1) # eq. 1 total error
    total_array2.append(total_error2) # eq. 2 total error
    round_array.append(round_error) # rounding error
    #-------------------------------------------#

    # last step per iteration: reduce h s.t. (h->0)
    h_array.append(h) # save h vals
    h = 0.25*h        # decrease h

#----------------------------------------------------#
# converting to numpy arrays for plotting purposes:
trunc_array1 = np.array(trunc_array1)
trunc_array2 = np.array(trunc_array2)
total_array1 = np.array(total_array1)
total_array2 = np.array(total_array2)
round_array = np.array(round_array)
#----------------------------------------------------#
# Plot Equation 1
plt.figure(figsize=(8,6))
plt.loglog(h_array, trunc_array1, label="Eq. 1 Truncation Error Bound", linestyle="--", color="red")
plt.loglog(h_array, total_array1, label="Eq. 1 Total Error Bound", linestyle="--", color="blue")
plt.loglog(h_array, round_array, label="Rounding Error Bound", linestyle="--", color="black")

plt.xlabel(r"$\log_{10} h$") # x-axis, h values
plt.ylabel(r"$\log_{10} | \text{error} |$") # y-axis, positive values
plt.title("Eq. 1 Error Bound vs. h")
plt.legend() # create legend for all five lines
plt.grid(True, which="both", linestyle="--")
#plt.show()
#plt.savefig("Eq1plot.png") # saving an image is the only way I could view it
#----------------------------------------------------#
# Plot Equation 2
plt.figure(figsize=(8,6))
plt.loglog(h_array, trunc_array2, label="Eq. 2 Truncation Error Bound", linestyle="--", color="red")
plt.loglog(h_array, total_array2, label="Eq. 2 Total Error Bound", linestyle="--", color="blue")
plt.loglog(h_array, round_array, label="Rounding Error Bound", linestyle="--", color="black")

plt.xlabel(r"$\log_{10} h$") # x-axis, h values
plt.ylabel(r"$\log_{10} | \text{error} |$") # y-axis, positive values
plt.title("Eq. 2 Error Bound vs. h")
plt.legend() # create legend for all five lines
plt.grid(True, which="both", linestyle="--") 
# plt.savefig("Eq2plot.png") # saving an image is the only way I could view it

#----------------------------------------------------#
# Printing reports

# Printing total error:
print("\n#---------------------------------------------------#")
print("                 Total Error Values:                   ")
print("\nEquation 1:")
print("Iteration with minimum error = ", total_imin1)
print("Minimum error = ", total_min1)
print("Iteration with maximum error = ", total_imax1)
print("Maximum error = ", total_max1)
print("\nEquation 2:")
print("Iteration with minimum error = ", total_imin2)
print("Minimum error = ", total_min2)
print("Iteration with maximum error = ", total_imax2)
print("Maximum error = ", total_max2)
print("#-----------------------------------------------------#")


# Printing truncation error:
print("\n#---------------------------------------------------#")
print("              Truncation Error Values:                 ")
print("       For large h, truncation error dominates         ")
#print("\nOriginal f(x) Approximation error = ", error3)
print("\nEquation 1:")
print("Iteration with minimum error = ", imin1)
print("Minimum error = ", te_min1)
print("Iteration with maximum error = ", imax1)
print("Maximum error = ", te_max1)
print("\nEquation 2:")
print("Iteration with minimum error = ", imin2)
print("Minimum error = ", te_min2)
print("Iteration with maximum error = ", imax2)
print("Maximum error = ", te_max2)
print("#-----------------------------------------------------#")


# Printing rounding error:
print("\n#---------------------------------------------------#")
print("              Rounding Error Values:                   ")
print("       For small h, rounding error dominates           ")
print("\nIteration with minimum rounding error = ", imin)
print("Minimum error = ", re_min)
print("\nIteration with maximum rounding error = ", imax)
print("Minimum error = ", re_max)
print("#-----------------------------------------------------#")

# Print conclusion from findings
print("\n#---------------------------------------------------#")
print("                     Conclusions:                      ")
print("\n1. For high iteration # and small h, rounding error dominates.")
print("2. For low iteration # and large h, truncation error dominates.")
print("3. Equation 1 optimal h value = ", total_opth1)
print("4. Equation 2 optimal h value = ", total_opth2)
print("5. Total Error increases after too many iterations.")
print("\n NOTE: Both graphs can be saved as a .png file. See lines 192 and 205 to save files.\n")
