import numpy as np
import statistics


class estatistica:

    def __init__(self):
        self.dados = []
        self.numero_elementos = 0
        self.elemento = 0

    def iniciar(self):
        self.numero_elementos = int(input('Digite o numero de dados para análise:'))

        for i in range(self.numero_elementos):
            self.elemento = float(input('Digite o dado %i:' % (i+1)))
            self.dados.append(self.elemento)

        print('\nA lista de dados para análise  é :', self.dados)
        input("Press Enter to continue...")

        print('\nO valor mínimo é igual a:', np.min(self.dados))
        print('O valor máximo é igual a:', np.max(self.dados))
        print('A média é igual a:', np.mean(self.dados))
        print('A mediana é igual a:', np.median(self.dados))
        print('A variancia é igual a:', np.var(self.dados))
        print('O desvio padrão é igual a:', np.std(self.dados))
        print('A moda é igual a:', statistics.mode(self.dados))


estatistica = estatistica()
estatistica.iniciar()

