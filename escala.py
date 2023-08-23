# Criar um dicionário vazio para armazenar as escalas
escalas = {}

# define a escala cromatica. 
notas = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
# define a regra para achar a escala maior e menor 
intervalos_maior = [2, 2, 1, 2, 2, 2, 1] # T T ST T T T ST
intervalos_menor = [2, 1, 2, 2, 1, 2, 2] # T ST T T ST T T

#gera a escala com a primeira nota aplicando a regra de T T ST T T T ST 
def gerar_escala(nota, intervalos):
    inicial = notas.index(nota)
    escala = [nota]
    
    for i in intervalos:
        inicial = (inicial + i) % len(notas)
        escala.append(notas[inicial])
    return " ".join(escala)

# Percorrer as notas e gerar as escalas maiores e menores naturais
for nota in notas:
    # Gerar a escala maior natural e adicionar ao dicionário com a chave "nota maior"
    escala_maior = gerar_escala(nota, intervalos_maior)
    escalas[nota + " MAIOR"] = escala_maior
    # Gerar a escala menor natural e adicionar ao dicionário com a chave "nota menor"
    escala_menor = gerar_escala(nota, intervalos_menor)
    escalas[nota + " MENOR"] = escala_menor
escala = escalas[input('qual a escala voce quer:').upper()]
print(escala)
