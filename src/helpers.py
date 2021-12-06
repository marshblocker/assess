from os.path import realpath, splitext, join, isfile
from os import getcwd, remove
from enum import Enum


class TC(Enum):
    GREEN = '\033[92m'
    RED   = '\033[91m'
    ENDC  = '\033[0m'


#-------------------------Helper functions-------------------------------------

def rm_nl(line: str) -> str:
    return line.rstrip('\n')


def rm_ext(file: str) -> str:
    return splitext(file)[0]


def build_fpth(fname: str) -> str:
    fnamecl: str = rm_ext(fname)
    fpth: str = realpath(join(getcwd(), f'{fnamecl}.py'))

    assert(isfile(fpth)), f'fpth = {fpth} is not a real path.'

    return fpth


def build_testpth(fnamecl: str, testpth: str) -> str:
    testpth = realpath(join(testpth, f'{fnamecl}_test.txt'))

    assert(isfile(testpth)), f'testpth = {testpth} is not a real path.'

    return testpth

#------------------------Main functions----------------------------------------

def is_same_line_count(lc_new: int, lc_old: int) -> bool:
    if lc_old == lc_new:
        return True
    else:
        diff = lc_old - lc_new

        if diff > 0:
            if diff == 1:
                print(f'The program outputs {diff} line less compared to the test case.')
            else:
                print(f'The program outputs {diff} lines less compared to the test case.')
        else:
            if diff == -1:
                print(f'The program outputs {-diff} line more compared to the test case.')
            else:
                print(f'The program outputs {-diff} lines more compared to the test case.')

        return False


def check_per_line_if_equal(new_out_lst: list[str], 
                            old_out_lst: list[str],
                            same: bool
                            ) -> bool:
    line: int = 1
    mistakes_count: int = 0

    for new, old in zip(new_out_lst, old_out_lst):
        if new.rstrip() != old.rstrip():
            same = False
            mistakes_count += 1
            print(f'{TC.RED.value}Line {line} wrong!{TC.ENDC.value}')
            print(f'Old: {rm_nl(old)}')
            print(f'New: {rm_nl(new)}')
        else:
            print(f'{TC.GREEN.value}Line {line} correct!{TC.ENDC.value}')

        line += 1

    if same:
        print(f'{TC.GREEN.value}No mistakes. Good job! ^.^{TC.ENDC.value}')
    else:
        print(f'{TC.RED.value}{mistakes_count} mistakes. Time to fix it! \\*v*/{TC.ENDC.value}')

    return same 


def verify_delete_fout(fout: str) -> None:
    clean: str = input(f'Delete the generated {fout} file? [y/n]: ')
    
    if clean.capitalize() != 'N':
        cleaned_fpath: str =  realpath(join(getcwd(), fout))
        assert(isfile(cleaned_fpath)), f'cleaned_fpath = {cleaned_fpath} is not a real path.'
        remove(cleaned_fpath)