import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node1 = TextNode("This is test text node",TextType.LINK)
        node2 = TextNode("This is test text node",TextType.IMAGE)
        self.assertNotEqual(node1,node2)

    def test_urlnone(self):
        node1 = TextNode("This is test text node",TextType.LINK)
        self.assertIsNone(node1.url)


if __name__ == "__main__":
    unittest.main()
