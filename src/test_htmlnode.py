import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):

    def test_check_props(self):
        node1 = HTMLNode(
            tag="p",
            value="this is the introduction",
            props={"href": "https://google.com", "somekey": "somevalue"},
        )
        target = ' href="https://google.com" somekey="somevalue"'
        self.assertEqual(target, node1.props_to_html())

    def test_check_single_prop(self):
        node1 = HTMLNode(
            tag="a",
            value="Visit the homepage",
            props={"href": "https://www.google.com"},
        )
        target = ' href="https://www.google.com"'
        self.assertEqual(target, node1.props_to_html())

    def test_check_3_prop(self):
        node1 = HTMLNode(
            tag="a",
            value="Somethin else",
            props={"key1": "value1", "key2": "value2", "key3": "value3"},
        )
        target = ' key1="value1" key2="value2" key3="value3"'
        self.assertEqual(target, node1.props_to_html())

    def test_leaf_to_html_p(self):
        node1 = LeafNode(
            tag= "p",
            value="This is a test paragraph for the test case!"
        )
        self.assertEqual(node1.to_html(), "<p>This is a test paragraph for the test case!</p>")

    def test_leaf_to_html_h1(self):
        node1 = LeafNode(
            tag= "h1",
            value="This is a test heading with level 1 for the test case!"
        )
        self.assertEqual(node1.to_html(), "<h1>This is a test heading with level 1 for the test case!</h1>")

    def test_leaf_to_html_div(self):
        node1 = LeafNode(
            tag= "div",
            value="This is a test div for the test case!"
        )
        self.assertEqual(node1.to_html(), "<div>This is a test div for the test case!</div>")
