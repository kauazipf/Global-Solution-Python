from usuario import Usuario
from validacao import validar_senha, validar_documento

# Código para o usuario se cadastrar
def cadastrar_usuario():
    while True:
        print("\nO login deve ser cadastrado com os seguintes critérios: ")
        print("\tNome de usuário - Deve conter pelo menos 8 digitos!")
        print("\tEmail - Deve conter @ e . para cadastrar um email!")
        print("\tDocumento - CPF (14 Digitos) RG (11 Digitos) ambos usando (. e -)")
        username = input("Cadastre um login: ")

        print("\nA senha deve ser cadastrado com os seguintes critérios: ")
        print("\tDeve conter pelo menos 8 digitos!")
        print("\tDeve conter todas as seguintes opções!")  
        print("\t(Letras maiusculas, Letras minusculas, Números e Caracteres especiais)")       
        password = input("Cadastre uma senha: ")

        if validar_senha(password):
            return Usuario(username, password)
        else:
            print("A senha nao atende aos criterios minimos.")