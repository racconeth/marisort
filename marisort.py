import sys
import getopt

def main(argv):
    # Default input and output file names
    input_file = 'input.txt'
    output_file = 'output.txt'

    # Read the command-line options
    try:
        opts, args = getopt.getopt(argv, 'hi:o:', ['ifile=', 'ofile='])
    except getopt.GetoptError:
        print('marisort.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    # Process the options -h
    for opt, arg in opts:
        if opt == '-h':
            print('marisort.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ('-i', '--ifile'):
            input_file = arg
        elif opt in ('-o', '--ofile'):
            output_file = arg

    # Open the input file for reading
    with open(input_file, 'r') as f:
        # Read the contents of the file into a string
        contents = f.read()

    # Replace all occurrences of quotation marks and commas with a blank space
    contents = contents.replace('"', '').replace(',', '')

    # Open the output file for writing
    with open(output_file, 'w') as f:
        # Write the modified contents to the output file
        f.write(contents)

if __name__ == '__main__':
    main(sys.argv[1:])
