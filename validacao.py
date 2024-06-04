# Código de validação

# Código para validar a opção de cadastro com documento 
def validar_documento(documento):
    if len(documento) == 14:
        if documento[3] == '.' and documento[7] == '.' and documento[11] == '-':
            return all(c.isdigit() for c in documento[:3] + documento[4:7] + documento[8:11] + documento[12:])
    elif len(documento) == 11:
        return documento.isdigit()
    return False

# Código para validar a senha cadastrada
def validar_senha(password):
    if len(password) < 12:
        return False

    has_digit = any(c.isdigit() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_special = any(c in '!@#$%&*()[]{};,.:/\\|' for c in password)

    return has_digit and has_upper and has_lower and has_special
