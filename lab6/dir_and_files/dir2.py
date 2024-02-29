fp = open('dir2.py', 'a+')
print("hello world1", file=fp)
import os
print('Exist:', os.access('lab6\dir2.py', os.F_OK))
print('Readable:', os.access('lab6\dir2.py', os.R_OK))
print('Writable:', os.access('lab6\dir2.py', os.W_OK))
print('Executable:', os.access('lab6\dir2.py', os.X_OK))