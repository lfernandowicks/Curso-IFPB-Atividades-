#%%
# função para imprimir para usuário
print ('Olá mundo!')
#%%
# função para entrada de dados
input('Qual é seu nome?')
# %%
# perguntar o nome do usuário e inserir na variável
name = input('What is you name?')

# imprimir o valor da variável 
print(name)
print(f'Hello, {name}!')
# %%
# perguntar o nome do usuário e inserir na variável
name = input("What´s your name?")

# Retorno do script com saudação
print("Hello, ", end="")
print(name)

# %%
# usara \'\' para aspas na saída
print('Hello, \'friend\'')
# %%
# perguntar o nome do usuário e inserir na variável
name = input("What's your name?")

# remover os espaços das extremidades
name = name.strip()

# Retorno do script com saudação e nome
print(f'Hello, {name}')

# %%
name ="          luis  "

# remover os espaços das extremidades e transformar a primeira letra em maiúsculo
name = name.strip().title()

# Retorno do script com saudação e nome
print(f"Hello, {name}")
# %%
'''mais concisão
perguntar o nome do usuário e inserir na variável
remover os espaços das extremidades e transformar a primeira letra em maiúsculo'''
name = input("What's your name? ").strip().title()

# Retorno do script com saudação e nome
print(f"Hello, {name}")
# %%
# Transformar as letras em maiúsculo
name = "luis".upper()
print(name)
# %%
# Transformar as letras em menúsculas
name = "LUIS".lower()
print(name)
# %%
name = "Luis Fernando"

# Realizar a contagem de n na variável name
qtN = name.count("n")

# Saída do nome e das quantidades de n no nome
print(f"Seu nome, {name}, tem {qtN} n")

print(type(qtN))
# %%
# trabalhando com numeros
# Solicitando número inteiro e guardando na variável x
x = int(input("What´s x: "))
# Solicitando número inteiro e guardando na variável y
y = int(input("What's y: "))

# Realizando a soma de x e y e guardando na variável z
z = x + y

print(f"The sum of x and y is: {z}")
# %%
