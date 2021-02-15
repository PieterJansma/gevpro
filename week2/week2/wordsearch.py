import json
import argparse
import sys


def solve(puzzle, words):
    """loops through file make a lng string to look for words,
    both left to right and top to bottom are searched for words"""
    with open(words) as inp:
        word_docu = json.load(inp)
        word_collect = {word.upper() for word in word_docu["words"]}

    with open(puzzle) as puzzle:
        letter_str = ''
        word_lst = []
        letter_verti = ''

        for line in puzzle:
            puzzle_str = line.rstrip() + ' '
            word_lst.append(puzzle_str)
            letter_str = letter_str + puzzle_str

        for i in range(len(word_lst)):
            letter_verti = letter_verti + ' '
            for word in word_lst:
                letter_verti = letter_verti + word[i]
        letter_str = letter_str + letter_verti

        words_puzzle = []

    for word in word_collect:
        if word in letter_str:
            words_puzzle.append(word)

    return words_puzzle


def main(argv):
    words = 'words.json'
    if len(sys.argv) == 3:
        words = argv[2]

    puzzle = argv[1]
    print(solve(puzzle, words))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("puzzlefile", type=argparse.FileType('r'),
                        help="Enter your puzzle file")
    args = parser.parse_args()
    main(sys.argv)
