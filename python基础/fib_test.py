import unittest



"""递归函数 """      
def recur(a):
   if a == 1 or a == 2:
       return 1
   else:
       return(recur(a-1) + recur(a-2))
       
"""输出数组"""    
def fib(n):
    if n <= 0:
        return False
    else:
        fibs = []
        for i in range(1, n + 1):
            fibs.append(recur(i))
        return fibs


class FibTest(unittest.TestCase):
    def test_generate_5_fibs(self):
        self.assertEqual(fib(5), [1, 1, 2, 3, 5])

    def test_generate_10_fibs(self):
        self.assertEqual(fib(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_generate_negative_number_fibs(self):
        self.assertEqual(fib(-1), False)

    def test_generate_0_number_fibs(self):
        self.assertEqual(fib(0), False)

    def test_generate_1_number_fibs(self):
        self.assertEqual(fib(1), [1])

    def test_generate_2_number_fibs(self):
        self.assertEqual(fib(2), [1, 1])


if __name__ == '__main__':
    unittest.main()
