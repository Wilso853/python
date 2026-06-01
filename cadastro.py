import time
import datetime

def tempo():
    for i in range(10):
        time.sleep(0.1)
        print("⏳ " + str(i), end="\r")


def hora():
    hora2 = datetime.datetime.now().strftime("%H:%M:%S")
    print(hora2)
    return hora2


dados = {
    "nome":"",
    "email":"",
    "idade":"",
    "numero":"",
    "sair":"",
    "comandos":""
}
def comandos():
    print(" ============")
    print("|sair         |\n|novo_cadastro|\n|hora         |\n|menu         |")
    print(" ============")


def dado():
    print("="*10)
    print("Nome:",dados["nome"])
    print("Email:", dados["email"])
    print("Idade:", dados["idade"])
    print("Numero de celular:", dados["numero"])
    print("="*10)

def novo_cadastro():
    dados["nome"] = input("Seu nome: ")
    dados["email"]= input("Seu email: ")
    dados["idade"]=int(input("Sua idade:"))
    dados["numero"]=int(input("Seu numero de celular: "))


tempo()
print("cadastro iniciado as",hora())
dados["nome"]=input("Seu nome: ")
dados["email"]=input("Seu email: ")
dados["idade"]=int(input("Sua idade:"))
dados["numero"]=int(input("Seu numero de celular: "))
print("cadastro salvo")

while True:
    msg = input(">>: ").lower().strip()
    resposta = dados.get(msg, "Erro, comando invalido")
    if msg == "sair":
        tempo()
        print("cadastro encerrado")
        break
    elif msg == "menu":
        tempo()
        comandos()
    elif msg == "dado":
        tempo()
        dado()
    elif msg == "novos_dados":
        tempo()
        novo_cadastro()
    else:
        print("BOT:", resposta)
