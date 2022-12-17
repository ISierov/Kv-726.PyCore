def list_animals(animals):
    return ''.join(list(str(x + 1) + '. ' + animals[x] + '\n' for x in range(len(animals))))
