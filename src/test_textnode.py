import unittest
from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("sometest", "italic", "google.com")
        node2 = TextNode("sometest", "italic", "google.com")
        self.assertEqual(node1, node2)

    def test_not_eq(self):
        node1 = TextNode("sometest", "italic", "google.com")
        node2 = TextNode("sometest", "bold", "google.com")
        self.assertNotEqual(node1, node2)

    def test_no_url(self):
        node1 = TextNode("sometest", "italic")
        expected = "TextNode(sometest, italic, None)"
        self.assertEqual(node1.__repr__(), expected)


if __name__ == "__main__":
    unittest.main()
