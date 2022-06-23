import json


class EmailJaCadastrado(Exception):
    def __init__(self, message='Já existe usuário cadastrado com esse e-mail'):
        self.message = message
        super().__init__(self.message)


class EmailInvalido(Exception):
    def __init__(self, message='E-mail informado inválido!'):
        self.message = message
        super().__init__(self.message)


class NomeInvalido(Exception):
    def __init__(self, message='Nome informado inválido!'):
        self.message = message
        super().__init__(self.message)


class ListaVazia(Exception):
    def __init__(self, message='Digite ao menos um item.'):
        self.message = message
        super().__init__(self.message)


def valida_nome(nome: str) -> bool:
    return nome.replace(" ", "").isalpha()


def valida_email(email: str) -> bool:
    return (email.count('@') == 1 and email.replace("@", 'a').replace('.', 'a').replace("_", 'a').isalnum())


def existe_email_na_base(registros, email: str) -> list:
    return list(filter(lambda x: x['email'] == email, registros['musicos']))


def padroniza_listas(lista: list) -> list:
    return [elemento.title() for elemento in lista]


def validacoes_gerais(registros: dict) -> dict:
    try:
        email = input("Digite seu e-mail: ").lower()
        if existe_email_na_base(registros, email):
            print("\nJá existe usuário registrado com esse e-mail\n")
            raise EmailJaCadastrado()
        if not valida_email(email):
            print(f"\nEmail '{email}' inválido!\n")
            raise EmailInvalido()

        nome = input("Digite seu nome: ").title()
        if not valida_nome(nome):
            print(
                f"Nome {nome} inválido. Por favor, insira apenas letras e espaços.")
            raise NomeInvalido()

        generos = pede_lista(
            mensagem="Digite os gêneros musicais de sua preferencia")

        instrumentos = pede_lista(
            mensagem="Digite os intrumentos que você toca (pressione enter caso tenha terminado)")

        print("\nInformações: \n",
              f"{'Nome':<30}: {nome}\n",
              f'{"E-mail":<30}: {email}\n',
              f'{"Gêneros musicais":<30}: {str(generos)[1:-1]}\n',
              f"{'Instrumentos':<30}: {str(instrumentos)[1:-1]}")

        registros = cadastra_na_base(
            registros, nome, email, generos, instrumentos)

        return registros

    except:
        print("Não foi possível concluir o cadastro.\n")


def pede_lista(mensagem: str) -> list:
    lista = list()
    print(mensagem, end='\n\n')
    item = input()
    while item != "":
        lista.append(item)
        item = input()

    if not lista:
        print("Digite ao menos um item")
        raise ListaVazia()

    return padroniza_listas(lista)


def cadastra_na_base(registros: dict, nome: str, email: str, generos: list, instrumentos: list) -> dict:
    generos = padroniza_listas(generos)
    instrumentos = padroniza_listas(instrumentos)
    novo_registro = {'nome': nome, 'email': email,
                     'generos': generos, 'instrumentos': instrumentos}
    registros['musicos'].append(novo_registro)

    print('\nCadastro efetuado com sucesso!')

    return registros


def abre_ou_cria_arquivo(nome_do_arquivo: str) -> dict:
    try:
        with open(nome_do_arquivo, 'r', encoding='utf-8') as arquivo:
            registros = json.load(arquivo)

    except FileNotFoundError:
        print(f'\nCriando nova base: "{nome_do_arquivo[:-5]}"')
        with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
            registros = {'musicos': []}

    return registros


def filtra_dados(dicionario: dict, filtro_nome: str = "", filtro_email: str = "", filtro_instrumento: str = "", filtro_genero: str = "", condicional: str = '1') -> bool:
    condicao1 = filtro_nome in dicionario['nome'] if filtro_nome != "" else ""
    condicao2 = dicionario['email'] == filtro_email if filtro_email != "" else ""
    condicao3 = filtro_instrumento in dicionario['instrumentos'] if filtro_instrumento != "" else ""
    condicao4 = filtro_genero in dicionario['generos'] if filtro_genero != "" else ""

    if condicional == '1':
        condicoes_validas = [condicao for condicao in [
            condicao1, condicao2, condicao3, condicao4] if (condicao != "")]
        return (False not in condicoes_validas)

    elif condicional == '2':
        return (condicao1 or condicao2 or condicao3 or condicao4)


def gera_lista_filtrada(registros, filtro_nome: str = "", filtro_email: str = "", filtro_instrumento: str = "", filtro_genero: str = "", condicional: str = '1') -> list:
    return list(filter(lambda x: filtra_dados(x, filtro_nome=filtro_nome, filtro_email=filtro_email,
                                              filtro_instrumento=filtro_instrumento, filtro_genero=filtro_genero,
                                              condicional=condicional), registros['musicos']))


def buscar_musicos(registros: list) -> None:
    print(
        "Digite os filtros desejados para a busca (caso nao deseja incluir o filtro apresentado, pressioone [Enter])")
    filtro_nome = input("Nome: ").title()
    filtro_email = input("E-mail: ").lower()
    filtro_instrumento = input("Instrumento: ").title()
    filtro_genero = input('Gênero musical: ').title()

    condicional = input(
        "O resultado da busca deve atender:\n\t[1] - A todos os filtros\n\t[2] - A qualquer um deles:\n")

    while condicional not in ['1', '2']:
        print('Condição inválida')
        condicional = input(
            "O resultado da busca deve atender:\n\t[1] - A todos os filtros\n\t[2] - A qualquer um deles:\n")

    musicos_encontrados = gera_lista_filtrada(registros, filtro_nome=filtro_nome, filtro_email=filtro_email,
                                              filtro_instrumento=filtro_instrumento, filtro_genero=filtro_genero,
                                              condicional=condicional)

    apresenta_resultado_busca(musicos_encontrados)


