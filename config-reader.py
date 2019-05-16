import configparser
import argparse
import os

shape = ""
color = ""

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description='Config reader example.')
    arg_parser.add_argument('--color', nargs=1, help='set the color value')
    arg_parser.add_argument('--shape', nargs=1, help='set the shape value')
    arg_parser.add_argument('--file', nargs=1, help='read the configuration from file_name')
    arg_parser.add_argument('--env', action='store_true', help='read the configuration from Environment Variables CONFIG_COLOR and CONFIG_SHAPE')
    arguments = arg_parser.parse_args()

    if arguments.env:
        print('Reading configuration from Environment Variables')
        try:
            color = os.environ['CONFIG_COLOR']
        except:
            print('Error reading CONFIG_COLOR Variable')
        try:
            shape = os.environ['CONFIG_SHAPE']
        except:
            print('Error reading from CONFIG_SHAPE Variable')
        print('"color" = ', color)
        print('"shape" = ', shape)

    if arguments.file:
        filename = arguments.file[0]
        print('Reading configuration from Config File ', filename)
        try:
            config_file = open(filename,"r")
        except:
            print('Error opening Config File ',filename)
        else:
            config = configparser.ConfigParser()
            try:
                config.read_file(config_file)
            except:
                print('Error reading INI data from Config File')
            else:
                if 'DEFAULT' in config:
                    shape = config['DEFAULT']['shape']
                    color = config['DEFAULT']['color']
                    print('"color" = ', color)
                    print('"shape" = ', shape)
                else:
                    print('Missing [DEFAULT] section. No Config read from file')

    if arguments.color:
        color = arguments.color[0]
        print('Configuration from Command Line option --color ', color)

    if arguments.shape:
        shape = arguments.shape[0]
        print('Configuration from Command Line option --shape ', shape)

    if color == "" or shape == "":
        print('Error: "color" and "shape" must be both defined and not empty')
        arg_parser.print_help(file=None)
        exit(1)
    else:
        print('Final configuration is: "color" = ', color, ', "shape" = ',shape)
