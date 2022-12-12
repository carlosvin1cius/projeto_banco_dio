menu = """
[1] DEPÓSITO
[2] SAQUE
[3] EXTRATO
[X] FINALIZAR
-- """
extrato = ""
saldo = c = 0
while True:
    valor = 0
    opcao = input(menu)

# OPERAÇÃO RELACIONADA A DEPÓSITO:
    if opcao == "1":
      print("DEPÓSITO:")
      while valor <= 0:
        valor = int(input("VALOR DE DEPÓSITO: R$"))
        if valor < 0:
          print("Valor invalido, apenas valores positivos são aceitos.")
        else:
          print(f"DEPÓSITO REALIZADO NO VALOR: R${valor:.2f}")
          saldo += valor
          extrato += f"DEPÓSITO: R${valor:.2f}\n"
          extrato += f"SALDO: {saldo}\n"

# OPERAÇÃO RELACIONADA A SAQUE:
    elif opcao == "2":
      print("SAQUE:")
      while valor <= 0:
        valor = int(input("SAQUE: VALOR R$"))
        if valor < 0:
          print("Valor invalido, apenas valores positivos são aceitos.")  
        elif valor > saldo:
          print(f"""SALDO INSUFICIENTE:
          Saldo atual: R${saldo:.2f}
          Saque solicitado: R${valor:.2f}""")
        elif c >= 3 or valor > 500:
          if c >= 3:
            print(f"Limites diario de {c} saques alcançado! Tente novamente amanhã.")
          else:
            print(f"valor de R${valor:.2f} é superior ao seu limite determinado para cada saque, R$500,00.")
        else:
          c += 1
          extrato += f"SAQUE: R${valor:.2f}\n"
          extrato += f"SALDO: {saldo}\n"
          saldo -= valor
          print(f"""SAQUE REALIZADO:
           Saldo atual: R${saldo:.2f}
           Saque realizado: R${valor:.2f}""")


# EXIBINDO O EXTRATO
    elif opcao == "3":
      print("="*30)
      print("EXTRATO:")
      print("="*30)
      print()
      print(extrato)


# ACIONANDO O BREAK DO TRUE E FECHANDO A OPERAÇÃO  
    elif opcao in "Xx":
      print ("Obrigado, até mais...")
      break

# CASO NENHUMA OPÇÃO VALIDA SEJA ESCOLHIDA 
    else:
      print("Opção inexistente, favor selecione uma das funções a seguir.")