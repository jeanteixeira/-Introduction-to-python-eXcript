def minha_func():
	print("fala galera")

minha_func()
print

#param
def soma(a,b):
	total = a+b
	print("O total da soma de a + b e igual: ", total)

soma(3,6)
print

#parametros default
def login(sistema,user="root",psw="123"):
	print("O sistema escolhido foi: ",sistema)
	print("O usuario: ", user)
	print("A senha: ",psw)
	
login('Ubuntu')

print

#Argumentos posicionais VS Argumentos nomeados
def dados_pessoais(nome,sobrenome,idade,sexo):
	print("Nome: {}\nSobrenome: {}\nIdade: {}\nSexo: {}"
	.format(nome,sobrenome,idade,sexo))
	print

dados_pessoais("claudio","carvalho",30,True)
dados_pessoais(sexo=True,sobrenome="carvalho",nome="claudio",idade=30)


#Return
def mult(x,y):
	resultado = x*y
	return resultado

print(mult(4,3))

print

#Multiple Return
def func():
	return 1,2

a, b = func()

print(a)
print(b)
print

def pot(x):
	qd = x**2
	cube = x**3
	
	return qd, cube

q,c = pot(10)
print(q)
print(c)

print

#Multiple parameter
def lista_de_argumentos(*args):
	print(args)

lista_de_argumentos(1,2,3,4,5)
lista_de_argumentos("um","dois","tres","quatro")

print

def lista_de_argumentos_associativos(**kwargs):
	print(kwargs)

lista_de_argumentos_associativos(a=1,b=2,c=3,d=4)
lista_de_argumentos_associativos(um=1,dois=2,tres=3,quatro=4)	

print

def argumentos(*args,**kwargs):
	print(args)
	print(kwargs)

argumentos(1,2,3,4,um=1,dois=2,tres=3,quatro=4)
