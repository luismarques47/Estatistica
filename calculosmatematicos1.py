import math

class calculos:

    def __init__(self):
        self.expoente = 0
        self.numero = 0
        self.m = 0
        self.n = 0
        self.x = 0
        self.y = 0
        self.resultado = 0
        self.opcao = 0

    def iniciar(self):

        while(self.opcao != 5):

            print('1 -  fatorial')
            print('2 -  combinação')
            print('3 -  exponenciação')
            print('4 -  yˆx')
            print('5 -  sair')
            self.opcao = int(input('ESCOLHA UMA DAS OPÇÃO ACIMA:'))

            if self.opcao == 1:
                calculos.fatorial()
            if self.opcao == 2:
                 calculos.combinacao()
            if self.opcao == 3:
                calculos.exponenciacao()
            if self.opcao == 4:
                calculos.yelevadox()
            if self.opcao == 5:
                exit()

    def fatorial(self):

        self.numero = int(input('Entre com o valor para calcular o fatorial:'))
        print('resultado  = ', math.factorial(self.numero))

    def combinacao(self):

        self.m = int(input('Entre com o valor para m:'))
        self.n = int(input('Entre com o valor para n:'))
        self.resultado = math.factorial(self.m)/(math.factorial(self.n)*math.factorial(self.m-self.n))
        print('resultado = {:.2f}'.format(self.resultado))


    def exponenciacao(self):
        self.numero = float(input('Entre com o valor para calcular eˆx:'))
        print('resultado  = {:.4f}'.format(math.exp(self.numero)))

    def yelevadox(self):
        self.y = float(input('Entre com o valor para y:'))
        self.x = float(input('Entre com o valor para x:'))
        print('resultado  = {:.4f}'.format(self.y**self.x))


calculos = calculos()
calculos.iniciar()



