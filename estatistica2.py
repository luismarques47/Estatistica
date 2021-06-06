class estatistica:

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

        for i in range(self.numero_elementos):
            self.somaxifi = self.somaxifi + self.xi[i] * self.fi[i]
            self.somafi = self.somafi + self.fi[i]

            if i == 0:
                self.Fi.append(self.fi[i])
            else:
                self.Fi.append(self.Fi[i-1] + self.fi[i])


        tmp = max(self.fi)
        indice = self.fi.index(tmp)
        self.Moda = self.xi[indice]

        print('\nA média é igual a:', self.somaxifi / self.somafi)


        Md = self.somafi / 2
        for i in range(self.numero_elementos):
            if self.Fi[i] > Md:
                index = i
                break
        if (self.numero_elementos % 2) == 0:
            self.Mediana = (self.xi[index]+self.xi[index-1])/2
        else:
            self.Mediana = self.xi[index]

        self.intervalo_classe = input('Existe intervalo de classe?')
        if self.intervalo_classe == 'sim' or 's':
            self.intervalo_classe = int(input('Entre com a variação do intervalo'))
            self.Mediana = (self.xi[index]-self.intervalo_classe/2 +
                            ((Md-self.Fi[index-1])*self.intervalo_classe)/self.fi[index])
            D1 = self.fi[indice]-self.fi[indice-1]
            D2 = self.fi[indice] - self.fi[indice + 1]
            self.Moda = self.xi[indice]-self.intervalo_classe/2 + (D1/(D1+D2))*self.intervalo_classe

        print('A moda é igual a:', self.Moda)
        print('A mediana é igual a:', self.Mediana)


estatistica = estatistica()
estatistica.iniciar()
