print('-' * 29,'\ncalcular a área do circulo', '\nBy Tálison Guimarães', '\n','-' * 28)

raio = float(input('\nDigite o raio do circulo: '))

cal = raio ** 2
cal1 = 3.14 * cal

print('''
a = π . r²
a = π x {}²
a = π x {}
a = {}
'''.format(raio, cal, cal1))
