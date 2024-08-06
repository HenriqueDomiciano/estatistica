from scipy.stats import norm
import sys

if __name__== '__main__':

    n_amostras = int(sys.argv[1])
    alpha = float(sys.argv[2])
    z_score = norm.ppf(1-(alpha/2))
    cons = input("Conservador[Y/N]").upper()=='Y'
    if cons:
        p = 0.5 
    else:
        p = float(input("Digite a proporção: "))
    erro = z_score*(((p*(1-p))/n_amostras)**0.5)

    print(f"erro = {erro} ")