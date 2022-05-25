  
from http.client import PRECONDITION_REQUIRED
import json
import os.path
import sys

def obter_dados():
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados


# Valida a escolha da categoria feita pelo usuário
def pede_categoria(dados):
    categorias = listar_categorias(dados)

    # Tratando a entrada do usuário para que aceite palavras divididas por espaço, minúscula e maiúscula
    categoria = input('Escreva uma categoria da qual deseja consultar: ').replace(" ", '_').lower()

    while categoria not in categorias:
        categoria = input('Categoria inválida! Escreva uma categoria da qual deseja consultar: ').replace(" ", '_')
    return categoria


# Lista todas as categorias existentes na base de dados
def listar_categorias(dados):

    # Garantir valores únicos para cada categoria
    categorias = set()

    for dado in dados:
        categorias.add(dado['categoria'])

    return list(categorias)
    

# Lista todos os produtos de determinada categoria presentes na base de dados
def listar_por_categoria(dados, categoria):
    produtos = []

    for dado in dados:
        if dado['categoria'] == categoria:
            produtos.append(dado)
            
    return produtos


# Achei melhor ja mandar a lista de produtos de determinada categoria para a função só avaliar o mais caro (menos responsabilidade)
def produto_mais_caro(produtos):
    mais_caro = produtos[0]

    # Optei por ir comparando os produtos e removendo os mais baratos 
    # Se houver mais de um produto com o mesmo preço (mais caro) mantém e retorna todos
    for produto in produtos[1:]:
        if float(produto['preco']) < float(mais_caro['preco']):
            produtos.remove(produto)
        else: # maior ou igual
            produtos.remove(mais_caro)
            mais_caro = produto
    return mais_caro


# Mesma lógico do de cima, mas retornando o mais barato
def produto_mais_barato(produtos):

    mais_barato = produtos[0]

    for produto in produtos[1:]:
        if float(produto['preco']) > float(mais_barato['preco']):
            produtos.remove(produto)
        else: # maior ou igual
            produtos.remove(mais_barato)
            mais_barato = produto
    return mais_barato


# Retorna os 10 produtos mais caros dentro do banco de dados
def top_10_caros(dados):

    dados = sorted(dados, key = lambda x: float(x['preco']), reverse = True)

    return dados[:10]


# Retorna os 10 produtos mais caros dentro do banco de dados
def top_10_baratos(dados):

    dados = sorted(dados, key = lambda x: float(x['preco']))

    return dados[:10]


# Exibe as funcionalidades para o usuário e chama funções adequadas de acordo com a escolha do mesmo
def menu(dados):
    opcao =""


    # Repete as opções enquanto o usuário não digita a opção de saída
    while opcao != '0':
        replace(" ", '_')
        
        # Valida a opção escolhida pelo usuário
        while opcao not in [str(i) for i in range(7)]:
            opcao = input("""Erro! Por favor, digite uma opção válida\n
            Menu principal. Por favor, digite a opção que deseja acessar:
                [1] - Listas as categorias
                [2] - Listar produtos de uma categoria
                [3] - Produto mais caro por categoria
                [4] - Produto mais barato por categoria
                [5] - Top 10 produtos mais caros
                [6] - Top 10 produtos mais baratos
                [0] - Sair
        """)

    
        if opcao == '1':
            categorias = sorted(listar_categorias(dados))

            # Printando de maneira mais agradável para o usuário
            for categoria in categorias:
                print(categoria.upper().replace("_", " "))

        elif opcao == '2':
            categoria = pede_categoria(dados)
            
            produtos = listar_por_categoria(dados, categoria)

            print(f'Os produtos dessa categoria são:\n')

            # Printando os produtos de maneira mais amigável para o usuário
            for produto in produtos:
                print(f"Id: {produto['id']}, Preço: {produto['preco']}")

        elif opcao == '3':
            categoria = pede_categoria(dados)

            produtos = listar_por_categoria(dados, categoria)

            mais_caro = produto_mais_caro(produtos)

            print("O(s) produto(s) mais caro(s) dessa categoria é(são):\n")

            # Estrutura feita para funcionar em caso de empate de dois ou mais produtos
            for produto in produtos:
                print(f'Id: {produto["id"]}, Preço: {produto["preco"]}')
        
        elif opcao == '4':
            categoria = pede_categoria(dados)

            produtos = listar_por_categoria(dados, categoria)

            mais_barato = produto_mais_barato(produtos)

            print("O(s) produto(s) mais barato(s) dessa categoria é(são):\n")

            for produto in produtos:
                print(f'Id: {produto["id"]}, Preço: {produto["preco"]}')

        elif opcao == '5':
            # os outros eu fiz 'na mao' para testar raciocinio e para pegar valores repetidos (caso houvessem), este vou usar o metódo ensinado pelo prof (key = lambda):
            produtos = top_10_caros(dados)

            print('Os 10 produtos mais caros são:\n')
            
            # Contador para exibir a posição do produto no ranking de preços
            rank = 1

            for produto in produtos:
                print(f'{rank}) Id: {produto["id"]}, Preço: {produto["preco"]}')
                rank +=1

        elif opcao == '6':
            produtos = top_10_baratos(dados)
            rank = 1

            print('Os 10 produtos mais baratos são:\n')          
            for produto in produtos:
                print(f'{rank}) Id: {produto["id"]}, Preço: {produto["preco"]}')
                rank += 1

    # Mensagem de saída (só é executada de o usuário escolher a opção de saída)
    print("Muito obrigado. Até a próxima!")



dados = obter_dados()
menu(dados)
