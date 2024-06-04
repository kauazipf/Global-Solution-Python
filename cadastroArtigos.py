# Definindo uma lista para armazenar os artigos cadastrados
artigos = []

# Função para cadastrar um novo artigo
def cadastrar_artigos():
    artigo = {}
    artigo['titulo'] = input("Digite o titulo do artigo: ")
    artigo['subtitulo'] = input("Digite o subtitulo do artigo: ")
    artigo['texto'] = input("Digite o seu artigo: ")
    
    artigos.append(artigo)
    print("Artigo cadastrado com sucesso!\n")

# Função para exibir todos os artigos cadastrados
def exibir_artigos():
    if len(artigos) == 0:
        print("Nenhum carro cadastrado.\n")
    else:
        for i, artigo in enumerate(artigos):
            print(f"Artigo {i+1}:")
            for chave, valor in artigo.items():
                print(f"{chave.capitalize()}: {valor}")
            print("")