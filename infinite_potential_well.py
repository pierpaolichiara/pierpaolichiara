#progetto per calcolare e plottare autovalori e autostati di un elettrone in una buca di potenziale infinita e larga L
#import
import numpy as np
import matplotlib  
import scipy as sp


#parameters electron_mass, hbar, elementary_charge
hbar = constants.hbar
m = constants.m_e
pi = constants.pi

#input n, L
print('This programme gives the first n eigenfunctions and eigenvalues of an electron in a infinite potential well with a width L.') 
width =float(input('Please, insert the width of the potential well in Angstrom: L = '))           
n=int(input('Please, insert the number of the first eigenvalues and eigenstates of the electron you want to know: n = ')) 

#x?????
#L=width*                             #convertire unita' di misura

#definition of functions, to be put in separate files py
def eigenfunction(L,n):
  psi_n=sqrt(2/L)*cos(n*pi*x/L)
  return(psi_n)

def eigenvalues(L,n):         #definisco direttamente  E_n senza E_1?
  E_1=hbar**2pi**2/(2mL**2)   #meglio definirla fuori dalla funzione? altrimenti a ogni n la ricalcola inutilmente
  E_n=n**2*E_1                            # 
  return(E_n)

#calculations
for level in range (n):
  print(level, eigenfunction(L,n), eigenvalues(L,n)
  

#plot
