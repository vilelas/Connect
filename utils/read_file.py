def read_file(file_path):
    # Abre o arquivo em modo de leitura
    with open(file_path, "r") as f:
        # Inicializa a matriz como uma lista vazia
        matrix = []

        # Lê todas as linhas do arquivo e armazena em uma lista
        lines = f.readlines()

        # Percorre cada linha da lista
        for line in lines:
            # Divide a linha em uma lista de valores separados por espaços
            values = line.split()

            # Adiciona a lista de valores à matriz
            matrix.append(values)

    # Retorna a matriz
    return matrix
