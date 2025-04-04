from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

### 
#  TextNodes will represent inline elements in HTML
#  Normal text, bold text, italic text, code text, links, and images
#  as dictated by the TextType Enum
# 

class TextNode():
    
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other_node):
        if(self.text == other_node.text and self.text_type == other_node.text_type and self.url == other_node.url):
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"  