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

# Solution astucieuse, mais il est possible de rédiger un script plus court.
# Voici l'une de mes propositions:

for a in range(1930,2018): # Boucle qui passe toutes les années de 1930 à 2017
	for x in range(1001,2000): # Boucle qui passe les 1000 numéros de permis possible à chaque année
	# J'imprime ensuite un assemblage fait de :
	# D'abord, je transforme les années en «string» (chaîne de caractères) et je n'en conserve que les deux derniers caractères
	# Puis je transforme aussi en «string» les nombres générés par la 2e boucle (qui va de 1000 à 1999) et je n'en conserve que les trois derniers caractères
		print(str(a)[2:] + str(x)[1:])