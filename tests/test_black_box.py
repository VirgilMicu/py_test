import unittest

from src.linear_search import linear_search

v0 = 1.1
v1_1 = [2, 3, 2, 3, 4, 5, 2, 7, 8, 9]
v1_2 = [2, 3, 2, 3, 4, 5]
v2_1 = [4]
v2_2 = [3, 2, 3, 4]
v3 = [3, 2, 3, 4, 5.2]   
v4 = [3, 2, 3, 4, 5]

a1 = 4
a2 = 99
a3 = [2]

class Tests(unittest.TestCase):
    def test_f ():
        assert linear_search(v0, a2) == -1   # intrari: non-vector + intreg 
        assert linear_search(v1_1, a2) == -1 # intrari: vector semnificativ mai mare decat 5 + intreg 
        assert linear_search(v1_2, a2) == -1 # intrari: vector mai mare la limita decat 5 + intreg 
        assert linear_search(v2_1, a2) == -1 # intrari: vector de lungime 1 + intreg 
        assert linear_search(v2_2, a2) == -1 # intrari: vector mai mic la limita decat 5 + intreg 
        assert linear_search(v3, a2) == -1   # intrari: vector care nu contine doar intregi + intreg 
        assert linear_search(v4, a1) == 3    # intrari: valide, cheia este in vector pe pozitia 4 (indice 3)
        assert linear_search(v4, a2) == -1   # intrari: valide, cheia nu este in vector
        assert linear_search(v4, a3) == -1   # intrari: vector de 5 intregi + non-intreg

if __name__ == '__main__':
    unittest.main()
