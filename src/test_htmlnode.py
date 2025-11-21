import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
        node1 = LeafNode(tag="p", value="This is a test paragraph for the test case!")
        self.assertEqual(
            node1.to_html(), "<p>This is a test paragraph for the test case!</p>"
        )

    def test_leaf_to_html_h1(self):
        node1 = LeafNode(
            tag="h1", value="This is a test heading with level 1 for the test case!"
        )
        self.assertEqual(
            node1.to_html(),
            "<h1>This is a test heading with level 1 for the test case!</h1>",
        )

    def test_leaf_to_html_div(self):
        node1 = LeafNode(tag="div", value="This is a test div for the test case!")
        self.assertEqual(
            node1.to_html(), "<div>This is a test div for the test case!</div>"
        )

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_mixed_children(self):
        p1 = LeafNode("p", "paragraph1")
        p2 = LeafNode("p", "paragraph2")

        h1 = LeafNode("h1", "heading1")
        h2 = LeafNode("h2", "heading2")

        p3 = LeafNode("p", "paragraph3")

        div1 = ParentNode("div", [p1, p2])
        div2 = ParentNode("div", [h1, h2])

        div3 = ParentNode("div", [div1, div2, p3])

        self.assertEqual(
            div3.to_html(),
            "<div><div><p>paragraph1</p><p>paragraph2</p></div><div><h1>heading1</h1><h2>heading2</h2></div><p>paragraph3</p></div>",
        )
