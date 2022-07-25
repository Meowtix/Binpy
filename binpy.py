#!/usr/bin/python3

import sys, getopt

def error_out(severity):
    print('Exit code: ', severity)
    print(sys.argv[0], '-i <binary_number> -o <type_of_conversion>')
    print('For more help, type: \n', sys.argv[0], '-h')
    sys.exit(severity)


def is_binary(number):
    for n in number:
        if n not in ('0', '1'):
            return False
    return True


def to_hex(binary):
    bin_to_hex_map = {
        '0000': '0',
        '0001': '1',
        '0010': '2',
        '0011': '3',
        '0100': '4',
        '0101': '5',
        '0110': '6',
        '0111': '7',
        '1000': '8',
        '1001': '9',
        '1010': 'A',
        '1011': 'B',
        '1100': 'C',
        '1101': 'D',
        '1110': 'E',
        '1111': 'F'
    }

    hexa = ''
    binary_chunks = [binary[i:i+4] for i in range(0, len(binary), 4)]
    for chunk in binary_chunks:
        if len(chunk) < 4:
            missing = '0' * (4 - len(chunk))
            hexa += bin_to_hex_map[missing + chunk]
        else:
            hexa += bin_to_hex_map[chunk]

    return hexa


def to_decimal(binary):
    nums = list(binary)
    result = 0
    for i, num in enumerate(nums):
        result += int(num) * pow(2, len(nums) - i - 1)
    
    return result


def convert(binary, convert_to):
    convert_args = ('decimal', 'hexadecimal', 'dec', 'hex')
    if convert_to.lower() not in convert_args or not is_binary(binary):
        error_out(1)
    print(binary, ' --> ', 'HEX(16)' if convert_to.lower() in ('hex', 'hexadecimal') else 'DEC(10)')

    if convert_to.lower() in ('dec', 'decimal'):
        print(to_decimal(binary))
    elif convert_to.lower() in ('hex', 'hexadecimal'):
        print(to_hex(binary))


def main(argv):
    binary = ''
    convert_to = ''
    try:
        opts, args = getopt.getopt(argv[1:], 'hi:o:', ['--help', '--input', '--output'])
    except getopt.GetoptError():
        error_out(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(argv[0].capitalize(), '-- Convert from binary to decimal or hexadecimal')
            print('Usage:')
            print('\t', argv[0], '-i <binary_number> -o <type_of_conversion>')
            print('\t -i, --input \t\t Type in a number in binary format')
            print('\t -o, --output \t\t Type of conversion can be "decimal or dec, hexadecimal or hex"')
            print('\n')
            print('Exit status:')
            print('0: OK')
            print('1: Invalid arguments or options')
            print('2: Severe')
            sys.exit(0)
        elif opt in ('-i', '--input'):
            binary = arg
        elif opt in ('-o', '--output'):
            convert_to = arg
        else:
            error_out(1)

    convert(binary, convert_to)


if __name__ == "__main__":
    main(sys.argv)