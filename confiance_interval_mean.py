from scipy.stats import norm
import sys

def usage():
    return '''
    '''

if __name__ == "__main__":
    N_amostras = int(sys.argv[1])
    alpha =  float(sys.argv[2])
    media  = float(sys.argv[3])
    desvio_padrao =  float(sys.argv[4])
    z_score = norm.ppf(1-(alpha/2))
    erro = z_score*(desvio_padrao/(N_amostras**0.5))
    print(f"erro : {erro} intervalo de confiança = {(media-erro,media+erro) }")
