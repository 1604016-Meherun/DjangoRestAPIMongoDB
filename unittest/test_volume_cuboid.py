import unittest
import volume_cuboid

#def cuboid_volume(l):
 #   if type(l) not in [int,float]:
#        raise TypeError('The length of cuboid can only be a valid integer or a float')
 #   return l*l*l

class TestCuboid(unittest.TestCase):
    def test_volume(self):
        self.assertAlmostEqual(volume_cuboid.cuboid_volume(2),8)
        self.assertAlmostEqual(volume_cuboid.cuboid_volume(1),1)
        self.assertAlmostEqual(volume_cuboid.cuboid_volume(0),0)
        #self.assertAlmostEqual(volume_cuboid.cuboid_volume(5.5),166.375)
    def test_input_value(self):
        self.assertRaises(TypeError, volume_cuboid.cuboid_volume, True)