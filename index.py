import json
import random
import os
import csv
def Jogo(nome, vidas, pontos):
    os.system("cls")
    print(nome + " tenta advinhar o número que calculei")
    numero = random.randrange(50)
    print(Pista(numero))
    while True:
        resposta = int(input("Sorte> "))
        if vidas == 0 or vidas < 1:
            break
        if resposta != numero:
            vidas = menosPontos(vidas, pontos)
            os.system("cls")
            print("Ops, não é este o número!")
            print("Pontos: ", pontos)
            print("Vidas: ", vidas)
            numero = random.randrange(50)
            print(Pista(numero))
        else:
            pontos = maisPontos(pontos, vidas, nome)
            numero = random.randrange(50)
            os.system("cls")
            print("\nSim este é o número, vamos a outro!")
            if vidas < 6:
                vidas += 1
            print("Pontos: ", pontos)
            print("Vidas: ", vidas)
            print(Pista(numero))      
    print("Terminou o Jogo!")
    print("Você Perdeu " + nome + "!!\nPontos: ", pontos)
    Salvar(nome, pontos)
    r = int(input("\n\n1 - Voltar ao Menu\n2 - Ver Vencedores\n3 - Sair\nResposta> "))
    if r == 1:
        Menu()
    elif r == 2:
        Vencedores()
    else:
        Sair()
#
def Pista(num):
    if num > 0 and num < 11:
        pista = "Pista >> É menor que 10"
    elif num > 19 and num < 31:
        pista = "Pista >> É maior ou igual a 20 e menor que 30"
    elif num > 39 and num < 50:
        pista = "Pista >> É maior ou igual a 40 e menor que 50"
    else:
        pista = "Má sorte não tem pista para você " + nome
    return pista
#
def menosPontos(vidas, pontos):
    if vidas < 0 or vidas == 0:
        print("Você Perdeu " + nome + "!!\n Pontos: ", pontos)
    else:
        vidas -= 1
    return vidas
#
def maisPontos(pontos, vidas, nome):
    pontos += 1
    if pontos == 10 or pontos > 10:
        print("Parabéns " + nome + " você terminou o jogo!")
        Salvar(nome, pontos)
        Vencedores()
    return pontos
#
def Salvar(nome, pontos):
    data = {"Nome":nome,"Pontos":pontos}
    json_data = json.dumps(data) 
    python_dict = json.loads(json_data)
    with open("winners.txt", "a", newline="") as f:
        w = csv.writer(f)
        w.writerow([python_dict["Pontos"], python_dict["Nome"]])
#
def Sair():
    sair = int(input("Vai sair, tem certeza?\n1 - Sim \n 2 - Não \n Resposta> "))
    if sair == 1:
        exit
#
def Vencedores():
    os.system("cls")
    print("Pontos,Nome")
    f = open("winners.txt","r")
    x = f.read()
    print(x)
    r = int(input("\n1 - Voltar ao Menu\n2 - Sair\nResposta> "))
    if r == 1:
        Menu()
    else:
        Sair()
#
def Sobre():
    os.system("cls")
    print("<======== Advinhe o Número ========>")
    print("#GotTheNumber")
    r = int(input("\n\n1 - Voltar ao Menu\n2 - Sair\nResposta> "))
    if r == 1:
        Menu()
    else:
        Sair()
#
def Menu():
    os.system("cls")
    resp = int(input("<======== Menu ========> \n1 - Jogar \n2 - Pontuações\n3 - Sobre\n4 - Sair\nResposta> "))
    if resp == 1:
        nome = str(input("Diga o seu nome> "))
        Jogo(nome, vidas, pontos)
    elif resp == 2:
        Vencedores()
    elif resp == 3:
        Sobre()
    else:
        Sair()
#
nome = ""
vidas = 3
pontos = 0
Menu()