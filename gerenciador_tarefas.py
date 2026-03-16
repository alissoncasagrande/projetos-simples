#GERENCIADOR DE TAREFAS
# Escreva um programa que permita ao usuário criar uma lista de tarefas. 
# O programa deve permitir que o usuário adicione novas tarefas, marque 
# tarefas como concluídas e exiba a lista de tarefas pendentes. 
# O programa deve continuar a solicitar ações do usuário até que ele decida sair.
# 

import os
import datetime
from xmlrpc.client import DateTime

class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.concluida = None

    def tarefa_ok(self):
        self.concluida = datetime.datetime.now()

class GerenciadorTarefas: 
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao):
        tarefa = Tarefa(descricao)
        self.tarefas.append(tarefa)

    def marcar_concluida(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].tarefa_ok()

    def exibir_tarefas_pendentes(self):
        print("Tarefas Pendentes:")
        for i, tarefa in enumerate(self.tarefas):
            if not tarefa.concluida:
                print(f"{i}. {tarefa.descricao}")
    def exibir_tarefas_concluidas(self):
        print("Tarefas Concluídas:")
        for i, tarefa in enumerate(self.tarefas):
            if tarefa.concluida:
                print(f"{i}. {tarefa.descricao} (Concluída em: {tarefa.concluida.strftime('%d/%m/%Y %H:%M:%S')})")        


#-- MAIN --
gerenciador = GerenciadorTarefas()

clear_command = 'cls' if os.name == 'nt' else 'clear'
os.system(clear_command)

while True:
    print("Gerenciador de Tarefas")
    print("=====================") 
    print("1. Adicionar Tarefa")
    print("2. Marcar Tarefa como Concluída")
    print("3. Exibir Tarefas Pendentes")
    print("4. Exibir Tarefas Concluídas")
    print("5. Sair")
    print("=====================")  
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        descricao = input("Digite a descrição da tarefa: ")
        gerenciador.adicionar_tarefa(descricao)
    elif escolha == '2':
        indice = int(input("Digite o índice da tarefa a ser marcada como concluída: "))
        gerenciador.marcar_concluida(indice)
    elif escolha == '3':
        gerenciador.exibir_tarefas_pendentes()
    elif escolha == '4':
        gerenciador.exibir_tarefas_concluidas()
    elif escolha == '5':
        break
    else:
        print("Opção inválida. Tente novamente :P")

    input("Pressione Enter para continuar...")

os.system(clear_command)
print("Obrigado por usar o Gerenciador de Tarefas! Até a próxima :)")


