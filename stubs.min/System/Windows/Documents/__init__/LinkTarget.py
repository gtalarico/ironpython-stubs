class LinkTarget(object):
    """
    Represents an element on a page that can be linked to from other documents or other places in the same document.
    
    LinkTarget()
    """
    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the element that this System.Windows.Documents.LinkTarget identifies as a linkable element.

Get: Name(self: LinkTarget) -> str

Set: Name(self: LinkTarget) = value
"""


