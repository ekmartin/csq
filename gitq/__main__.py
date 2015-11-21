import sys
import gitq.cli


def main(args=None):
    gitq.cli.main(args=args)

if __name__ == '__main__':
    main(sys.argv[1:])
