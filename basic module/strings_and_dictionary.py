#SPLIT, REPLACE
l = "lista de caracteres"
print(l)
print(l.replace("de",""))

a = l.split(" ")
print(a)

a = a[0] + " " + a[2]
print(a)

print

#iterando
s = "iterando string"
for c in s:
	print(c)

indice = 0

while indice < len(s):
	print(indice, s[indice])
	indice +=1

print

#Dictionary
d1 = dict()
print(type(d1))
d1['aaa'] = 1000
d1['bbb'] = 2000
d1['ccc'] = 3000
print(d1)
print(d1['bbb'])
print

tel = {}
tel = {123456: "jean", 123654: "ivo", 654321: "ana", 654123: "duda"}
print(tel)
print(len(tel))
print(tel.keys())
print(tel.values())
