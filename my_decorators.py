import time


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