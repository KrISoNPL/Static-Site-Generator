from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, textType, url=None):
        self.text = text
        self.textType = textType
        self.url = url

    def __eq__(self, obj):
        return (
            self.text == obj.text 
            and self.textType == obj.textType 
            and self.url == obj.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.textType.value}, {self.url})"

