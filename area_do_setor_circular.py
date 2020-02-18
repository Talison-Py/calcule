print('-' * 30,'\nÁrea do setor circular','\nBy Tálison Guimarães\n', '-' * 29)

grau = int(input('\nDigite o grau da questão: '))
raio  = float(input('Digite o raio: '))

cal = grau * raio
raio1 = raio ** 2
cal2 = grau * raio1
cal3 = cal2 / 360
cal4 = cal2 * 3.14
cal5 = cal4 / 360

print('\n','''
A = 360°    π{}²
   ------ = -------
    {}°     x

a = 360°x = {}π x {} 
a = 360°x = {}π
a = {}π / 360°
a = {:.1f}π
ou 
a = {} / 360°
a = {}
'''
.format(raio, grau, grau, raio1, cal2, cal2, cal3, cal4, cal5))
