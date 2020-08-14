import unittest

class Rect:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def intersect(self, rect: 'Rect') -> bool:
        if (abs(self.x - rect.x) > self.width/2 + rect.width/2 or
            abs(self.y - rect.y) > self.height/2 + rect.height/2):
            ##print('不相交')
            return True
        else:
            ##print('相交')
            return False


class RectTest(unittest.TestCase):
    def test_intersect_for_crossing_rects(self):
        self.assertFalse(Rect(1, 1, 1, 1).intersect(Rect(1, 1, 0.5, 0.5)))
 
    def test_intersect_for_crossing_rects_1(self):
        self.assertTrue(Rect(3, 3, 1, 1).intersect(Rect(1, 1, 0.5, 0.5)))
        
    def test_intersect_for_crossing_rects_2(self):
        self.assertTrue(Rect(3, 4, 1, 1).intersect(Rect(1, 1, 6, 0.5)))
        
    def test_intersect_for_crossing_rects_3(self):
        self.assertFalse(Rect(3, 4, 1, 1).intersect(Rect(1, 1, 6, 6)))

if __name__ == '__main__':
    unittest.main()
