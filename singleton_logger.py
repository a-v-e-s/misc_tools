class SingletonLogger(object):


    class __SingletonLogger(object):

        def __init__(self, filename='/var/log/singleton.log'):
            self.filename = filename
        
        def __str__(self):
            return '{0!r} {1}'.format(self, self.filename)

        def _write_log(self, level, msg):
            with open(self.filename, 'a') as log_file:
                log_file.write('[{}] {}\n'.format(level, msg))

        def critical(self, msg, level='CRITICAL'):
            self._write_log(level, msg)

        def error(self, msg, level='ERROR'):
            self._write_log(level, msg)

        def warn(self, msg, level='WARN'):
            self._write_log(level, msg)

        def info(self, msg, level='INFO'):
            self._write_log(level, msg)

        def debug(self, msg, level='DEBUG'):
            self._write_log(level, msg)


    instance = None

    def __new__(cls, filename):
        if not SingletonLogger.instance:
            SingletonLogger.instance = SingletonLogger.__SingletonLogger(filename)

        return SingletonLogger.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)
