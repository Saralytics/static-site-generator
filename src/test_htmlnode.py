import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_node_create(self):
        node = HTMLNode(tag="p", value="this is a paragraph")
        expected = """HTMLNode(p, this is a paragraph, None, None). Props are None"""
        self.assertEqual(node.__repr__(), expected)

    def test_props_to_html(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(tag="a", value="link", props=props)
        actual = node.props_to_html()
        expected = ' href="https://www.google.com" target="_blank"'

        self.assertEqual(actual, expected)


class TestLeafNode(unittest.TestCase):
    def test_node_create(self):
        node = LeafNode(tag="p", value="this is a paragraph")
        expected = """HTMLNode(p, this is a paragraph, None). Props are None"""
        self.assertEqual(node.__repr__(), expected)

    def test_node_create_no_value(self):
        with self.assertRaises(TypeError):
            LeafNode(tag="p")

    def to_html_no_attr(self):
        node = LeafNode(tag="p", value="this is a paragraph")
        expected = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), expected)

    def to_html_with_attr(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected = '<a href="https: // www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected)

    def to_html_no_tag(self):
        node = LeafNode("I'm a plain text!")
        expected = "I'm a plain text!"
        self.assertEqual(node.to_html(), expected)


# <p>This is a paragraph of text.</p>
# <a href="https://www.google.com">Click me!</a>

if __name__ == "__main__":
    unittest.main()
