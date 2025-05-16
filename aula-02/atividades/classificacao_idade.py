#Descobrindo se a pessoa é idosa, adulta, adolescente, criança ou bebê

id = int(input("Digite a sua idade: "))

if id >= 65:
    print("Você é idoso")
elif id >=18:
    print("Você é adulto")
elif id >=12:
    print("Você é adolescente")
elif id >= 3:
    print("Você é uma criança")
else:
    print("Você é um bebê")
