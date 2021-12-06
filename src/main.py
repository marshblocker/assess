# Goal: To create a program that checks if the output of a given program is
#       equal to its expected output. This expected output is the past output
#       of the program stored in a txt file.
from sys import argv
from os.path import basename
from os import system

from helpers import *


def build_path() -> tuple[str, str]:

    match len(argv):
        case 1:
            print('No argument given!')
            exit()
        case 2:
            fname = argv[1]
            testpth = ''
        case 3:
            fname = argv[1]
            testpth = ''
            if argv[2] != '.':
                testpth = argv[2]
        case _:
            print('Number of arguments exceed 2!')
            exit()

    fnamecl = rm_ext(fname)  # fname without .py

    fpth = build_fpth(fname)
    testpth = build_testpth(fnamecl, testpth)

    return (fpth, testpth)


def assess(fpth: str, testpth: str) -> bool:

    same: bool = True

    fnamecl: str = rm_ext(basename(fpth))
    fout: str = f'{fnamecl}_out.txt'

    system(f'python {fnamecl}.py > {fout}')  # Log stdout of fname to fout.

    with open(fout) as new_out:
        with open(testpth) as old_out:
            new_out_lst: list[str] = new_out.readlines()
            old_out_lst: list[str] = old_out.readlines()

            if not is_same_line_count(len(new_out_lst), len(old_out_lst)):
                same = False
            else:
                same = check_per_line_if_equal(new_out_lst, old_out_lst, same)

    verify_delete_fout(fout)

    return same


def main_():
    fpth, testpth = build_path()
    assess(fpth, testpth)


