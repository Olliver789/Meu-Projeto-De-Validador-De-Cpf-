#modulos
from time import sleep
import os
#funçoes
#func de limpar terminal
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

#funçao de reticencias
def ret():
    print('.'),sleep(0.3),print('.'),sleep(0.9),print('.'),sleep(8)

#validar o cpf
def validarI():
    while True:
        #pede o cpf e faz o tratamento para a validaçao
        limpar()
        print('='*10,'Validador De CPF','='*10)
        cpf1 = int(input('Digite O CPF Para Validação => '))
        cpf2 = len(str(cpf1))
        cpf3 = str(cpf1)
        #verifica se o cpf tem 11 caracteres para começar as contas de validar
        if cpf2 == 11:
            print('Aguarde Um Momento Validação Em Andamento')
            ret()
            #define cada digito do cpf separado
            n1 = int(cpf3[0])*10
            n2 = int(cpf3[1])*9
            n3 = int(cpf3[2])*8
            n4 = int(cpf3[3])*7
            n5 = int(cpf3[4])*6
            n6 = int(cpf3[5])*5
            n7 = int(cpf3[6])*4
            n8 = int(cpf3[7])*3
            n9 = int(cpf3[8])*2
            #verifica se o cpf não é so numeros repetidos
            if cpf3[0] == cpf3[1] and cpf3[1] == cpf3[2] and cpf3[2] == cpf3[3]:
                print('cpf invalido digitos repetidos')
                sleep(2)
                continue
            else:
                #começa a calcular
                resto = (n1+n2+n3+n4+n5+n6+n7+n8+n9)%11
                if resto < 2:
                    Digito = 0
                    if Digito == int(cpf3[9]):
                        n1 = int(cpf3[0])*11
                        n2 = int(cpf3[1])*10
                        n3 = int(cpf3[2])*9
                        n4 = int(cpf3[3])*8
                        n5 = int(cpf3[4])*7
                        n6 = int(cpf3[5])*6
                        n7 = int(cpf3[6])*5
                        n8 = int(cpf3[7])*4
                        n9 = int(cpf3[8])*3
                        n10 = int(cpf3[9])*2
                        resto = (n1+n2+n3+n4+n5+n6+n7+n8+n9+n10)%11
                        if resto < 2:
                            Digito = 0
                            if Digito == int(cpf3[10]):
                                print('CPF Valido')
                            else:
                                print('CPF Invalido')
                        elif resto >= 2:
                            Digito = 11-resto
                            if Digito == int(cpf3[10]):
                                print('cpf valido')
                            else:
                                print('CPF Invalido')
                    else:
                        print('Erro CPF Invalido')
                        sleep(2)
                        pass
                elif resto >= 2:
                    Digito = 11-resto
                    if Digito == int(cpf3[9]):
                        n1 = int(cpf3[0])*11
                        n2 = int(cpf3[1])*10
                        n3 = int(cpf3[2])*9
                        n4 = int(cpf3[3])*8
                        n5 = int(cpf3[4])*7
                        n6 = int(cpf3[5])*6
                        n7 = int(cpf3[6])*5
                        n8 = int(cpf3[7])*4
                        n9 = int(cpf3[8])*3
                        n10 = int(cpf3[9])*2
                        resto = (n1+n2+n3+n4+n5+n6+n7+n8+n9+n10)%11
                        if resto < 2:
                            Digito = 0
                            if Digito == int(cpf3[10]):
                                print('CPF Valido')
                                sleep(2)
                            else:
                                print('CPF Invalido')
                                sleep(2)
                        elif resto >= 2:
                            Digito = 11-resto
                            if Digito == int(cpf3[10]):
                                print('cpf valido')
                                sleep(2)
                            else:
                                print('CPF Invalido')
                                sleep(2)

        else:
            print('Cpf Invalido Quantidade De Digitos invalidos')
            sleep(2)
            continue
#inicio codigo 
def inicio():
    validarI()
#rodar codigo
inicio()
