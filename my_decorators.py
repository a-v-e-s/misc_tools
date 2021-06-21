import time


def timer(f):

    def wrapped_f(*args, **kwargs):

        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print('Time Elapsed:\t'+str(end-start)+' seconds')
        
        return result
    
    return wrapped_f
