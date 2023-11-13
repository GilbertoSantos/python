import datetime

#Variaveis
## Variaveis referente saldo
flo_saldo = 30.45

## Variaveis referente depositos
flo_deposito = 0

## Variaveis referente saques
flo_saque = 0
flo_saque_limite  = 500
int_saque_qtd_dia = 0
int_saque_qtd_max_diario = 3

## Variaveis referente extratos
str_extrato_largura = 60
str_extrato_movimentos = ""
dat_data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
str_extrato_data  = f"{dat_data_hora}".center(str_extrato_largura)
str_extrato_saldo = f"Saldo inicial: R$ {flo_saldo}".center(str_extrato_largura)

## Variaveis referente menu
str_opcao_menu = ""

#Constantes
MENU = """
 ##### BANCO DIO #####

 [d] Depositar
 [s] Sacar
 [e] Extrato
 [q] Sair

"""

while True:
    print(MENU)
    str_opcao_menu = input("Informe a opção desejada: ")

#Opção depósito
    if str_opcao_menu == "d":
        #Solicita valor enquanto usuário informar valor menor que zero
        while flo_deposito <= 0:
            flo_deposito = float(input("Informe o valor do depósito: ") or 0)

            if flo_deposito > 0:
                flo_saldo += flo_deposito
                dat_data_hora=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                str_extrato_movimentos += f"{dat_data_hora}".center(20)
                str_extrato_movimentos += f"Depósito: R$ {flo_deposito:>.2f}".center(20)
                str_extrato_movimentos += f"Saldo: R$ {flo_saldo:>.2f}".center(20)
                str_extrato_movimentos += f"\n"
                print("Depósito efetuado.")
                break
            else:
                print("Informe um valor maior que zero")
#Opção saque
    elif str_opcao_menu == "s":
        if int_saque_qtd_dia <= int_saque_qtd_max_diario:
            while flo_saque <= 0 or flo_saque > flo_saque_limite:
                flo_saque = float(input("Informe o valor da retirada: ") or 0)

                if flo_saque > 0:
                    if flo_saque <= flo_saque_limite:
                        if flo_saldo >= flo_saque:
                            flo_saldo -= flo_saque
                            int_saque_qtd_dia += 1
                            dat_data_hora=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                            str_extrato_movimentos += f"{dat_data_hora}".center(20)
                            str_extrato_movimentos += f"Saque: R$ {flo_saque:>.2f}".center(20)
                            str_extrato_movimentos += f"Saldo: R$ {flo_saldo:>.2f}".center(20)
                            str_extrato_movimentos += f"\n"
                            print("Retire o dinheiro.")
                            break
                        else:
                            print("Saldo insuficiente.")
                            break
                    elif flo_saque > flo_saque_limite:
                        print("Valor informado excede o valor limite por saque.")
                else:
                    print("Informe um valor maior que zero")
        else:
            print("Quantidade de saques diários excedido.")
#Opção extrato
    elif str_opcao_menu == "e":
        str_extrato_corpo  = ""
        str_extrato_banco  = " BANCO DIO ".center(str_extrato_largura, "#")
        str_extrato_topo   = " Extrato ".center(str_extrato_largura, "-")
        str_extrato_vazio  = "Sem movimentações".center(str_extrato_largura)
        str_extrato_rodape = "-".center(str_extrato_largura, "-")

        str_extrato_corpo += f"{str_extrato_banco}\n"
        str_extrato_corpo += f"{str_extrato_topo}\n"
        str_extrato_corpo += f"{str_extrato_data}\n"
        str_extrato_corpo += f"{str_extrato_saldo}\n"
        str_extrato_corpo += f"{str_extrato_vazio if not str_extrato_movimentos else str_extrato_movimentos}\n"
        str_extrato_corpo += f"{str_extrato_rodape}\n"

        print(str_extrato_corpo)
#Opção sair
    elif str_opcao_menu == "q":
        print("Tenha um bom dia!!!")
        break
#Opção inválida
    else:
        print("Informe uma opção válida")
