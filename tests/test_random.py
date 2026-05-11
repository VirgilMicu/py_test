import unittest
from scr.linear_search import linear_search
import random as ra

def oracol (vect, key):
    try: 
        i = vect.index(key)
    except:
        i = -1 
    return i   

ra.seed(99)

class Tests(unittest.TestCase):
    def test_linear_search (self):
        for _ in range (100):
            lst =  list(int(ra.random()*20)-10 for k in range(5))
            v = int(ra.random()*20)-10
            assert linear_search(lst, v) == oracol(lst, v)  

if __name__ == '__main__':
    unittest.main()
