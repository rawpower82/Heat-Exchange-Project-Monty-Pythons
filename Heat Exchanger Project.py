
import sys
import numpy as np
import sympy as sp
sp.init_printing()


def define_capacity(average, liquid_type):  # Parameters: Either average_hot or average_cold (depending on which stream), liquid type
    T = average
    # Define Specific Heat Capacities
    capacity_water = 276370 - 2090.1 * T + 8.125 * (T**2) - 0.014116 * (T**3) + 0.0000093701 * (T**4)
    capacity_tetraflo = 651080 - 9505.7 * T + 62.835 * (T**2) - 0.18264 * (T**3) + 0.00020031 * (T**4)
    capacity_ethanol = 102640 - 139.63 * T - .030341 * (T**2) + .0020386 * (T**3) + 0.0 * (T**4)
    capacity_trimethyl = 95300 - 696.70 * T - 1.3765 * (T**2) + .0021734 * (T**3) + 0.0 * (T**4)
    if liquid_type == water:
        return capacity_water
    elif liquid_type == tetraflo:
        return capacity_tetra
    elif liquid_type == ethanol:
        return capacity_ethanol
    elif liquid_type == trimethyl:
        return capacity_trimethyl


# Melting and Boiling Points 
melt_water = 273.15 # K
boil_water = 373.15 # K
melt_tetraflo = 172.00 # K
boil_tetraflo = 247.08 # K
melt_ethanol = 159.05 # K
boil_ethanol = 351.44 # K
melt_trimethyl = 165.777 # K
boil_trimethyl = 372.388 # K

# Molecular Weights
weight_water = 18.01528 # g/mol 
weight_tetraflo = 102.03089 # g/mol 
weight_ethanol = 46.06844 # g/mol 
weight_trimethyl = 114.22852 # g/mol 

# Input Liquid Types 
water = '1'
tetraflo = '2'
ethanol = '3'
trimethyl = '4'
print ("The liquid types are:")
print ("\t1) water")
print ("\t2) 1,1,1,2-tetrafluoroethane")
print ("\t3) ethanol")
print ("\t4) 2,2,4-trimethylpentane")
print ()
liquid_type_hot = input("What type of liquid is the hot stream? (Enter the number): ")
while liquid_type_hot != water and liquid_type_hot != tetraflo and liquid_type_hot != ethanol and liquid_type_hot != trimethyl:
    liquid_type_hot = input("Invalid entry. Please select an integer 1-4: ")
liquid_type_cold = input("What type of liquid is the cold stream? (Enter the number): ")
while liquid_type_cold != water and liquid_type_cold != tetraflo and liquid_type_cold != ethanol and liquid_type_cold != trimethyl:
    liquid_type_cold = input("Invalid entry. Please select an integer 1-4: ")

# Assign Constants to Hot Stream
if liquid_type_hot == water:
    hot_melt = melt_water
    hot_boil = boil_water
    hot_weight = weight_water
elif liquid_type_hot == tetraflo:
    hot_melt = melt_tetraflo
    hot_boil = boil_tetraflo
    hot_weight = weight_tetraflo
elif liquid_type_hot == ethanol:
    hot_melt = melt_ethanol
    hot_boil = boil_ethanol
    hot_weight = weight_ethanol
elif liquid_type_hot == trimethyl:
    hot_melt = melt_trimethyl
    hot_boil = boil_trimethyl
    hot_weight = weight_trimethyl

# Assign Constants to Cold Stream
if liquid_type_cold == water:
    cold_melt = melt_water
    cold_boil = boil_water
    cold_weight = weight_water
elif liquid_type_cold == tetraflo:
    cold_melt = melt_tetraflo
    cold_boil = boil_tetraflo
    cold_weight = weight_tetraflo
elif liquid_type_cold == ethanol:
    cold_melt = melt_ethanol
    cold_boil = boil_ethanol
    cold_weight = weight_ethanol
elif liquid_type_cold == trimethyl:
    cold_melt = melt_trimethyl
    cold_boil = boil_trimethyl
    cold_weight = weight_trimethyl
    





# Input Heat Transfer Coefficient (J/(s*m^2*K))
U_u=input("What units would you like to enter the heat transfer coefficient in, J/s*m^2*K or Btu/s*ft^2*R? enter 'Joules' or 'BTU':")
while U_u!='joules' and U_u != "Joules" and U_u!='BTU':
    U_u=input("invalid entry. please enter 'Joules' or 'BTU':")
# Input Heat Transfer Coefficient (J/(s*m^2*K))
U = input("What is the overall heat transfer coefficient (U) of the heat exchanger?: ")
try:
    U = float(U)
except: 
    print ("Error. Must enter a positive number. Goodbye.")
    sys.exit()
