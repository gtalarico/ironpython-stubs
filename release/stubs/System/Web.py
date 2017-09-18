# encoding: utf-8
# module System.Web calls itself Web
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class AspNetHostingPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission):
    """
    Controls access permissions in ASP.NET hosted environments. This class cannot be inherited.
    
    AspNetHostingPermission(state: PermissionState)
    AspNetHostingPermission(level: AspNetHostingPermissionLevel)
    """
    def Copy(self):
        """
        Copy(self: AspNetHostingPermission) -> IPermission
        
            When implemented by a derived class, creates and returns an identical copy of the current 
             permission object.
        
            Returns: A copy of the current permission object.
        """
        pass

    def FromXml(self, securityElement):
        """
        FromXml(self: AspNetHostingPermission, securityElement: SecurityElement)
            Reconstructs a permission object with a specified state from an XML encoding.
        
            securityElement: The System.Security.SecurityElement containing the XML encoding to use to reconstruct the 
             permission object.
        """
        pass

    def Intersect(self, target):
        """
        Intersect(self: AspNetHostingPermission, target: IPermission) -> IPermission
        
            When implemented by a derived class, creates and returns a permission that is the intersection 
             of the current permission and the specified permission.
        
        
            target: A permission to combine with the current permission. It must be of the same type as the current 
             permission.
        
            Returns: An System.Security.IPermission that represents the intersection of the current permission and 
             the specified permission; otherwise, null if the intersection is empty.
        """
        pass

    def IsSubsetOf(self, target):
        """
        IsSubsetOf(self: AspNetHostingPermission, target: IPermission) -> bool
        
            Returns a value indicating whether the current permission is a subset of the specified 
             permission.
        
        
            target: The System.Security.IPermission to combine with the current permission. It must be of the same 
             type as the current System.Security.IPermission.
        
            Returns: true if the current System.Security.IPermission is a subset of the specified 
             System.Security.IPermission; otherwise, false.
        """
        pass

    def IsUnrestricted(self):
        """
        IsUnrestricted(self: AspNetHostingPermission) -> bool
        
            Returns a value indicating whether unrestricted access to the resource that is protected by the 
             current permission is allowed.
        
            Returns: true if unrestricted use of the resource protected by the permission is allowed; otherwise, 
             false.
        """
        pass

    def ToXml(self):
        """
        ToXml(self: AspNetHostingPermission) -> SecurityElement
        
            Creates an XML encoding of the permission object and its current state.
            Returns: A System.Security.SecurityElement containing the XML encoding of the permission object, 
             including any state information.
        """
        pass

    def Union(self, target):
        """
        Union(self: AspNetHostingPermission, target: IPermission) -> IPermission
        
            Creates a permission that is the union of the current permission and the specified permission.
        
            target: A permission to combine with the current permission. It must be of the same type as the current 
             permission.
        
            Returns: An System.Security.IPermission that represents the union of the current permission and the 
             specified permission.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, level: AspNetHostingPermissionLevel)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current hosting permission level for an ASP.NET application.

Get: Level(self: AspNetHostingPermission) -> AspNetHostingPermissionLevel

Set: Level(self: AspNetHostingPermission) = value
"""



class AspNetHostingPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """
    Allows security actions for System.Web.AspNetHostingPermission to be applied to code using declarative security. This class cannot be inherited.
    
    AspNetHostingPermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: AspNetHostingPermissionAttribute) -> IPermission
        
            Creates a new System.Web.AspNetHostingPermission with the permission level previously set by the 
             System.Web.AspNetHostingPermissionAttribute.Level property.
        
            Returns: An System.Security.IPermission that is the new System.Web.AspNetHostingPermission.
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

    Level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current hosting permission level.

Get: Level(self: AspNetHostingPermissionAttribute) -> AspNetHostingPermissionLevel

Set: Level(self: AspNetHostingPermissionAttribute) = value
"""



class AspNetHostingPermissionLevel(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the trust level that is granted to an ASP.NET Web application.
    
    enum AspNetHostingPermissionLevel, values: High (500), Low (300), Medium (400), Minimal (200), None (100), Unrestricted (600)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    High = None
    Low = None
    Medium = None
    Minimal = None
    None = None
    Unrestricted = None
    value__ = None


