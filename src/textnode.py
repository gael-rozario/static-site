from enum import Enum


class TextType(Enum):
    PLAIN = "plain"
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
