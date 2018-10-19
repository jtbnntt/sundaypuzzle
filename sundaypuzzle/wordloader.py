def load_words():
    with open('enable1.txt') as file:
        return [line.strip() for line in file.readlines()]
