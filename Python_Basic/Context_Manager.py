#to open a file
with open('note.txt','w') as file:#with statement is a context manager to make sure to correctly close the file again even if there are exception
    file.write('some todo....')

#the full code of with
file = open('note.txt','w')
try:
    file.write('some todo....')
finally:
    file.close()#close is to get resource freed up

#with statement for lock
from threading import Lock
lock = Lock()

lock.acquire()
#...to do sth safely...
lock.release()#without this there will be a dead lock and the program is not gonna continue

"""
#better way
with lock:
    #...to do sth safely...
    
"""
"""#implement a context manager for classes
class ManagedFile:
    def __init__(self,filename):
        self.filename =filename
    def __enter__(self):
        print('enter')
        self.file = open(self.filename,'w')
        return self.file
    
    def __exit__(self,exc_type,exc_value,exc_traceback):
        if self.file:
            self.file.close()
        #to handle exception
        if exc_type is not None:
            print('exception has been handle')
        print('exc:',exc_type,exc_value)
        print('exit')
        return True#to not raise exception

#use with statement
with ManagedFile('note.txt') as file:
    print('do some stuff..')
    file.write('some todo....')
    file.somemethod()#to raise excption
print('continuing')        """
#to implement this  with functions
from contextlib import contextmanager
@contextmanager
def open_managed_file(filename):
    f = open(filename,'w')
    try:
        yield f
    finally:
        f.close()

with open_managed_file('notes.txt') as f:
    f.write('some todo....')