class IConnector:
    """ An interface which provides access to connector in Autodesk Revit MEP document. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CoordinateSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The coordinate system of the connector.

Get: CoordinateSystem(self: IConnector) -> Transform

"""

    Domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The domain of the connector.

Get: Domain(self: IConnector) -> Domain

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The height of the connector.

Get: Height(self: IConnector) -> float

"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The location of the connector in family document.

Get: Origin(self: IConnector) -> XYZ

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The radius of the connector.

Get: Radius(self: IConnector) -> float

"""

    Shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The shape of the connector.

Get: Shape(self: IConnector) -> ConnectorProfileType

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The width of the connector.

Get: Width(self: IConnector) -> float

"""


