"""
byte.py: Convert an integer to a binary string
Useful teaching tool for learning how binary math works.
Also useful for never needing to learn how binary math works.
"""


def byte(n):
    # Type and Value testing:
	if type(n) != int:
		try:
			n = int(n)
		except ValueError:
			raise TypeError('n must be an integer between 0 and 255')
	if n > 255 or n < 0 or n % 1 != 0:
		raise ValueError('n must be an integer between 0 and 255')
    #
    # Initialize the list:
	byte = ['0', '0', '0', '0', '0', '0', '0', '0']
    #
    # The following is a simple algorithm for turning decimal numbers into binary bytes:
	if n >= 128:
		byte[0] = '1'
		n -= 128
	if n >= 64:
		byte[1] = '1'
		n -= 64
	if n >= 32:
		byte[2] = '1'
		n -= 32
	if n >= 16:
		byte[3] = '1'
		n -= 16
	if n >= 8:
		byte[4] = '1'
		n -= 8
	if n >= 4:
		byte[5] = '1'
		n -= 4
	if n >= 2:
		byte[6] = '1'
		n -= 2
	if n >= 1:
		byte[7] = '1'
		n -= 1
    #
    # If n isn't zero now we messed up...
	if n != 0:
		raise Exception('byte function has been improperly programmed and something went wrong.\nSorry.')
    #
    # Convert the list to a string and return it
	return ''.join(byte)


if __name__ == '__main__':
    from sys import argv
    print(byte(argv[1]))