import unittest
from textnode import TextNode, TextType
from splitnodes import split_nodes_image, split_nodes_link


#
# Split nodes-image
#
# "This is text with a link [to boot dev](https://www.boot.dev) and image ![alt-text](https://i.imgur.com/zjjcJKZ.png)"
#           NORM                        LINK                     N          IMG

class TestSplitImagesLinks(unittest.TestCase):
    #if there are no normal nodes to split the resulting list should be identical to the input list
    # def test_no_normal_nodes(self):
    #     node1 = TextNode("BOLD", TextType.BOLD)
    #     node2 = TextNode("ITALIC", TextType.ITALIC)
    #     node3 = TextNode("CODE", TextType.CODE)
    #     nodes = [node1, node2, node3]
    #     self.assertListEqual(nodes, split_nodes_image(nodes))

    # def test_no_image_found(self):
    #     nodes = [TextNode("alt text", TextType.NORMAL)]
    #     self.assertListEqual(nodes , split_nodes_image(nodes))

    def test_one_image_node(self):
        nodes = [TextNode("Here is an image ![alt-text](https://i.imgur.com/zjjcJKZ.png) with some text after it", TextType.NORMAL)]
        expected = [
            TextNode("Here is an image ", TextType.NORMAL),
            TextNode("alt-text", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" with some text after it", TextType.NORMAL)
        ]
        self.assertListEqual(split_nodes_image(nodes), expected)

    def test_multiple_image_one_line(self):
        pass


    def test_multiple_image_nodes(self):
        pass
        # nodes = [
        #     TextNode("BOLD PLACEHOLDER", TextType.BOLD),
        #     TextNode("Here is an image ![alt-text](https://i.imgur.com/zjjcJKZ.png) with some text after it", TextType.NORMAL),
        #     TextNode("ITALIC PLACEHOLDER", TextType.ITALIC),
        #     TextNode("presetimage", TextType.IMAGE,"https://i.imgur.com/zjjcJKZ2.png"),
        #     TextNode("Here is an image ![alt-text](https://i.imgur.com/zjjcJKZ3.png) with some text after it", TextType.NORMAL)
        # ]
        # expected = [
        #     TextNode("BOLD PLACEHOLDER", TextType.BOLD),
        #     TextNode("Here is an image ", TextType.NORMAL),
        #     TextNode("alt-text", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
        #     TextNode(" with some text after it", TextType.NORMAL),
        #     TextNode("ITALIC PLACEHOLDER", TextType.ITALIC),
        #     TextNode("presetimage", TextType.IMAGE,"https://i.imgur.com/zjjcJKZ2.png"),
        #     TextNode("Here is an image ", TextType.NORMAL),
        #     TextNode("alt-text", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ3.png"),
        #     TextNode(" with some text after it", TextType.NORMAL)
        # ]
        # self.assertListEqual(expected, split_nodes_image(nodes))