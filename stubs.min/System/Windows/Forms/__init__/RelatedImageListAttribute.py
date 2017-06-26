class RelatedImageListAttribute(Attribute, _Attribute):
    """
    Indicates which System.Windows.Forms.ImageList a property is related to.
    
    RelatedImageListAttribute(relatedImageList: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, relatedImageList):
        """ __new__(cls: type, relatedImageList: str) """
        pass

    RelatedImageList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the related System.Windows.Forms.ImageList

Get: RelatedImageList(self: RelatedImageListAttribute) -> str

"""


