# 1 — Antecessor e sucessor

Y = int(input('Fala um número: '))

print(f'Seu antecessor é {Y - 1}')
print(f'Seu sucessor é {Y + 1}')


# 2 — Dobro, triplo e raiz quadrada

print(f'Dobro: {Y * 2}')
print(f'Triplo: {Y * 3}')
print(f'Raiz quadrada: {Y ** (1/2)}')


# 3 — Média de duas notas

nota = int(input('Sua nota do primeiro bimestre: '))
nota2 = float(input('Agora a do segundo: '))

print(f'A sua média é {(nota + nota2) / 2}')


# 4 — Conversor de metros

m = float(input('Fala um valor em metros: '))

c = m * 100
mm = m * 1000

print(f'{m} m = {c} cm')
print(f'{m} m = {mm} mm')
