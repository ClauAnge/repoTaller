print("Prblema condicional pide la edad y muestra un mensaje con tipo de entrada y pago")
edad= int(input("Cual es tu edad..."))
if edad<4:
    print ("Entrada gratis")
elif edad<=4 or edad<=12:
    print("Boleto infatil $40")
elif edad<=13 or edad<=59:
    print("Boleto general $70")
elif edad>=60:
    print("Boleto de adulto descuento $35")
else:
    print("entrada invalida")