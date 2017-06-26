class DnsPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """
    Specifies permission to request information from Domain Name Servers.
    
    DnsPermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: DnsPermissionAttribute) -> IPermission
        
            Creates and returns a new instance of the System.Net.DnsPermission class.
            Returns: A System.Net.DnsPermission that corresponds to the security declaration.
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

