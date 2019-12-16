import os
import filecmp
import shutil

def is_same(dir1, dir2):
    """
    Compare two directory trees content.
    Return False if they differ, True is they are the same.
    """
    compared = filecmp.dircmp(dir1, dir2)
    if (compared.left_only or compared.right_only or compared.diff_files
        or compared.funny_files):
        print(f'Same files: {compared.same_files}')
        print('Diff in files')
        print(f'Present in left only: {compared.left_only}')
        print(f'Present in right only: {compared.right_only}')
        print(f'Differ in file: {compared.diff_files}')
        return False
    for subdir in compared.common_dirs:
        if not is_same(os.path.join(dir1, subdir), os.path.join(dir2, subdir)):
            return False
    return True 


def replace_mkdir(outputdir):
    if os.path.exists(outputdir):
        shutil.rmtree(outputdir, ignore_errors=False, onerror=None)
    os.makedirs(outputdir, exist_ok=True)