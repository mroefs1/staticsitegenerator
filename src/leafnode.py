from htmlnode import HTMLNode

###
# A LeafNode is a type of HTMLNode that represents a single HTML tag with no children. 
# For example, a simple <p> tag with some text inside of it:
###

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None or self.value == "":
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return f"{self.value}"
        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"