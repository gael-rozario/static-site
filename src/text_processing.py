def split_node_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []

    markdown_inline_tags = ["**", "~~", "__", "_", "`", "*"]

    for node in old_nodes:

        if node.text_type.value != "text":
            new_nodes.append(node)
