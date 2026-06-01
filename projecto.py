dados = {
    "nome":"wilson",
    "sobrenome":"Figueiredo",
    "idade":17,
    "sair":""
}
def calculadora():
    numero1 = int(input("digite o primeiro numero:"))
    numero2 = int(input("digite o segundo numero:"))
    print("(1) somar")
    print("(2) subtrair")
    print("(3) multiplicar")
    print("(4) dividir")
    opcao = input("digite um opcao:")
    if opcao == "1":
        print("soma:", numero1 + numero2)
    elif opcao == "2":
        print("subtracao:", numero1 - numero2)
    elif opcao == "3":
        print("multiplicacao:", numero1 * numero2)
    elif  opcao == "4":
        print("divisao:", numero1 / numero2)
    else:
        print("opcao invalida")


while True:
    msg = input("Voce: ").strip().lower()
    resposta = dados.get(msg, "Erro, comando nao encotrado")
    if msg == "sair":
        print("saindo....")
        break
    elif msg == "calculadora":
        calculadora()
    else:
        print("Bot:", resposta)