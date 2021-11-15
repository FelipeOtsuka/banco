clientes = ["Ana", 1000, "Beatriz", 1000]
opcao=str(input('consultar saldo,saque,depositar ou sair?'))
while opcao!= "sair" :
  if opcao== "saldo":
    nome=str(input("informe o nome desejado"))
    if nome=="Ana":
      print(clientes[0:2])
    elif nome=="Beatriz":
      print(clientes[2:4])
  elif opcao=="saque":
    nome=str(input("informe o nome do saque"))
    if nome=="Ana":
      valor=int(input("informe o valor desejado"))
      if valor<=clientes[1]:
        print("o valor foi sacado")
        clientes[1]=clientes[1]-valor
      else:
        print("voce nao possui o valor desejado para fazer o saque")
    elif nome=="Beatriz":
      valor=int(input("informe o valor desejado"))
      if valor<=clientes[3]:
        print("o valor foi sacado")
        clientes[3]=clientes[3]-valor
      else:
        print("voce nao possui o valor desejado para fazer o saque")
  if opcao=="depositar":
      nome=str(input("informe o nome desejado"))
      if nome=="Beatriz":
         valor=int(input("informe o valor desejado"))
         if valor<=clientes[1]:
           print('o valor foi depositado')
           clientes[1]=clientes[1]-valor
           clientes[3]=clientes[3]+valor
         else:
           print("voce nao possui o valor desejado para fazer o saque")
      elif nome=="Ana":
        valor=int(input("informe o valor desejado"))
        if valor<=clientes[3]:
          print('o valor foi depositado')
          clientes[3]=clientes[3]-valor
          clientes[1]=clientes[1]+valor
        else:
          print("voce nao possui o valor desejado para fazer o saque")
  opcao=str(input('consultar saldo,saque,depositar ou sair?'))


       