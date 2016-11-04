"""
NAO FUNCIONA
lista_nums = [100,200,300,400]
for item in lista_nums:
	item += 1000
print(lista_nums)

"""	

#Range Function
lista_nums = [100,200,300,400,500]
for item in range(len(lista_nums)):
	lista_nums[item] += 1000
print(lista_nums)

#Enumerate Function
lista_nums = [100,200,300,400,500]
for idx,item in enumerate(lista_nums):
	lista_nums[idx] += 1000
print(lista_nums)
print

#Slace list
lista = "Bem-vindo ao curso de python!"
print(lista[::-1])
print(lista[4:])
print(lista[:10])
print(lista[4::3])

print

#POP, APPEND, DEL
lista = ['aaa','bbb','ccc']
print(lista)
lista.append('ddd')
print(lista)
lista.pop()
print(lista)
lista.pop(0)
print(lista)

lista = ['aaa','bbb','ccc','ddd','eee','fff']
print(lista)
del(lista[::2])
print(lista)

print

#Order
lista = ['jean','ana','ivo','duda','vini','carlianne','camila']
print(lista)
lista.reverse()
print(lista)
lista.reverse()
print(lista)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

print

#INDEX, COUNT
lista = ['jean', 'ivo', 'duda', 'camila', 'jean', 'ana', 'carlianne', 'vini','jean']

print("repete-se",lista.count("jean") ,"vezes o nome jean")
print("indice da primeira ocorrencia de jean e: ",lista.index("jean"))
print("indice de ana e: ",lista.index("ana"))

print

#TUPLE
t = ('aaa',1,True)
print(t)
print(type(t))
