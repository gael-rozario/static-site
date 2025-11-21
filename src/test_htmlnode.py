import unittest

from htmlnode import HTMLNode


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
