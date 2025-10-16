       #CALCULARDORA DE MEDIA ESCOLAR#


n1 = float(input("qual é a sua nota do 1 bimestre"))
n2 = float(input("qual é a sua nota do 2 bimestre"))
n3 = float(input("qual é a sua nota do 3 bimestre"))
n4 = float(input("qual é a sua nota do 4 bimestre"))

total = n1 + n2 + n3 + n4 

media = total/4

print(media)

if media > 7.0:
    print("aprovado")
elif  media > 5.0 and media < 7.0:
    print("recuperacão")
else:
    print("reprovado")