import argparse
parser = argparse.ArgumentParser()
parser.add_argument('name', default=True)
parser.add_argument('hold', action='store', nargs='+')
name_group = parser.add_mutually_exclusive_group()
name_group.add_argument('--firstname', action='store_true',
                        help='print first name using argparse')
name_group.add_argument('--lastname', action='store_true',
                        help="print last name using argparse")
args = parser.parse_args()
my_string = ' '.join(parser.parse_args().hold)
if args.firstname:
    print(args.hold[0])
elif args.lastname:
    print(args.hold[1])
else:
    print(my_string)
