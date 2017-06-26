class Localization(object):
    """ The System.Windows.Localization class defines attached properties for localization attributes and comments. """
    @staticmethod
    def GetAttributes(element):
        """
        GetAttributes(element: object) -> str
        
            Gets the value of the System.Windows.Localization.AttributesProperty attached property from a specified element.
        
            element: A System.Object that represents the element whose attached property you want to retrieve.
            Returns: A System.String value that represents the localization attribute.
        """
        pass

    @staticmethod
    def GetComments(element):
        """
        GetComments(element: object) -> str
        
            Gets the value of the System.Windows.Localization.CommentsProperty attached property from a specified element.
        
            element: A System.Object that represents the element whose attached property you want to retrieve.
            Returns: A System.String value that represents the localization comment.
        """
        pass

    @staticmethod
    def SetAttributes(element, attributes):
        """
        SetAttributes(element: object, attributes: str)
            Sets the System.Windows.Localization.AttributesProperty attached property for the specified element.
        
            element: A System.Object that represents the element whose attached property you want to set.
            attributes: A System.String that specifies the localization attributes.
        """
        pass

    @staticmethod
    def SetComments(element, comments):
        """
        SetComments(element: object, comments: str)
            Sets the System.Windows.Localization.CommentsProperty attached property to the specified element.
        
            element: A System.Object that represents the element whose attached property you want to set.
            comments: A System.String that specifies the localization comments.
        """
        pass

    AttributesProperty = None
    CommentsProperty = None
    __all__ = [
        'AttributesProperty',
        'CommentsProperty',
        'GetAttributes',
        'GetComments',
        'SetAttributes',
        'SetComments',
    ]

