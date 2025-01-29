#Estructura de datos

NUM = 8
nums = [0] * NUM
total = 0
for i in range(NUM):
    nums[i] = int(input("Ingrese un digito: "))
    total += nums[i]
    print("El total de numeros es:", total)