from textnode import TextNode, TextType


def split_node_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []

    for node in old_nodes:

        # Skip non-text nodes
        if node.text_type != TextType.TEXT.value:
            new_nodes.append(node)
            continue

        text = node.text

        # Check if delimiter exists in text
        if delimiter not in text:
            new_nodes.append(node)
            continue

        # Validate that delimiters are properly paired
        delimiter_count = text.count(delimiter)
        if delimiter_count % 2 != 0:
            raise ValueError(f"Invalid markdown: unmatched delimiter '{delimiter}' in text: {text}")

        # Split the text by delimiter
        parts = text.split(delimiter)

        # Process the parts
        for i, part in enumerate(parts):
            if part == "":
                continue

            # Even indices are regular text, odd indices are formatted text
            if i % 2 == 0:
                # Regular text
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                # Formatted text (inside delimiters)
                new_nodes.append(TextNode(part, text_type))

    return new_nodes




