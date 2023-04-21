#include <stdio.h>
#include <string.h>

#define MAX_ALUNOS 30

struct Aluno {
    char nome[50];
    int idade;
    char email[50];
    char celular[20];
};

int numAlunos = 0;
struct Aluno listaAlunos[MAX_ALUNOS];

void adicionarAluno() {
    if (numAlunos >= MAX_ALUNOS) {
        printf("Erro: o limite de alunos foi atingido.\n");
        return;
    }
    
    struct Aluno novoAluno;
    
    printf("Digite o nome completo do aluno: "); // mensagem de entrada alterada
    scanf(" %[^\n]s", novoAluno.nome); // utilização de espaço em branco e %[^\n]s para ler todo o nome com espaço
    
    printf("Digite a idade do aluno: ");
    scanf("%d", &novoAluno.idade);
    
    printf("Digite o email do aluno: ");
    scanf("%s", novoAluno.email);
    
    printf("Digite o celular do aluno: ");
    scanf("%s", novoAluno.celular);
    
    listaAlunos[numAlunos] = novoAluno;
    numAlunos++;
    
    printf("Aluno adicionado com sucesso.\n");
}

void removerAluno() {
    char nome[50];
    int indice = -1;
    int i;

    printf("Digite o nome do aluno a ser removido: ");
    scanf(" %[^\n]s", nome);

    for (i = 0; i < numAlunos; i++) {
        if (strcmp(listaAlunos[i].nome, nome) == 0) {
            indice = i;
            break;
        }
    }

    if (indice == -1) {
        printf("Aluno nao encontrado.\n");
        return;
    }

    for (i = indice; i < numAlunos - 1; i++) {
        listaAlunos[i] = listaAlunos[i+1];
    }

    numAlunos--;

    printf("Aluno removido com sucesso.\n");
}

void imprimirAlunos() {
    printf("\n--- Lista de Alunos ---\n\n");
    int i, j, min_index;
    struct Aluno temp;

    // selection sort para ordenar a lista de alunos em ordem alfabética pelo nome
    for (i = 0; i < numAlunos - 1; i++) {
        min_index = i;
        for (j = i + 1; j < numAlunos; j++) {
            if (strcmp(listaAlunos[j].nome, listaAlunos[min_index].nome) < 0) {
                min_index = j;
            }
        }
        if (min_index != i) {
            temp = listaAlunos[i];
            listaAlunos[i] = listaAlunos[min_index];
            listaAlunos[min_index] = temp;
        }
    }

    // imprimir a lista de alunos ordenada em ordem alfabética pelo nome
    for (i = 0; i < numAlunos; i++) {
        printf("Nome: %s\n", listaAlunos[i].nome);
        printf("Idade: %d\n", listaAlunos[i].idade);
        printf("E-mail: %s\n", listaAlunos[i].email);
        printf("Celular: %s\n", listaAlunos[i].celular);
        printf("\n");
    }
}

int main() {
    int opcao;
    
    do {
        printf("Escolha uma opcao:\n");
        printf("1. Adicionar aluno\n");
        printf("2. Remover aluno\n");
        printf("3. Imprimir lista de alunos\n");
        printf("4. Sair\n");
        printf("Opcao: ");
        scanf("%d", &opcao);
        
        switch (opcao) {
            case 1:
                adicionarAluno();
                break;
            case 2:
                removerAluno();
                break;
            case 3:
                imprimirAlunos();
                break;
            case 4:
                printf("Encerrando o programa...\n");
                break;
            default:
                printf("Opcao invalida.\n");
                break;
        }
    } while (opcao != 4);

    return 0;
}

