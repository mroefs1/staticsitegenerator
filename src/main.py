from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

def main():
    tn = TextNode("This is dummy text", TextType.LINK, "https://boot.dev")
    print(tn)


def text_node_to_html_node(textnode):
    # if textnode.text_type not in TextType:
    #     raise Exception("textnode has incorrect TextType")
    match textnode.text_type:
        case TextType.NORMAL:
            return LeafNode(None, textnode.text, None)
        case TextType.BOLD:
            return LeafNode("b", textnode.text, None)
        case TextType.ITALIC:
            return LeafNode("i", textnode.text, None)
        case TextType.CODE:
            return LeafNode("code", textnode.text, None)
        case TextType.LINK:
            return LeafNode("a", textnode.text, {"href": textnode.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": textnode.url, "alt": textnode.text})
        case _:
            raise Exception("textnode has incorrect TextType")
    
    return 

main()