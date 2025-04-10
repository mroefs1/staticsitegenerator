import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("<h>", "HEADER")
        result = repr(node)
        expected = "HTMLNode(tag=<h>, value=HEADER, children=None, props=None)"
        self.assertEqual(result, expected)

    def test_repr_all_none(self):
        node = HTMLNode()
        result = repr(node)
        expected = "HTMLNode(tag=None, value=None, children=None, props=None)"
        self.assertEqual(result, expected)

    def test_props_to_html(self):
        node = HTMLNode(tag="a", value="Google.com", children=None, props={"href": "www.google.com", "target": "_blank"})
        result = node.props_to_html()
        expected = " href=\"www.google.com\" target=\"_blank\""
        self.assertEqual(result, expected)

    

if __name__ == "__main__":
    unittest.main()