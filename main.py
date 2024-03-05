import time
import random

def addition(m,level):
	base = 0
	top = 10
	match level :
		case 2 :
			top = 20
		case 3 :
			top = 100
		case 4 :
			while True : 
				base = input("base = ")
				try :
					if int(base) or True :
						break
				except :
					pass
				print("Base doit être un nombre")
			while True :
				top = input("top = ")
				try :
					if int(top) or True :
						break
				except :
					pass
				print("Top doit être un nombre")
		case other :
			pass
		
	corrects = 0
	for i in range(1,int(m)+1):
		a = random.randint(base,top)
		b = random.randint(base,top)
		print("Calcul n°",i,":")
		x = input(str(a) +" + " + str(b) + " = ")
		if int(x) == (a+b) :
			corrects+=1
			print("Correct\n")
		else :
			print("Incorrect\n")
	print("Résultat:",corrects,"/",m)

def différence(m,level):
	pass

def multiplication(m,level):
	pass

def division(m,level):
	pass

def puissance(m,level):
	pass

def modulo(m,level):
	pass


def main() :
	print("Menu principal")
	print(80 * "-" + "\n")
	print("Opérations :")
	print("\t 1) + Addition")
	print("\t 2) - Différence")
	print("\t 3) * Multiplication")
	print("\t 4) / Division entière")
	print("\t 5) ^ Puissance")
	print("\t 6) % Modulo")
	print("\n\t 0) Quitter le programme.\n")
	n = 0
	m = 0
	level = 0

	while True :
		n = input("Choisir l'opération avec un numéro : ")
		try :
			if int(n) in range(1,7) :
				break
		except :
			pass
		print("Les options sont : 0,1,2,3,4,5 et 6.")

	if int(n) == 0 :
		exit()

	while True :
		m = input("Choisir le nombre d'opération entre 1 et 100: ")
		try :
			if int(m) in range(0,101) :
				break
		except :
			pass
		print("Il faut que le nombre soit entre 1 et 100 compris.")

	print("Difficultées :")
	print("\t 1) Facile ")
	print("\t 2) Intermédiaire ")
	print("\t 3) Difficilé ")
	print("\t 4) Customisable ")

	while True :
		level = input("Choisir la difficulté :")
		try :
			if int(level) in range(1,5) :
				break
		except :
			pass
		print("Les options sont : 1,2,3 et 4.")

	match int(n) :
		case 1 :
			addition(m,level)
		case 2 :
			différence(m,level)
		case 3 :
			multiplication(m,level)
		case 4 :
			division(m,level)
		case 5 :
			puissance(m,level)
		case 6 :
			modulo(m,level)
	
	main()

main()