from turtle import title
import matplotlib.pyplot as plt
import numpy as np


cp=1004 
R=287
gamma=1.4
T0=216.7
PCI =44800
Tt4= 2200
a0=295.07
M = PCI/(cp*T0)

pi_c_values=[]

f_M0_values=[]
f_M0_5_values=[]
f_M1_values=[]
f_M1_5_values=[]
f_M2_values=[]
f_M2_5_values=[]
f_M3_values=[]


fstar_M0_values=[]
fstar_M0_5_values=[]
fstar_M1_values=[]
fstar_M1_5_values=[]
fstar_M2_values=[]
fstar_M2_5_values=[]
fstar_M3_values=[]

s_M0_values= []
s_M0_5_values= []
s_M1_values= []
s_M1_5_values= []
s_M2_values= []
s_M2_5_values= []
s_M3_values= []

n_theo_M0_values= []
n_theo_M0_5_values= []
n_theo_M1_values= []
n_theo_M1_5_values= []
n_theo_M2_values= []
n_theo_M2_5_values= []
n_theo_M3_values= []


for pi_c in np.arange(1,40,1): 
    
        tau_lambda= 7.6 #tau_lambda varies [6,10]
        

        tau_r_M0 = 1 + (((gamma-1)/2)*(0**2))
        tau_r_M0_5 = 1 + (((gamma-1)/2)*(0.5**2))
        tau_r_M1 = 1 + (((gamma-1)/2)*(1**2))
        tau_r_M1_5 = 1 + (((gamma-1)/2)*(1.5**2))
        tau_r_M2 = 1 + (((gamma-1)/2)*(2**2))
        tau_r_M2_5 = 1 + (((gamma-1)/2)*(2.5**2))
        tau_r_M3 = 1 + (((gamma-1)/2)*(3**2))        
        
        tau_c = pi_c**((gamma-1)/gamma)
        tau_t_M0 = 1 - ((tau_r_M0/tau_lambda)*(tau_c -1))
        tau_t_M0_5 = 1 - ((tau_r_M0_5 /tau_lambda)*(tau_c -1))
        tau_t_M1 = 1 - ((tau_r_M1/tau_lambda)*(tau_c -1))
        tau_t_M1_5  = 1 - ((tau_r_M1_5/tau_lambda)*(tau_c -1))
        tau_t_M2 = 1 - ((tau_r_M2/tau_lambda)*(tau_c -1))
        tau_t_M2_5 = 1 - ((tau_r_M2_5/tau_lambda)*(tau_c -1))
        tau_t_M3 = 1 - ((tau_r_M3/tau_lambda)*(tau_c -1))

#Calcul of specific thrust values 
        fstar_M0 = a0 *( np.sqrt((2/(gamma-1))*(tau_lambda/(tau_r_M0*tau_c))*((tau_r_M0 * tau_c * tau_t_M0)-1)) - 0)
        fstar_M0_5 = a0 *( np.sqrt((2/(gamma-1))*(tau_lambda/(tau_r_M0_5*tau_c))*((tau_r_M0_5 * tau_c * tau_t_M0_5)-1)) - 0.5)
        fstar_M1 = a0 *( np.sqrt((2/(gamma-1))*(tau_lambda/(tau_r_M1*tau_c))*((tau_r_M1 * tau_c * tau_t_M1)-1)) - 1)
        fstar_M1_5 = a0 *( np.sqrt((2/(gamma-1))*(tau_lambda/(tau_r_M1_5*tau_c))*((tau_r_M1_5 * tau_c * tau_t_M1_5)-1)) - 1.5)
        fstar_M2 = a0 *( np.sqrt((2/(gamma-1))*(tau_lambda/(tau_r_M2*tau_c))*((tau_r_M2 * tau_c * tau_t_M2)-1)) - 2)
        fstar_M2_5 = a0 *( np.sqrt((2/(gamma-1))*(tau_lambda/(tau_r_M2_5*tau_c))*((tau_r_M2_5 * tau_c * tau_t_M2_5)-1)) - 2.5)
        fstar_M3 = a0 *( np.sqrt((2/(gamma-1))*(tau_lambda/(tau_r_M3*tau_c))*((tau_r_M3 * tau_c * tau_t_M3)-1)) - 3)

        fstar_M0_values.append(fstar_M0)
        fstar_M0_5_values.append(fstar_M0_5)
        fstar_M1_values.append(fstar_M1)
        fstar_M1_5_values.append(fstar_M1_5)
        fstar_M2_values.append(fstar_M2)
        fstar_M2_5_values.append(fstar_M2_5)
        fstar_M3_values.append(fstar_M3)

#Calcul of fuel/air ratio values 
        f_M0 = ((cp * T0)/PCI)*(tau_lambda- (tau_r_M0*tau_c))
        f_M0_5 = ((cp * T0)/PCI)*(tau_lambda- (tau_r_M0_5*tau_c))
        f_M1 = ((cp * T0)/PCI)*(tau_lambda- (tau_r_M1*tau_c))
        f_M1_5 = ((cp * T0)/PCI)*(tau_lambda- (tau_r_M1_5*tau_c))
        f_M2 = ((cp * T0)/PCI)*(tau_lambda- (tau_r_M2*tau_c))
        f_M2_5 = ((cp * T0)/PCI)*(tau_lambda- (tau_r_M2_5*tau_c))
        f_M3 = ((cp * T0)/PCI)*(tau_lambda- (tau_r_M3*tau_c))
   
        f_M0_values.append(f_M0)
        f_M0_5_values.append(f_M0_5)
        f_M1_values.append(f_M1)
        f_M1_5_values.append(f_M1_5)
        f_M2_values.append(f_M2)
        f_M2_5_values.append(f_M2_5)
        f_M3_values.append(f_M3)

