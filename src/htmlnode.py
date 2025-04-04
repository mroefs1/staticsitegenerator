# HTMLNode" class will represent a "node" in an HTML document tree (like a <p> tag and its contents, 
# or an <a> tag and its contents). It can be block level or inline, and is designed to only output HTML.

# tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
# value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
# children - A list of HTMLNode objects representing the children of this node
# props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}

#Why default is NoneType
# An HTMLNode without a tag will just render as raw text
# An HTMLNode without a value will be assumed to have children
# An HTMLNode without children will be assumed to have a value
# An HTMLNode without props simply won't have any attributes

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("child classes will override")
    
    def props_to_html(self):
        if self.props == None:
            raise ValueError("No props present for HTML Node")
        html_string = ""
        for key in self.props:
            html_string += f" {key}=\"{self.props[key]}\""
        return html_string
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    

    