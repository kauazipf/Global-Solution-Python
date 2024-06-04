# Código do menu

# Código do menu principal
def menu_principal():
    print("\n--- Menu Principal ---")
    print("1. Cadastrar usuario")
    print("2. Fazer login")
    print("3. Sair")
    opcao = input("Escolha uma opcao: ")
    return opcao

# Código do menu para quando o usuário ja estiver logado
def menu_logado():
    print("\n--- Menu Logado ---")
    print("1. Principais causas da poluição oceanica")
    print("2. Cadastrar um artigo")
    print("3. Artigos Cadastrados")
    print("4. Participantes")
    print("5. Fazer logout")
    opcao = input("Escolha uma opcao: ")
    return opcao
