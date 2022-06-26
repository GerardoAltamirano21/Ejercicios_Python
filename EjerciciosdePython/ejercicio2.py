#Realizar un programa que permita ingresar 3 valores numéricos, presentar el número mayor, el
#menor y el intermedio.

my_list = []
num1 = int(input("Ingresar el primer numero: "))
my_list.append(num1)
num2 = int(input("Ingresar el segundo valor: "))
my_list.append(num2)
num3 = int(input("Ingresar el tercer valor: "))
my_list.append(num3)

men_mylist = min(my_list)
may_mylist = max(my_list)
med_mylist = (num1 + num2 + num3) - men_mylist - may_mylist
print(f'El numero {men_mylist} es el menor \nEl numero {may_mylist} es el Mayor \nEl numero {med_mylist} es el Intermedio')