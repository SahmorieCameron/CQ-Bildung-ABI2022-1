import argparse

parser = argparse.ArgumentParser(description="Examples for the usage of argparse")
# Positional arguement. By using just a string, the module knows that THIS is a positional argument.
# if it doesn't start with a minus, it is counted as a positional argument. Must have something within the quotation marks.
# nargs
parser.add_argument(
    "integers", metavar="N", type=int, nargs="+", help="an integer for the accumulator"
)
parser.add_argument("-p", "--print", action="store_true", help="print out the result")
parser.add_argument(
    "-x", "--xvalue", action="store", type=int, default=0, help="The first value"
)
parser.add_argument(
    "-y", "--yvalue", action="store", type=int, default=0, help="The second value"
)
args = parser.parse_args()

sum1 = 0
for elem in args.integers:
    sum1 += elem

if args.print:
    print(sum1)
    print(args.xvalue + args.yvalue)
