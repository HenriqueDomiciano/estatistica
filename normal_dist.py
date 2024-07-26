#!/usr/bin/env python3
 
from scipy.stats import norm
import sys

def usage()->str:
    return f'''
    Calcula a distribuição normal já com o desvio padrão ajustado para o número de amostras : 
    Exemplo : 
        python3 normal_dist.py 20 50 180 160 170
    Saída:
        Desvio padrão an=mostral é 11.180339887498947
        A probabilidade de 160.0 < sample < 170.0 é 0.1487
    Usage ; 
    python3 {sys.argv[0]} N_of_samples desvio_padrao media interval1 interval2
    N of samples -Número de amostras  
    desvio_padrao - desvio da população
    interval 1 - intervalo menor
    interval 2 - intervalo maior
    '''




if __name__ == "__main__":
    if len(sys.argv)!=6:
        print(usage())
        exit()
    
    N_of_samples = int(sys.argv[1])
    desvio = float(sys.argv[2])/(N_of_samples**0.5)
    media = float(sys.argv[3])
    interval1 = float(sys.argv[4])
    interval2 = float(sys.argv[5])

    print(f"Desvio padrão amostral é {desvio}")
    probabilidade_ate_inferior = norm.cdf(interval1,loc=media,scale=desvio)    
    probabilidade_ate_superior = norm.cdf(interval2,loc=media,scale=desvio)

    print(f'A probabilidade de {interval1} < sample < {interval2} é {round(probabilidade_ate_superior - probabilidade_ate_inferior,4)}')



