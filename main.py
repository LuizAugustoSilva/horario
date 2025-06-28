from converter_planilha import geraDicionario
from itertools import combinations

# Carrega os dados
nomes, dados, convercao, n = geraDicionario()

# Inverte os dados: horário -> pessoas que têm disponível
horarios_disponiveis = {}
for pessoa, horarios in dados.items():
    for horario_str, idx in horarios.items():
        if horario_str not in horarios_disponiveis:
            horarios_disponiveis[horario_str] = set()
        horarios_disponiveis[horario_str].add(pessoa)

# Total de pessoas no grupo
total_pessoas = set(dados.keys())

# Função para verificar se um conjunto de horários cobre todas as pessoas
def cobre_todos(horarios):
    pessoas_cobertas = set()
    for h in horarios:
        pessoas_cobertas.update(horarios_disponiveis[h])
    return pessoas_cobertas == total_pessoas

# Lista de todos os horários disponíveis
todos_horarios = list(horarios_disponiveis.keys())

# Coleta todas as combinações válidas de até 3 horários que cubram todos
combinacoes_validas = []
for r in range(1, 3):  # 1, 2 ou 3 horários
    for combinacao in combinations(todos_horarios, r):
        if cobre_todos(combinacao):
            combinacoes_validas.append(combinacao)

# Exibe os resultados
print(f"\nTotal de combinações encontradas: {len(combinacoes_validas)}\n")
for i, c in enumerate(combinacoes_validas, 1):
    print(f"Opção {i}:")
    for horario in c:
        print(f" - {horario}")
    print()
