import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_imagetext_to_html(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://media.istockphoto.com/id/89957463/photo/trust.jpg?s=1024x1024&w=is&k=20&c=h8Xi8uevnJDZ3XdjczS-v-4cvyQsyqG10hhYWm9ojW0=")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<img src=\"https://media.istockphoto.com/id/89957463/photo/trust.jpg?s=1024x1024&w=is&k=20&c=h8Xi8uevnJDZ3XdjczS-v-4cvyQsyqG10hhYWm9ojW0=\" alt=\"This is an image\" >")


if __name__ == "__main__":
    unittest.main()
