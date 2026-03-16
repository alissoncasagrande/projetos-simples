#Calculadora Simples
# Escreva um programa que funcione como uma calculadora simples. 
# O programa deve solicitar ao usuário que insira dois números e 
# a operação desejada (adição, subtração, multiplicação ou divisão). 
# O programa deve então realizar a operação e exibir o resultado para o usuário. 
# O programa deve continuar a solicitar operações até que o usuário decida sair.    


import keyboard
import os

class Calculadora:
    def __init__(self):
        self._resultado = 0 # para armazenar o resultado atual da calculadora
        self._display = "" # para armazenar o valor atual do display
        self._ultima_operacao = None # para armazenar a última operação realizada
        self._novo_numero = False # para indicar se o próximo número digitado deve substituir o display atual ou ser adicionado a ele
    def executar_operacao(self, operacao):
        try:
            if (self._ultima_operacao is None):
                # se não houver uma operação anterior, apenas atualiza o resultado com o valor do display
                self._resultado = float(self._display) if self._display else 0
            else:
                if self._ultima_operacao == "+":
                    self.adicionar()
                elif operacao == "-":
                    self.subtrair()
                elif self._ultima_operacao == "*":
                    self.multiplicar()
                elif self._ultima_operacao == "/":
                    self.dividir()

            self._display = str(self._resultado)
            self._ultima_operacao = operacao
            self._novo_numero = True
        except ZeroDivisionError:
            self.limpar()
            self._display = "Erro"

    def nvl(self, valor):
        return valor if valor else "0"
    def adicionar(self):
        self._resultado += float(self.nvl(self._display))
        return self._resultado
    def subtrair(self):
        self._resultado -= float(self.nvl(self._display))
        return self._resultado
    def multiplicar(self):
        self._resultado *= float(self.nvl(self._display))
        return self._resultado
    def dividir(self):
        self._resultado /= float(self.nvl(self._display))
        return self._resultado
    def backspace(self):
        self._display = self._display[:-1]
    def limpar(self):
        self._resultado = 0
        self._display = ""
    def chk_display(self):
        try:
            float(self._display)
            return True
        except ValueError:
            return False
    def get_display(self):
        return self._display
    def add_display(self, valor):
        if self._novo_numero:
            self._display = "" # limpa o display para o próximo número
            self._novo_numero = False

        #if not self.chk_display(): self._display = "" # limpa o display se o valor atual não for um número válido
        if self._display == "Erro": self._display = "" # limpa o display se estiver mostrando um erro

        if valor == "." and "." in self._display:
            return  # evita dois pontos decimais
        self._display += str(valor)

# -- MAIN --      
calculadora = Calculadora()
clear_command = 'cls' if os.name == 'nt' else 'clear'

while True:
    os.system(clear_command)
    print("Pressione Q para sair:")
    print("Operações: +, -, *, /")
    print("----------------------------------")
    print(f"Display: {calculadora.get_display()}")
    print("----------------------------------")
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:  # só captura quando a tecla é pressionada
        tecla = event.name

        if tecla in ['+', '-', '*', '/']:
            calculadora.executar_operacao(tecla)
        elif tecla in ['=', 'enter']:
            calculadora.executar_operacao(None)
        elif tecla == 'backspace':
            calculadora.backspace()
        elif tecla == 'c':
            calculadora.limpar()
        elif tecla in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
            calculadora.add_display(tecla)
        
        if tecla.lower() == "q":
            print("Encerrando...")
            break


#obs: nao fuciona como eu quero
