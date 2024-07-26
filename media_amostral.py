#!/usr/bin/env python3
 
from scipy.stats import t
import sys

def usage()->str:
    return f'''
    Usage ; 
    python3 {sys.argv[0]} N_of_samples desvio_padrao media interval1 interval2
    N of samples -Número de amostras  
    desvio_padrao - desvio padrão 
    interval 1 -intervalo menor
    interval 2 - intervalo maior
    '''




if __name__ == "__main__":
    if len(sys.argv)!=6:
        print(usage())
        exit()
    
    N_of_samples = int(sys.argv[1])
    desvio = float(sys.argv[2])
    media = float(sys.argv[3])
    interval1 = float(sys.argv[4])
    interval2 = float(sys.argv[5])

    grau_de_liberdade = N_of_samples - 1

    index_inferior = (interval1 - media)/(desvio/(N_of_samples**0.5))
    index_superior = (interval2 - media)/(desvio/(N_of_samples**0.5))

    probabilidade_ate_inferior = t.cdf(index_inferior,df = grau_de_liberdade)    
    probabilidade_ate_superior = t.cdf(index_superior,df=grau_de_liberdade)

    print(f'A probabilidade de {interval1} < u < {interval2} é {round(probabilidade_ate_superior - probabilidade_ate_inferior,4)}')



