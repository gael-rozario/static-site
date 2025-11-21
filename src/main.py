from htmlnode import HTMLNode, LeafNode
from textnode import TextNode, TextType


def main():
    title = TextNode("This is the heading", TextType.BOLD)
    print(title)

    intro = LeafNode("p", "This is a paragraph of text", {"class": "sample class"})
    print(intro.to_html())


main()
