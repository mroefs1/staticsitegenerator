from main import text_node_to_html_node
from textnode import TextNode, TextType
import unittest


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_bad_text_type(self):
        with self.assertRaises(Exception):
            node = TextNode("This is a text node", TextType.HELLO, None)
            htmlnode = text_node_to_html_node(node)

    def test_no_text_type(self):
        with self.assertRaises(Exception):
            node = TextNode("this is a text node", None, None)
            htmlnode = text_node_to_html_node(node)

    def test_normal(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_link(self):
        node = TextNode("Google", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})
        self.assertEqual(html_node.value, "Google")

    def test_img(self):
        node = TextNode("alt-text", TextType.IMAGE, "https://www.google.com/images")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.google.com/images", "alt": "alt-text"}
            or {"alt": "alt-text", "src": "https://www.google.com/images"}
        )
        self.assertEqual(html_node.value, "")
