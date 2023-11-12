#from collections import namedtuple
#pez = namedtuple("Pez", ["nombre", "especie", "peso"])
#pez1 = pez("pecesin", "pez payaso", "1")
#print(pez)


#from collections import Counter
#estudiantes = "Nicolas Leandro Jose
#print(Counter(estudiantes.split()))


from datetime import datetime, timedelta

dt = datetime.now()


dt_prueba = datetime(2023, 11, 6)


#print(dt_prueba.year)
#print(dt_prueba.month)
#print(dt_prueba.day)


t = timedelta(days=4, seconds= 1000)

delta = dt + t

print(dt)
print(delta)