class VertexIndexPair(object):
    """
    Represents a connection between vertices in the top and bottom profile of a blend.
    
    VertexIndexPair(iTop: int, iBottom: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, iTop, iBottom):
        """ __new__(cls: type, iTop: int, iBottom: int) """
        pass

    Bottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index of the vertex pair from the bottom profile.

Get: Bottom(self: VertexIndexPair) -> int

Set: Bottom(self: VertexIndexPair) = value
"""

    Top = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index of the vertex pair from the top profile.

Get: Top(self: VertexIndexPair) -> int

Set: Top(self: VertexIndexPair) = value
"""


