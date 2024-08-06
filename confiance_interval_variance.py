#!/usr/bin/env python3
 
from scipy.stats import chi2
import sys


if __name__ == "__main__":
    
    N_of_samples = int(sys.argv[1])
    variance = float(sys.argv[2])
    alpha = float(sys.argv[3])

    grau_de_liberdade = N_of_samples - 1


    r1 = chi2.ppf((1-(alpha/2)),df = grau_de_liberdade)    
    r2 = chi2.ppf((alpha/2),df=grau_de_liberdade)

    inferior = grau_de_liberdade * variance / r1
    superior = grau_de_liberdade * variance / r2

    print(f'O intervalo de confiança é {inferior,superior} para alpha = {1- alpha} amplitude {abs(superior-inferior)}')
