from enum import Enum

from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:

    # def __init__(self, text, text_type, url=None):
    #
    # def __eq__(self, compared):

    def __init__(self, text, text_type, url=None) -> None:
        self.text = text
        self.text_type = text_type.value
        self.url = url

    def __eq__(self, compared, /) -> bool:
        if (
            self.text == compared.text
            and self.text_type == compared.text_type
            and self.url == compared.url
        ):
            return True
        return False

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):

    node = None

    if text_node.text_type == "text":
        node = LeafNode(tag=None, value=text_node.text)
    if text_node.text_type == "bold":
        node = LeafNode("b", text_node.text)
    if text_node.text_type == "italic":
        node = LeafNode("i", text_node.text)
    if text_node.text_type == "code":
        node = LeafNode("code", text_node.text)
    if text_node.text_type == "link":
        node = LeafNode("a", text_node.text, props={"href": text_node.url})
    if text_node.text_type == "image":
        node = LeafNode(
            "img", None, props={"src": text_node.url, "alt": text_node.text}
        )

    return node
