from binascii import hexlify
from os import urandom


def _createId():
	return hexlify(urandom(3))
