from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType


def main():
    title = TextNode("This is the heading", TextType.BOLD)
    print(title)

    intro = LeafNode("p", "This is a paragraph of text", {"class": "sample class"})
    print(intro.to_html())

    i1 = LeafNode("h1", "This is a first heading")
    i2 = LeafNode("h2", "This is a second heading")
    i3 = LeafNode("h3", "This is a third heading")

    div1 = ParentNode("div", children=[i1, i2, i3], props={"class": "headings"})

    p1 = LeafNode("p", "This is some first paragraph for testing")
    p2 = LeafNode("p", "This is some second paragraph for testing")
    p3 = LeafNode("p", "This is some group of paragraph for testing")

    div2 = ParentNode("div", children=[p1, p2], props={"class": "paragraphs"})

    mixeddiv = ParentNode(
        "div", children=[div1, div2, p3], props={"class": "heading_and_paragraphs"}
    )

    print(mixeddiv.to_html())


main()
