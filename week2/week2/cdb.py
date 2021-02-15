import xml.etree.ElementTree as ET


def get_adjectives(file):
    """Loops through xml file and looks for xml attribute,
    if its an adjective it returns the word"""
    return {xml.attrib['form'] for xml in file
            if 'ADJ' == xml.attrib['pos']}


def main():
    file = 'cdb-sample.xml'
    tree = ET.parse(file)
    infile = tree.getroot()
    print(len(get_adjectives(infile)), get_adjectives(infile))


if __name__ == '__main__':
    main()
