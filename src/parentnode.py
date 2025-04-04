from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag or self.tag == "":
            raise ValueError("Parent Nodes must have a valid tag")
        if not self.children or self.children == []:
            raise ValueError("ParentNode must have children")
        starting_tag = f"<{self.tag}>"
        ending_tag = f"</{self.tag}>"
        middle = ""
        if self.props:
            starting_tag = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            middle += child.to_html() 
        return starting_tag + middle + ending_tag
    
