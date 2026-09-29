#%%
# while loops
i = 10

while i != 0:
    print("Cachorro")
    i = i - 1
# %%
# while loops
i = 0

while i <= 3:
    print("Cachorro")
    i = i + 1
# %%
# while loops
i = 0

while i <= 3:
    print("Cachorro")
    i += 1

# %%
# for loops
for i in [0,1,2,3,4]:
    print(i)
    print("Cachorro")
# %%
# for loops
for i in range(21):
    print(i)
# %%
# for loops
for i in range(10):
    print("Cachorro")
# %%
# comando break e continue
while True:
    tempo = int(input("Quantos ans de estudo você tem?"))
    if tempo < 0:
        continue
    else:
        break
# %%
# for loops
for i in range(50):
    if i == 11:
        break
    print("Cachorro")
# %%
while True:
    tempo = int(input("Quantos anos de estudo você tem? "))
    if tempo > 0:
        break

for i in range(tempo):
    print("cachorro")
# %%
# função principal
def main():
    impressao(obter_numero())

# função que solicita um número do usuário e retorna o valor
def obter_numero():
    while True:
        nvezes = int(input("Quantas vezes você quer que a palavra deve ser impressa?"))
        if nvezes > 1:
            return nvezes

# função que imprime a palavra cachorro  o número de vezes que o usuário definiu
def impressao(nvezes):
    for i in range(nvezes):
        print("Cachorro")

main()
# %%
# função que solicita um número do usuário e retorna o valor
def numero():
    nvezes = int(input("Quantas vezes você quer que a palavra deve ser impressa?"))
    if nvezes > 1:
        return nvezes
# função que imprime a palavra cachorro  o número de vezes que o usuário definiu
def impressao(nvezes):
    for i in range(nvezes):
        print("Cachorro")

impressao(numero())
# %%
# trabalhando com listas
alunos = ["Luis", "João", "Camila", "José"]

print(alunos[0])
print(alunos[1])
print(alunos[2])
print(alunos[3])

print(alunos)
# %%
