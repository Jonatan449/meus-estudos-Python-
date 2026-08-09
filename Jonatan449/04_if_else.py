ano = int(input('Em que ano você nasceu? '))

idade = 2030 - ano

if idade >= 18:
    print(f'Em 2030 você será maior de idade e terá {idade} anos.')
else:
    print(f'Em 2030 você será menor de idade e vai ter {idade} anos')
