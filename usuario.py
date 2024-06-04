# Código para definir o usuário

from validacao import validar_documento

class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.logged_in = False

    def fazer_login(self, login, password):
        if '@' in login and '.' in login:
            if login == self.username and password == self.password:
                self.logged_in = True
                print("Login realizado com sucesso!")
            else:
                print("Usuario ou senha incorretos.")
        elif (login.isalnum() or '_' in login) and login.isascii():
            if login == self.username and password == self.password:
                self.logged_in = True
                print("Login realizado com sucesso!")
            else:
                print("Usuario ou senha incorretos.")
        elif validar_documento(login):
            if login == self.username and password == self.password:
                self.logged_in = True
                print("Login realizado com sucesso!")
            else:
                print("Usuario ou senha incorretos.")
        else:
            print("Formato de login invalido.")

    def fazer_logout(self):
        self.logged_in = False
        print("Logout realizado com sucesso!")

    @property
    def esta_logado(self):
        return self.logged_in