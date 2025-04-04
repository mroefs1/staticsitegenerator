import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_init(self):
        node = LeafNode("p","Leaf Node!")
        expected = "LeafNode(tag=p, value=Leaf Node!, props=None)"
        self.assertEqual(repr(node),expected)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello World!")
        self.assertEqual(node.to_html(), "<p>Hello World!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Google", {"href": "google.com"})
        self.assertEqual(node.to_html(), "<a href=\"google.com\">Google</a>")

    def test_leaf_to_html_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None, None).to_html()

    def test_leaf_to_html_value_empty_string(self):
        with self.assertRaises(ValueError):
            LeafNode("p", "", None).to_html()
        

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "VALUE!", None)
        self.assertEqual(node.to_html(), "VALUE!")