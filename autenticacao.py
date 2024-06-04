# Código de autenticação

from usuario import Usuario
from validacao import validar_documento

# Código para autenticar o usuário no login
def fazer_login(usuario, login, password):
    if '@' in login and '.' in login:
        if login == usuario.username and password == usuario.password:
            usuario.logged_in = True
            print("Login realizado com sucesso!")
        else:
            print("Usuário ou senha incorretos.")
    elif (login.isalnum() or '_' in login) and login.isascii():
        if login == usuario.username and password == usuario.password:
            usuario.logged_in = True
            print("Login realizado com sucesso!")
        else:
            print("Usuário ou senha incorretos.")
    elif validar_documento(login):
        if login == usuario.username and password == usuario.password:
            usuario.logged_in = True
            print("Login realizado com sucesso!")
        else:
            print("Usuário ou senha incorretos.")
    else:
        print("Formato de login inválido.")