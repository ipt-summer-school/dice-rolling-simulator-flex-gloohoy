import random
facets_group = []
numbers_group = []
numbers_dm = []

quantity = int( input ("how much dices?: ") )

i = 1
# спрашиваю кол-во граней
while i <= quantity:
    facets = int( input ("how much facets on dice?: ") )
    facets_group.append (facets)
    i+=1
# по циклу рандомно выбираю число от 1 до кол-ва граней, удаляя первый элемент и возвращая его через facets_group.pop
y = 1
while y <= quantity:
    a = facets_group.pop()
    r = random.randrange(1, a, 1)
    # дальше добавляю эти числа в группу
    numbers_group.append ()
    y+=1

t = 1
while t <= quantity:
    a = facets_group.pop()
    r = random.randrange(1, a, 1)
    # дальше добавляю эти числа в группу
    numbers_dm.append ()
    y+=1

itoggroup = sum(numbers_group)
itogdm = sum(numbers_dm)
print ("DMs result is ", itogdm ) print ("groups result is ", itoggroup)

if itoggroup > itogdm:
print ( "my congradulations, dudes" )
elif itogdm > itoggroup:
print ("well, shit happenes")
else:
print ("Drow! One more time?)")

