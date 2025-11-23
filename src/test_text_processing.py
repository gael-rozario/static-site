import unittest

from textnode import TextNode, TextType
from text_processing import split_node_delimiter


class TestSplitNodeDelimiter(unittest.TestCase):

    def test_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        result = split_node_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_bold_delimiter(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        result = split_node_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_italic_delimiter(self):
        node = TextNode("This is *italic* text", TextType.TEXT)
        result = split_node_delimiter([node], "*", TextType.ITALIC)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_multiple_delimiters(self):
        node = TextNode("Code `block1` and `block2` here", TextType.TEXT)
        result = split_node_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("Code ", TextType.TEXT),
            TextNode("block1", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("block2", TextType.CODE),
            TextNode(" here", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_no_delimiter(self):
        node = TextNode("This is plain text", TextType.TEXT)
        result = split_node_delimiter([node], "`", TextType.CODE)
        expected = [TextNode("This is plain text", TextType.TEXT)]
        self.assertEqual(result, expected)

    def test_unmatched_delimiter(self):
        node = TextNode("This has unmatched `delimiter", TextType.TEXT)
        with self.assertRaises(ValueError) as context:
            split_node_delimiter([node], "`", TextType.CODE)
        self.assertIn("Invalid markdown: unmatched delimiter", str(context.exception))

    def test_non_text_node_passthrough(self):
        node = TextNode("Already bold", TextType.BOLD)
        result = split_node_delimiter([node], "`", TextType.CODE)
        expected = [TextNode("Already bold", TextType.BOLD)]
        self.assertEqual(result, expected)

    def test_multiple_nodes(self):
        nodes = [
            TextNode("First `code` node", TextType.TEXT),
            TextNode("Second `code` node", TextType.TEXT)
        ]
        result = split_node_delimiter(nodes, "`", TextType.CODE)
        expected = [
            TextNode("First ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" node", TextType.TEXT),
            TextNode("Second ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" node", TextType.TEXT)
        ]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
