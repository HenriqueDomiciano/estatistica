#!/usr/bin/env python3
 
from scipy.stats import f
import sys

def usage()->str:
    return f'''
    Usage ; 
    python3 {sys.argv[0]} N_of_samples desvio_padrao media interval1 interval2
    N of samples1 -Número de amostras 1
    n OF SAMPLES 2 - Numero de amostras 2
    variancia 1 - variancia da primeira parte 
    variancia 2 - variancia da segunda parte
    interval 1 -intervalo menor
    interval 2 - intervalo maior
    '''




if __name__ == "__main__":
    if len(sys.argv)!=7:
        print(usage())
        exit()
    
    N_of_samples = int(sys.argv[1])
    N_of_samples2 = int(sys.argv[2])
    variancia1 = float(sys.argv[3])
    variancia2 = float(sys.argv[4])
    interval1 = float(sys.argv[5])
    interval2 = float(sys.argv[6])

    grau_de_liberdade1 = N_of_samples - 1
    grau_de_liberade2 = N_of_samples2 -1

    probabilidade_ate_inferior = f.cdf(interval1,dfn = grau_de_liberdade1, dfd = grau_de_liberade2)    
    probabilidade_ate_superior = f.cdf(interval2,dfn = grau_de_liberdade1, dfd = grau_de_liberade2)    

    print(f'A probabilidade de {interval1} < s² < {interval2} é {round(probabilidade_ate_superior - probabilidade_ate_inferior,4)}')



