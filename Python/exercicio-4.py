# Faça um programa que receba um número e verifique se ele é positivo ou negativo.

numero = float(input("Insira o número: "))

if(numero > 0):
    print(f"O número {numero} é positivo!")    

elif(numero == 0):
    print(f"O número {numero} é nulo!")

else:
    print(f"O número {numero} é negativo!")