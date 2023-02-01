import bz2
import pickle

dogs_dict = { 'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16 }

sfile = bz2.BZ2File('smallerfile','w')
pickle.dump(dogs_dict,sfile)


# For python2 to python3
# infile=open(dogs_dict)
# pickle.load(infile,encoding='latin1')
# pickle.load(infile,encoding='bytes')if the object contains Numpy