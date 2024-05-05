from textnode import (TextNode,
                      text_type_text,
                      text_type_code,
                      text_type_bold,
                      text_type_image,
                      text_type_link)
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link
import unittest


class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_length(self):
        oldnode = TextNode(
            "This is text with a `code block` word", text_type_text)

        new_nodes = split_nodes_delimiter([oldnode], "`", text_type_code)
        self.assertEqual(len(new_nodes), 3)

    def test_split_multiple_nodes(self):
        oldnodes = [TextNode(
            "This is text with a `code block` word", text_type_text),
            TextNode(
            "This is text with a `bold` word", text_type_text)
        ]

        new_nodes = split_nodes_delimiter(oldnodes, "`", text_type_code)
        self.assertEqual(len(new_nodes), 6)

    def test_split_nodes_bold(self):
        oldnodes = [TextNode(
            "This is text with a **hightlight** word", text_type_text),
        ]

        new_nodes = split_nodes_delimiter(oldnodes, "**", text_type_bold)
        expected = [
            TextNode("This is text with a ", text_type_text),
            TextNode("hightlight", text_type_bold),
            TextNode(" word", text_type_text),
        ]
        self.assertEqual(new_nodes, expected)

    # test edgec cases
    # text node is empty
    # text node doesn't match text type
    # open delimiters


class TestLinkExtractor(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        actual = extract_markdown_images(text)
        expected = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                    ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
        self.assertEqual(actual, expected)

    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        actual = extract_markdown_links(text)
        expected = [("link", "https://www.example.com"),
                    ("another", "https://www.example.com/another")]
        self.assertEqual(actual, expected)

    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])

        expected = [
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_image,
                     "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
            TextNode(
                "second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
            ),
        ]

        self.assertEqual(new_nodes, expected)

    def test_split_nodes_image_2(self):
        node = TextNode(
            " and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)", text_type_text, None)
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode(" and an ", text_type_text),
            TextNode("image", text_type_image,
                     "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and a [link](https://boot.dev)", text_type_text),

        ]

        self.assertEqual(new_nodes, expected)
        print(new_nodes)

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)",
            text_type_text,
        )
        new_nodes = split_nodes_link([node])

        expected = [
            TextNode("This is text with a ", text_type_text),
            TextNode("link", text_type_link,
                     "https://www.example.com"),
            TextNode(" and ", text_type_text),
            TextNode(
                "another", text_type_link, "https://www.example.com/another"
            ),
        ]

        self.assertEqual(new_nodes, expected)


if __name__ == "__main__":
    unittest.main()
