import unittest
from block_markdown import markdown_to_blocks


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):

        doc = """This is **bolded** paragraph

                    This is another paragraph with *italic* text and `code` here
                    This is the same paragraph on a new line

                    * This is a list
                    * with items
                    """
        blocks = markdown_to_blocks(doc)
        expected = ['This is **bolded** paragraph', 'This is another paragraph with *italic* text and `code` here\n                    This is the same paragraph on a new line',
                    '* This is a list\n                    * with items']
        self.assertEqual(blocks, expected)
