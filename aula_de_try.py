while True:
    try:
        idade = int(input("Sua idade: "))
        print("Idade salva:", idade)
        break
    except ValueError:
        print("Erro! Digite apenas numeros.")
        print("Programa continua aqui...")