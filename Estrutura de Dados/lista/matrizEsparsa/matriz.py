class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []
    
    def adicionar_notas(self, notas):
        self.notas = notas
    
    def calcular_media(self):
        media = sum(self.notas) / len(self.notas)
        return round(media, 2)

class MatrizEsparsa:
    def __init__(self):
        self.alunos = {}
    
    def adicionar_aluno(self):
        nome = input("Digite o nome do aluno: ")
        if nome not in self.alunos:
            notas = []
            for i in range(3):
                nota = float(input(f"Digite a {i+1}ª nota de {nome}: "))
                notas.append(nota)
            aluno = Aluno(nome)
            aluno.adicionar_notas(notas)
            self.alunos[nome] = aluno
            print(f"Aluno {nome} adicionado com sucesso!")
        else:
            print("O aluno já existe.")
    
    def imprimir_notas(self):
        if not self.alunos:
            print("Não há alunos registrados.")
            return
        
        # Ordenar os alunos em ordem alfabética pelo nome
        alunos_ordenados = sorted(self.alunos.keys())
        
        print(f"{'Nome':<15} {'1ª Nota':<10} {'2ª Nota':<10} {'3ª Nota':<10} {'Média':<10}")
        for nome in alunos_ordenados:
            aluno = self.alunos[nome]
            notas = aluno.notas
            media = aluno.calcular_media()
            print(f"{nome:<15} {notas[0]:<10.2f} {notas[1]:<10.2f} {notas[2]:<10.2f} {media:<10.2f}")
    
    def editar_notas(self, nome):
        if nome in self.alunos:
            notas = []
            for i in range(3):
                nota = float(input(f"Digite a {i+1}ª nota de {nome}: "))
                notas.append(nota)
            self.alunos[nome].adicionar_notas(notas)
            print(f"Notas do aluno {nome} atualizadas com sucesso!")
        else:
            print("Aluno não encontrado.")
    
    def buscar_aluno(self, nome):
        if nome in self.alunos:
            aluno = self.alunos[nome]
            print(f"Notas do aluno {nome}: {aluno.notas}")
            media = aluno.calcular_media()
            print(f"Média do aluno {nome}: {media}")
        else:
            print("O aluno não existe.")
    
    def excluir_aluno(self, nome):
        if nome in self.alunos:
            del self.alunos[nome]
            print(f"Aluno {nome} excluído com sucesso!")
        else:
            print("O aluno não existe.")

matriz_esparsa = MatrizEsparsa()

import sys

# Resto do código...

while True:
    print("===== MENU =====")
    print("1. Adicionar aluno")
    print("2. Editar notas de um aluno")
    print("3. Buscar aluno e calcular média")
    print("4. Excluir aluno")
    print("5. Imprimir notas dos alunos")
    print("0. Sair")

    opcao = sys.stdin.readline().strip()

    if opcao == "1":
        matriz_esparsa.adicionar_aluno()
    elif opcao == "2":
        nome = sys.stdin.readline().strip()
        matriz_esparsa.editar_notas(nome)
    elif opcao == "3":
        nome = sys.stdin.readline().strip()
        matriz_esparsa.buscar_aluno(nome)
    elif opcao == "4":
        nome = sys.stdin.readline().strip()
        matriz_esparsa.excluir_aluno(nome)
    elif opcao == "5":
        matriz_esparsa.imprimir_notas()
    elif opcao == "0":
        break
    else:
        print("Opção inválida. Tente novamente.")

print("Programa encerrado.")
