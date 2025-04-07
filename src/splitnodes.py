from textnode import TextNode, TextType

###
# Takes in a list of "old nodes", a delimiter, and a text type.
#
# Will return a list of new nodes where any "normal" nodes are potentially split by delimiter into multiple nodes based on syntax
#
# 
###


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node) #if the node is not a normal node, no need to split it 
            continue
        count = node.text.count(delimiter)
        if count % 2 != 0:
            raise Exception(f"Invalid Markdown Syntax: Expected closing {delimiter}")
        split = node.text.split(delimiter)
        starts_with = node.text.startswith(delimiter) #does the string start with the delim? use to do the ol flipperooni  
        ends_with = node.text.endswith(delimiter)
        if starts_with or ends_with: #need to get rid of extra "" element from split() when text starts or ends with delimited section
            split.remove("")
        for part in split:
            if starts_with:
                new_nodes.append(TextNode(part, text_type))
            else:
                new_nodes.append(TextNode(part, TextType.NORMAL))
            starts_with = not starts_with
    return new_nodes



    

