class TemplateKey(ResourceKey, ISupportInitialize):
    """ When used as a resource key for a data template, allows the data template to participate in the lookup process. """
    def Equals(self, o):
        """
        Equals(self: TemplateKey, o: object) -> bool
        
            Returns a value that indicates whether the given instance is identical to this instance of System.Windows.TemplateKey.
        
            o: The object to compare for equality.
            Returns: true if the two instances are identical; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: TemplateKey) -> int
        
            Returns the hash code for this instance of System.Windows.TemplateKey.
            Returns: The hash code for this instance of System.Windows.TemplateKey.
        """
        pass

    def ToString(self):
        """
        ToString(self: TemplateKey) -> str
        
            Returns a string representation of this System.Windows.TemplateKey.
            Returns: A string representation of this System.Windows.TemplateKey.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, templateType: TemplateType)
        __new__(cls: type, templateType: TemplateType, dataType: object)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Assembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the assembly that contains the template definition.

Get: Assembly(self: TemplateKey) -> Assembly

"""

    DataType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type for which the template is designed.

Get: DataType(self: TemplateKey) -> object

Set: DataType(self: TemplateKey) = value
"""


    TemplateType = None

