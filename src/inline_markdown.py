import re
from typing import List, Tuple
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image, text_type_link
)


def split_nodes_delimiter(old_nodes: "List[TextNode]", delimiter: str, text_type: str) -> "List[TextNode]":
    new_nodes = []

    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        splits = node.text.split(delimiter)
        if len(splits) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")

        split_nodes = []
        for i in range(len(splits)):
            if splits[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(splits[i], text_type_text))
            else:
                split_nodes.append(TextNode(splits[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text: str) -> List[Tuple[str, str]]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text: str) -> List[Tuple[str, str]]:
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes: list):
    new_nodes = []
    for old_node in old_nodes:
        # case when old node is empty -> skip and continue
        if old_node.url == "":
            new_nodes.append(old_node)
        if old_node.text == "":
            continue

        split_pattern = r".*?!\[.*?\]\(.*?\)"
        splits = re.findall(split_pattern, old_node.text)
        for part in splits:
            text = [i for i in re.split(
                r"!\[.*?\]\(.*?\)", part) if i != ""][0]

            new_nodes.append(TextNode(text, text_type_text))
            alt_text, link = extract_markdown_images(part)[0]
            new_nodes.append(
                TextNode(alt_text, text_type_image, link))

        remaining = re.split(
            split_pattern, old_node.text)
        remaining = [i for i in remaining if i != ""]
        if remaining:
            new_nodes.append(
                TextNode(remaining[0], text_type_text))
        return new_nodes


def split_nodes_link(old_nodes: list):
    new_nodes = []
    for old_node in old_nodes:
        # case when old node is empty -> skip and continue
        if old_node.url == "":
            new_nodes.append(old_node)
        if old_node.text == "":
            continue

        split_pattern = r".*?\[.*?\]\(.*?\)"
        splits = re.findall(split_pattern, old_node.text)
        for part in splits:
            text = [i for i in re.split(
                r"\[.*?\]\(.*?\)", part) if i != ""][0]

            new_nodes.append(TextNode(text, text_type_text))
            alt_text, link = extract_markdown_links(part)[0]
            new_nodes.append(
                TextNode(alt_text, text_type_link, link))
        remaining = re.split(
            split_pattern, old_node.text)
        remaining = [i for i in remaining if i != ""]
        if remaining:
            new_nodes.append(
                TextNode(remaining[0], text_type_text))
        return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    # nodes = split_nodes_link(nodes)
    return nodes
