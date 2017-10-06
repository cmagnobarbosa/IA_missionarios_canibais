#!/usr/bin/env python2.7.12
#-*- coding: utf-8 -*-
#codigo feito por Lucas Félix(Zoin), Carlos Magno (Gands), Matheus Reis(Pera) e Samuel Ribeiro(Tup boy)
from random import randint #modulo para gerar random
from copy import copy
import time
def verifica(lado_inicial, lado_final):
	cont = 0
	cont2 = 0
	a = 0
	b = 0
	for i in lado_inicial:
		if(i==0):
			cont=cont+1 #conto o número de missionários
		else:
			cont2=cont2+1 #conto o número de canibais
	for i in lado_final:
		if(i==0):
			a=a+1
		else:
			b=b+1
	print lado_inicial, lado_final
	#time.sleep(1)
	if (cont2>cont and cont!=0)	or (b>a and a!=0):
		return False
	# primeiro caso o número de missionários tem que ser
	#sempre maior que canibais, ou número de missionario igual a zero do outro lado o número de missionario é maior 
	else:
		return True

def retira_personagem(personagem, quantidade, lado_inicial, lado_final):
	i=0
	cont=0
	quantidade = quantidade + 1 
	while(i<len(lado_inicial)):
		if(lado_inicial[i]==personagem):
			cont=cont+1
		i=i+1
	if(cont>=quantidade): #quer dizer que tá tudo bem, posso retirar
		i=0
		while(i<quantidade):
			lado_inicial.remove(personagem)
			lado_final.append(personagem)
			i=i+1
		return lado_inicial, lado_final
	else:
		return False, False
def retira_personagem_especial(lado_inicial, lado_final):
	a = 0
	b = 0
	for i in lado_inicial:
		if(i==1):
			a=a+1
		else:
			b=b+1
	#personagens que serão enviados

	if(a+b>=2):
		j = randint(0,3)
		if (j==0) and (b==2): #envio dois missionários
			lado_inicial.remove(0)
			lado_final.append(0)
			lado_inicial.remove(0)
			lado_final.append(0)
		elif (j==1) and (a==2): #envio dois canibais
			lado_inicial.remove(1)
			lado_final.append(1)
			lado_inicial.remove(1)
			lado_final.append(1)
 		elif (j==2 or j==3) and (a>=1 and b>=1):
 			lado_inicial.remove(0)
			lado_final.append(0)
			lado_inicial.remove(1)
			lado_final.append(1)

		return lado_inicial, lado_final
	else:
		return False, False

def checkpoint(lado_inicial, lado_final, estados, i):
	estados.append("Na iteração: ")
	estados.append(str(i))
	estados.append('\t')
	estados.append(str(lado_inicial))
	estados.append('\t')
	estados.append(str(lado_final))
	estados.append('\n')
	return estados
def metodo():
	#0 representa missionários, 1 representa canibais
	lado_inicial = [0, 0, 0, 1, 1, 1]
	lado_final = []
	backup_inicial = []
	estados = []
	backup_final = []
	flag=0
	iteracao = 0
	checkpoint(lado_inicial, lado_final, estados, 0)
	while(len(lado_final)!=6):
		#barco pode levar uma ou duas pessoas
		flag=0
		cont=0
		while(flag==0):
			j = randint(0,1) #quantidade de personagens que serão retirados
			if(j==0): i = randint(0,1) 
			else: i = randint(0,3) # 0 dois missionarios, 1 dois canibais, 2 um missionario e um canibal, 3 um missionario e um cabinal
			
			if not (type(backup_inicial)==bool):
				backup_inicial = copy(lado_inicial)
				backup_final = copy(lado_final)
			else:
				lado_inicial = copy(backup_inicial)
				lado_final = copy(backup_final)
			if(len(lado_inicial)==1):
				aux = lado_inicial[0]
				retira_personagem(aux, 0, lado_inicial, lado_final)
			if (i==0) or (i==1):
				lado_inicial, lado_final = retira_personagem(i, j, lado_inicial, lado_final)
			elif (i==2)or(i==3):
				if(len(lado_inicial)>1):
					lado_inicial, lado_final = retira_personagem_especial(lado_inicial, lado_final)
			if(lado_inicial!=False): #quer dizer que ele não é boolean
				if(cont==100):
					print 'restart'
					lado_inicial = [0, 0, 0, 1, 1, 1]
					lado_final = []
					estados = []
					iteracao = 0
					break
				if(verifica(lado_inicial, lado_final)==False): #quer dizer que deu merda
					lado_inicial = copy(backup_inicial)
					lado_final = copy(backup_final)
				else:
					if(backup_inicial==lado_inicial): #quer dizer que continuou a mesma coisa
						lado_inicial = copy(backup_inicial)
						lado_final = copy(backup_final)
					else:
						flag=1
						break
			else:
				lado_inicial = copy(backup_inicial)
				lado_final = copy(backup_final)
			cont=cont+1
		backup_inicial = copy(lado_inicial)
		backup_final = copy(lado_final)
		iteracao = iteracao + 1
		estados = checkpoint(lado_inicial, lado_final, estados, iteracao)
		if(len(lado_final)==6):
			break
		t = 0
		cont=0
		while(flag==1):
			if not (type(backup_inicial)==bool):
				backup_inicial = copy(lado_inicial)
				backup_final = copy(lado_final)
			else:
				lado_inicial = copy(backup_inicial)
				lado_final = copy(backup_final)
			if(len(lado_final)==1): #volto apenas um personagem
				j = randint(0,1)
				i = randint(0,1)
				lado_final, lado_inicial = retira_personagem(i, j-1, lado_final, lado_inicial)
			else:
				i = randint(0,3)
				if(i == 0 or i == 1):
					i = randint(0,1)
					lado_final, lado_inicial = retira_personagem(i, 0, lado_final, lado_inicial)
				else:
					if (i==1) or (i==0):	
						lado_final, lado_inicial = retira_personagem(i, j, lado_final, lado_inicial)
					elif (i==2)or(i==3):
						if(len(lado_final)>1):
							lado_final, lado_incio = retira_personagem_especial(lado_final, lado_inicial)
						else:
							i = randint(0,1)
							lado_final, lado_inicial = retira_personagem(i, j-1, lado_final, lado_inicial)
			if(lado_final!=False):
				if(cont==100):
					print 'restart'
					lado_inicial = [0, 0, 0, 1, 1, 1]
					lado_final = []
					estados = []
					iteracao = 0
					break

				if(verifica(lado_final, lado_inicial)==False): #quer dizer que deu merda
					lado_inicial = copy(backup_inicial)
					lado_final = copy(backup_final)
				else:
					if(lado_final==backup_final): #quer dizer que continuou a mesma coisa
						lado_inicial = copy(backup_inicial)
						lado_final = copy(backup_final)
					else:
						flag=0
						break
			else:
				lado_inicial = copy(backup_inicial)
				lado_final = copy(backup_final)
			cont=cont+1
		backup_inicial = copy(lado_inicial)
		backup_final = copy(lado_final)
		iteracao =  iteracao +1
		estados = checkpoint(lado_inicial, lado_final, estados, iteracao)
	return iteracao, estados

i, estados = metodo()
print ''.join(estados)