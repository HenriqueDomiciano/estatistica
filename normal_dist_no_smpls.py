#!/usr/bin/env python3
 
from scipy.stats import norm
import sys

def usage()->str:
    return f'''
    Esse Script calcula a probabilidade de um intervalo na curva normal, deve se apresentar a média o desvio padrão e os intervalospara rodar.

    Exemplo: Assuma que uma população possui QI que pode ser modelado pela curva normal com média 100 e desvio padrão 1, calcule a probabilidade de uma pessoa dessa população ao 
    acaso ter QI entre 101 e 102 
    
    Rode : 
        python3 normal_dist_no_smpls.py 1 100 101 102

    Saida:
        Desvio padrão da média é 1.0
        A probabilidade de 101.0 < sample < 102.0 é 0.1359 

    Usage : 
    python3 {sys.argv[0]} desvio_padrao media interval1 interval2
    desvio_padrao - desvio da população
    media - media
    interval 1 -intervalo menor
    interval 2 - intervalo maior
    '''

if __name__ == "__main__":
    if len(sys.argv)!=5:
        print(usage())
        exit()
    
    desvio = float(sys.argv[1])
    media = float(sys.argv[2])
    interval1 = float(sys.argv[3])
    interval2 = float(sys.argv[4])

    print(f"Desvio padrão da média é {desvio}")
    probabilidade_ate_inferior = norm.cdf(interval1,loc=media,scale=desvio)    
    probabilidade_ate_superior = norm.cdf(interval2,loc=media,scale=desvio)

    print(f'A probabilidade de {interval1} < sample < {interval2} é {round(probabilidade_ate_superior - probabilidade_ate_inferior,4)}')



