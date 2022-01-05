import time
import threading
import _thread
import sys


def exit_after(s):
    """ decorator function to exit decorated function after s seconds: """
    
    def quit_function(f_name):
        """ kill main thread, informing user that it timed out. """
        print(f'{f_name} took too long.', file=sys.stderr)
        sys.stderr.flush()
        _thread.interrupt_main()
    
    def outer(fn):
    
        def inner(*args, **kwargs):
            timer = threading.Timer(s, quit_function, args=[fn.__name__])
            timer.start()
            try:
                result = fn(*args, **kwargs)
            finally:
                timer.cancel()
    
            return result
    
        return inner
    
    return outer


def timer(f):

    def wrapped_f(*args, **kwargs):

        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print('Time Elapsed:\t'+str(end-start)+' seconds')
        
        return result
    
    return wrapped_f


class recursive_timer:

    def __init__(self, f):
        self.f = f
        self.active = False
    
    def __call__(self, *args, **kwargs):
        
        if self.active:
            return self.f(*args, **kwargs)
        
        try:
            self.active = True
            start = time.perf_counter()
            val = self.f(*args, **kwargs)
            elapsed = time.perf_counter() - start
            print(f'Elapsed time:\t{elapsed} seconds')
            return val
        
        finally:
            self.active = False