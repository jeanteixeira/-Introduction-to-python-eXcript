print("WHILE")
x = 0
while(x<=10):
	print(x)
	x+=1
	
print	
print("WHILE/ELSE")
x = 0
while(x<=10):
	print(x)
	x+=1
else:
	print("else")

print
print("FOR")
for c in "Data Science":
	print(c)

print
print("Range Function")

print(range(10))
print(range(0,10,1))

print
print("BREAK")

print("Entrou no loop")
for item in range(10):
	print(item)
	if(item==6):
		break
print("Saiu do loop")

print
print("CONTINUE")

print("Entrou no loop")
for item in range(10):

	if(item%2==0):
		continue
	else:
		print(item)
print("Saiu do loop")