#Calcul od specific thrust fuel consumption values 
        s_M0 = a0 * (f_M0/ fstar_M0)
        s_M0_5 = a0 * f_M0_5/ fstar_M0_5
        s_M1 = a0 * f_M1/ fstar_M1
        s_M1_5 = a0 * f_M1_5/ fstar_M1_5
        s_M2 = a0 * f_M2/ fstar_M2
        s_M2_5 = a0 * f_M2_5/ fstar_M2_5
        s_M3 = a0 * f_M3/ fstar_M3
        s_M0_values.append(s_M0)
        s_M0_5_values.append(s_M0_5)
        s_M1_values.append(s_M1)
        s_M1_5_values.append(s_M1_5)
        s_M2_values.append(s_M2)
        s_M2_5_values.append(s_M2_5)
        s_M3_values.append(s_M3)

#Calcul of the thermal efficiency values 
        n_theo_M0 = 1 - (1/(tau_r_M0*tau_c))
        n_theo_M0_5 = 1 - (1/(tau_r_M0_5*tau_c))
        n_theo_M1 = 1 - (1/(tau_r_M1*tau_c))
        n_theo_M1_5 = 1 - (1/(tau_r_M1_5*tau_c))
        n_theo_M2 = 1 - (1/(tau_r_M2*tau_c))
        n_theo_M2_5 = 1 - (1/(tau_r_M2_5*tau_c))
        n_theo_M3 = 1 - (1/(tau_r_M3*tau_c))
        n_theo_M0_values.append(n_theo_M0)
        n_theo_M0_5_values.append(n_theo_M0_5)
        n_theo_M1_values.append(n_theo_M1)
        n_theo_M1_5_values.append(n_theo_M1_5)
        n_theo_M2_values.append(n_theo_M2)
        n_theo_M2_5_values.append(n_theo_M2_5)
        n_theo_M3_values.append(n_theo_M3)
        
        
        pi_c_values.append(pi_c)

                #PLOTTING

#1° plotting the specific thrust
plt.subplot(3,2,1,title='The specific thrust',xlabel='Pi c', ylabel='F* (N.s/Kg)')
plt.plot(pi_c_values,fstar_M0_values, color="#2d1ae2", linewidth= 1)
plt.plot(pi_c_values,fstar_M0_5_values, color="#f01a97", linewidth= 1)
plt.plot(pi_c_values,fstar_M1_values, color="#000000",linewidth= 1 )
plt.plot(pi_c_values,fstar_M1_5_values, color="#93880b",linewidth= 1 )
plt.plot(pi_c_values,fstar_M2_values, color="#93430b", linewidth= 1)
plt.plot(pi_c_values,fstar_M2_5_values, color="#f75c1b", linewidth= 1)
plt.plot(pi_c_values,fstar_M3_values, color="#00FF00", linewidth= 1)

#2° plotting  feul/air ration
plt.subplot(3,2,2,title='The feul air ratio',xlabel='Pi c', ylabel='f')
M0, =plt.plot(pi_c_values,f_M0_values, color="#2d1ae2", linewidth=1)
M0_5, =plt.plot(pi_c_values,f_M0_5_values, color="#f01a97", linewidth=1)
M1, =plt.plot(pi_c_values,f_M1_values, color="#000000", linewidth=1)
M1_5, =plt.plot(pi_c_values,f_M1_5_values, color="#93880b", linewidth=1)
M2, =plt.plot(pi_c_values,f_M2_values, color="#93430b", linewidth=1)
M2_5, =plt.plot(pi_c_values,f_M2_5_values, color="#f75c1b", linewidth=1)
M3, =plt.plot(pi_c_values,f_M3_values, color="#00FF00", linewidth=1)
                               
#3° plotting the thrust-specific fuel consumption
plt.subplot(3,2,3,
title='The thrust-specific fuel consumption',
xlabel='Pi c', ylabel='S (Kg/N.s)')
plt.plot(pi_c_values,s_M0_values, color="#2d1ae2", linewidth= 1)
plt.plot(pi_c_values,s_M0_5_values, color="#f01a97", linewidth= 1)
plt.plot(pi_c_values,s_M1_values, color="#000000",linewidth= 1 )
plt.plot(pi_c_values,s_M1_5_values, color="#93880b",linewidth= 1 )
plt.plot(pi_c_values,s_M2_values, color="#93430b", linewidth= 1)
plt.plot(pi_c_values,s_M2_5_values, color="#f75c1b", linewidth= 1)
plt.plot(pi_c_values,s_M3_values, color="#00FF00", linewidth= 1)

#4° plotting the thermal efficiency
plt.subplot(3,2,4,
title='The thermal efficiency',
xlabel='Pi c', ylabel='n th')
plt.plot(pi_c_values,n_theo_M0_values, color="#2d1ae2", linewidth= 1)
plt.plot(pi_c_values,n_theo_M0_5_values, color="#f01a97", linewidth= 1)
plt.plot(pi_c_values,n_theo_M1_values, color="#000000",linewidth= 1 )
plt.plot(pi_c_values,n_theo_M1_5_values, color="#93880b",linewidth= 1 )
plt.plot(pi_c_values,n_theo_M2_values, color="#93430b", linewidth= 1)
plt.plot(pi_c_values,n_theo_M2_5_values, color="#f75c1b", linewidth= 1)
plt.plot(pi_c_values,n_theo_M3_values, color="#00FF00", linewidth= 1)

plt.subplot(3,2,5)
plt.legend([M0,M0_5, M1,M1_5,M2, M2_5,M3], ['M=0','M=0.5','M=1', 'M=1.5', 'M=2', 'M=2.5', "M=3"])

plt.show()

