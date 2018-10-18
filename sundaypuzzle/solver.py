import sundaypuzzle.wordloader as wordloader

from argparse import ArgumentParser


def main(name_length):
    words = wordloader.load_words()
    word_map = {}

    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in word_map:
            word_map[sorted_word] = []
        word_map[sorted_word].append(word)

    with open('people.txt') as people_file:
        people = [person.strip() for person in people_file.readlines()]

    for person in people:
        last_name = person.split()[-1]
        if len(last_name) == name_length and 'e' in last_name:
            converted_last_name = ''.join(sorted([letter for letter in last_name.lower() if letter != 'e'] + ['f', 'i']))
            if converted_last_name in word_map:
                for word in word_map[converted_last_name]:
                    print('{} -> {}'.format(person, word))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--name-length', type=int, default=6)
    args = parser.parse_args()
    main(args.name_length)