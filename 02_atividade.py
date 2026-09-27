#%%
# valores de ponto flutuante
x = 0.5
# saída do tipo do dado
print(type(x))
# %%
# Solicitando número decimal e guardando na variável x
x = float(input("Insira um valor decimal"))

print(x)
# %%
# Solicitando número decimal e guardando na variável salário
salario = float(input("Qual é seu salário? "))
# Solicitando número decimal e guardando na variável extra
extra = float(input("Quanto você fez de hora extra? "))

# Realzando a soma e imprimindo
print(salário + extra)

# %%
# função para arredondar
# Solicitando número decimal e guardando na variável salário
salario = float(input("Qual foi seu salário? "))
# Solicitando número decimal e guardando na variável extra
extra = float(input("Quanto você fez de extra? "))

# Realizando a soma de salário e extra e arredondando o resultado
salario_total = round(salario + extra)

print(salario_total)
# %%
# Solicitando número decimal e guardando na variável salário
salario = float(input("Qual foi seu salário? "))
# Solicitando número decimal e guardando na variável extra
extra = float(input("Quanto você fez de extra? "))

# função round() para arredondar
salario_total = round(salario + extra)

print(f'{salario_total:,}')

# %%
# Solicitando número decimal e guardando na variável salário
salario = float(input("Qual foi seu salário? "))
# Solicitando número decimal e guardando na variável extra
extra = float(input("Quanto você fez de extra? "))

# Variável que guarda o valor do dia trabalhado
salario_doDia = (salario + extra)/30

print(salario_doDia)
# %%
# Solicitando número decimal e guardando na variável salário
salario = float(input("Qual foi seu salário? "))
# Solicitando número decimal e guardando na variável extra
extra = float(input("Quanto você fez de extra? "))

# Variável que guarda o valor do dia trabalhado
salario_doDia = (salario + extra)/30
# Variável que guarda o valor do dia trabalhado arredondado
salario_doDia = round(salario_doDia,2)

print(salario_doDia)
# %%
# Solicitando número decimal e guardando na variável salário
salario = float(input("Qual foi seu salário? "))
# Solicitando número decimal e guardando na variável extra
extra = float(input("Quanto você fez de extra? "))

# Variável que guarda o valor do dia trabalhado
salario_doDia = (salario + extra)/30

# Definindo a saída com duas casas decimais depois da vírgula
print(f"{salario_doDia:.2f}")

# %%
# booleans
a = True
b = False

# condicional
if a:
    print("A é verdadeiro")
else:
    print("A é Falso")


# %%
# perguntar o nome, remover espaços nas extremidades e primeira letra maiúscula
name = input("What's your name? ").title().strip()

# imprimir a saida
print(f"Olá, {name}")

# %%
#Criando função para saudar usuário
def hello():
    print("Olá!")

# função para solicitar dados do usuário
name = input("What's your name? ").strip().title()

#chamando a função
hello()
print(f'Olá, {name}')

# %%
#Criando função para saudar usuário com parâmetros
def hello(to):
    print("Olá!", to)

# função para solicitar dados do usuário
name = input("What's your name? ").strip().title()

#chamando a função
hello(name)


# %%
#Criando função para saudar usuário com parâmetro padrão
def hello(to="Mundo"):
    print("Olá!", to)

#chamando a função
#hello()
print(hello())
# %%
# função principal que solicita o nome do usuário
def main():
    # solicita o nome do usuário
    name = input("What's yout name? ").strip().title()
    # chama a função hello com parâmetro
    hello(name)

main()
# %%
# função que calcula o quadrado de um número
def square(x):
    return x*x

# função que solicita um número do usuário e retorna seu valor ao quadrado
def value_square():
    x = int(input("Digite um número para saber o seu quadrado: "))
    print (f"O quadrado de {x} é",square(x))

# chamar a função value_square()
value_square()

# guardar o quadrado de 25 na variável a
a= square(25)

print(f"O quadrado de 25 é {a}")
    
    
# %%
