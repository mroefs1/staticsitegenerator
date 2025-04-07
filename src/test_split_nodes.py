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

    def test_invalid_bold_syntax(self):
        with self.assertRaises(Exception):
            nodes = [TextNode("This has an **invalid* syntax", TextType.NORMAL)]
            split_nodes_delimiter(nodes, "**", TextType.BOLD)

    def test_starts_with_bold(self):
        nodes = [TextNode("**bolded section,** this starts with", TextType.NORMAL)]
        expected = [
            TextNode("bolded section,", TextType.BOLD),
            TextNode(" this starts with", TextType.NORMAL)
        ]
        self.assertEqual(split_nodes_delimiter(nodes, "**", TextType.BOLD), expected)

    def test_ends_with_bold(self):
        nodes = [TextNode("bolded section, **this ends with**", TextType.NORMAL)]
        expected = [
            TextNode("bolded section, ", TextType.NORMAL),
            TextNode("this ends with", TextType.BOLD)
        ]
        self.assertEqual(split_nodes_delimiter(nodes, "**", TextType.BOLD), expected)

    def test_consecutive_bolds(self): #idk why the fuck anyone would do this 
        nodes = [TextNode("This has **consecutive** **bolded** sections", TextType.NORMAL)]
        expected = [
            TextNode("This has ", TextType.NORMAL),
            TextNode("consecutive", TextType.BOLD),
            TextNode(" ", TextType.NORMAL),
            TextNode("bolded", TextType.BOLD),
            TextNode(" sections", TextType.NORMAL)
        ]
        self.assertEqual(split_nodes_delimiter(nodes, "**", TextType.BOLD), expected)

    def test_multiple_bold_nodes(self):
        nodes = [TextNode("This has **two** separate **bold** sections", TextType.NORMAL), TextNode("2This has **two** separate **bold** sections", TextType.NORMAL)]
        expected = [
            TextNode("This has ", TextType.NORMAL),
            TextNode("two", TextType.BOLD),
            TextNode(" separate ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" sections", TextType.NORMAL),
            TextNode("2This has ", TextType.NORMAL),
            TextNode("two", TextType.BOLD),
            TextNode(" separate ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" sections", TextType.NORMAL)
        ]
        self.assertEqual(split_nodes_delimiter(nodes, "**", TextType.BOLD), expected)

    def test_one_italic_node(self):
        nodes = [TextNode("This has a __italic section__ in it", TextType.NORMAL)]
        expected = [
            TextNode("This has a ", TextType.NORMAL),
            TextNode("italic section", TextType.ITALIC),
            TextNode(" in it", TextType.NORMAL)
        ]
        self.assertEqual(split_nodes_delimiter(nodes, "__", TextType.ITALIC), expected)

    def test_one_code_node(self):
        nodes = [TextNode("This has a `code section` in it", TextType.NORMAL)]
        expected = [
            TextNode("This has a ", TextType.NORMAL),
            TextNode("code section", TextType.CODE),
            TextNode(" in it", TextType.NORMAL)
        ]
        self.assertEqual(split_nodes_delimiter(nodes, "`", TextType.CODE), expected)

    def test_multiple_calls(self):
        node = [TextNode("this has a **bold** section and an __italic__ section", TextType.NORMAL)]
        expected = [
            TextNode("this has a ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" section and an ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" section", TextType.NORMAL)
        ]
        split = split_nodes_delimiter(node, "**", TextType.BOLD)
        split = split_nodes_delimiter(split, "__", TextType.ITALIC)
        self.assertEqual(split, expected)

    def test_triple_calls(self):
        node = [TextNode("this has a **bold** section and an __italic__ section and a `code` section", TextType.NORMAL)]
        expected = [
            TextNode("this has a ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" section and an ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" section and a ", TextType.NORMAL),
            TextNode("code", TextType.CODE),
            TextNode(" section", TextType.NORMAL)
        ]
        split = split_nodes_delimiter(node, "**", TextType.BOLD)
        split = split_nodes_delimiter(split, "__", TextType.ITALIC)
        split = split_nodes_delimiter(split, "`", TextType.CODE)
        self.assertEqual(split, expected)

    def test_triple_calls_multiple_parts(self):
        node = [TextNode("this has **two** **bold** sections and two __italic__ __sections__ and two `code` `block` sections", TextType.NORMAL)]
        expected = [
            TextNode("this has ", TextType.NORMAL),
            TextNode("two", TextType.BOLD),
            TextNode(" ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" sections and two ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" ", TextType.NORMAL),
            TextNode("sections", TextType.ITALIC),
            TextNode(" and two ", TextType.NORMAL),
            TextNode("code", TextType.CODE),
            TextNode(" ", TextType.NORMAL),
            TextNode("block", TextType.CODE),
            TextNode(" sections", TextType.NORMAL)
        ]
        split = split_nodes_delimiter(node, "**", TextType.BOLD)
        split = split_nodes_delimiter(split, "__", TextType.ITALIC)
        split = split_nodes_delimiter(split, "`", TextType.CODE)
        self.assertEqual(split, expected)

    def test_multiple_nodes_call_one(self):
        nodes = [
            TextNode("Bold 1: **Bold**", TextType.NORMAL), 
            TextNode("Bold 2: **Bold2**", TextType.NORMAL),
            TextNode("Italic: __Italic__", TextType.NORMAL),
            TextNode("Code: `Code`", TextType.NORMAL)
            ]
        expected = [
            TextNode("Bold 1: ", TextType.NORMAL),
            TextNode("Bold", TextType.BOLD), 
            TextNode("Bold 2: ", TextType.NORMAL),
            TextNode("Bold2", TextType.BOLD),
            TextNode("Italic: __Italic__", TextType.NORMAL),
            TextNode("Code: `Code`", TextType.NORMAL)
        ]
        split = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(expected, split)

    def test_multiple_nodes_call_all(self):
        nodes = [
            TextNode("Bold 1: **Bold**", TextType.NORMAL), 
            TextNode("Bold 2: **Bold2**", TextType.NORMAL),
            TextNode("Italic: __Italic__", TextType.NORMAL),
            TextNode("Code: `Code`", TextType.NORMAL)
            ]
        expected = [
            TextNode("Bold 1: ", TextType.NORMAL),
            TextNode("Bold", TextType.BOLD), 
            TextNode("Bold 2: ", TextType.NORMAL),
            TextNode("Bold2", TextType.BOLD),
            TextNode("Italic: ", TextType.NORMAL),
            TextNode("Italic", TextType.ITALIC),
            TextNode("Code: ", TextType.NORMAL),
            TextNode("Code", TextType.CODE)
        ]
        split = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        split = split_nodes_delimiter(split, "__", TextType.ITALIC)
        split = split_nodes_delimiter(split, "`", TextType.CODE)
        self.assertEqual(expected, split)

    def test_empty_with_start(self):
        nodes = [TextNode("**BOLD** with ** ** section", TextType.NORMAL)]
        expected = [
            TextNode("BOLD", TextType.BOLD),
            TextNode(" with ", TextType.NORMAL),
            TextNode(" ", TextType.BOLD),
            TextNode(" section", TextType.NORMAL)
        ]
        self.assertEqual(split_nodes_delimiter(nodes, "**", TextType.BOLD), expected)


