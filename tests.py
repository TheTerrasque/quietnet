# -*- coding: utf-8 -*-
import unittest
import psk

E = ["test", "This is a long paragraph", 
    "This is some binary data I am testing".encode("zip"),
    "", "testing øæå"
    ]

class TestEncoding(unittest.TestCase):
    def test_encoding(self):
        for x in E:
            data = psk.encode(x)
            self.assertTrue(psk.is_done(data))
            dataBork = data[:-1]
            self.assertTrue(not psk.is_done(dataBork))
            s = psk.decode(data)
            self.assertEqual(x, s)

if __name__ == '__main__':
    unittest.main()
