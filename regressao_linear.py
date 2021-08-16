import pandas as pd
import scipy
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import math


def rsquared(x, y):
    """ Return R^2 where x and y are array-like."""

    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)
    return r_value**2

#arquivo = input('digite nome do arquivo:')
dados = pd.read_excel('regressao.xlsx')

#renomeando as colunas
dados = dados.rename(columns={'Tabela 1': 'coluna 1', 'Unnamed: 1': 'coluna 2', 'Unnamed: 2': 'coluna 3'})

#removendo a linha 0
dados = dados.drop(0)

#removendo todas as colunas com NaN
dados = dados.dropna(axis=1, how='all')
print(dados)

#converte dados para tipo float
dados['coluna 2'] = dados['coluna 2'].astype('float64')
dados['coluna 3'] = dados['coluna 3'].astype('float64')

X = dados['coluna 2'].values.reshape(-1,1)
y = dados['coluna 3'].values.reshape(-1,1)
reg = LinearRegression()
reg.fit(X, y)
print("O modelo é: Y = {:.5} + {:.5}X".format(reg.intercept_[0], reg.coef_[0][0]))

f_previsaoes = reg.predict(X)

#calculo da correlacao ao quadrado
correlacao_quad = rsquared(dados['coluna 2'], dados['coluna 3'])

plt.figure(figsize = (16,8))
plt.scatter(
    dados['coluna 2'],
    dados['coluna 3'],
    c='red')


plt.plot(
    dados['coluna 2'],
    f_previsaoes,
    c='blue',
    linewidth=3,
    linestyle=':'
)

A = reg.coef_[0][0]
B = reg.intercept_[0]

if A < 0:
    SINAL = -1
else:
    SINAL =1

plt.text(dados['coluna 2'].mean(), dados['coluna 3'].mean(), "O modelo é: Y = {:.5} + {:.5}X".format(B,A), fontsize=20)
plt.text(dados['coluna 2'].mean(), dados['coluna 3'].mean()-dados['coluna 3'].mean()*0.1, "A correlação  =  {:.5}".format(SINAL*math.sqrt(correlacao_quad)), fontsize=20)
plt.show()


print('COEFICIENTE DE DETERMINAÇÃO =  ', correlacao_quad)
