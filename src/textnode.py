from htmlnode import LeafNode
from typing import List

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode():
    def __init__(self, text: str, text_type: str, url: str = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value: object) -> bool:
        if self.text == value.text and self.text_type == value.text_type and self.url == value.url:
            return True
        return False

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(textnode) -> LeafNode:

    if textnode.text_type == text_type_text:
        return LeafNode(textnode.text)
    elif textnode.text_type == text_type_bold:
        return LeafNode("b", textnode.text)
    elif textnode.text_type == text_type_italic:
        return LeafNode("i", textnode.text)
    elif textnode.text_type == text_type_code:
        return LeafNode("code", textnode.text)
    elif textnode.text_type == text_type_link:
        return LeafNode("a", textnode.text, {"href": textnode.url})
    elif textnode.text_type == text_type_image:
        return LeafNode("img", "", {"src": textnode.url, "alt": textnode.text})
    else:
        raise ValueError("This text type is not supported")
