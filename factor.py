#!/usr/bin/python3

def factor(__n):

    __factorList = []

    if __n > 0 or __n < 0:
        for __i in range(1, abs(int(__n))+1):
            if __n % __i == 0:
                __factorList.append(__i)
    elif __n == 0:
        __factorList.append("Undefined")
    return __factorList

def main():

    import argparse
    from sys import exit

    __parser = None
    __args = None

    __parser = argparse.ArgumentParser()
    __parser.add_argument("number", help="Number to factor", type=int)
    __args = __parser.parse_args()
    print(str(factor(__args.number)))
    exit()

main()
