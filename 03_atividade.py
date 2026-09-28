#%%
# Operadores de comparação
# variável recebe um valor inteiro
x = int(input("Qual o valor de x? "))
y = int(input("Qual o valor de y? "))

# estrutura condicional que informa qual o número é maior
if x < y:
    print(f'{x} é menor que {y}')
else:
    print(f'{x} é maior que {y}')
# %%
# variável x recebe um valor inteiro
x = int(input("Qual o valor de x? "))
# variável y recebe um valor inteiro
y = int(input("Qual o valor de y? "))

# variável a recebe um valor booleano
a = x < y

# estrutura condicional que informa qual o número é maior
if a:
    print(f'{x} (x) é menor que {y} (y)')
else:
    print(f'{x} (x) é maior que {y} (y)')
# %%
# variável x recebe um valor inteiro
x = int(input("Qual o valor de x? "))
# variável y recebe um valor inteiro
y = int(input("Qual o valor de y? "))

# estrutura condicional que informa qual o número é maior
if x < y:
    print(f'{x} (x) é menor que {y} (y)')
if x > y:
    print(f'{x} (x) é maior que {y} (y)')
if x == y:
    print(f'{x} (x) é igual a {y} (y)')
# %%
# variável x recebe um valor inteiro
x = int(input("Qual o valor de x? "))
# variável y recebe um valor inteiro
y = int(input("Qual o valor de y? "))

# estrutura condicional que informa qual o número é maior
if x < y:
    print(f'{x} (x) é menor que {y} (y)')
elif x > y:
    print(f'{x} (x) é maior que {y} (y)')
else:
    print(f'{x} (x) é igual a {y} (y)')
# %%
'''
OR
True or True = True
True or False = True
False or True = True
False or False = False
'''
# variável x recebe um valor inteiro
x = int(input("Qual o valor de x? "))
# variável y recebe um valor inteiro
y = int(input("Qual o valor de y? "))

# estrutura condicional que informa se as variáveis são iguais
if x < y or x > y:
    print(f'{x} (x) e {y} (y) não são iguais')
else:
    print(f'{x} (x) e {y} (y) são iguais')


# %%
# variável x recebe um valor inteiro
x = int(input("Qual o valor de x? "))
# variável y recebe um valor inteiro
y = int(input("Qual o valor de y? "))

# estrutura condicional que informa se as variáveis são iguais
if x != y:
    print(f'{x} (x) e {y} (y) não são iguais')
else:
    print(f'{x} (x) e {y} (y) são iguais')
# %%
'''
AND
True and True = True
True and False = False
False and True = False
False and False = False
'''
nota = int(input("Qual foi sua nota? "))

if nota > 90 and nota <=100:
    print("Grade A")
elif nota > 80 and nota <=90:
    print("Grade B")
elif nota > 70 and nota <=80:
    print("Grade C")
elif nota >= 60 and nota <=70:
    print("Grade D")
else:
    print("Grade E")
# %%
nota = int(input("Qual foi sua nota? "))

if nota > 90:
    print("Grade A")
elif nota >= 80:
    print("Grade B")
elif nota >= 70:
    print("Grade C")
elif nota >= 60:
    print("Grade D")
else:
    print("Grade E")
# %%
# % resto da divisão
# verificar se x é impar ou par
x = int(input("Qual o valor de x? "))

if x % 2 == 0:
    print(f"{x} é um número par")
else:
    print(f"{x} é um número ímpar")

# %%
# funções para determinar se um número é par ou ímpar
def main():
    y = int(input("Digite um valor para saber se é ímpar ou par"))

    if par(y):
        print(f"O número {y} é par")
    else:
        print(f"O número {y} é ímpar")

def par(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()

# %%
# funções para determinar se um número é par ou ímpar
def main():
    y = int(input("Digite um valor para saber se é ímpar ou par"))

    if par(y):
        print(f"O número {y} é par")
    else:
        print(f"O número {y} é ímpar")

def par(n):
    # código mais conciso
    return True if n % 2 == 0 else False

main()

# %%
# funções para determinar se um número é par ou ímpar
def main():
    y = int(input("Digite um valor para saber se é ímpar ou par"))

    if par(y):
        print(f"O número {y} é par")
    else:
        print(f"O número {y} é ímpar")

def par(n):
    # código mais conciso
    return n % 2 == 0

main()

# %%
# Comparar valores
nome_cidade = input("Qual o nome da sua cidade? ")

if nome_cidade == "João Pessoa" or nome_cidade == "Campina Grande" or nome_cidade == "Patos":
    print("Estado: Paraíba")
elif nome_cidade == "Recife":
    print("Estado: Pernambuco")
else:
    print("Cidade não encontrada")
# %%
nome_cidade = input("Qual o nome da sua cidade?")

match nome_cidade:
    case "João Pessoa" | "Campina Grande" | "Patos":
        print("Estado: Paraíba")
    case "Recife" | "Olinda":
        print("Estado: Pernambuco")
    case _:
        print("Não encontrado")

# %%
