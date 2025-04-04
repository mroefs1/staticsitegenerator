import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, None, None).to_html()

    def test_to_html_empty_tag(self):
        with self.assertRaises(ValueError):
            ParentNode("",None,None).to_html()

    def test_to_html_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("a", None, None).to_html()

    def test_to_html_empty_children(self):
        with self.assertRaises(ValueError):
            ParentNode("p", [], None).to_html()

    def test_to_html_with_props(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("a", [child_node], {"href": "https://www.google.com"})
        self.assertEqual(
            parent_node.to_html(),
            "<a href=\"https://www.google.com\"><span><b>grandchild</b></span></a>",
        )

    def test_multiple_children(self):
        parent_node = ParentNode("ul", [
            LeafNode("li", "Item 1"),
            LeafNode("li", "Item 2"),
            LeafNode("li", "Item 3")
        ])
        self.assertEqual(
            parent_node.to_html(),
            "<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>"
        )

    def test_mixed_child_types(self):
        parent_node = ParentNode("div", [
            LeafNode("span", "Text"),
            ParentNode("ul", [
                LeafNode("li", "Item")
            ])
        ])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>Text</span><ul><li>Item</li></ul></div>"
        )

    def test_multiple_props(self):
        node = ParentNode("div", [LeafNode("span", "Text")], {
            "id": "main", 
            "class": "container"
        })
        # Note: The order of props might vary, so you might need to adjust this test
        self.assertTrue(
            node.to_html() == '<div id="main" class="container"><span>Text</span></div>' or
            node.to_html() == '<div class="container" id="main"><span>Text</span></div>'
        )