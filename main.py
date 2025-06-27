from converter_planilha import geraDicionario
import heapq


def dijkstra(G, start, end):
    dist = {v: float('inf') for v in G}
    prev = {v: None for v in G}
    dist[start] = 0
    queue = [(0, start)]

    while queue:
        d, u = heapq.heappop(queue)
        if u == end:
            break
        for v in G.get(u, []):
            alt = d + 1  # peso fixo
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(queue, (alt, v))

    path = []
    u = end
    if prev[u] or u == start:
        while u is not None:
            path.insert(0, u)
            u = prev[u]
    return path, dist[end]


dados, convercao, n = geraDicionario()

G = {}
pessoas = list(dados.keys())
convercao[0] = "start"
convercao[n] = "end"

# Cria conexões internas por pessoa (todos os horarios de uma pessoa são conectados entre si)
for pessoa, horarios in dados.items():
    indices = list(horarios.values())
    for i in indices:
        G[i] = [x for x in indices if x != i]

# Conecta pessoas sucessivas com base em interseção de horarios
for i in range(len(pessoas) - 1):
    atual = dados[pessoas[i]]
    proxima = dados[pessoas[i + 1]]
    intersecao = set(atual.keys()) & set(proxima.keys())
    for horario in intersecao:
        origem = atual[horario]
        destino = proxima[horario]
        G.setdefault(origem, []).append(destino)

# Cria nós de início e fim
start = 0
end = n
G[start] = list(dados[pessoas[0]].values())
G[end] = []
for val in dados[pessoas[-1]].values():
    G.setdefault(val, []).append(end)

# Executa Dijkstra
caminho, custo = dijkstra(G, start, end)
print("Caminho encontrado:", caminho)
print("Custo:", custo)

horarios_comun = []

for i in caminho:
    if convercao[i] not in horarios_comun:
        horarios_comun.append(convercao[i])

print(horarios_comun)