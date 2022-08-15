#Entradas
salario = float(input("Indica tu salario: "))
#Procesamiento
isr = salario * 0.2136
total = salario - isr
#Salidas
print(f"El ISR descontado es ${isr}")
print(f"El total de tu salario es ${total}")
