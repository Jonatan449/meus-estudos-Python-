real=float(input('Quantos reais você quer converter em dólar americano?: '))
dolar=real/5.08
print('_'*52)
print(f'com {real:.2f} real(is) você consegue comprar {dolar:.2f} dólar(es)')
print('_'*52)
#lembrando que esse valor é o valor do dólar de hoje(09/08/2026), então pode ser que em datas diferentes ele erre, ou seja, não é um conversor de câmbio real.