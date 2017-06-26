class LinkElementId(object):
    """
    LinkElementId represents an element in a linked document.
    
    LinkElementId(linkInstanceId: ElementId, elementId: ElementId)
    LinkElementId(elementId: ElementId)
    """
    def Equals(self, obj):
        """
        Equals(self: LinkElementId, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to the current 
             System.Object.
        
        
            obj: Another object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, linkInstanceId: ElementId, elementId: ElementId)
        __new__(cls: type, elementId: ElementId)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    HostElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the element in the host, or invalidElementId if there is a link.

Get: HostElementId(self: LinkElementId) -> ElementId

"""

    LinkedElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the element in the link, or invalidElementId if no link.

Get: LinkedElementId(self: LinkElementId) -> ElementId

"""

    LinkInstanceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the link, or invalidElementId if no link.

Get: LinkInstanceId(self: LinkElementId) -> ElementId

"""


