# Endereço mal formatado
endereco = " Av. Tenente Marques  - Polvilho, Cajamar - SP"

# Transformar endereço em maiúsculo
def F01_TransfMaiusculo(pEnder):
    return pEnder.upper()

# Retirar abreviação de Rua
def F02_AlterarRua(pEnder):
    pEnder = pEnder.replace("R.", " RUA ")
    pEnder = pEnder.replace(" R ", " RUA ")
    return pEnder
# Retirar abreviação de Avenida
def F03_TrocarAvenida(pEnder):
    pEnder = pEnder.replace("AV ", " AVENIDA ")
    pEnder = pEnder.replace("AV. ", " AVENIDA ")
    pEnder = pEnder.replace("AVEN ", " AVENIDA ")
    return pEnder

# Retirar espaços desnecesários
def F04_RemoveEspaco(pEnder):
    pEnder = pEnder.replace("  ", " ")
    pEnder = pEnder.replace("   ", " ")
    return pEnder

# Remover acentuação
def F05_Acentuacao(pEnder):
    pEnder = pEnder.replace("Ã", "A")
    pEnder = pEnder.replace("Â", "A")
    pEnder = pEnder.replace("Õ", "O")
    pEnder = pEnder.replace("Ô", "O")
    pEnder = pEnder.replace("Ó", "O")
    pEnder = pEnder.replace("Ê", "E")
    pEnder = pEnder.replace("É", "E")
    pEnder = pEnder.replace("Í", "I")
    pEnder = pEnder.replace("Ú", "U")
    return pEnder

# Apresentar endereço sem formatação
print("ANTES: ", endereco)

# Chamada de funções
endereco = F01_TransfMaiusculo(endereco)
endereco = F02_AlterarRua(endereco)
endereco = F03_TrocarAvenida(endereco)
endereco = F04_RemoveEspaco(endereco)
endereco = F05_Acentuacao(endereco)
# Apresentar endereço com formatação
print("DEPOIS: ", endereco)