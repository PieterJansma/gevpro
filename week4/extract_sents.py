import gzip
import re
import sys


def tokenizer(text):
    """This function strip all unnecessary strings,
    and return a tokenised list of lines"""

    lines = []

    s = re.compile('[^ ]...*?[A-Z]*[a-z][áéúíó]*[.?!][.\']*')
    with gzip.open(text, 'rt') as file:
        for line in file:
            line = line.rstrip()
            string_find = s.findall(line)
            lines.append(string_find)
            all = [item for sublist in lines for item in sublist]
    final_list = []
    for line in all:
        r = re.sub('(?<=[^ ])(?=[.,:;!?"\'])|(?<=[.,!?:;"\'])'
                   '(?=[^ ])', r' ', line)
        final_list.append(r)
    return final_list


def main():
    text = str(sys.argv[1])
    token_text = '\n'.join(tokenizer(text))
    print(token_text.strip(' '))


if __name__ == '__main__':
    main()
