dados = {
    "nome":"wilson",
    "sobrenome":"Figueiredo",
    "idade":17,
    "sair":""
}
while True:
    msg = input("Voce: ").strip().lower()
    resposta = dados.get(msg, "Erro, comando nao encotrado")
    if msg == "sair":
        print("saindo....")
        break
    print("Bot:", resposta)