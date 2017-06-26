class PolymeshFacet(object):
    """ A class representing one triangular piece - a facet - in a polymesh topology. """
    def GetVertices(self):
        """
        GetVertices(self: PolymeshFacet) -> IList[int]
        
            Returns the three vertices that define this facet
        """
        pass

    def ToString(self):
        """
        ToString(self: PolymeshFacet) -> str
        
            Returns formatted string showing (V1, V2, V3) with values formatted as regular 
             integers
        """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: PolymeshFacet) -> bool

"""

    V1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The first vertex of the facet

Get: V1(self: PolymeshFacet) -> int

"""

    V2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The second vertex of the facet

Get: V2(self: PolymeshFacet) -> int

"""

    V3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The third vertex of the facet

Get: V3(self: PolymeshFacet) -> int

"""