if U < 0:
    print ("Error: Cannot have a negative heat transfer coefficient. Goodbye.")
    sys.exit()
# Convert AES to SI    
if U_u=='joules' or U_u == "Joules":
    U=U
elif U_u== 'BTU':
    U=U*20441.96

    
    


# Input Flow Rates

# SI: kg/s 
# AES: lb/s ???
# 1 lb/s = 0.453592 kg/s 

# Flow Rate of the Cold Stream
# Identify Units
kg_o_lb = input("Would you like to input the flow rate of the cold stream in kg/s or lb/s ? Enter 'kg' for kg/s or 'lb' for lb/s: ")
while kg_o_lb != 'kg' and kg_o_lb != 'lb':
    kg_o_lb = input("Invalid entry. Please enter 'kg' for kg/s or 'lb' for lb/s: ")
# Input Flow Rate
flow_cold = input("What is the flow rate of the cold stream?: ")
valid = False
while valid == False:       # Loop which validates input 
    try:
        flow_cold = float(flow_cold)    # Makes sure that a number is entered rather than a string.
        valid = True
    except:
        flow_cold = input("Error. Please enter a number:")
# Convert AES to SI
if kg_o_lb == 'lb':
    flow_cold = flow_cold * 0.453592
if flow_cold < 0:        # Makes sure that the flow rate is not negative
    print ("Error: Cannot have a negative flow rate. Goodbye.")
    sys.exit()

    
# Flow Rate of the Hot Stream
# Identify Units
kg_o_lb = input("Would you like to input the flow rate of the hot stream in kg/s or lb/s ? Enter 'kg' for kg/s or 'lb' for lb/s: ")
while kg_o_lb != 'kg' and kg_o_lb != 'lb':
    kg_o_lb = input("Invalid entry. Please enter 'kg' for kg/s or 'lb' for lb/s: ")
# Input Flow Rate
flow_hot = input("What is the flow rate of the hot stream?: ")
valid = False
while valid == False:       # Loop which validates input 
    try:
        flow_hot = float(flow_hot)    # Makes sure that a number is entered rather than a string.
        valid = True
    except:
        flow_hot = input("Error. Please enter a number:")
# Convert AES to SI
if kg_o_lb == 'lb':
    flow_hot = flow_hot * 0.453592      # lb/s * (kg/s)/(lb/s) = kg/s
if flow_hot < 0:        # Makes sure that the flow rate is not negative
    print ("Error: Cannot have a negative flow rate. Goodbye.")
    sys.exit()
    
    
    
    
    
    
# Input Temperatures


# Temperature of Cold Stream Input
# Identify Units
k_o_f = input("Would you like to input the temperature of the cold input stream in Kelvin or Rankine? Enter 'K' for Kelvin or 'F' for Fahrenheit: ")
while k_o_f != 'K' and k_o_f != 'F':
    k_o_f = input("Invalid entry. Please enter 'K' for Kelvin or 'F' for Fahrenheit: ")
# Input Temperature
T_ci = input("What is the input temperature of the cold stream?: ")
valid = False
while valid == False:       # Loop which validates input 
    try:
        T_ci = float(T_ci)    # Makes sure that a number is entered rather than a string.
        valid = True
         # Convert AES to SI
        if k_o_f == 'F':
            T_ci = (T_ci+459.67) * 5.0/9.0
        if T_ci <= cold_melt:        # Makes sure that the temperature does not result in a solid
            T_ci = input("Error. This substance is a solid when it is at or below " + str(cold_melt) + "K (or " + str("{0:.2f}".format((cold_melt* 9.0/5.0)-459.67)) + "F). Enter a valid temperature: ")
            valid = False
        elif T_ci >= cold_boil:      # Makes sure that the temperature does not result in a gas
            T_ci = input("Error. This substance is a gas when it is at or above " + str(cold_boil) + "K (or " + str("{0:.2f}".format((cold_boil* 9.0/5.0)-459.67)) + "F). Enter a valid temperature: ")
            valid = False
    except:
        T_ci = input("Error. Please enter a number:")
   

        
# Temperature of Hot Stream Input
# Identify Units
k_o_f = input("Would you like to input the temperature of the hot input stream in Kelvin or Rankine? Enter 'K' for Kelvin or 'F' for Fahrenheit: ")
while k_o_f != 'K' and k_o_f != 'F':
    k_o_f = input("Invalid entry. Please enter 'K' for Kelvin or 'F' for Fahrenheit: ")
