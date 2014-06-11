#-*- coding: utf-8 -*-

import random, re, sys

def main(arg):
	slownik = openDictionary()
	if arg == []:
		nazwisko = randomName()
		odmiany = findForms(nazwisko, slownik)
		for odmiana in odmiany:
			print odmiana
	else:
		for x in arg:
			nazwisko = re.sub(r'\n', '', str(x))
			odmiany = findForms(nazwisko, slownik)
			for odmiana in odmiany:
				print odmiana

def analogy(nazwisko, slownik):
	g = range(len(nazwisko), 1, -1)
	odmiany = []
	for i in g:
		indeks = -1
		for obj in slownik:
			if obj[0][-i:] == nazwisko[-i:]:
				indeks = i
				break
		if indeks > -1:
			odmienione = []
			for slowko in obj:
				odmiana = nazwisko[:len(nazwisko)-i] + slowko[len(obj[0])-i:]
				odmiany.append(odmiana)
			break
	if odmiany == []:
		for i in range(1, 7, 1):
			odmiany.append(nazwisko)
	return odmiany

def findForms(nazwisko, slownik):
	odmiany = []
	if '-' in nazwisko:
		i = nazwisko.index('-');
		czlon1 = analogy(nazwisko[:i], slownik)
		czlon2 = analogy(nazwisko[i+1:], slownik)
		czlon1[6] = czlon1[6][:-1] #wołacz
		for j in range(0,7,1):
			odmiany.append(czlon1[j] + '-' + czlon2[j])
		return odmiany
	elif 'vel' in nazwisko:
		nazw = nazwisko.split(" ")
		czlon1 = analogy(list(nazw[0].decode("UTF-8")), slownik)
		czlon2 = analogy(list(nazw[2].decode("UTF-8")), slownik)
		#wołacz
		czlon1[6] = czlon1[6][:-1]
		for j in range(0, 7, 1):
			odmiany.append(czlon1[j] + " vel " + czlon2[j])
		return odmiany
	else:
		odmiany = analogy(nazwisko, slownik)
		return odmiany
		
def openDictionary():
	fp = open("odmiany.txt")
	slownikowe = []
	slownik = []
	for line in fp:
		slowa = line.split()
		slownikowe.append(slowa[0])
		slownik.append(slowa)
	fp.close()
	return slownik

def randomName():
	nazwisko = ""
	wzor = []
	n = random.randint(1,339529)

	fp = open("nazwi.txt")
	for i, line in enumerate(fp):
		if i == n:
			nazwisko = re.sub(r'\n', '', line)
			nazwlit = list(nazwisko.decode("UTF-8"))
		elif i > n:
			break
	fp.close()
	return nazwisko		

if __name__ == "__main__":
   main(sys.argv[1:])