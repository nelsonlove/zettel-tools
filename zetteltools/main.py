import argparse
import subprocess
import sys


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    # create the top-level parser
    parser = argparse.ArgumentParser(description='CLI tools for use with The Archive.app.')
    parser.add_argument('query',
                        nargs='*',
                        help='Query to pass to The Archive.app')
    parser.add_argument('-m', '--match',
                        action='store_true',
                        help='Find the best match and display it')

    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    if args.match:
        url_keyword = 'match'
    else:
        url_keyword = 'search'

    activate_command = 'tell application "The Archive" to activate'
    subprocess.run(['osascript', '-e', activate_command])

    url = 'thearchive://%s/%s' % (url_keyword, ' '.join(args.query))
    subprocess.run(['open', url])


if __name__ == "__main__":
    main()
