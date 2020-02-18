print('-' * 25,'\nBy Tálison Guimarães \n', '-'* 25)
print('Calcular equação de segundo grau por Baskara. \n')

ValorA = int(input('Digite o valor de A: '))
ValorB = int(input('Digite o valor de B: '))
ValorC = int(input('Digite o valor de C: '))

if ValorA < 0 and ValorB > 0 and ValorC < 0:
    delt = ValorB **2 
    delT = -4 * ValorA * ValorC
    delT = delT * -1
    delta = delt - delT
    print('Δ = {}'.format(delta))

    divDEdelta = 2 * ValorA
    caldel = (- ValorB + delta) / divDEdelta
    caldel1 = (- ValorB - delta) / divDEdelta
         
    if ValorA == -1:
        print('Portanto,1 as raízes da equação -x² + {}x {} = 0'.format(ValorB, ValorC),'''
X¹ = {} 
X² = {}'''.format(caldel, caldel1))
    else:
        print('Portanto,1 as raízes da equação {}x² + {}x {} = 0'.format(ValorA, ValorB, ValorC),'''
X¹ = {} 
X² = {}'''.format(caldel, caldel1))

elif ValorA > 0 and ValorB > 0 and ValorC < 0:
    delt = ValorB **2 
    delT = -4 * ValorA * ValorC
    delta = delt + delT
    print('Δ = {}'.format(delta))

    divDEdelta = 2 * ValorA
    delta = delta ** 0.5
    caldel = ( - ValorB + delta) / divDEdelta
    caldel1 = ( - ValorB - delta) / divDEdelta
    
        
    if ValorA == 1:
        print('Portanto,2 as raízes da equação x² + {}x {} = 0'.format(ValorB, ValorC),'''
X¹ = {} 
X² = {}'''.format(caldel, caldel1))
    
    else:
        print('Portanto,2 as raízes da equação {}x² + {}x {} = 0'.format(ValorA, ValorB, ValorC),'''
X¹ = {} 
X² = {}'''.format(caldel, caldel1))
    
elif ValorA < 0 and ValorB > 0 and ValorC > 0:
    delt = ValorB **2 
    delT = -4 * ValorA * ValorC
    delta = delt + delT
    print('Δ = {}'.format(delta))

    divDEdelta = 2 * ValorA
    delta = delta ** 0.5
    caldel = (- ValorB + delta) / divDEdelta
    caldel1 = (- ValorB - delta) / divDEdelta
    
    if ValorA == -1:
        print('Portanto,3 as raízes da equação -x² + {}x + {} = 0'.format(ValorB, ValorC),'''
X¹ = {} 
X² = {}'''.format(caldel, caldel1))
    else: 
        print('Portanto,3 as raízes da equação {}x² + {}x + {} = 0'.format(ValorB, ValorC),'''
X¹ = {} 
X² = {}'''.format(caldel, caldel1))  
    
elif ValorA > 0 and ValorB < 0 and ValorC < 0: 
    delt = ValorB ** 2
    delT = -4 * ValorA * ValorC
    delta = delt + delT
    print('Δ = {}'.format(delta))
   
    divDEdelta = 2 * ValorA
    delta = delta ** 0.5
    ValorB = ValorB * -1
    caldel =  (ValorB + delta) / divDEdelta       
    caldel1 =  (ValorB - delta) / divDEdelta
    
    if ValorA == 1:
        print('Portanto, as raízes da equação x² - {}x {} = 0'.format(ValorB, ValorC),'''
X¹ = {} 
X² = {}'''.format(caldel, caldel1))
    else:
        print('Portanto, as raízes da equação {}x² - {}x {} = 0'.format(ValorA, ValorB, ValorC),'''
X¹ = {} 
X² = {}'''.format(caldel, caldel1))

elif ValorA > 0 and ValorB < 0 and ValorC > 0:
    delt = ValorB ** 2
    delT = - 4 * ValorA * ValorC
    delT = delT * -1
    delta = delt - delT
    print('Δ = {}'.format(delta))

    divDEdelta = 2 * ValorA
    delta = delta ** 0.5
    ValorB = ValorB * -1
    caldel = (ValorB + delta) / divDEdelta
    caldel1 = (ValorB - delta) / divDEdelta
    if ValorA == 1:
        print('Portanto, as2 raízes da equação x² - {}x + {} = 0'.format(ValorB, ValorC),'''
X¹ = {} 
X² = {}'''.format(caldel, caldel1))
    else:
        print('Portanto, as raízes da equação {}x² - {}x + {} = 0'.format(ValorA, ValorB, ValorC),'''
X¹ = {} 
X² = {}'''.format(caldel, caldel1))

elif ValorA > 0 and ValorB > 0 and ValorC > 0:
    delt = ValorB ** 2
    delT = -4 * ValorA * ValorC
    delT = delT * -1
    delta = delt - delT
    print('Δ = {}'.format(delta))

    divDEdelta = 2 * ValorA
    delta = delta ** 0.5
    caldel = (- ValorB + delta) / divDEdelta
    caldel1 = (- ValorB - delta) / divDEdelta
    
    if ValorA == 1:
        print('Portanto, as raízes da equação x² + {}x + {} = 0'.format(ValorB, ValorC),'''
X¹ = {} 
X² = {}'''.format(caldel, caldel1))
    else:
        print('Portanto, as raízes da equação {}x² + {}x + {} = 0'.format(ValorA, ValorB, ValorC),'''
X¹ = {} 
X² = {}'''.format(caldel,
caldel1))

else:
    print('Desculpe, ainda não posso fazer este calculo.')