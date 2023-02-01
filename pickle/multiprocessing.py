import pathos.multiprocessing as mp
from math import cos

p = mp.Pool(2)

p.map(lambda x:x**2, range(10))