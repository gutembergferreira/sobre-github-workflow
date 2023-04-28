# Conjunto de REGEX para validação de entradas.
import re


def validar_email(email):
    regex = r"^[\w-]+(?:\.[\w-]+)*@(?:[\w-]+\.)+[a-zA-Z]{2,}$"
    return re.match(regex, email) is not None
  
def validar_cep(cep):
    regex = r"^\d{5}-?\d{3}$"
    return re.match(regex, cep) is not None
  
def validar_cpf(cpf):
# Remove caracteres não numéricos
    cpf = re.sub(r"[^\d]", "", cpf)

    # Verifica se tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False

    # Calcula os dígitos verificadores
    sum = 0
    for i in range(9):
        sum += int(cpf[i]) * (10 - i)
    remainder = (sum * 10) % 11
    if remainder == 10 or remainder == 11:
        remainder = 0
    if remainder != int(cpf[9]):
        return False
    sum = 0
    for i in range(10):
        sum += int(cpf[i]) * (11 - i)
    remainder = (sum * 10) % 11
    if remainder == 10 or remainder == 11:
        remainder = 0
    if remainder != int(cpf[10]):
        return False

    # CPF válido
    return True
  
def validar_telefone(telefone):
    regex = r"^\(?\d{2}\)?[-.\s]?\d{4,5}[-.\s]?\d{4}$"
    return re.match(regex, telefone) is not None

  
 
  
