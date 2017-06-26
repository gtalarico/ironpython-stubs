class WebPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """
    Specifies permission to access Internet resources. This class cannot be inherited.
    
    WebPermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: WebPermissionAttribute) -> IPermission
        
            Creates and returns a new instance of the System.Net.WebPermission class.
            Returns: A System.Net.WebPermission corresponding to the security declaration.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, action):
        """ __new__(cls: type, action: SecurityAction) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Accept = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the URI string accepted by the current System.Net.WebPermissionAttribute.

Get: Accept(self: WebPermissionAttribute) -> str

Set: Accept(self: WebPermissionAttribute) = value
"""

    AcceptPattern = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a regular expression pattern that describes the URI accepted by the current System.Net.WebPermissionAttribute.

Get: AcceptPattern(self: WebPermissionAttribute) -> str

Set: AcceptPattern(self: WebPermissionAttribute) = value
"""

    Connect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the URI connection string controlled by the current System.Net.WebPermissionAttribute.

Get: Connect(self: WebPermissionAttribute) -> str

Set: Connect(self: WebPermissionAttribute) = value
"""

    ConnectPattern = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a regular expression pattern that describes the URI connection controlled by the current System.Net.WebPermissionAttribute.

Get: ConnectPattern(self: WebPermissionAttribute) -> str

Set: ConnectPattern(self: WebPermissionAttribute) = value
"""


