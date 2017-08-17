# -*- coding: utf-8 -*-

from docopt import docopt

__doc__ = \
    """Parser the air condition remote signal code.
    
    Usage:
        signal_parser.py <file_to_parse> [out_file]
        
    Options:
        -h  --help              Show this screen.
        -v  --version           Show tool version.
    """


def parse_ir_code(file, out_file=None):
    """from the remote raw code file record by lirc::mode2 tool
    :param file: remote raw code file
    :param out_file: save to the target file
    :return: Noting is bast.
    """
    pass


def main():
    args = docopt(__doc__, version="0.1")
    print(args)


if __name__ == '__main__':
    main()
