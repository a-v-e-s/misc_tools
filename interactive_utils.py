"""
Stuff I frequently use in interactive python sessions

"""


import builtins
import os
import random
import time
from dataclasses import dataclass


# Pathological test case input generators:
pathological_numbers = lambda minimum, maximum, length: [random.randint(minimum, maximum) for _ in range(length)]
pathological_values = lambda values, length: [random.choice(values) for _ in range(length)]


def timer(func, *args, **kwargs):
	""" A basic timer function """

	start = time.time()
	ret = func(*args, **kwargs)
	print(f'{time.time() - start} seconds elapsed.')

	return ret


@dataclass
class Constants:
	""" Contains useful values. """

	home = os.getenv('HOME')

	@staticmethod
	def exceptions():
		""" Return a list of all builtin exceptions. """
		
		excs = list()
		
		for name in dir(builtins):
			try:
				if issubclass(getattr(builtins, name), Exception):
					excs.append(name)
			except TypeError:
				pass
		
		return excs