# Input Temperature
T_hi = input("What is the input temperature of the hot stream?: ")
valid = False
while valid == False:     # Loop which makes sure that a number is entered. 
    try:
        T_hi = float(T_hi)
        valid = True
        # Convert AES to SI
        if k_o_f == 'F':
            T_hi = (T_hi+459.67) * 5.0/9.0
        if T_hi <= hot_melt:        # Makes sure that the temperature does not result in a solid
            T_hi = input("Error. This substance is a solid when it is at or below " + str(hot_melt) + "K (or " + str("{0:.2f}".format((hot_melt* 9.0/5.0)-459.67)) + "F). Enter a valid temperature: ")
            valid = False
        elif T_hi >= hot_boil:      # Makes sure that the temperature does not result in a gas
            T_hi = input("Error. This substance is a gas when it is at or above " + str(hot_boil) + "K (or " + str("{0:.2f}".format((hot_boil* 9.0/5.0)-459.67)) + "F). Enter a valid temperature: ")
            valid = False
    except:
        T_hi = input("Error. Please enter a number:")
    
        
        
# Temperature of One Output
ho_co = input("Would you like to enter the output temperature of the hot or cold stream? Enter 'hot' or 'cold': ")
while ho_co != 'hot' and ho_co != 'cold':
    ho_co = input("Invalid entry. Please enter 'hot' or 'cold': ")
if ho_co == 'hot':
    # Identify Units
    k_o_f = input("Would you like to input the temperature of the hot output stream in Kelvin or Rankine? Enter 'K' for Kelvin or 'F' for Fahrenheit: ")
    while k_o_f != 'K' and k_o_f != 'F':
        k_o_f = input("Invalid entry. Please enter 'K' for Kelvin or 'F' for Fahrenheit: ")
    # Input Temperature
    T_ho = input("What is the output temperature of the hot stream?: ")
    valid = False
    while valid == False:       # Loop which makes sure that a number is entered. 
        try:
            T_ho = float(T_ho)
            valid = True
            # Convert AES to SI
            if k_o_f == 'F':
                T_ho = (float(T_ho)+459.67) * 5.0/9.0
            if T_ho <= hot_melt:        # Makes sure that the temperature does not result in a solid
                T_ho = input("Error. This substance is a solid when it is at or below " + str(hot_melt) + "K (or " + str("{0:.2f}".format((hot_melt* 9.0/5.0)-459.67)) + "F). Enter a valid temperature: ")
                valid = False
            elif T_ho >= hot_boil:      # Makes sure that the temperature does not result in a gas
                T_ho = input("Error. This substance is a gas when it is at or above " + str(hot_boil) + "K (or " + str("{0:.2f}".format((hot_boil * 9.0/5.0)-459.67)) + "F). Enter a valid temperature: ")
                valid = False
        except:
            T_ho = input("Error. Please enter a number:")
        
    # Calculate 4th temperature using first two equations
    averageT_hot = (T_hi+T_ho)/2
    capacity_hot = define_capacity(averageT_hot, liquid_type_hot)
    q = flow_hot * capacity_hot * (T_hi-T_ho)
    T_co = sp.Symbol("T_co")
    if liquid_type_cold == water:
        y = sp.Eq(q,flow_cold*(T_co-T_ci)*(276370 - 2090.1 * ((T_co+T_ci)/2) + 8.125 * (((T_co+T_ci)/2)**2) - 0.014116 * (((T_co+T_ci)/2)**3) + 0.0000093701 * (((T_co+T_ci)/2)**4)))
    elif liquid_type_cold == tetraflo:
        y = sp.Eq(q,flow_cold*(T_co-T_ci)*651080 - 9505.7 * ((T_co+T_ci)/2) + 62.835 * (((T_co+T_ci)/2)**2) - 0.18264 * (((T_co+T_ci)/2)**3) + 0.00020031 * (((T_co+T_ci)/2)**4))
    elif liquid_type_cold == ethanol:
        y = sp.Eq(q,flow_cold*(T_co-T_ci)*102640 - 139.63 * ((T_co+T_ci)/2) - .030341 * (((T_co+T_ci)/2)**2) + .0020386 * (((T_co+T_ci)/2)**3) + 0.0 * (((T_co+T_ci)/2)**4))
    elif liquid_type_cold == trimethyl:
        y = sp.Eq(q,flow_cold*(T_co-T_ci)*95300 - 696.70 * ((T_co+T_ci)/2) - 1.3765 * (((T_co+T_ci)/2)**2) + .0021734 * (((T_co+T_ci)/2)**3) + 0.0 * (((T_co+T_ci)/2)**4))
    z = sp.solve(y,T_co)   
    for i in range(np.size(z)-1):
        try:
            float(z[i])
        except:
            break
        if z[i].evalf() >= T_ci:
            T_co = z[i].evalf()
    print ("The output temperature of the cold stream is: " + str("{0:.2f}".format(T_co)) + "K")
    
