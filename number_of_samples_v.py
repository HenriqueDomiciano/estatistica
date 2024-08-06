#!/usr/bin/env python3

from scipy.stats import norm
import sys 


def usage()->str:
    return '''
    '''

if __name__ ==  "__main__":
    
    variancia = float(sys.argv[1])
    media = float(sys.argv[2]) 
    confianca = float(sys.argv[3])
    error = float(sys.argv[4]) 
    z_score = norm.ppf((1-confianca/2))

    amostras = (z_score*(variancia**0.5)/error)**2
    print(f"O número de amostras necessárias é de {amostras} para o erro de {error}")
