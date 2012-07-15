import soupbintcp
import sys

'''
Created on Jul 14, 2012

@author: jon
'''


def main():
    if len(sys.argv) < 2:
        sys.exit('Usage: %s input-file' % sys.argv[0])

    data = file(sys.argv[1], "rb")

    for packet in soupbintcp.parse(data):
        print packet

if __name__ == '__main__':
    main()
