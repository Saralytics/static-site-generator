from typing import List
import re
from htmlnode import ParentNode, LeafNode
block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ul = "unordered_list"
block_type_li = "ordered_list"


def markdown_to_blocks(markdown: str) -> List[str]:
    pattern = r"\n\s*\n"
    blocks = []
    # split the markdown string by newline
    # for each part, remove leading or trailing whitespaces
    # of the part is empty, skip
    # append to resut list
    parts = re.split(pattern, markdown)
    parts = [part.strip() for part in parts if part.strip()]
    blocks.extend(parts)

    return blocks


def markdown_to_html(blocks: List[str]) -> ParentNode:
    tag = "div"
    children = []
    for block in blocks:
        block_html = block_to_html_node(block)
        children.append(block_html)

    return ParentNode(tag, children)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_li:
        return li_to_html_node(block)
    if block_type == block_type_ul:
        return ul_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    raise ValueError("Invalid block type")


def block_to_block_type(block: str) -> str:
    # if block start with 1-6 # characters, followed by a space, then heading block

    # if block start with 3 backticks and end with 3 backticks, then code block
    # if each line start with >  it's a quote block (need to find all consective lines that start with >)
    # if each line start with * or - , it's unordered list
    # Every line in an ordered list block must start with a number followed by a . character and a space. The number must start at 1 and increment by 1 for each line.
    # If none of the above conditions are met, the block is a normal paragraph.
    lines = block.split("\n")

    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ul
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ul
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_li
    return block_type_paragraph


def paragraph_to_html_node(block):
    tag = "p"
    value = block
    return LeafNode(tag, value)


def heading_to_html_node():
    pass


def code_to_html_node():
    pass


def block_type_olist():
    pass


def li_to_html_node():
    pass


def ul_to_html_node():
    pass


def quote_to_html_node():
    pass
