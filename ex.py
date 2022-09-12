# x= [1,2,3,4]
# print(len(x))

lst= ['touchMe', 'Sebsatain', 'heroHero', 'yuri alpha', 'Aura']

first_slice = lst[::-1]
# second_slice = first_slice[:y]
# third_slice = second_slice[x:]
last_slice = first_slice[::1]



strings=['touchMe', 'Sebsatain', 'heroHero', 'yuri alpha', 'Aura']

arr=[]
for idx in  range(1,len(strings)):
    print(strings[idx])

people = {"Tim": 21, "Joe": 18, "Sarah": 25, "Jennie": 26, "Bill": 34}

result = sorted(people, key=people.get)
print(result)