from time import sleep as sono  #eu baixo da internet uma função que deixa o progama congelado por um tempo
while True: # eu crio uma repetição infinita
    decis = str(input("Você deseja usar esse progama na forma explicativa?[s/n]: ")).strip().upper()[0]
    if decis == 'S':
        print("Primeiramente seja bem vindo, me chamo Daniel Matos e espero ganhar os pontos que preciso do trabalho")
        print("Esse é um progama que calcula equações do segundo grau.")# escrevo isso na tela
        print("-=-" * 30) # mostro -=- 30 vezes na tela
        sono(2)  # congelo por três segundos
        a = float(input("Digite o valor de a: ")) # vou receber o primeiro valor na incóginita a
        print("-=-" * 30) #mostro -=- 30 vezes de novo
        b = float(input("Digite o valor de b: ")) # vou receber o segundo valor e guardar na incóginita b
        print("-=-" * 30)
        c = float(input("Digite o valor de c: ")) # faço a mesma coisa

        delta = b**2 - 4 * a * c # calculo o DELTA
        sono(1)
        print("-=-" * 30)
        print(f"Primeiramente devemos calcular o DELTA. O cálculo dele é assim: b elevado a 2 -4ac ") #mostro na tela como se faz o calculo
        print("-=-" * 30)
        sono(5)
        print(f"{b} elevado a dois é {b**2}. -4 vezes {a} vezes {c} é igual a {-4 * a * c}.")
        print("-=-" * 30)
        sono(5)
        print(f"Logo, a soma entre {b**2} e {-4 * a * c} é igual a {delta}. Esse é o DELTA.")
        if delta < 0: # se o delta for menor que zero
            print("Como o delta é menor que zero esse resultado não convém.")
            break # acaba o progama

        if delta > 0:
            print("Como o DELTA é maior que o zero o resultado final vai ter duas raízes reais e distintas. ")

        if delta == 0:
            print("Como o DELTA é 0 o resultado final vai ter duas raízes reais e iguais. ")
        sono(5)
        print("-=-" * 30)
        print("Forma positiva")
        sono(2)
        print("Agora que calculamos o DELTA, devemos calcular o x. x = -b mais raiz de delta / 2a")
        xmais1 = -b + delta**0.5
        teste = 2 * a
        xmais2 = xmais1 / teste
        sono(5)
        print(f"-b da: {-b}. Mais raiz quadrada de DELTA da: {+delta ** 0.5}. 2a da: {2 * a}. ")
        print(f"Logo: -b mais raiz quadrada de DELTA / 2a é igual a: {xmais2}. Esse é o resultado onde a raiz do DELTA é positivo.")

        sono(5)
        print("-=-" * 30)
        print("Forma negativa")
        sono(2)
        print("x = -b menos raiz de delta / 2a")
        xmenos1 = -b - delta** 0.5
        xmenos2 = xmenos1 / teste
        print(f"-b da {-b}. Menos raiz quadrada de DELTA da: {-delta ** 0.5}. 2a da: {2 * a}")
        print(f"Logo: -b menos raiz quadrada de DELTA / 2a é igual a: {xmenos2}. Esse é o resultado onde a raiz do DELTA é negativo ")
        sono(5)
        print("-=-" * 30)
        print(f"A resposta então foi: \033[1;31m{xmais2}\033[1;97m  e \033[1;32m{xmenos2}\033[1;97m. Lembrando que o progama não deixa nenhum valor em forma de fração")
    else:
        a = float(input("Digite o valor de a: "))
        print("-=-" * 30)
        b = float(input("Digite o valor de b: "))
        print("-=-" * 30)
        c = float(input("Digite o valor de c: "))

        delta = b ** 2 - 4 * a * c
        print(f"Delta = {delta}")

        xmais1 = -b + delta ** 0.5
        teste = 2 * a
        xmais2 = xmais1 / teste

        xmenos1 = -b - delta ** 0.5
        xmenos2 = xmenos1 / teste
        print("-=-" * 30)
        sono(2)
        print(f"A resposta então foi: \033[1;31m{xmais2}\033[1;97m e \033[1;32m{xmenos2}\033[1;97m. Lembrando que o progama não deixa nenhum valor em forma de fração.")

    exi = str(input("Deseja ir embora?[s/n]: ")).strip().upper()[0]
    if exi == "S":

        break
sono(2)
print("Obrigado por usar um aplicativo feito por Daniel Matos.")
print("FIM!")