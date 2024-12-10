import random
losowane=[]
wylosowane=[]
for i in range(6):
    losowane.append(i+1)
for element in losowane:
    print(element, end=' ')

def losuj1(losowane,wylosowane):
    while(len(wylosowane)<6):
        index=random.randint(0,len(losowane)-1)
        if not(losowane[index] in wylosowane):
            wylosowane.append(losowane[index])
print()
print(wylosowane)
print(losowane)
losuj1(losowane,wylosowane)
print(wylosowane)


typowane=[]
print()
while(len(typowane) < 6):
    liczba = int(input("Podaj liczbę"))
    if (liczba>0 and liczba<50) and (not liczba in  typowane):
        typowane.append(liczba)
    else:
        print("podana liczba była już podawana lub jest poza zakresem")


print(typowane)

