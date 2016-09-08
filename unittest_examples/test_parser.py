import unittest
import parser

class TestParser(unittest.TestCase):
 
    def test_00_parse_digit(self):
        i = parser.parse("1")
        assert type(i) is int
        assert i == 1
        for i in range(0,10):
            assert parser.parse(str(i)) == i

    def test_01_parse_integer(self):
        assert parser.parse("123") == 123

    def test_02_parse_float(self):
        assert parser.parse("1.23") == 1.23

if __name__ == '__main__':
    unittest.main(verbosity = 2)