print('-' * 31,'\nÁrea da coroa circular', '\nBy Tálison Guimarães\n', '-' * 30)

R = float(input('\nDigite o valor do raio maio: '))
r = float(input('Digite o valor do o raio menor: '))

if R > r:
    cR = R ** 2
    cr = r ** 2
    cal = cR - cr
    cal1 = cal * 3.14
    print('''
a = π (R² - r²)
a = π ({}² - {}²)
a = π ({:.2f} - {:.2f})
a = {}π 
ou
a = {} . 3.14
a = {}'''
.format(R, r, cR, cr, cal, cal, cal1))

else:
    print('\nOpss!!! Tem algo errado no valores acima.')