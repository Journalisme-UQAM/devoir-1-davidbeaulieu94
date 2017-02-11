#coding:utf-8

permis=list(range(30000,100000))
print(permis)

permis2=list(range(0,10))

permis3=list(range(10,100))

permis4=list(range(100,1000))

permis5=list(range(1000,10000))

permis6=list(range(10000,18000))
# print(permis+permis2+permis3+permis4+permis5+permis6)

for permi in permis:
    print('{}'.format(permi))

for permi2 in permis2:
    print('0000{}'.format(permi2))
    
for permi3 in permis3:
    print('000{}'.format(permi3))
    
for permi4 in permis4:
    print('00{}'.format(permi4))
    
for permi5 in permis5:
    print('0{}'.format(permi5))
    
for permi6 in permis6:
    print('{}'.format(permi6))
