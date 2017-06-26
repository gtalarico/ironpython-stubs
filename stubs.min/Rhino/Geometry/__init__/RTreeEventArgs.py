class RTreeEventArgs(EventArgs):
    # no doc
    Cancel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Cancel(self: RTreeEventArgs) -> bool

Set: Cancel(self: RTreeEventArgs) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: RTreeEventArgs) -> int

"""

    IdB = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IdB(self: RTreeEventArgs) -> int

"""

    IdBPtr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IdBPtr(self: RTreeEventArgs) -> IntPtr

"""

    IdPtr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IdPtr(self: RTreeEventArgs) -> IntPtr

"""

    SearchBoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SearchBoundingBox(self: RTreeEventArgs) -> BoundingBox

Set: SearchBoundingBox(self: RTreeEventArgs) = value
"""

    SearchSphere = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SearchSphere(self: RTreeEventArgs) -> Sphere

Set: SearchSphere(self: RTreeEventArgs) = value
"""

    Tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tag(self: RTreeEventArgs) -> object

Set: Tag(self: RTreeEventArgs) = value
"""


