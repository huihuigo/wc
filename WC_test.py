import WC
import unittest


class TestWc(unittest.TestCase):

    def test_count_char(self):
        self.assertEqual(WC.count_char('testchar.c'), 36)
        self.assertEqual(WC.count_char('testword.c'), 44)
        self.assertEqual(WC.count_char('testline.c'), 20)

    def test_count_word(self):
        self.assertEqual(WC.count_word('testchar.c'), 6)
        self.assertEqual(WC.count_word('testword.c'), 8)
        self.assertEqual(WC.count_word('testline.c'), 2)

    def test_count_line(self):
        self.assertEqual(WC.count_line('testchar.c'), 2)
        self.assertEqual(WC.count_line('testword.c'), 4)
        self.assertEqual(WC.count_line('testline.c'), 8)

    def test_count_all(self):
        self.assertEqual(WC.count_all('test.c'), (4,3,4))
        self.assertEqual(WC.count_all('test2.c'), (1,2,1))


if __name__ == '__main__':
    unittest.main()