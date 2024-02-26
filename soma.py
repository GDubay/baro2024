soma= 0
contador =0
print("Digite os numero para calcular a média. Digite 0 (zero) para terminar.")
while True:
    valor=float(input("Digite um numero"))
    if valor ==0:
       break
    soma +=valor
    contador += 1
    if contador==0:
        print("Nenhum numero foi inserido.")
    else:
        media =soma/contador
        print("A media dos nmumero inseridos é:", media)  
