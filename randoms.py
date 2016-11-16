import os
import sys
import random

#Random bytes
bytes = os.urandom(32)

#Random int
csprng = random.SystemRandom()
rand_int = csprng.randint(0, sys.maxsize)

#Output
print(bytes)
print(rand_int)