import unittest
from textnode import TextNode, TextType
from splitnodes import split_nodes_delimiter


class TestSplitNodes(unittest.TestCase):
    #if there are no normal nodes to split the resulting list should be identical to the input list
    def test_no_normal_nodes(self):
        node1 = TextNode("BOLD", TextType.BOLD)
        node2 = TextNode("ITALIC", TextType.ITALIC)
        node3 = TextNode("CODE", TextType.CODE)
        nodes = [node1, node2, node3]
        self.assertEqual(nodes, split_nodes_delimiter(nodes, "**", TextType.BOLD))
        self.assertEqual(nodes, split_nodes_delimiter(nodes, "_", TextType.ITALIC))
        self.assertEqual(nodes, split_nodes_delimiter(nodes, "`", TextType.CODE))

    def test_one_bold_node(self):
        nodes = [TextNode("This has a **bold section** in it", TextType.NORMAL)]
        expected = [
            TextNode("This has a ", TextType.NORMAL),
            TextNode("bold section", TextType.BOLD),
            TextNode(" in it", TextType.NORMAL)
        ]
        self.assertEqual(split_nodes_delimiter(nodes, "**", TextType.BOLD), expected)

    def test_multiple_bold_sections(self):
        nodes = [TextNode("This has **two** separate **bold** sections", TextType.NORMAL)]
        expected = [
            TextNode("This has ", TextType.NORMAL),
            TextNode("two", TextType.BOLD),
            TextNode(" separate ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" sections", TextType.NORMAL)
        ]
        self.assertEqual(split_nodes_delimiter(nodes, "**", TextType.BOLD), expected)