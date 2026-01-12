# Formatação de String
# Um tipo de formatação é a f-strings, que iremos usar abaixo

nome = 'Ricardo Souza'
altura = 1.85
peso = 78
imc = peso/altura**2

linha_1 = f'Seu nome é {nome}'
linha_2 = f'Sua Altura é {altura} m'
linha_3 = f'Seu peso é {peso} kg'
linha_4 = f'Seu imc é {imc:.2f}' 

print(linha_1)
print(linha_2)
print(linha_3)
print(linha_4)

#Outra forma é utilizar a função format.

a='AAA'
b='BBB'
c=1.2346
string='a={} b={} c={:.2f}'
formato = string.format(a,b,c)
print(formato)

#ou posso indicar os índices, a ordem começa no zero
string='a={2:.2f} b={1} c={0}'
formato2 = string.format(a,b,c)
print(formato2)





