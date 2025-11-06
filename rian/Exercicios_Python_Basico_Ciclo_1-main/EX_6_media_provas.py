# Escreva um programa que pede ao usuário o nome de um aluno e as notas de 3 provas que este aluno realizou.
# No fim o programa deve mostrar na tela a média das 3 provas
# Dica:
# Para calcular a média das provas você deve dividir a soma das notas das provas pela quantidade de provas realizadas
# media = soma / 3

# OUTPUT ESPERADO:

# | ______________________________ |
# | SISTEMA DE PROVAS
# | ______________________________ |
# | Nome do aluno: Fulano
# | Nota da primeira prova: 9.8
# | Nota da segunda prova: 7
# | Nota da terceira prova: 8.5
# | ______________________________ |
# | Aluno: Fulano 
# | Média: 8.43
# | Aluno aprovado
# | ______________________________ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

aluno = input("qual o nome do aluno: ")
n1 = float(input("qual a sua nota da primeira_prova"))
n2 = float(input("qual a sua nota da segunda_prova"))
n3 = float(input("qual a sua nota da terceira_prova"))

media = (n1 + n2 + n3)/3

if media >= 5.0 and media <=10.0:
    print("aprovado")

elif media <= 4.9 and media >= 3.0:
    print("recuperação")

elif media <=2.9:
    print("reprovado")

else:
    print()