from pytablewriter import MarkdownTableWriter
import sys
import getopt
import json


def main(argv):

    inputfile = ''
    outputfile = ''
    tablename = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:n:", ["ifile=", "ofile=", "tname="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile> -n <tablename>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile> -n <tablename>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-n", "--tname"):
            tablename = arg
    print('Input file is: ', inputfile)
    print('Output file is: ', outputfile)
    print('Table name is: ', tablename)

    with open(inputfile, 'r') as f:
        array = json.load(f)

    data = []
    for x in range(len(array['rows'])):
        row = []
        for el in array['headings']:
            row.append(array['rows'][x][el])
        data.append(row)

    writer = MarkdownTableWriter()
    writer.table_name = tablename
    writer.headers = array['headings']
    writer.value_matrix = data
    writer.margin = 1  # add a whitespace for both sides of each cell

    writer.write_table()


if __name__ == "__main__":
    main(sys.argv[1:])
