#!/usr/bin/env python3
 
from scipy.stats import chi2
import sys

def usage()->str:
    return '''
    Esse Script calcula a probabilidade entre intervalos de possiveis variancias 

     Exemplo: Em um experimento foram feitas 20 medidas de altura e obtida uma variancia de 2 m²
     calcule qual a probabilidade de em uma amostra de 20 medidas a variancia estar entre 1.5 e 4
        Use : 
            python3 variancia_amostral.py 20 2 1.5 4
            Stdout : 
            A probabilidade de 1.5 < s² < 4.0 é 0.763

    python3 N_of_samples variance interval1 interval2
    
    N of samples -Número de amostras  
    variance - variancia
    interval 1 -intervalo menor
    interval 2 - intervalo maior
    '''




if __name__ == "__main__":
    if len(sys.argv)<5:
        print(usage())
        exit
    
    N_of_samples = int(sys.argv[1])
    variance = float(sys.argv[2])
    interval1 = float(sys.argv[3])
    interval2 = float(sys.argv[4])

    grau_de_liberdade = N_of_samples - 1

    index_inferior = grau_de_liberdade * (interval1/variance)
    index_superior = grau_de_liberdade * (interval2/variance)

    probabilidade_ate_inferior = chi2.cdf(index_inferior,df = grau_de_liberdade)    
    probabilidade_ate_superior = chi2.cdf(index_superior,df=grau_de_liberdade)

    print(f'A probabilidade de {interval1} < s² < {interval2} é {round(probabilidade_ate_superior - probabilidade_ate_inferior,4)}')



