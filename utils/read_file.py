def read_file(path):
    with open(path, "r") as f:
        matriz = []
        linha = f.readlines()

        for i in range(len(linha)):
            matriz.append((linha[i].split()))
    return matriz