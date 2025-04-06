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
        if delimiter == "**": #TextType.BOLD
            count = node.count(delimiter)
            split = node.text.split(delimiter)
            print(f"SPLIT: {split}")


    return new_nodes

    

