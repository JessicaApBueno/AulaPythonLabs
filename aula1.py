print("hello world")
print("melancia")

#exercicío 1
#Criando uma variável no Python!!
fruta_citrica_maio = "melancia"
#Imprimindo a variável
print(fruta_citrica_maio)

#Expressões Matemáticas Python

print (2*3+3**2)

carro = "fox"
print(carro)

# Função para adicionar uma pessoa á lista
def adicionar_pessoa(lista, nome, idade, profissao):
    pessoa = {"nome": nome, "idade": idade, "profissao": profissao}
    lista.append(pessoa)

#Função para mostrar as pessoas da lista

def exibir_pessoas(lista):
    print("Lista de pessoas cadastradas")
    for pessoa in lista:
        print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Profissao: {pessoa['profissao']}")

# Lista para armazenar pessoas
pessoas = []

# Adicionando