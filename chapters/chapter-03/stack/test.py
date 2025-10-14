def search_key(box, path="Main box"):
    """
    Procura a chave dentro de caixas aninhadas
    caixa: pode ser 'chave' ou uma lista de caixas
    path: caminho percorrido até agora
    """
    if box == "key":
        print(f"Key found in {path}!")
        return True
    
    if isinstance(box, list):
        for i, inner_box in enumerate(box, start=1):
            if search_key(inner_box, path + f" -> Box {i}"):
                return True
    return False

main_box = [
    [],
    [[], []],
    [[], ["key"]],
    [[]]
]


# Practical test of the function explainded in the book
print(search_key(main_box))
