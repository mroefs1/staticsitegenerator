from link_extract import extract_markdown_images, extract_markdown_links
import unittest

class TestLinkExtract(unittest.TestCase):
    def test_img_simple(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        result = extract_markdown_images(text)
        self.assertListEqual(expected, result)

    def test_link_simple(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        result = extract_markdown_links(text)
        self.assertListEqual(expected, result)

    def test_both_empty_text(self):
        text = ""
        expected = []
        result1 = extract_markdown_images(text)
        result2 = extract_markdown_links(text)
        self.assertListEqual(expected, result1)
        self.assertListEqual(expected, result2)