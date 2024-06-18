import random
timelist=["сегодня","завтра","вскором времени"]
eventlist=["вы встретите","с вами случтся","вы получите"]
objectlist=["что-то не обычное","небольшой инцидент","большой сюрприз"]


while True:
   znak=input("Введите ваш зз:")
   if znak in["Рыбы","Телец","Овен","Близнецы","Рак","Лев","Дева","Весы","Скорпион","Стрелец","Козерог","Водолей",]:
     t=random.choice(timelist)
     e=random.choice(eventlist)
     q=random.choice(objectlist)
     print(t,e,q)
   else:
     print("нет предскзания")
