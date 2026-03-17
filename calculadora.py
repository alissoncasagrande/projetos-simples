#Calculadora Simples
# Escreva um programa que funcione como uma calculadora simples. 
# O programa deve solicitar ao usuário que insira dois números e 
# a operação desejada (adição, subtração, multiplicação ou divisão). 
# O programa deve então realizar a operação e exibir o resultado para o usuário. 
# O programa deve continuar a solicitar operações até que o usuário decida sair.    

# Problema conhecido ao somar 10 + 2, ficar clicando + ele soma o resultado do display ao inves de ir incrementando 2;

from pickle import TRUE
import time
import keyboard
import os

class Calculadora:
    def __init__(self):
        self._valores = [0,]            # para armazenar os valores digitados (lista com apenas um valor 0 inicialmente, para pilha de operacoes
        self._valores_idx = 0           # para controlar o índice dos valores digitados (0 ou 1) (excluir)
        self._display = "0"             # para armazenar o valor atual do display
        self._operacao_anterior = None  # para armazenar a última operação realizada
        self._display_printed = False   # para controlar se o display já foi impresso na tela

        self._debug_str = ""

        self._novo_numero = False # para indicar se o próximo número digitado deve substituir o display atual ou ser adicionado a ele

    def definir_operacao(self, operacao):
        self._novo_numero = False # manutencao do display.
        v = float(self.nvl(self._display))
        x = ""

        self._valores.append(v) # adiciona o valor atual do display à lista de valores

        if ( self._operacao_anterior is not None): #falta tratar quando for '=' ou enter
            x = self.concluir_operacao(self._operacao_anterior) # realiza a operação anterior antes de definir a nova operação

        if not x : x = str(v) # se não houve calculos, o valor atual do display é mantido

        if operacao not in ['=', 'enter']:
            self._operacao_anterior = operacao
        else:
            self._operacao_anterior = None # limpa a operação anterior para evitar cálculos subsequentes indesejados

        #self._debug_str += " v:"+str(v)+" x:"+str(x)
        self.show_resultado_display(x)

    def concluir_operacao(self, operacao): 
        try:
            if operacao == "+":
                x = self.adicionar()
            elif operacao == "-":
                x = self.subtrair()
            elif operacao == "*":
                x = self.multiplicar()
            elif operacao == "/":
                x = self.dividir()

            return x
        except ZeroDivisionError:
            self.limpar()
            return "Erro"

    def show_resultado_display(self,valor):
        #self._debug_str += " valor:"+str(valor)
        if valor is not None:
            self._display = str(valor)
        self._novo_numero = True # indica que o próximo número digitado deve substituir o resultado atual
        self.setPrinted(False) # marca o display como não impresso para que seja atualizado na próxima impressão da tela
        return self._display

    def nvl(self, valor):
        return valor if valor else "0"
    
    def adicionar(self):
        a = self._valores.pop()
        b = self._valores.pop()
        r = b + a #para nao inverter valores de sinal na adição
        self._valores.append(r)
        return r

    def subtrair(self):
        a = self._valores.pop()
        b = self._valores.pop()
        r = b - a # ordem invertida para subtração
        self._valores.append(r)
        return r

    def multiplicar(self):
        a = self._valores.pop()
        b = self._valores.pop()
        r = b * a
        self._valores.append(r)
        return r

    def dividir(self):
        a = self._valores.pop()
        b = self._valores.pop()
        r = b / a
        self._valores.append(r)
        return r

    def backspace(self):
        self._display = self._display[:-1]
        if (self._display == ""): self._display = "0"
        self.setPrinted(False) # marca o display como não impresso para que seja atualizado na próxima impressão da tela
        return self._display
    
    def limpar(self):
        self._debug_str = ""
        self._primeiro_valor = 0
        self._segundo_valor = 0
        self._display = "0"
        self._ultima_operacao = None
        self.setPrinted(False) # marca o display como não impresso para que seja atualizado na próxima impressão da tela
        return 
    
    def chk_display(self):
        try:
            float(self._display)
            return True
        except ValueError:
            return False
    def set_display(self, valor):
        pass    
    
    def get_display(self):
        return self._display
    
    def add_display(self, valor):
        self.setPrinted(False) # marca o display como não impresso para que seja atualizado na próxima impressão da tela

        if self._novo_numero:
            self._display = "0" # limpa o display para o próximo número
            self._novo_numero = False

        if not self.chk_display(): self._display = "0" # limpa o display se o valor atual não for um número válido

        if valor == "." and "." in self._display:
            return  # evita dois pontos decimais
        if (self._display == "0"):
            self._display = str(valor)  # substitui o zero inicial
        else:
            self._display += str(valor)

    def isPrinted(self):
        return self._display_printed
    def setPrinted(self, value):
        self._display_printed = value

# -- MAIN --      

#funcoes auxiliares
def on_pressionar_tecla(event):
    global deveParar

    tecla = event.name.lower()  # obtém o nome da tecla pressionada e converte para minúscula

    if (tecla is not None):  # verifica se uma tecla foi realmente lida
        if tecla in ['+', '-', '*', '/']:
            calculadora.definir_operacao(tecla)
        elif tecla in ['=', 'enter']: # somente para ficar mais explicito
            calculadora.definir_operacao(tecla) 
        elif tecla == 'backspace':
            calculadora.backspace()
        elif tecla in ['c','esc']:
            calculadora.limpar()
        elif tecla in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
            calculadora.add_display(tecla)
        
        if tecla.lower() == "q": deveParar = True

def imprime_tela():
    if (not calculadora.isPrinted()):
        os.system(clear_command) # limpa a tela
        print("Pressione Q para sair")
        print("Use Backspace para apagar, C para limpar")
        print("Operações: +, -, *, /"," Enter ou = para calcular")
        print("----------------------------------")
        print(f"Display: {calculadora.get_display()}")
        print("----------------------------------")
        #print("debug: ", calculadora._valores, "op anterior: ", calculadora._operacao_anterior, "debug: ", calculadora._debug_str)

        calculadora.setPrinted(True) # marca o display como impresso para evitar impressões repetidas
    return

#-- VARIAVEIS --

clear_command = 'cls' if os.name == 'nt' else 'clear' # comando para limpar a tela, dependendo do sistema operacional
deveParar = False #variavel para parar o Loop principal (tecla 'Q' para sair do programa)
tempoFPS = 1/15    # tempo de espera para ajustar o FPS, em segundos

# registra a função de callback para eventos de tecla pressionada, 
# com supressão para evitar que as teclas sejam registradas como eventos normais do sistema
keyboard.on_press(on_pressionar_tecla, suppress=True)

calculadora = Calculadora() # instancia a classe Calculadora para criar um objeto que irá gerenciar as operações e o display da calculadora

while not deveParar:
    time.sleep(tempoFPS) # aguarda um curto período para controlar a taxa de atualização do display
    imprime_tela()

print("Calculadora encerrada. Obrigado por usar!")
print('')
