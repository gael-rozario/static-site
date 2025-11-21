class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):

        if self.props is None:
            return None

        string_repr = ""

        for prop in self.props:
            prop_rep = f' {prop}="{self.props[prop]}"'
            string_repr += prop_rep

        return string_repr

    def __repr__(self) -> str:

        return f"{{\n Tag: {self.tag}\n Value: {self.value}\n Children: {self.children}\n Props: {self.props}\n}}"


class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self):

        if self.value is None:
            raise ValueError

        if self.tag is None:
            return self.value

        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"

        return f"<{self.tag} {self.props_to_html()} >{self.value}</{self.tag}>"


class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):

        if self.tag is None:
            raise ValueError("Tag cannot be empty")

        if self.children is None:
            raise ValueError("Children should not be empty")

        rendered_childred = ""

        for child in self.children:
            rendered_childred += child.to_html()

        return f"<{self.tag}>{rendered_childred}</{self.tag}>"
