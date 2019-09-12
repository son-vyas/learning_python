import argparse
parser = argparse.ArgumentParser()
parser.add_argument('name', default=True)
parser.add_argument('hold', action='store', nargs='+')
name_group = parser.add_mutually_exclusive_group()
