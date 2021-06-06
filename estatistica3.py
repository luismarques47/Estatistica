class Estatistica:

    def __init__(self):
        self.xi = []
        self.fi = []
        self.Fi = []
        self.numero_elementos = 0
        self.elemento = 0
        self.somaxifi = 0
        self.somafi = 0
        self.Mediana = 0
        self.Moda = 0
        self.intervalo_classe = 0
        self.ic = 'n'
        self.Desvio = 0
        self.somafixi2 = 0
        self.media = 0
        self.Variancia = 0
        self.index = 0
        self.coeficientevariacao = 0

    def iniciar(self):
        self.numero_elementos = int(input('Digite o numero de dados para análise:'))

        for i in range(self.numero_elementos):
            self.elemento = float(input('Digite o elemento x%i:' % (i + 1)))
            self.xi.append(self.elemento)
            self.elemento = float(input('Digite o elemento f%i:' % (i + 1)))
            self.fi.append(self.elemento)

        print('\nA lista de dados xi para análise  é :', self.xi)
        print('\nA lista de dados fi para análise  é :', self.fi)
        input("Press Enter to continue...")

        self.ic = input('Existe intervalo de classe? (sim(s) ou não(n)')

        if self.ic == 's':
            self.intervalo_classe = int(input('Entre com a variação do intervalo'))

        for i in range(self.numero_elementos):
            self.somaxifi = self.somaxifi + self.xi[i] * self.fi[i]
            self.somafi = self.somafi + self.fi[i]

            if i == 0:
                self.Fi.append(self.fi[i])
            else:
                self.Fi.append(self.Fi[i - 1] + self.fi[i])

    def valormedio(self):
        self.media = self.somaxifi / self.somafi
        print('\nA média é igual a:', self.media)

    def mediana(self):
        md = self.somafi / 2
        for i in range(self.numero_elementos):
            if self.Fi[i] > md:
                self.index = i
                break
        if (self.numero_elementos % 2) == 0:
            self.Mediana = (self.xi[self.index] + self.xi[self.index - 1]) / 2
        else:
            self.Mediana = self.xi[self.index]

        if self.ic == 'sim' or 's':
            self.Mediana = (self.xi[self.index] - self.intervalo_classe / 2 +
                            ((md - self.Fi[self.index - 1]) * self.intervalo_classe) / self.fi[self.index])

        print('A mediana é igual a:', self.Mediana)

    def moda(self):

        tmp = max(self.fi)
        indice = self.fi.index(tmp)
        self.Moda = self.xi[indice]

        if self.ic == 'sim' or 's':
            d1 = self.fi[indice] - self.fi[indice - 1]
            d2 = self.fi[indice] - self.fi[indice + 1]
            self.Moda = self.xi[indice] - self.intervalo_classe / 2 + (d1 / (d1 + d2)) * self.intervalo_classe

        print('A moda é igual a:', self.Moda)

    def variancia(self):

        for i in range(self.numero_elementos):
            self.somafixi2 = self.somafixi2 + self.fi[i]*(self.xi[i])**2

        self.Variancia = self.somafixi2 / self.somafi - (self.somaxifi / self.somafi)**2

        print('A variania é igual a:', self.Variancia)

    def desvio(self):

        self.Desvio = self.Variancia**0.5

        print('O desvio padrão é igual a:', self.Desvio)

    def coeficientedevariacao(self):

        self.coeficientevariacao = (self.Desvio/self.media)*100

        print('O Coeficiente de variação é igual a:', self.coeficientevariacao)


estatistica = Estatistica()
estatistica.iniciar()
estatistica.valormedio()
estatistica.mediana()
estatistica.moda()
estatistica.variancia()
estatistica.desvio()
estatistica.coeficientedevariacao()