elif ho_co == 'cold':
    # Identify Units
    k_o_f = input("Would you like to input the temperature of the could output stream in Kelvin or Rankine? Enter 'K' for Kelvin or 'F' for Fahrenheit: ")
    while k_o_f != 'K' and k_o_f != 'F':
        k_o_f = input("Invalid entry. Please enter 'K' for Kelvin or 'F' for Fahrenheit: ")
    # Input Temperature
    T_co = input("What is the output temperature of the cold stream?: ")
    valid = False
    while valid == False:       # Loop which makes sure that a number is entered. 
        try:
            T_co = float(T_co)
            valid = True
            # Convert AES to SI
            if k_o_f == 'F':
                T_co = (float(T_co)+459.67) * 5.0/9.0
            if T_co <= cold_melt:        # Makes sure that the temperature does not result in a solid
                T_co = input("Error. This substance is a solid when it is at or below " + str(cold_melt) + "K (or " + str("{0:.2f}".format((cold_melt * 9.0/5.0)-459.67)) + "F). Enter a valid temperature: ")
                valid = False
            elif T_co >= cold_boil:      # Makes sure that the temperature does not result in a gas
                T_co = input("Error. This substance is a gas when it is at or above " + str(cold_boil) + "K (or " + str("{0:.2f}".format((cold_boil * 9.0/5.0)-459.67)) + "F). Enter a valid temperature: ")
                valid = False
        except:
            T_co = input("Error. Please enter a number:")
        
    # Calculate 4th temperature using first two equations
    averageT_cold = (T_ci+T_co)/2
    capacity_cold = define_capacity(averageT_cold, liquid_type_cold)
    q = flow_cold * capacity_cold * (T_co-T_ci)
    T_ho = sp.Symbol("T_ho")
    if liquid_type_hot == water:
        y = sp.Eq(q,flow_hot*(T_hi-T_ho)*(276370 - 2090.1 * ((T_ho+T_hi)/2) + 8.125 * (((T_ho+T_hi)/2)**2) - 0.014116 * (((T_ho+T_hi)/2)**3) + 0.0000093701 * (((T_ho+T_hi)/2)**4)))
    elif liquid_type_hot == tetraflo:
        y = sp.Eq(q,flow_hot*(T_hi-T_ho)*(651080 - 9505.7 * ((T_ho+T_hi)/2) + 62.835 * (((T_ho+T_hi)/2)**2) - 0.18264 * (((T_ho+T_hi)/2)**3) + 0.00020031 * (((T_ho+T_hi)/2)**4)))
    elif liquid_type_hot == ethanol:
        y = sp.Eq(q,flow_hot*(T_hi-T_ho)*(102640 - 139.63 * ((T_ho+T_hi)/2) - .030341 * (((T_ho+T_hi)/2)**2) + .0020386 * (((T_ho+T_hi)/2)**3) + 0.0 * (((T_ho+T_hi)/2)**4)))
    elif liquid_type_hot == trimethyl:
        y = sp.Eq(q,flow_hot*(T_hi-T_ho)*(95300 - 696.70 * ((T_ho+T_hi)/2) - 1.3765 * (((T_ho+T_hi)/2)**2) + .0021734 * (((T_ho+T_hi)/2)**3) + 0.0 * (((T_ho+T_hi)/2)**4)))
    z = sp.solve(y,T_ho)
    for i in range(np.size(z)-1):
        try:
            float(z[i])
        except:
            break
        if z[i].evalf() <= T_hi:
            T_ho = z[i].evalf()
    print ("The output temperature of the hot stream is: " + str("{0:.2f}".format(T_ho)) + "K")
    
    
# Define Temperature Log Mean and delta T 1 & 2
dt1= float(abs(T_hi-T_co))
dt2= float(abs(T_ho-T_ci))
dtlm=(dt2-dt1)/(np.log(dt2/dt1))

    
# Define R, P, and F        
R=(T_hi-T_ho)/(T_co-T_ci)
P=(T_co-T_ci)/(T_hi-T_ci)
F=(((R**2+1)**(1/2))/(R-1))*(sp.log((1-P)/(1-P*R))/sp.log((2-P*(R+1-(R**2+1)**.5))/(2-P*(R+1+(R**2+1)**.5))))

# Find surface area
averageT_hot = (T_hi+T_ho)/2
capacity_hot = define_capacity(averageT_hot, liquid_type_hot)
q = flow_hot*capacity_hot*(T_hi-T_ho)/hot_weight
A=q/(F*U*dtlm) # m^2

# Find cost
cost = 1000 * A # USD
print ("\nThe area of the heat exchanger is: " + str("{0:.2f}".format(A)) + " m^2\n")
print ("The cost of the heat exchanger is: $" + str("{0:.2f}".format(cost)))