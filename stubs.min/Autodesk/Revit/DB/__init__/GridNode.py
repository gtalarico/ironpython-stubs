class GridNode(object):
    """
    A structure that represents a particular location in (U,V) from a grid.
    
    GridNode(uIndex: int, vIndex: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, uIndex, vIndex):
        """
        __new__[GridNode]() -> GridNode
        
        __new__(cls: type, uIndex: int, vIndex: int)
        """
        pass

    UIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The node's index along the U axis.

Get: UIndex(self: GridNode) -> int

Set: UIndex(self: GridNode) = value
"""

    VIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The node's index along the V axis.

Get: VIndex(self: GridNode) -> int

Set: VIndex(self: GridNode) = value
"""


