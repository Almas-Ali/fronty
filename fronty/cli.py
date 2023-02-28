import argparse

from fronty import __version__


def main():
    parser = argparse.ArgumentParser(
        description='Fronty - A frontend web framework', prog='fronty')

    parser.add_argument('--version', action='version',
                        version=f'Fronty {__version__}')
    parser.add_argument('--author', action='store_true',
                        help='show program\'s author name and exit'
                        )

    args = parser.parse_args()

    if args.author:
        print('Md. Almas Ali')
    else:
        parser.print_help()