def apresenta_resultado_busca(filtrado: list) -> None:
    print('\nCadastro(s) encontrados: \n')
    print('-' * 55)
    for musico in filtrado:
        print(f'{"Nome":<30}: {musico["nome"]}\n',
              f'{"E-mail":<30}: {musico["email"]}\n',
              f'{"Gêneros musicais":<30}: {str(musico["generos"])[1:-1]}\n',
              f"{'Instrumentos':<30}: {str(musico['instrumentos'])[1:-1]}\n",
              "-"*55, sep="")


def escolhe_opcao() -> str:
    print("\nOque deseja fazer?\n\nEscolha uma opção: \n",
          "[1] - Cadastrar músico\n",
          "[2] - Buscar músico\n",
          "[3] - Modificar cadastro\n",
          "[4] - Montar Bandas\n",
          "[0] = Sair\n")
    return input()


def modifica_lista(lista: list) -> list:
    print(f'\n{"Os registros atuais são: ":<35}: {str(lista)[1:-1]}\n')

    lista = pede_lista(
        "Digite todos os itens que deseja que apareça no cadastro (pressione [Enter] caso tiver terminado)")

    return lista


def modificar_cadastro(registros: list) -> list:
    email = input("Digite o e-mail do cadastro a ser modificado: ")
    if not existe_email_na_base(registros, email):
        print(f'Erro! Não existe o e-mail "{email}" cadastrado na base.')
        return

    cadastro_encontrado = gera_lista_filtrada(registros, filtro_email=email)[0]
    apresenta_resultado_busca([cadastro_encontrado])
    registros['musicos'].remove(cadastro_encontrado)

    print('\nQual informação deseja alterar?\n',
          '[1] - Gêneros musicais\n[2] - Instrumentos\n', sep="")

    alteracao_desejada = input()
    while alteracao_desejada not in ['1', '2']:
        print("Opção inválida!\n",
              '\nQual informação deseja alterar?\n',
              '[1] - Gêneros musicais\n[2] - Instrumentos\n', sep="")
        alteracao_desejada = input()

    lista_desejada = {"1": 'generos',
                      "2": 'instrumentos'}
    nova_lista = modifica_lista(
        lista=(cadastro_encontrado[lista_desejada[alteracao_desejada]]))
    cadastro_encontrado[lista_desejada[alteracao_desejada]] = nova_lista
    registros['musicos'].append(cadastro_encontrado)

    return registros


def menu(nome_do_arquivo: str) -> None:
    print("Bem vindo ao vivamusica.com!!! Site que já ajudou a montar centenas de bandas pelo Brasil.")

    registros = abre_ou_cria_arquivo(nome_do_arquivo)

    opcoes = {
        "1": validacoes_gerais,
        "2": buscar_musicos,
        "3": modificar_cadastro,
        "4": montar_banda
    }

    opcao = ""
    while opcao != "0":
        opcao = escolhe_opcao()

        if opcao not in opcoes and opcao != "0":
            print("Opção inválida!")
            continue

        elif opcao in ['1', '3']:
            registros = opcoes[opcao](registros)

        elif opcao in ['2', '4']:
            opcoes[opcao](registros)

    else:
        with open(nome_do_arquivo, 'w') as arquivo:
            arquivo.write(json.dumps(registros, indent=4))

        print("\nMuito obrigado por utilizar o vivamusica.com! Até a próxima.")


def montar_banda(registros: list) -> None:
    print("Yeah! Vamos ajudá-lo a montar sua próxima banda.\n\nDe quantos musicos você precisa?")
    numero_musicos = input()

    while not numero_musicos.isdigit():
        numero_musicos = input('Por favor, digite um numero válido: ')
    numero_musicos = int(numero_musicos)

    print("\nAgora, digite os instrumentos de cada músico que busca:\n")
    instrumentos_buscados = padroniza_listas(
        [input(f"Músico {i + 1}: ") for i in range(numero_musicos)])
    genero_buscado = input('\nDigite o gênero a ser buscado: ').title()

    musicos_encontrados = [gera_lista_filtrada(
        registros, filtro_instrumento=instrumento, filtro_genero=genero_buscado) for instrumento in instrumentos_buscados]
    musicos_encontrados = [(musico['email'], instrumento)
                           for lista_instrumento in musicos_encontrados for musico in lista_instrumento for instrumento in musico['instrumentos']]

    combinacoes = faz_combinacoes(musicos_encontrados, numero_musicos)

    bandas = filtra_combinacoes(
        combinacoes, numero_musicos, instrumentos_buscados)

    for banda in bandas:
        print(banda)

    return


def filtra_combinacoes(combinacoes, elementos, lista_instrumentos):
    lista = combinacoes
    for grupo in lista:
        for i in range(elementos):
            if grupo[i][1] != lista_instrumentos[i]:
                lista.remove(grupo)
                break

    for banda in lista:
        confere = set()
        for musico in banda:
            confere.add(musico[0])

        if len(confere) < elementos:
            lista.remove(banda)

    return lista


def faz_combinacoes(lista, comprimento, lista_aux=[]):

    if len(lista_aux) == comprimento:
        return [lista_aux]

    combinada = []
    for i, val in enumerate(lista):
        lista_copia = lista_aux.copy()
        lista_copia.append(val)
        combinada += faz_combinacoes(lista[i+1:], comprimento, lista_copia)
    return combinada


menu('teste.json')
