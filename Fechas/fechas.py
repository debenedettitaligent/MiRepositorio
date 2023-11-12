import datetime

ahora = datetime.datetime.now()
cumple = datetime.datetime(2024, 5, 13)
nacimiento = datetime.datetime(1988, 5, 13)

diferencia_cumple = cumple - ahora
edad = ahora.year - nacimiento.year

print(f"Tu edad es {edad} años")
print(f"Falta {diferencia_cumple.total_seconds()} segundos para tu cumpleaños")


