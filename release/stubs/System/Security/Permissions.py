# encoding: utf-8
# module System.Security.Permissions calls itself Permissions
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class SecurityAttribute(Attribute, _Attribute):
    """ Specifies the base attribute class for declarative security from which System.Security.Permissions.CodeAccessSecurityAttribute is derived. """
    def CreatePermission(self):
        """
        CreatePermission(self: SecurityAttribute) -> IPermission
        
            When overridden in a derived class, creates a permission object that can then be serialized into 
             binary form and persistently stored along with the System.Security.Permissions.SecurityAction in 
             an assembly's metadata.
        
            Returns: A serializable permission object.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, action: SecurityAction) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a security action.

Get: Action(self: SecurityAttribute) -> SecurityAction

Set: Action(self: SecurityAttribute) = value
"""

    Unrestricted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether full (unrestricted) permission to the resource protected by the attribute is declared.

Get: Unrestricted(self: SecurityAttribute) -> bool

Set: Unrestricted(self: SecurityAttribute) = value
"""



class CodeAccessSecurityAttribute(SecurityAttribute, _Attribute):
    """ Specifies the base attribute class for code access security. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, action: SecurityAction) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class IUnrestrictedPermission:
    """ Allows a permission to expose an unrestricted state. """
    def IsUnrestricted(self):
        """
        IsUnrestricted(self: IUnrestrictedPermission) -> bool
        
            Returns a value indicating whether unrestricted access to the resource protected by the 
             permission is allowed.
        
            Returns: true if unrestricted use of the resource protected by the permission is allowed; otherwise, 
             false.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class EnvironmentPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission, IBuiltInPermission):
    """
    Controls access to system and user environment variables. This class cannot be inherited.
    
    EnvironmentPermission(state: PermissionState)
    EnvironmentPermission(flag: EnvironmentPermissionAccess, pathList: str)
    """
    def AddPathList(self, flag, pathList):
        """
        AddPathList(self: EnvironmentPermission, flag: EnvironmentPermissionAccess, pathList: str)
            Adds access for the specified environment variables to the existing state of the permission.
        
            flag: One of the System.Security.Permissions.EnvironmentPermissionAccess values.
            pathList: A list of environment variables (semicolon-separated).
        """
        pass

    def Copy(self):
        """
        Copy(self: EnvironmentPermission) -> IPermission
        
            Creates and returns an identical copy of the current permission.
            Returns: A copy of the current permission.
        """
        pass

    def FromXml(self, esd):
        """
        FromXml(self: EnvironmentPermission, esd: SecurityElement)
            Reconstructs a permission with a specified state from an XML encoding.
        
            esd: The XML encoding to use to reconstruct the permission.
        """
        pass

    def GetPathList(self, flag):
        """
        GetPathList(self: EnvironmentPermission, flag: EnvironmentPermissionAccess) -> str
        
            Gets all environment variables with the specified 
             System.Security.Permissions.EnvironmentPermissionAccess.
        
        
            flag: One of the System.Security.Permissions.EnvironmentPermissionAccess values that represents a 
             single type of environment variable access.
        
            Returns: A list of environment variables (semicolon-separated) for the selected flag.
        """
        pass

    def Intersect(self, target):
        """
        Intersect(self: EnvironmentPermission, target: IPermission) -> IPermission
        
            Creates and returns a permission that is the intersection of the current permission and the 
             specified permission.
        
        
            target: A permission to intersect with the current permission. It must be of the same type as the 
             current permission.
        
            Returns: A new permission that represents the intersection of the current permission and the specified 
             permission. This new permission is null if the intersection is empty.
        """
        pass

    def IsSubsetOf(self, target):
        """
        IsSubsetOf(self: EnvironmentPermission, target: IPermission) -> bool
        
            Determines whether the current permission is a subset of the specified permission.
        
            target: A permission that is to be tested for the subset relationship. This permission must be of the 
             same type as the current permission.
        
            Returns: true if the current permission is a subset of the specified permission; otherwise, false.
        """
        pass

    def IsUnrestricted(self):
        """
        IsUnrestricted(self: EnvironmentPermission) -> bool
        
            Returns a value indicating whether the current permission is unrestricted.
            Returns: true if the current permission is unrestricted; otherwise, false.
        """
        pass

    def SetPathList(self, flag, pathList):
        """
        SetPathList(self: EnvironmentPermission, flag: EnvironmentPermissionAccess, pathList: str)
            Sets the specified access to the specified environment variables to the existing state of the 
             permission.
        
        
            flag: One of the System.Security.Permissions.EnvironmentPermissionAccess values.
            pathList: A list of environment variables (semicolon-separated).
        """
        pass

    def ToXml(self):
        """
        ToXml(self: EnvironmentPermission) -> SecurityElement
        
            Creates an XML encoding of the permission and its current state.
            Returns: An XML encoding of the permission, including any state information.
        """
        pass

    def Union(self, other):
        """
        Union(self: EnvironmentPermission, other: IPermission) -> IPermission
        
            Creates a permission that is the union of the current permission and the specified permission.
        
            other: A permission to combine with the current permission. It must be of the same type as the current 
             permission.
        
            Returns: A new permission that represents the union of the current permission and the specified 
             permission.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, flag: EnvironmentPermissionAccess, pathList: str)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class EnvironmentPermissionAccess(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies access to environment variables.
    
    enum (flags) EnvironmentPermissionAccess, values: AllAccess (3), NoAccess (0), Read (1), Write (2)
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

    AllAccess = None
    NoAccess = None
    Read = None
    value__ = None
    Write = None


class EnvironmentPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """
    Allows security actions for System.Security.Permissions.EnvironmentPermission to be applied to code using declarative security. This class cannot be inherited.
    
    EnvironmentPermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: EnvironmentPermissionAttribute) -> IPermission
        
            Creates and returns a new System.Security.Permissions.EnvironmentPermission.
            Returns: An System.Security.Permissions.EnvironmentPermission that corresponds to this attribute.
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

    All = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sets full access for the environment variables specified by the string value.

Get: All(self: EnvironmentPermissionAttribute) -> str

Set: All(self: EnvironmentPermissionAttribute) = value
"""

    Read = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets read access for the environment variables specified by the string value.

Get: Read(self: EnvironmentPermissionAttribute) -> str

Set: Read(self: EnvironmentPermissionAttribute) = value
"""

    Write = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets write access for the environment variables specified by the string value.

Get: Write(self: EnvironmentPermissionAttribute) -> str

Set: Write(self: EnvironmentPermissionAttribute) = value
"""



class FileDialogPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission, IBuiltInPermission):
    """
    Controls the ability to access files or folders through a File dialog box. This class cannot be inherited.
    
    FileDialogPermission(state: PermissionState)
    FileDialogPermission(access: FileDialogPermissionAccess)
    """
    def Copy(self):
        """
        Copy(self: FileDialogPermission) -> IPermission
        
            Creates and returns an identical copy of the current permission.
            Returns: A copy of the current permission.
        """
        pass

    def FromXml(self, esd):
        """
        FromXml(self: FileDialogPermission, esd: SecurityElement)
            Reconstructs a permission with a specified state from an XML encoding.
        
            esd: The XML encoding used to reconstruct the permission.
        """
        pass

    def Intersect(self, target):
        """
        Intersect(self: FileDialogPermission, target: IPermission) -> IPermission
        
            Creates and returns a permission that is the intersection of the current permission and the 
             specified permission.
        
        
            target: A permission to intersect with the current permission. It must be the same type as the current 
             permission.
        
            Returns: A new permission that represents the intersection of the current permission and the specified 
             permission. This new permission is null if the intersection is empty.
        """
        pass

    def IsSubsetOf(self, target):
        """
        IsSubsetOf(self: FileDialogPermission, target: IPermission) -> bool
        
            Determines whether the current permission is a subset of the specified permission.
        
            target: A permission that is to be tested for the subset relationship. This permission must be the same 
             type as the current permission.
        
            Returns: true if the current permission is a subset of the specified permission; otherwise, false.
        """
        pass

    def IsUnrestricted(self):
        """
        IsUnrestricted(self: FileDialogPermission) -> bool
        
            Returns a value indicating whether the current permission is unrestricted.
            Returns: true if the current permission is unrestricted; otherwise, false.
        """
        pass

    def ToXml(self):
        """
        ToXml(self: FileDialogPermission) -> SecurityElement
        
            Creates an XML encoding of the permission and its current state.
            Returns: An XML encoding of the permission, including state information.
        """
        pass

    def Union(self, target):
        """
        Union(self: FileDialogPermission, target: IPermission) -> IPermission
        
            Creates a permission that is the union of the current permission and the specified permission.
        
            target: A permission to combine with the current permission. It must be of the same type as the current 
             permission.
        
            Returns: A new permission that represents the union of the current permission and the specified 
             permission.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, access: FileDialogPermissionAccess)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Access = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the permitted access to files.

Get: Access(self: FileDialogPermission) -> FileDialogPermissionAccess

Set: Access(self: FileDialogPermission) = value
"""



class FileDialogPermissionAccess(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of access to files allowed through the File dialog boxes.
    
    enum (flags) FileDialogPermissionAccess, values: None (0), Open (1), OpenSave (3), Save (2)
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

    None = None
    Open = None
    OpenSave = None
    Save = None
    value__ = None


class FileDialogPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """
    Allows security actions for System.Security.Permissions.FileDialogPermission to be applied to code using declarative security. This class cannot be inherited.
    
    FileDialogPermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: FileDialogPermissionAttribute) -> IPermission
        
            Creates and returns a new System.Security.Permissions.FileDialogPermission.
            Returns: A System.Security.Permissions.FileDialogPermission that corresponds to this attribute.
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

    Open = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether permission to open files through the file dialog is declared.

Get: Open(self: FileDialogPermissionAttribute) -> bool

Set: Open(self: FileDialogPermissionAttribute) = value
"""

    Save = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether permission to save files through the file dialog is declared.

Get: Save(self: FileDialogPermissionAttribute) -> bool

Set: Save(self: FileDialogPermissionAttribute) = value
"""



class FileIOPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission, IBuiltInPermission):
    """
    Controls the ability to access files and folders. This class cannot be inherited.
    
    FileIOPermission(state: PermissionState)
    FileIOPermission(access: FileIOPermissionAccess, path: str)
    FileIOPermission(access: FileIOPermissionAccess, pathList: Array[str])
    FileIOPermission(access: FileIOPermissionAccess, control: AccessControlActions, path: str)
    FileIOPermission(access: FileIOPermissionAccess, control: AccessControlActions, pathList: Array[str])
    """
    def AddPathList(self, access, *__args):
        """
        AddPathList(self: FileIOPermission, access: FileIOPermissionAccess, pathList: Array[str])
            Adds access for the specified files and directories to the existing state of the permission.
        
            access: A bitwise combination of the System.Security.Permissions.FileIOPermissionAccess values.
            pathList: An array containing the absolute paths of the files and directories.
        AddPathList(self: FileIOPermission, access: FileIOPermissionAccess, path: str)
            Adds access for the specified file or directory to the existing state of the permission.
        
            access: A bitwise combination of the System.Security.Permissions.FileIOPermissionAccess values.
            path: The absolute path of a file or directory.
        """
        pass

    def Copy(self):
        """
        Copy(self: FileIOPermission) -> IPermission
        
            Creates and returns an identical copy of the current permission.
            Returns: A copy of the current permission.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: FileIOPermission, obj: object) -> bool
        
            Determines whether the specified System.Security.Permissions.FileIOPermission object is equal to 
             the current System.Security.Permissions.FileIOPermission.
        
        
            obj: The System.Security.Permissions.FileIOPermission object to compare with the current 
             System.Security.Permissions.FileIOPermission.
        
            Returns: true if the specified System.Security.Permissions.FileIOPermission is equal to the current 
             System.Security.Permissions.FileIOPermission object; otherwise, false.
        """
        pass

    def FromXml(self, esd):
        """
        FromXml(self: FileIOPermission, esd: SecurityElement)
            Reconstructs a permission with a specified state from an XML encoding.
        
            esd: The XML encoding used to reconstruct the permission.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: FileIOPermission) -> int
        
            Gets a hash code for the System.Security.Permissions.FileIOPermission object that is suitable 
             for use in hashing algorithms and data structures such as a hash table.
        
            Returns: A hash code for the current System.Security.Permissions.FileIOPermission object.
        """
        pass

    def GetPathList(self, access):
        """
        GetPathList(self: FileIOPermission, access: FileIOPermissionAccess) -> Array[str]
        
            Gets all files and directories with the specified 
             System.Security.Permissions.FileIOPermissionAccess.
        
        
            access: One of the System.Security.Permissions.FileIOPermissionAccess values that represents a single 
             type of file access.
        
            Returns: An array containing the paths of the files and directories to which access specified by the 
             access parameter is granted.
        """
        pass

    def Intersect(self, target):
        """
        Intersect(self: FileIOPermission, target: IPermission) -> IPermission
        
            Creates and returns a permission that is the intersection of the current permission and the 
             specified permission.
        
        
            target: A permission to intersect with the current permission. It must be the same type as the current 
             permission.
        
            Returns: A new permission that represents the intersection of the current permission and the specified 
             permission. This new permission is null if the intersection is empty.
        """
        pass

    def IsSubsetOf(self, target):
        """
        IsSubsetOf(self: FileIOPermission, target: IPermission) -> bool
        
            Determines whether the current permission is a subset of the specified permission.
        
            target: A permission that is to be tested for the subset relationship. This permission must be the same 
             type as the current permission.
        
            Returns: true if the current permission is a subset of the specified permission; otherwise, false.
        """
        pass

    def IsUnrestricted(self):
        """
        IsUnrestricted(self: FileIOPermission) -> bool
        
            Returns a value indicating whether the current permission is unrestricted.
            Returns: true if the current permission is unrestricted; otherwise, false.
        """
        pass

    def SetPathList(self, access, *__args):
        """
        SetPathList(self: FileIOPermission, access: FileIOPermissionAccess, pathList: Array[str])
            Sets the specified access to the specified files and directories, replacing the current state 
             for the specified access with the new set of paths.
        
        
            access: A bitwise combination of the System.Security.Permissions.FileIOPermissionAccess values.
            pathList: An array containing the absolute paths of the files and directories.
        SetPathList(self: FileIOPermission, access: FileIOPermissionAccess, path: str)
            Sets the specified access to the specified file or directory, replacing the existing state of 
             the permission.
        
        
            access: A bitwise combination of the System.Security.Permissions.FileIOPermissionAccess values.
            path: The absolute path of the file or directory.
        """
        pass

    def ToXml(self):
        """
        ToXml(self: FileIOPermission) -> SecurityElement
        
            Creates an XML encoding of the permission and its current state.
            Returns: An XML encoding of the permission, including any state information.
        """
        pass

    def Union(self, other):
        """
        Union(self: FileIOPermission, other: IPermission) -> IPermission
        
            Creates a permission that is the union of the current permission and the specified permission.
        
            other: A permission to combine with the current permission. It must be the same type as the current 
             permission.
        
            Returns: A new permission that represents the union of the current permission and the specified 
             permission.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, access: FileIOPermissionAccess, path: str)
        __new__(cls: type, access: FileIOPermissionAccess, pathList: Array[str])
        __new__(cls: type, access: FileIOPermissionAccess, control: AccessControlActions, path: str)
        __new__(cls: type, access: FileIOPermissionAccess, control: AccessControlActions, pathList: Array[str])
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AllFiles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the permitted access to all files.

Get: AllFiles(self: FileIOPermission) -> FileIOPermissionAccess

Set: AllFiles(self: FileIOPermission) = value
"""

    AllLocalFiles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the permitted access to all local files.

Get: AllLocalFiles(self: FileIOPermission) -> FileIOPermissionAccess

Set: AllLocalFiles(self: FileIOPermission) = value
"""



class FileIOPermissionAccess(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of file access requested.
    
    enum (flags) FileIOPermissionAccess, values: AllAccess (15), Append (4), NoAccess (0), PathDiscovery (8), Read (1), Write (2)
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

    AllAccess = None
    Append = None
    NoAccess = None
    PathDiscovery = None
    Read = None
    value__ = None
    Write = None


class FileIOPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """
    Allows security actions for System.Security.Permissions.FileIOPermission to be applied to code using declarative security. This class cannot be inherited.
    
    FileIOPermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: FileIOPermissionAttribute) -> IPermission
        
            Creates and returns a new System.Security.Permissions.FileIOPermission.
            Returns: A System.Security.Permissions.FileIOPermission that corresponds to this attribute.
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

    All = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets full access for the file or directory that is specified by the string value.

Get: All(self: FileIOPermissionAttribute) -> str

Set: All(self: FileIOPermissionAttribute) = value
"""

    AllFiles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the permitted access to all files.

Get: AllFiles(self: FileIOPermissionAttribute) -> FileIOPermissionAccess

Set: AllFiles(self: FileIOPermissionAttribute) = value
"""

    AllLocalFiles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the permitted access to all local files.

Get: AllLocalFiles(self: FileIOPermissionAttribute) -> FileIOPermissionAccess

Set: AllLocalFiles(self: FileIOPermissionAttribute) = value
"""

    Append = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets append access for the file or directory that is specified by the string value.

Get: Append(self: FileIOPermissionAttribute) -> str

Set: Append(self: FileIOPermissionAttribute) = value
"""

    ChangeAccessControl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the file or directory in which access control information can be changed.

Get: ChangeAccessControl(self: FileIOPermissionAttribute) -> str

Set: ChangeAccessControl(self: FileIOPermissionAttribute) = value
"""

    PathDiscovery = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the file or directory to which to grant path discovery.

Get: PathDiscovery(self: FileIOPermissionAttribute) -> str

Set: PathDiscovery(self: FileIOPermissionAttribute) = value
"""

    Read = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets read access for the file or directory specified by the string value.

Get: Read(self: FileIOPermissionAttribute) -> str

Set: Read(self: FileIOPermissionAttribute) = value
"""

    ViewAccessControl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the file or directory in which access control information can be viewed.

Get: ViewAccessControl(self: FileIOPermissionAttribute) -> str

Set: ViewAccessControl(self: FileIOPermissionAttribute) = value
"""

    ViewAndModify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the file or directory in which file data can be viewed and modified.

Get: ViewAndModify(self: FileIOPermissionAttribute) -> str

Set: ViewAndModify(self: FileIOPermissionAttribute) = value
"""

    Write = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets write access for the file or directory specified by the string value.

Get: Write(self: FileIOPermissionAttribute) -> str

Set: Write(self: FileIOPermissionAttribute) = value
"""



class GacIdentityPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IBuiltInPermission):
    """
    Defines the identity permission for files originating in the global assembly cache. This class cannot be inherited.
    
    GacIdentityPermission(state: PermissionState)
    GacIdentityPermission()
    """
    def Copy(self):
        """
        Copy(self: GacIdentityPermission) -> IPermission
        
            Creates and returns an identical copy of the current permission.
            Returns: A copy of the current permission.
        """
        pass

    def FromXml(self, securityElement):
        """
        FromXml(self: GacIdentityPermission, securityElement: SecurityElement)
            Creates a permission from an XML encoding.
        
            securityElement: A System.Security.SecurityElement  that contains the XML encoding to use to create the 
             permission.
        """
        pass

    def Intersect(self, target):
        """
        Intersect(self: GacIdentityPermission, target: IPermission) -> IPermission
        
            Creates and returns a permission that is the intersection of the current permission and the 
             specified permission.
        
        
            target: A permission to intersect with the current permission. It must be of the same type as the 
             current permission.
        
            Returns: A new permission that represents the intersection of the current permission and the specified 
             permission. The new permission is null if the intersection is empty.
        """
        pass

    def IsSubsetOf(self, target):
        """
        IsSubsetOf(self: GacIdentityPermission, target: IPermission) -> bool
        
            Indicates whether the current permission is a subset of the specified permission.
        
            target: A permission object to test for the subset relationship. The permission must be of the same type 
             as the current permission.
        
            Returns: true if the current permission is a subset of the specified permission; otherwise, false.
        """
        pass

    def ToXml(self):
        """
        ToXml(self: GacIdentityPermission) -> SecurityElement
        
            Creates an XML encoding of the permission and its current state.
            Returns: A System.Security.SecurityElement that represents the XML encoding of the permission, including 
             any state information.
        """
        pass

    def Union(self, target):
        """
        Union(self: GacIdentityPermission, target: IPermission) -> IPermission
        
            Creates and returns a permission that is the union of the current permission and the specified 
             permission.
        
        
            target: A permission to combine with the current permission. It must be of the same type as the current 
             permission.
        
            Returns: A new permission that represents the union of the current permission and the specified 
             permission.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, state=None):
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class GacIdentityPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """
    Allows security actions for System.Security.Permissions.GacIdentityPermission to be applied to code using declarative security. This class cannot be inherited.
    
    GacIdentityPermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: GacIdentityPermissionAttribute) -> IPermission
        
            Creates a new System.Security.Permissions.GacIdentityPermission object.
            Returns: A System.Security.Permissions.GacIdentityPermission that corresponds to this attribute.
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


class HostProtectionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """
    Allows the use of declarative security actions to determine host protection requirements. This class cannot be inherited.
    
    HostProtectionAttribute()
    HostProtectionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: HostProtectionAttribute) -> IPermission
        
            Creates and returns a new host protection permission.
            Returns: An System.Security.IPermission that corresponds to the current attribute.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, action=None):
        """
        __new__(cls: type)
        __new__(cls: type, action: SecurityAction)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    ExternalProcessMgmt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether external process management is exposed.

Get: ExternalProcessMgmt(self: HostProtectionAttribute) -> bool

Set: ExternalProcessMgmt(self: HostProtectionAttribute) = value
"""

    ExternalThreading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether external threading is exposed.

Get: ExternalThreading(self: HostProtectionAttribute) -> bool

Set: ExternalThreading(self: HostProtectionAttribute) = value
"""

    MayLeakOnAbort = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether resources might leak memory if the operation is terminated.

Get: MayLeakOnAbort(self: HostProtectionAttribute) -> bool

Set: MayLeakOnAbort(self: HostProtectionAttribute) = value
"""

    Resources = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets flags specifying categories of functionality that are potentially harmful to the host.

Get: Resources(self: HostProtectionAttribute) -> HostProtectionResource

Set: Resources(self: HostProtectionAttribute) = value
"""

    SecurityInfrastructure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the security infrastructure is exposed.

Get: SecurityInfrastructure(self: HostProtectionAttribute) -> bool

Set: SecurityInfrastructure(self: HostProtectionAttribute) = value
"""

    SelfAffectingProcessMgmt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether self-affecting process management is exposed.

Get: SelfAffectingProcessMgmt(self: HostProtectionAttribute) -> bool

Set: SelfAffectingProcessMgmt(self: HostProtectionAttribute) = value
"""

    SelfAffectingThreading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether self-affecting threading is exposed.

Get: SelfAffectingThreading(self: HostProtectionAttribute) -> bool

Set: SelfAffectingThreading(self: HostProtectionAttribute) = value
"""

    SharedState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether shared state is exposed.

Get: SharedState(self: HostProtectionAttribute) -> bool

Set: SharedState(self: HostProtectionAttribute) = value
"""

    Synchronization = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether synchronization is exposed.

Get: Synchronization(self: HostProtectionAttribute) -> bool

Set: Synchronization(self: HostProtectionAttribute) = value
"""

    UI = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the user interface is exposed.

Get: UI(self: HostProtectionAttribute) -> bool

Set: UI(self: HostProtectionAttribute) = value
"""



class HostProtectionResource(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies categories of functionality potentially harmful to the host if invoked by a method or class.
    
    enum (flags) HostProtectionResource, values: All (511), ExternalProcessMgmt (4), ExternalThreading (16), MayLeakOnAbort (256), None (0), SecurityInfrastructure (64), SelfAffectingProcessMgmt (8), SelfAffectingThreading (32), SharedState (2), Synchronization (1), UI (128)
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

    All = None
    ExternalProcessMgmt = None
    ExternalThreading = None
    MayLeakOnAbort = None
    None = None
    SecurityInfrastructure = None
    SelfAffectingProcessMgmt = None
    SelfAffectingThreading = None
    SharedState = None
    Synchronization = None
    UI = None
    value__ = None


class IsolatedStorageContainment(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the permitted use of isolated storage.
    
    enum IsolatedStorageContainment, values: AdministerIsolatedStorageByUser (112), ApplicationIsolationByMachine (69), ApplicationIsolationByRoamingUser (101), ApplicationIsolationByUser (21), AssemblyIsolationByMachine (64), AssemblyIsolationByRoamingUser (96), AssemblyIsolationByUser (32), DomainIsolationByMachine (48), DomainIsolationByRoamingUser (80), DomainIsolationByUser (16), None (0), UnrestrictedIsolatedStorage (240)
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

    AdministerIsolatedStorageByUser = None
    ApplicationIsolationByMachine = None
    ApplicationIsolationByRoamingUser = None
    ApplicationIsolationByUser = None
    AssemblyIsolationByMachine = None
    AssemblyIsolationByRoamingUser = None
    AssemblyIsolationByUser = None
    DomainIsolationByMachine = None
    DomainIsolationByRoamingUser = None
    DomainIsolationByUser = None
    None = None
    UnrestrictedIsolatedStorage = None
    value__ = None


class IsolatedStoragePermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission):
    """ Represents access to generic isolated storage capabilities. """
    def FromXml(self, esd):
        """
        FromXml(self: IsolatedStoragePermission, esd: SecurityElement)
            Reconstructs a permission with a specified state from an XML encoding.
        
            esd: The XML encoding to use to reconstruct the permission.
        """
        pass

    def IsUnrestricted(self):
        """
        IsUnrestricted(self: IsolatedStoragePermission) -> bool
        
            Returns a value indicating whether the current permission is unrestricted.
            Returns: true if the current permission is unrestricted; otherwise, false.
        """
        pass

    def ToXml(self):
        """
        ToXml(self: IsolatedStoragePermission) -> SecurityElement
        
            Creates an XML encoding of the permission and its current state.
            Returns: An XML encoding of the permission, including any state information.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, state: PermissionState) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    UsageAllowed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type of isolated storage containment allowed.

Get: UsageAllowed(self: IsolatedStoragePermission) -> IsolatedStorageContainment

Set: UsageAllowed(self: IsolatedStoragePermission) = value
"""

    UserQuota = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the quota on the overall size of each user's total store.

Get: UserQuota(self: IsolatedStoragePermission) -> Int64

Set: UserQuota(self: IsolatedStoragePermission) = value
"""



class IsolatedStorageFilePermission(IsolatedStoragePermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission, IBuiltInPermission):
    """
    Specifies the allowed usage of a private virtual file system. This class cannot be inherited.
    
    IsolatedStorageFilePermission(state: PermissionState)
    """
    def Copy(self):
        """
        Copy(self: IsolatedStorageFilePermission) -> IPermission
        
            Creates and returns an identical copy of the current permission.
            Returns: A copy of the current permission.
        """
        pass

    def Intersect(self, target):
        """
        Intersect(self: IsolatedStorageFilePermission, target: IPermission) -> IPermission
        
            Creates and returns a permission that is the intersection of the current permission and the 
             specified permission.
        
        
            target: A permission to intersect with the current permission object. It must be of the same type as the 
             current permission.
        
            Returns: A new permission that represents the intersection of the current permission and the specified 
             permission. This new permission is null if the intersection is empty.
        """
        pass

    def IsSubsetOf(self, target):
        """
        IsSubsetOf(self: IsolatedStorageFilePermission, target: IPermission) -> bool
        
            Determines whether the current permission is a subset of the specified permission.
        
            target: A permission that is to be tested for the subset relationship. This permission must be of the 
             same type as the current permission.
        
            Returns: true if the current permission is a subset of the specified permission; otherwise, false.
        """
        pass

    def ToXml(self):
        """
        ToXml(self: IsolatedStorageFilePermission) -> SecurityElement
        
            Creates an XML encoding of the permission and its current state.
            Returns: An XML encoding of the permission, including any state information.
        """
        pass

    def Union(self, target):
        """
        Union(self: IsolatedStorageFilePermission, target: IPermission) -> IPermission
        
            Creates a permission that is the union of the current permission and the specified permission.
        
            target: A permission to combine with the current permission. It must be of the same type as the current 
             permission.
        
            Returns: A new permission that represents the union of the current permission and the specified 
             permission.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, state):
        """ __new__(cls: type, state: PermissionState) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class IsolatedStoragePermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """ Allows security actions for System.Security.Permissions.IsolatedStoragePermission to be applied to code using declarative security. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, action: SecurityAction) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    UsageAllowed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the level of isolated storage that should be declared.

Get: UsageAllowed(self: IsolatedStoragePermissionAttribute) -> IsolatedStorageContainment

Set: UsageAllowed(self: IsolatedStoragePermissionAttribute) = value
"""

    UserQuota = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the maximum user storage quota size.

Get: UserQuota(self: IsolatedStoragePermissionAttribute) -> Int64

Set: UserQuota(self: IsolatedStoragePermissionAttribute) = value
"""



class IsolatedStorageFilePermissionAttribute(IsolatedStoragePermissionAttribute, _Attribute):
    """
    Allows security actions for System.Security.Permissions.IsolatedStorageFilePermission to be applied to code using declarative security. This class cannot be inherited.
    
    IsolatedStorageFilePermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: IsolatedStorageFilePermissionAttribute) -> IPermission
        
            Creates and returns a new System.Security.Permissions.IsolatedStorageFilePermission.
            Returns: An System.Security.Permissions.IsolatedStorageFilePermission that corresponds to this attribute.
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


class KeyContainerPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission, IBuiltInPermission):
    """
    Controls the ability to access key containers. This class cannot be inherited.
    
    KeyContainerPermission(flags: KeyContainerPermissionFlags)
    KeyContainerPermission(state: PermissionState)
    KeyContainerPermission(flags: KeyContainerPermissionFlags, accessList: Array[KeyContainerPermissionAccessEntry])
    """
    def Copy(self):
        """
        Copy(self: KeyContainerPermission) -> IPermission
        
            Creates and returns an identical copy of the current permission.
            Returns: A copy of the current permission.
        """
        pass

    def FromXml(self, securityElement):
        """
        FromXml(self: KeyContainerPermission, securityElement: SecurityElement)
            Reconstructs a permission with a specified state from an XML encoding.
        
            securityElement: A System.Security.SecurityElement that contains the XML encoding used to reconstruct the 
             permission.
        """
        pass

    def Intersect(self, target):
        """
        Intersect(self: KeyContainerPermission, target: IPermission) -> IPermission
        
            Creates and returns a permission that is the intersection of the current permission and the 
             specified permission.
        
        
            target: A permission to intersect with the current permission. It must be the same type as the current 
             permission.
        
            Returns: A new permission that represents the intersection of the current permission and the specified 
             permission. This new permission is null if the intersection is empty.
        """
        pass

    def IsSubsetOf(self, target):
        """
        IsSubsetOf(self: KeyContainerPermission, target: IPermission) -> bool
        
            Determines whether the current permission is a subset of the specified permission.
        
            target: A permission to test for the subset relationship. This permission must be the same type as the 
             current permission.
        
            Returns: true if the current permission is a subset of the specified permission; otherwise, false.
        """
        pass

    def IsUnrestricted(self):
        """
        IsUnrestricted(self: KeyContainerPermission) -> bool
        
            Determines whether the current permission is unrestricted.
            Returns: true if the current permission is unrestricted; otherwise, false.
        """
        pass

    def ToXml(self):
        """
        ToXml(self: KeyContainerPermission) -> SecurityElement
        
            Creates an XML encoding of the permission and its current state.
            Returns: A System.Security.SecurityElement that contains an XML encoding of the permission, including 
             state information.
        """
        pass

    def Union(self, target):
        """
        Union(self: KeyContainerPermission, target: IPermission) -> IPermission
        
            Creates a permission that is the union of the current permission and the specified permission.
        
            target: A permission to combine with the current permission. It must be of the same type as the current 
             permission.
        
            Returns: A new permission that represents the union of the current permission and the specified 
             permission.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, flags: KeyContainerPermissionFlags)
        __new__(cls: type, flags: KeyContainerPermissionFlags, accessList: Array[KeyContainerPermissionAccessEntry])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AccessEntries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of System.Security.Permissions.KeyContainerPermissionAccessEntry objects associated with the current permission.

Get: AccessEntries(self: KeyContainerPermission) -> KeyContainerPermissionAccessEntryCollection

"""

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the key container permission flags that apply to all key containers associated with the permission.

Get: Flags(self: KeyContainerPermission) -> KeyContainerPermissionFlags

"""



class KeyContainerPermissionAccessEntry(object):
    """
    Specifies access rights for specific key containers. This class cannot be inherited.
    
    KeyContainerPermissionAccessEntry(keyContainerName: str, flags: KeyContainerPermissionFlags)
    KeyContainerPermissionAccessEntry(parameters: CspParameters, flags: KeyContainerPermissionFlags)
    KeyContainerPermissionAccessEntry(keyStore: str, providerName: str, providerType: int, keyContainerName: str, keySpec: int, flags: KeyContainerPermissionFlags)
    """
    def Equals(self, o):
        """
        Equals(self: KeyContainerPermissionAccessEntry, o: object) -> bool
        
            Determines whether the specified System.Security.Permissions.KeyContainerPermissionAccessEntry 
             object is equal to the current instance.
        
        
            o: The System.Security.Permissions.KeyContainerPermissionAccessEntry object to compare with the 
             currentinstance.
        
            Returns: true if the specified System.Security.Permissions.KeyContainerPermissionAccessEntry is equal to 
             the current System.Security.Permissions.KeyContainerPermissionAccessEntry object; otherwise, 
             false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: KeyContainerPermissionAccessEntry) -> int
        
            Gets a hash code for the current instance that is suitable for use in hashing algorithms and 
             data structures such as a hash table.
        
            Returns: A hash code for the current System.Security.Permissions.KeyContainerPermissionAccessEntry object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, keyContainerName: str, flags: KeyContainerPermissionFlags)
        __new__(cls: type, parameters: CspParameters, flags: KeyContainerPermissionFlags)
        __new__(cls: type, keyStore: str, providerName: str, providerType: int, keyContainerName: str, keySpec: int, flags: KeyContainerPermissionFlags)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the key container permissions.

Get: Flags(self: KeyContainerPermissionAccessEntry) -> KeyContainerPermissionFlags

Set: Flags(self: KeyContainerPermissionAccessEntry) = value
"""

    KeyContainerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the key container name.

Get: KeyContainerName(self: KeyContainerPermissionAccessEntry) -> str

Set: KeyContainerName(self: KeyContainerPermissionAccessEntry) = value
"""

    KeySpec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the key specification.

Get: KeySpec(self: KeyContainerPermissionAccessEntry) -> int

Set: KeySpec(self: KeyContainerPermissionAccessEntry) = value
"""

    KeyStore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the key store.

Get: KeyStore(self: KeyContainerPermissionAccessEntry) -> str

Set: KeyStore(self: KeyContainerPermissionAccessEntry) = value
"""

    ProviderName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the provider name.

Get: ProviderName(self: KeyContainerPermissionAccessEntry) -> str

Set: ProviderName(self: KeyContainerPermissionAccessEntry) = value
"""

    ProviderType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the provider type.

Get: ProviderType(self: KeyContainerPermissionAccessEntry) -> int

Set: ProviderType(self: KeyContainerPermissionAccessEntry) = value
"""



class KeyContainerPermissionAccessEntryCollection(object, ICollection, IEnumerable):
    """ Represents a collection of System.Security.Permissions.KeyContainerPermissionAccessEntry objects. This class cannot be inherited. """
    def Add(self, accessEntry):
        """
        Add(self: KeyContainerPermissionAccessEntryCollection, accessEntry: KeyContainerPermissionAccessEntry) -> int
        
            Adds a System.Security.Permissions.KeyContainerPermissionAccessEntry object to the collection.
        
            accessEntry: The System.Security.Permissions.KeyContainerPermissionAccessEntry object to add.
            Returns: The index at which the new element was inserted.
        """
        pass

    def Clear(self):
        """
        Clear(self: KeyContainerPermissionAccessEntryCollection)
            Removes all the System.Security.Permissions.KeyContainerPermissionAccessEntry objects from the 
             collection.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: KeyContainerPermissionAccessEntryCollection, array: Array[KeyContainerPermissionAccessEntry], index: int)
            Copies the elements of the collection to a compatible one-dimensional array, starting at the 
             specified index of the target array.
        
        
            array: The one-dimensional System.Security.Permissions.KeyContainerPermissionAccessEntry array that is 
             the destination of the elements copied from the current collection.
        
            index: The index in array at which copying begins.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: KeyContainerPermissionAccessEntryCollection) -> KeyContainerPermissionAccessEntryEnumerator
        
            Returns a System.Security.Permissions.KeyContainerPermissionAccessEntryEnumerator object that 
             can be used to iterate through the objects in the collection.
        
            Returns: A System.Security.Permissions.KeyContainerPermissionAccessEntryEnumerator object that can be 
             used to iterate through the collection.
        """
        pass

    def IndexOf(self, accessEntry):
        """
        IndexOf(self: KeyContainerPermissionAccessEntryCollection, accessEntry: KeyContainerPermissionAccessEntry) -> int
        
            Gets the index in the collection of the specified 
             System.Security.Permissions.KeyContainerPermissionAccessEntry object, if it exists in the 
             collection.
        
        
            accessEntry: The System.Security.Permissions.KeyContainerPermissionAccessEntry object to locate.
            Returns: The index of the specified System.Security.Permissions.KeyContainerPermissionAccessEntry object 
                """
        pass

    def Remove(self, accessEntry):
        """
        Remove(self: KeyContainerPermissionAccessEntryCollection, accessEntry: KeyContainerPermissionAccessEntry)
            Removes the specified System.Security.Permissions.KeyContainerPermissionAccessEntry object from 
             thecollection.
        
        
            accessEntry: The System.Security.Permissions.KeyContainerPermissionAccessEntry object to remove.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of items in the collection.

Get: Count(self: KeyContainerPermissionAccessEntryCollection) -> int

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the collection is synchronized (thread safe).

Get: IsSynchronized(self: KeyContainerPermissionAccessEntryCollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an object that can be used to synchronize access to the collection.

Get: SyncRoot(self: KeyContainerPermissionAccessEntryCollection) -> object

"""



class KeyContainerPermissionAccessEntryEnumerator(object, IEnumerator):
    """ Represents the enumerator for System.Security.Permissions.KeyContainerPermissionAccessEntry objects in a System.Security.Permissions.KeyContainerPermissionAccessEntryCollection. """
    def MoveNext(self):
        """
        MoveNext(self: KeyContainerPermissionAccessEntryEnumerator) -> bool
        
            Moves to the next element in the collection.
            Returns: true if the enumerator was successfully advanced to the next element; false if the enumerator 
             has passed the end of the collection.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def Reset(self):
        """
        Reset(self: KeyContainerPermissionAccessEntryEnumerator)
            Resets the enumerator to the beginning of the collection.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current entry in the collection.

Get: Current(self: KeyContainerPermissionAccessEntryEnumerator) -> KeyContainerPermissionAccessEntry

"""



class KeyContainerPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """
    Allows security actions for System.Security.Permissions.KeyContainerPermission to be applied to code using declarative security. This class cannot be inherited.
    
    KeyContainerPermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: KeyContainerPermissionAttribute) -> IPermission
        
            Creates and returns a new System.Security.Permissions.KeyContainerPermission.
            Returns: A System.Security.Permissions.KeyContainerPermission that corresponds to the attribute.
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

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the key container permissions.

Get: Flags(self: KeyContainerPermissionAttribute) -> KeyContainerPermissionFlags

Set: Flags(self: KeyContainerPermissionAttribute) = value
"""

    KeyContainerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the key container.

Get: KeyContainerName(self: KeyContainerPermissionAttribute) -> str

Set: KeyContainerName(self: KeyContainerPermissionAttribute) = value
"""

    KeySpec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the key specification.

Get: KeySpec(self: KeyContainerPermissionAttribute) -> int

Set: KeySpec(self: KeyContainerPermissionAttribute) = value
"""

    KeyStore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the key store.

Get: KeyStore(self: KeyContainerPermissionAttribute) -> str

Set: KeyStore(self: KeyContainerPermissionAttribute) = value
"""

    ProviderName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the provider name.

Get: ProviderName(self: KeyContainerPermissionAttribute) -> str

Set: ProviderName(self: KeyContainerPermissionAttribute) = value
"""

    ProviderType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the provider type.

Get: ProviderType(self: KeyContainerPermissionAttribute) -> int

Set: ProviderType(self: KeyContainerPermissionAttribute) = value
"""



class KeyContainerPermissionFlags(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of key container access allowed.
    
    enum (flags) KeyContainerPermissionFlags, values: AllFlags (13111), ChangeAcl (8192), Create (1), Decrypt (512), Delete (4), Export (32), Import (16), NoFlags (0), Open (2), Sign (256), ViewAcl (4096)
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

    AllFlags = None
    ChangeAcl = None
    Create = None
    Decrypt = None
    Delete = None
    Export = None
    Import = None
    NoFlags = None
    Open = None
    Sign = None
    value__ = None
    ViewAcl = None


class PermissionSetAttribute(CodeAccessSecurityAttribute, _Attribute):
    """
    Allows security actions for a System.Security.PermissionSet to be applied to code using declarative security. This class cannot be inherited.
    
    PermissionSetAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: PermissionSetAttribute) -> IPermission
        
            Creates and returns a new System.Security.IPermission.
            Returns: A new System.Security.IPermission.
        """
        pass

    def CreatePermissionSet(self):
        """
        CreatePermissionSet(self: PermissionSetAttribute) -> PermissionSet
        
            Creates and returns a new System.Security.PermissionSet.
            Returns: A new System.Security.PermissionSet.
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

    File = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a file containing the XML representation of a custom permission set to be declared.

Get: File(self: PermissionSetAttribute) -> str

Set: File(self: PermissionSetAttribute) = value
"""

    Hex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the hexadecimal representation of the XML encoded permission set.

Get: Hex(self: PermissionSetAttribute) -> str

Set: Hex(self: PermissionSetAttribute) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the permission set.

Get: Name(self: PermissionSetAttribute) -> str

Set: Name(self: PermissionSetAttribute) = value
"""

    UnicodeEncoded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the file specified by System.Security.Permissions.PermissionSetAttribute.File is Unicode or ASCII encoded.

Get: UnicodeEncoded(self: PermissionSetAttribute) -> bool

Set: UnicodeEncoded(self: PermissionSetAttribute) = value
"""

    XML = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the XML representation of a permission set.

Get: XML(self: PermissionSetAttribute) -> str

Set: XML(self: PermissionSetAttribute) = value
"""



class PermissionState(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies whether a permission should have all or no access to resources at creation.
    
    enum PermissionState, values: None (0), Unrestricted (1)
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

    None = None
    Unrestricted = None
    value__ = None


class PrincipalPermission(object, IPermission, ISecurityEncodable, IUnrestrictedPermission, IBuiltInPermission):
    """
    Allows checks against the active principal (see System.Security.Principal.IPrincipal) using the language constructs defined for both declarative and imperative security actions. This class cannot be inherited.
    
    PrincipalPermission(state: PermissionState)
    PrincipalPermission(name: str, role: str)
    PrincipalPermission(name: str, role: str, isAuthenticated: bool)
    """
    def Copy(self):
        """
        Copy(self: PrincipalPermission) -> IPermission
        
            Creates and returns an identical copy of the current permission.
            Returns: A copy of the current permission.
        """
        pass

    def Demand(self):
        """
        Demand(self: PrincipalPermission)
            Determines at run time whether the current principal matches the principal specified by the 
             current permission.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: PrincipalPermission, obj: object) -> bool
        
            Determines whether the specified System.Security.Permissions.PrincipalPermission object is equal 
             to the current System.Security.Permissions.PrincipalPermission.
        
        
            obj: The System.Security.Permissions.PrincipalPermission object to compare with the current 
             System.Security.Permissions.PrincipalPermission.
        
            Returns: true if the specified System.Security.Permissions.PrincipalPermission is equal to the current 
             System.Security.Permissions.PrincipalPermission object; otherwise, false.
        """
        pass

    def FromXml(self, elem):
        """
        FromXml(self: PrincipalPermission, elem: SecurityElement)
            Reconstructs a permission with a specified state from an XML encoding.
        
            elem: The XML encoding to use to reconstruct the permission.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PrincipalPermission) -> int
        
            Gets a hash code for the System.Security.Permissions.PrincipalPermission object that is suitable 
             for use in hashing algorithms and data structures such as a hash table.
        
            Returns: A hash code for the current System.Security.Permissions.PrincipalPermission object.
        """
        pass

    def Intersect(self, target):
        """
        Intersect(self: PrincipalPermission, target: IPermission) -> IPermission
        
            Creates and returns a permission that is the intersection of the current permission and the 
             specified permission.
        
        
            target: A permission to intersect with the current permission. It must be of the same type as the 
             current permission.
        
            Returns: A new permission that represents the intersection of the current permission and the specified 
             permission. This new permission will be null if the intersection is empty.
        """
        pass

    def IsSubsetOf(self, target):
        """
        IsSubsetOf(self: PrincipalPermission, target: IPermission) -> bool
        
            Determines whether the current permission is a subset of the specified permission.
        
            target: The permission that is to be tested for the subset relationship. This permission must be of the 
             same type as the current permission.
        
            Returns: true if the current permission is a subset of the specified permission; otherwise, false.
        """
        pass

    def IsUnrestricted(self):
        """
        IsUnrestricted(self: PrincipalPermission) -> bool
        
            Returns a value indicating whether the current permission is unrestricted.
            Returns: true if the current permission is unrestricted; otherwise, false.
        """
        pass

    def ToString(self):
        """
        ToString(self: PrincipalPermission) -> str
        
            Creates and returns a string representing the current permission.
            Returns: A representation of the current permission.
        """
        pass

    def ToXml(self):
        """
        ToXml(self: PrincipalPermission) -> SecurityElement
        
            Creates an XML encoding of the permission and its current state.
            Returns: An XML encoding of the permission, including any state information.
        """
        pass

    def Union(self, other):
        """
        Union(self: PrincipalPermission, other: IPermission) -> IPermission
        
            Creates a permission that is the union of the current permission and the specified permission.
        
            other: A permission to combine with the current permission. This must be of the same type as the 
             current permission.
        
            Returns: A new permission that represents the union of the current permission and the specified 
             permission.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, name: str, role: str)
        __new__(cls: type, name: str, role: str, isAuthenticated: bool)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class PrincipalPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """
    Allows security actions for the System.Security.Permissions.PrincipalPermission class to be applied to code by using declarative security. This class cannot be inherited.
    
    PrincipalPermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: PrincipalPermissionAttribute) -> IPermission
        
            Creates and returns a new System.Security.Permissions.PrincipalPermission object.
            Returns: An object  that corresponds to this attribute.
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

    Authenticated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the current principal has been authenticated by the underlying role-based security provider.

Get: Authenticated(self: PrincipalPermissionAttribute) -> bool

Set: Authenticated(self: PrincipalPermissionAttribute) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the identity associated with the current principal.

Get: Name(self: PrincipalPermissionAttribute) -> str

Set: Name(self: PrincipalPermissionAttribute) = value
"""

    Role = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets membership in a specified security role.

Get: Role(self: PrincipalPermissionAttribute) -> str

Set: Role(self: PrincipalPermissionAttribute) = value
"""



class PublisherIdentityPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IBuiltInPermission):
    """
    Represents the identity of a software publisher. This class cannot be inherited.
    
    PublisherIdentityPermission(state: PermissionState)
    PublisherIdentityPermission(certificate: X509Certificate)
    """
    def Copy(self):
        """
        Copy(self: PublisherIdentityPermission) -> IPermission
        
            Creates and returns an identical copy of the current permission.
            Returns: A copy of the current permission.
        """
        pass

    def FromXml(self, esd):
        """
        FromXml(self: PublisherIdentityPermission, esd: SecurityElement)
            Reconstructs a permission with a specified state from an XML encoding.
        
            esd: The XML encoding to use to reconstruct the permission.
        """
        pass

    def Intersect(self, target):
        """
        Intersect(self: PublisherIdentityPermission, target: IPermission) -> IPermission
        
            Creates and returns a permission that is the intersection of the current permission and the 
             specified permission.
        
        
            target: A permission to intersect with the current permission. It must be of the same type as the 
             current permission.
        
            Returns: A new permission that represents the intersection of the current permission and the specified 
             permission. This new permission is null if the intersection is empty.
        """
        pass

    def IsSubsetOf(self, target):
        """
        IsSubsetOf(self: PublisherIdentityPermission, target: IPermission) -> bool
        
            Determines whether the current permission is a subset of the specified permission.
        
            target: A permission that is to be tested for the subset relationship. This permission must be of the 
             same type as the current permission.
        
            Returns: true if the current permission is a subset of the specified permission; otherwise, false.
        """
        pass

    def ToXml(self):
        """
        ToXml(self: PublisherIdentityPermission) -> SecurityElement
        
            Creates an XML encoding of the permission and its current state.
            Returns: An XML encoding of the permission, including any state information.
        """
        pass

    def Union(self, target):
        """
        Union(self: PublisherIdentityPermission, target: IPermission) -> IPermission
        
            Creates a permission that is the union of the current permission and the specified permission.
        
            target: A permission to combine with the current permission. It must be of the same type as the current 
             permission.
        
            Returns: A new permission that represents the union of the current permission and the specified 
             permission.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, certificate: X509Certificate)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Certificate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an Authenticode X.509v3 certificate that represents the identity of the software publisher.

Get: Certificate(self: PublisherIdentityPermission) -> X509Certificate

Set: Certificate(self: PublisherIdentityPermission) = value
"""



class PublisherIdentityPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """
    Allows security actions for System.Security.Permissions.PublisherIdentityPermission to be applied to code using declarative security. This class cannot be inherited.
    
    PublisherIdentityPermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: PublisherIdentityPermissionAttribute) -> IPermission
        
            Creates and returns a new instance of System.Security.Permissions.PublisherIdentityPermission.
            Returns: A System.Security.Permissions.PublisherIdentityPermission that corresponds to this attribute.
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

    CertFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a certification file containing an Authenticode X.509v3 certificate.

Get: CertFile(self: PublisherIdentityPermissionAttribute) -> str

Set: CertFile(self: PublisherIdentityPermissionAttribute) = value
"""

    SignedFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a signed file from which to extract an Authenticode X.509v3 certificate.

Get: SignedFile(self: PublisherIdentityPermissionAttribute) -> str

Set: SignedFile(self: PublisherIdentityPermissionAttribute) = value
"""

    X509Certificate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an Authenticode X.509v3 certificate that identifies the publisher of the calling code.

Get: X509Certificate(self: PublisherIdentityPermissionAttribute) -> str

Set: X509Certificate(self: PublisherIdentityPermissionAttribute) = value
"""



class ReflectionPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission, IBuiltInPermission):
    """
    Controls access to non-public types and members through the System.Reflection APIs. Controls some features of the System.Reflection.Emit APIs.
    
    ReflectionPermission(state: PermissionState)
    ReflectionPermission(flag: ReflectionPermissionFlag)
    """
    def Copy(self):
        """
        Copy(self: ReflectionPermission) -> IPermission
        
            Creates and returns an identical copy of the current permission.
            Returns: A copy of the current permission.
        """
        pass

    def FromXml(self, esd):
        """
        FromXml(self: ReflectionPermission, esd: SecurityElement)
            Reconstructs a permission with a specified state from an XML encoding.
        
            esd: The XML encoding to use to reconstruct the permission.
        """
        pass

    def Intersect(self, target):
        """
        Intersect(self: ReflectionPermission, target: IPermission) -> IPermission
        
            Creates and returns a permission that is the intersection of the current permission and the 
             specified permission.
        
        
            target: A permission to intersect with the current permission. It must be of the same type as the 
             current permission.
        
            Returns: A new permission that represents the intersection of the current permission and the specified 
             permission. This new permission is null if the intersection is empty.
        """
        pass

    def IsSubsetOf(self, target):
        """
        IsSubsetOf(self: ReflectionPermission, target: IPermission) -> bool
        
            Determines whether the current permission is a subset of the specified permission.
        
            target: A permission that is to be tested for the subset relationship. This permission must be of the 
             same type as the current permission.
        
            Returns: true if the current permission is a subset of the specified permission; otherwise, false.
        """
        pass

    def IsUnrestricted(self):
        """
        IsUnrestricted(self: ReflectionPermission) -> bool
        
            Returns a value indicating whether the current permission is unrestricted.
            Returns: true if the current permission is unrestricted; otherwise, false.
        """
        pass

    def ToXml(self):
        """
        ToXml(self: ReflectionPermission) -> SecurityElement
        
            Creates an XML encoding of the permission and its current state.
            Returns: An XML encoding of the permission, including any state information.
        """
        pass

    def Union(self, other):
        """
        Union(self: ReflectionPermission, other: IPermission) -> IPermission
        
            Creates a permission that is the union of the current permission and the specified permission.
        
            other: A permission to combine with the current permission. It must be of the same type as the current 
             permission.
        
            Returns: A new permission that represents the union of the current permission and the specified 
             permission.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, flag: ReflectionPermissionFlag)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type of reflection allowed for the current permission.

Get: Flags(self: ReflectionPermission) -> ReflectionPermissionFlag

Set: Flags(self: ReflectionPermission) = value
"""



class ReflectionPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """
    Allows security actions for System.Security.Permissions.ReflectionPermission to be applied to code using declarative security.
    
    ReflectionPermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: ReflectionPermissionAttribute) -> IPermission
        
            Creates and returns a new System.Security.Permissions.ReflectionPermission.
            Returns: A System.Security.Permissions.ReflectionPermission that corresponds to this attribute.
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

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current allowed uses of reflection.

Get: Flags(self: ReflectionPermissionAttribute) -> ReflectionPermissionFlag

Set: Flags(self: ReflectionPermissionAttribute) = value
"""

    MemberAccess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether invocation of operations on non-public members is allowed.

Get: MemberAccess(self: ReflectionPermissionAttribute) -> bool

Set: MemberAccess(self: ReflectionPermissionAttribute) = value
"""

    ReflectionEmit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether use of certain features in System.Reflection.Emit, such as emitting debug symbols, is allowed.

Get: ReflectionEmit(self: ReflectionPermissionAttribute) -> bool

Set: ReflectionEmit(self: ReflectionPermissionAttribute) = value
"""

    RestrictedMemberAccess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether restricted invocation of non-public members is allowed. Restricted invocation means that the grant set of the assembly that contains the non-public member that is being invoked must be equal to, or a subset of, the grant set of the invoking assembly.

Get: RestrictedMemberAccess(self: ReflectionPermissionAttribute) -> bool

Set: RestrictedMemberAccess(self: ReflectionPermissionAttribute) = value
"""

    TypeInformation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether reflection on members that are not visible is allowed.

Get: TypeInformation(self: ReflectionPermissionAttribute) -> bool

Set: TypeInformation(self: ReflectionPermissionAttribute) = value
"""



class ReflectionPermissionFlag(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the permitted use of the System.Reflection and System.Reflection.Emit namespaces.
    
    enum (flags) ReflectionPermissionFlag, values: AllFlags (7), MemberAccess (2), NoFlags (0), ReflectionEmit (4), RestrictedMemberAccess (8), TypeInformation (1)
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

    AllFlags = None
    MemberAccess = None
    NoFlags = None
    ReflectionEmit = None
    RestrictedMemberAccess = None
    TypeInformation = None
    value__ = None


class RegistryPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission, IBuiltInPermission):
    """
    Controls the ability to access registry variables. This class cannot be inherited.
    
    RegistryPermission(state: PermissionState)
    RegistryPermission(access: RegistryPermissionAccess, pathList: str)
    RegistryPermission(access: RegistryPermissionAccess, control: AccessControlActions, pathList: str)
    """
    def AddPathList(self, access, *__args):
        """
        AddPathList(self: RegistryPermission, access: RegistryPermissionAccess, control: AccessControlActions, pathList: str)
            Adds access for the specified registry variables to the existing state of the permission, 
             specifying registry permission access and access control actions.
        
        
            access: One of the System.Security.Permissions.RegistryPermissionAccess values.
            control: One of the System.Security.AccessControl.AccessControlActions values.
            pathList: A list of registry variables (separated by semicolons).
        AddPathList(self: RegistryPermission, access: RegistryPermissionAccess, pathList: str)
            Adds access for the specified registry variables to the existing state of the permission.
        
            access: One of the System.Security.Permissions.RegistryPermissionAccess values.
            pathList: A list of registry variables (semicolon-separated).
        """
        pass

    def Copy(self):
        """
        Copy(self: RegistryPermission) -> IPermission
        
            Creates and returns an identical copy of the current permission.
            Returns: A copy of the current permission.
        """
        pass

    def FromXml(self, esd):
        """
        FromXml(self: RegistryPermission, esd: SecurityElement)
            Reconstructs a permission with a specified state from an XML encoding.
        
            esd: The XML encoding to use to reconstruct the permission.
        """
        pass

    def GetPathList(self, access):
        """
        GetPathList(self: RegistryPermission, access: RegistryPermissionAccess) -> str
        
            Gets paths for all registry variables with the specified 
             System.Security.Permissions.RegistryPermissionAccess.
        
        
            access: One of the System.Security.Permissions.RegistryPermissionAccess values that represents a single 
             type of registry variable access.
        
            Returns: A list of the registry variables (semicolon-separated) with the specified 
             System.Security.Permissions.RegistryPermissionAccess.
        """
        pass

    def Intersect(self, target):
        """
        Intersect(self: RegistryPermission, target: IPermission) -> IPermission
        
            Creates and returns a permission that is the intersection of the current permission and the 
             specified permission.
        
        
            target: A permission to intersect with the current permission. It must be of the same type as the 
             current permission.
        
            Returns: A new permission that represents the intersection of the current permission and the specified 
             permission. This new permission is null if the intersection is empty.
        """
        pass

    def IsSubsetOf(self, target):
        """
        IsSubsetOf(self: RegistryPermission, target: IPermission) -> bool
        
            Determines whether the current permission is a subset of the specified permission.
        
            target: A permission that is to be tested for the subset relationship. This permission must be of the 
             same type as the current permission.
        
            Returns: true if the current permission is a subset of the specified permission; otherwise, false.
        """
        pass

    def IsUnrestricted(self):
        """
        IsUnrestricted(self: RegistryPermission) -> bool
        
            Returns a value indicating whether the current permission is unrestricted.
            Returns: true if the current permission is unrestricted; otherwise, false.
        """
        pass

    def SetPathList(self, access, pathList):
        """
        SetPathList(self: RegistryPermission, access: RegistryPermissionAccess, pathList: str)
            Sets new access for the specified registry variable names to the existing state of the 
             permission.
        
        
            access: One of the System.Security.Permissions.RegistryPermissionAccess values.
            pathList: A list of registry variables (semicolon-separated).
        """
        pass

    def ToXml(self):
        """
        ToXml(self: RegistryPermission) -> SecurityElement
        
            Creates an XML encoding of the permission and its current state.
            Returns: An XML encoding of the permission, including any state information.
        """
        pass

    def Union(self, other):
        """
        Union(self: RegistryPermission, other: IPermission) -> IPermission
        
            Creates a permission that is the union of the current permission and the specified permission.
        
            other: A permission to combine with the current permission. It must be of the same type as the current 
             permission.
        
            Returns: A new permission that represents the union of the current permission and the specified 
             permission.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, access: RegistryPermissionAccess, pathList: str)
        __new__(cls: type, access: RegistryPermissionAccess, control: AccessControlActions, pathList: str)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class RegistryPermissionAccess(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the permitted access to registry keys and values.
    
    enum (flags) RegistryPermissionAccess, values: AllAccess (7), Create (4), NoAccess (0), Read (1), Write (2)
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

    AllAccess = None
    Create = None
    NoAccess = None
    Read = None
    value__ = None
    Write = None


class RegistryPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """
    Allows security actions for System.Security.Permissions.RegistryPermission to be applied to code using declarative security. This class cannot be inherited.
    
    RegistryPermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: RegistryPermissionAttribute) -> IPermission
        
            Creates and returns a new System.Security.Permissions.RegistryPermission.
            Returns: A System.Security.Permissions.RegistryPermission that corresponds to this attribute.
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

    All = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets full access for the specified registry keys.

Get: All(self: RegistryPermissionAttribute) -> str

Set: All(self: RegistryPermissionAttribute) = value
"""

    ChangeAccessControl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets change access control for the specified registry keys.

Get: ChangeAccessControl(self: RegistryPermissionAttribute) -> str

Set: ChangeAccessControl(self: RegistryPermissionAttribute) = value
"""

    Create = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets create-level access for the specified registry keys.

Get: Create(self: RegistryPermissionAttribute) -> str

Set: Create(self: RegistryPermissionAttribute) = value
"""

    Read = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets read access for the specified registry keys.

Get: Read(self: RegistryPermissionAttribute) -> str

Set: Read(self: RegistryPermissionAttribute) = value
"""

    ViewAccessControl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets view access control for the specified registry keys.

Get: ViewAccessControl(self: RegistryPermissionAttribute) -> str

Set: ViewAccessControl(self: RegistryPermissionAttribute) = value
"""

    ViewAndModify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a specified set of registry keys that can be viewed and modified.

Get: ViewAndModify(self: RegistryPermissionAttribute) -> str

Set: ViewAndModify(self: RegistryPermissionAttribute) = value
"""

    Write = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets write access for the specified registry keys.

Get: Write(self: RegistryPermissionAttribute) -> str

Set: Write(self: RegistryPermissionAttribute) = value
"""



class ResourcePermissionBase(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission):
    """ Allows control of code access security permissions. """
    def AddPermissionAccess(self, *args): #cannot find CLR method
        """
        AddPermissionAccess(self: ResourcePermissionBase, entry: ResourcePermissionBaseEntry)
            Adds a permission entry to the permission.
        
            entry: The System.Security.Permissions.ResourcePermissionBaseEntry to add.
        """
        pass

    def Clear(self, *args): #cannot find CLR method
        """
        Clear(self: ResourcePermissionBase)
            Clears the permission of the added permission entries.
        """
        pass

    def Copy(self):
        """
        Copy(self: ResourcePermissionBase) -> IPermission
        
            Creates and returns an identical copy of the current permission object.
            Returns: A copy of the current permission object.
        """
        pass

    def FromXml(self, securityElement):
        """
        FromXml(self: ResourcePermissionBase, securityElement: SecurityElement)
            Reconstructs a security object with a specified state from an XML encoding.
        
            securityElement: The XML encoding to use to reconstruct the security object.
        """
        pass

    def GetPermissionEntries(self, *args): #cannot find CLR method
        """
        GetPermissionEntries(self: ResourcePermissionBase) -> Array[ResourcePermissionBaseEntry]
        
            Returns an array of the System.Security.Permissions.ResourcePermissionBaseEntry objects added to 
             this permission.
        
            Returns: An array of System.Security.Permissions.ResourcePermissionBaseEntry objects that were added to 
             this permission.
        """
        pass

    def Intersect(self, target):
        """
        Intersect(self: ResourcePermissionBase, target: IPermission) -> IPermission
        
            Creates and returns a permission object that is the intersection of the current permission 
             object and a target permission object.
        
        
            target: A permission object of the same type as the current permission object.
            Returns: A new permission object that represents the intersection of the current object and the specified 
             target. This object is null if the intersection is empty.
        """
        pass

    def IsSubsetOf(self, target):
        """
        IsSubsetOf(self: ResourcePermissionBase, target: IPermission) -> bool
        
            Determines whether the current permission object is a subset of the specified permission.
        
            target: A permission object that is to be tested for the subset relationship.
            Returns: true if the current permission object is a subset of the specified permission object; otherwise, 
             false.
        """
        pass

    def IsUnrestricted(self):
        """
        IsUnrestricted(self: ResourcePermissionBase) -> bool
        
            Gets a value indicating whether the permission is unrestricted.
            Returns: true if permission is unrestricted; otherwise, false.
        """
        pass

    def RemovePermissionAccess(self, *args): #cannot find CLR method
        """
        RemovePermissionAccess(self: ResourcePermissionBase, entry: ResourcePermissionBaseEntry)
            Removes a permission entry from the permission.
        
            entry: The System.Security.Permissions.ResourcePermissionBaseEntry to remove.
        """
        pass

    def ToXml(self):
        """
        ToXml(self: ResourcePermissionBase) -> SecurityElement
        
            Creates and returns an XML encoding of the security object and its current state.
            Returns: An XML encoding of the security object, including any state information.
        """
        pass

    def Union(self, target):
        """
        Union(self: ResourcePermissionBase, target: IPermission) -> IPermission
        
            Creates a permission object that combines the current permission object and the target 
             permission object.
        
        
            target: A permission object to combine with the current permission object. It must be of the same type 
             as the current permission object.
        
            Returns: A new permission object that represents the union of the current permission object and the 
             specified permission object.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, state: PermissionState)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    PermissionAccessType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an enumeration value that describes the types of access that you are giving the resource.

"""

    TagNames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an array of strings that identify the resource you are protecting.

"""


    Any = '*'
    Local = '.'


class ResourcePermissionBaseEntry(object):
    """
    Defines the smallest unit of a code access security permission set.
    
    ResourcePermissionBaseEntry(permissionAccess: int, permissionAccessPath: Array[str])
    ResourcePermissionBaseEntry()
    """
    @staticmethod # known case of __new__
    def __new__(self, permissionAccess=None, permissionAccessPath=None):
        """
        __new__(cls: type)
        __new__(cls: type, permissionAccess: int, permissionAccessPath: Array[str])
        """
        pass

    PermissionAccess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an integer representation of the access level enumeration value.

Get: PermissionAccess(self: ResourcePermissionBaseEntry) -> int

"""

    PermissionAccessPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an array of strings that identify the resource you are protecting.

Get: PermissionAccessPath(self: ResourcePermissionBaseEntry) -> Array[str]

"""



class SecurityAction(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the security actions that can be performed using declarative security.
    
    enum SecurityAction, values: Assert (3), Demand (2), Deny (4), InheritanceDemand (7), LinkDemand (6), PermitOnly (5), RequestMinimum (8), RequestOptional (9), RequestRefuse (10)
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

    Assert = None
    Demand = None
    Deny = None
    InheritanceDemand = None
    LinkDemand = None
    PermitOnly = None
    RequestMinimum = None
    RequestOptional = None
    RequestRefuse = None
    value__ = None


class SecurityPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission, IBuiltInPermission):
    """
    Describes a set of security permissions applied to code. This class cannot be inherited.
    
    SecurityPermission(state: PermissionState)
    SecurityPermission(flag: SecurityPermissionFlag)
    """
    def Copy(self):
        """
        Copy(self: SecurityPermission) -> IPermission
        
            Creates and returns an identical copy of the current permission.
            Returns: A copy of the current permission.
        """
        pass

    def FromXml(self, esd):
        """
        FromXml(self: SecurityPermission, esd: SecurityElement)
            Reconstructs a permission with a specified state from an XML encoding.
        
            esd: The XML encoding to use to reconstruct the permission.
        """
        pass

    def Intersect(self, target):
        """
        Intersect(self: SecurityPermission, target: IPermission) -> IPermission
        
            Creates and returns a permission that is the intersection of the current permission and the 
             specified permission.
        
        
            target: A permission to intersect with the current permission. It must be of the same type as the 
             current permission.
        
            Returns: A new permission object that represents the intersection of the current permission and the 
             specified permission. This new permission is null if the intersection is empty.
        """
        pass

    def IsSubsetOf(self, target):
        """
        IsSubsetOf(self: SecurityPermission, target: IPermission) -> bool
        
            Determines whether the current permission is a subset of the specified permission.
        
            target: A permission that is to be tested for the subset relationship. This permission must be of the 
             same type as the current permission.
        
            Returns: true if the current permission is a subset of the specified permission; otherwise, false.
        """
        pass

    def IsUnrestricted(self):
        """
        IsUnrestricted(self: SecurityPermission) -> bool
        
            Returns a value indicating whether the current permission is unrestricted.
            Returns: true if the current permission is unrestricted; otherwise, false.
        """
        pass

    def ToXml(self):
        """
        ToXml(self: SecurityPermission) -> SecurityElement
        
            Creates an XML encoding of the permission and its current state.
            Returns: An XML encoding of the permission, including any state information.
        """
        pass

    def Union(self, target):
        """
        Union(self: SecurityPermission, target: IPermission) -> IPermission
        
            Creates a permission that is the union of the current permission and the specified permission.
        
            target: A permission to combine with the current permission. It must be of the same type as the current 
             permission.
        
            Returns: A new permission that represents the union of the current permission and the specified 
             permission.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, flag: SecurityPermissionFlag)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the security permission flags.

Get: Flags(self: SecurityPermission) -> SecurityPermissionFlag

Set: Flags(self: SecurityPermission) = value
"""



class SecurityPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """
    Allows security actions for System.Security.Permissions.SecurityPermission to be applied to code using declarative security. This class cannot be inherited.
    
    SecurityPermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: SecurityPermissionAttribute) -> IPermission
        
            Creates and returns a new System.Security.Permissions.SecurityPermission.
            Returns: A System.Security.Permissions.SecurityPermission that corresponds to this attribute.
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

    Assertion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether permission to assert that all this code's callers have the requisite permission for the operation is declared.

Get: Assertion(self: SecurityPermissionAttribute) -> bool

Set: Assertion(self: SecurityPermissionAttribute) = value
"""

    BindingRedirects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether code has permission to perform binding redirection in the application configuration file.

Get: BindingRedirects(self: SecurityPermissionAttribute) -> bool

Set: BindingRedirects(self: SecurityPermissionAttribute) = value
"""

    ControlAppDomain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether permission to manipulate System.AppDomain is declared.

Get: ControlAppDomain(self: SecurityPermissionAttribute) -> bool

Set: ControlAppDomain(self: SecurityPermissionAttribute) = value
"""

    ControlDomainPolicy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether permission to alter or manipulate domain security policy is declared.

Get: ControlDomainPolicy(self: SecurityPermissionAttribute) -> bool

Set: ControlDomainPolicy(self: SecurityPermissionAttribute) = value
"""

    ControlEvidence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether permission to alter or manipulate evidence is declared.

Get: ControlEvidence(self: SecurityPermissionAttribute) -> bool

Set: ControlEvidence(self: SecurityPermissionAttribute) = value
"""

    ControlPolicy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether permission to view and manipulate security policy is declared.

Get: ControlPolicy(self: SecurityPermissionAttribute) -> bool

Set: ControlPolicy(self: SecurityPermissionAttribute) = value
"""

    ControlPrincipal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether permission to manipulate the current principal is declared.

Get: ControlPrincipal(self: SecurityPermissionAttribute) -> bool

Set: ControlPrincipal(self: SecurityPermissionAttribute) = value
"""

    ControlThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether permission to manipulate threads is declared.

Get: ControlThread(self: SecurityPermissionAttribute) -> bool

Set: ControlThread(self: SecurityPermissionAttribute) = value
"""

    Execution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether permission to execute code is declared.

Get: Execution(self: SecurityPermissionAttribute) -> bool

Set: Execution(self: SecurityPermissionAttribute) = value
"""

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets all permission flags comprising the System.Security.Permissions.SecurityPermission permissions.

Get: Flags(self: SecurityPermissionAttribute) -> SecurityPermissionFlag

Set: Flags(self: SecurityPermissionAttribute) = value
"""

    Infrastructure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether code can plug into the common language runtime infrastructure, such as adding Remoting Context Sinks, Envoy Sinks and Dynamic Sinks.

Get: Infrastructure(self: SecurityPermissionAttribute) -> bool

Set: Infrastructure(self: SecurityPermissionAttribute) = value
"""

    RemotingConfiguration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether code can configure remoting types and channels.

Get: RemotingConfiguration(self: SecurityPermissionAttribute) -> bool

Set: RemotingConfiguration(self: SecurityPermissionAttribute) = value
"""

    SerializationFormatter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether code can use a serialization formatter to serialize or deserialize an object.

Get: SerializationFormatter(self: SecurityPermissionAttribute) -> bool

Set: SerializationFormatter(self: SecurityPermissionAttribute) = value
"""

    SkipVerification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether permission to bypass code verification is declared.

Get: SkipVerification(self: SecurityPermissionAttribute) -> bool

Set: SkipVerification(self: SecurityPermissionAttribute) = value
"""

    UnmanagedCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether permission to call unmanaged code is declared.

Get: UnmanagedCode(self: SecurityPermissionAttribute) -> bool

Set: UnmanagedCode(self: SecurityPermissionAttribute) = value
"""



class SecurityPermissionFlag(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies access flags for the security permission object.
    
    enum (flags) SecurityPermissionFlag, values: AllFlags (16383), Assertion (1), BindingRedirects (8192), ControlAppDomain (1024), ControlDomainPolicy (256), ControlEvidence (32), ControlPolicy (64), ControlPrincipal (512), ControlThread (16), Execution (8), Infrastructure (4096), NoFlags (0), RemotingConfiguration (2048), SerializationFormatter (128), SkipVerification (4), UnmanagedCode (2)
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

    AllFlags = None
    Assertion = None
    BindingRedirects = None
    ControlAppDomain = None
    ControlDomainPolicy = None
    ControlEvidence = None
    ControlPolicy = None
    ControlPrincipal = None
    ControlThread = None
    Execution = None
    Infrastructure = None
    NoFlags = None
    RemotingConfiguration = None
    SerializationFormatter = None
    SkipVerification = None
    UnmanagedCode = None
    value__ = None


class SiteIdentityPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IBuiltInPermission):
    """
    Defines the identity permission for the Web site from which the code originates. This class cannot be inherited.
    
    SiteIdentityPermission(state: PermissionState)
    SiteIdentityPermission(site: str)
    """
    def Copy(self):
        """
        Copy(self: SiteIdentityPermission) -> IPermission
        
            Creates and returns an identical copy of the current permission.
            Returns: A copy of the current permission.
        """
        pass

    def FromXml(self, esd):
        """
        FromXml(self: SiteIdentityPermission, esd: SecurityElement)
            Reconstructs a permission with a specified state from an XML encoding.
        
            esd: The XML encoding to use to reconstruct the permission.
        """
        pass

    def Intersect(self, target):
        """
        Intersect(self: SiteIdentityPermission, target: IPermission) -> IPermission
        
            Creates and returns a permission that is the intersection of the current permission and the 
             specified permission.
        
        
            target: A permission to intersect with the current permission. It must be of the same type as the 
             current permission.
        
            Returns: A new permission that represents the intersection of the current permission and the specified 
             permission. This new permission is null if the intersection is empty.
        """
        pass

    def IsSubsetOf(self, target):
        """
        IsSubsetOf(self: SiteIdentityPermission, target: IPermission) -> bool
        
            Determines whether the current permission is a subset of the specified permission.
        
            target: A permission that is to be tested for the subset relationship. This permission must be of the 
             same type as the current permission.
        
            Returns: true if the current permission is a subset of the specified permission; otherwise, false.
        """
        pass

    def ToXml(self):
        """
        ToXml(self: SiteIdentityPermission) -> SecurityElement
        
            Creates an XML encoding of the permission and its current state.
            Returns: An XML encoding of the permission, including any state information.
        """
        pass

    def Union(self, target):
        """
        Union(self: SiteIdentityPermission, target: IPermission) -> IPermission
        
            Creates a permission that is the union of the current permission and the specified permission.
        
            target: A permission to combine with the current permission. It must be of the same type as the current 
             permission.
        
            Returns: A new permission that represents the union of the current permission and the specified 
             permission.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, site: str)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Site = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current site.

Get: Site(self: SiteIdentityPermission) -> str

Set: Site(self: SiteIdentityPermission) = value
"""



class SiteIdentityPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """
    Allows security actions for System.Security.Permissions.SiteIdentityPermission to be applied to code using declarative security. This class cannot be inherited.
    
    SiteIdentityPermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: SiteIdentityPermissionAttribute) -> IPermission
        
            Creates and returns a new instance of System.Security.Permissions.SiteIdentityPermission.
            Returns: A System.Security.Permissions.SiteIdentityPermission that corresponds to this attribute.
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

    Site = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the site name of the calling code.

Get: Site(self: SiteIdentityPermissionAttribute) -> str

Set: Site(self: SiteIdentityPermissionAttribute) = value
"""



class StorePermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission):
    """
    Controls access to stores containing X.509 certificates. This class cannot be inherited.
    
    StorePermission(state: PermissionState)
    StorePermission(flag: StorePermissionFlags)
    """
    def Copy(self):
        """
        Copy(self: StorePermission) -> IPermission
        
            Creates and returns an identical copy of the current permission.
            Returns: A copy of the current permission.
        """
        pass

    def FromXml(self, securityElement):
        """
        FromXml(self: StorePermission, securityElement: SecurityElement)
            Reconstructs a permission with a specified state from an XML encoding.
        
            securityElement: A System.Security.SecurityElement that contains the XML encoding to use to reconstruct the 
             permission.
        """
        pass

    def Intersect(self, target):
        """
        Intersect(self: StorePermission, target: IPermission) -> IPermission
        
            Creates and returns a permission that is the intersection of the current permission and the 
             specified permission.
        
        
            target: A permission to intersect with the current permission. It must be of the same type as the 
             current permission.
        
            Returns: A new permission that represents the intersection of the current permission and the specified 
             permission. This new permission is null if the intersection is empty.
        """
        pass

    def IsSubsetOf(self, target):
        """
        IsSubsetOf(self: StorePermission, target: IPermission) -> bool
        
            Determines whether the current permission is a subset of the specified permission.
        
            target: A permission to test for the subset relationship. This permission must be of the same type as 
             the current permission.
        
            Returns: true if the current permission is a subset of the specified permission; otherwise, false.
        """
        pass

    def IsUnrestricted(self):
        """
        IsUnrestricted(self: StorePermission) -> bool
        
            Returns a value indicating whether the current permission is unrestricted.
            Returns: true if the current permission is unrestricted; otherwise, false.
        """
        pass

    def ToXml(self):
        """
        ToXml(self: StorePermission) -> SecurityElement
        
            Creates an XML encoding of the permission and its current state.
            Returns: A System.Security.SecurityElement that contains an XML encoding of the permission, including any 
             state information.
        """
        pass

    def Union(self, target):
        """
        Union(self: StorePermission, target: IPermission) -> IPermission
        
            Creates a permission that is the union of the current permission and the specified permission.
        
            target: A permission to combine with the current permission. It must be of the same type as the current 
             permission.
        
            Returns: A new permission that represents the union of the current permission and the specified 
             permission.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, flag: StorePermissionFlags)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type of System.Security.Cryptography.X509Certificates.X509Store access allowed by the current permission.

Get: Flags(self: StorePermission) -> StorePermissionFlags

Set: Flags(self: StorePermission) = value
"""



class StorePermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """
    Allows security actions for System.Security.Permissions.StorePermission to be applied to code using declarative security. This class cannot be inherited.
    
    StorePermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: StorePermissionAttribute) -> IPermission
        
            Creates and returns a new System.Security.Permissions.StorePermission.
            Returns: A System.Security.Permissions.StorePermission that corresponds to the attribute.
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

    AddToStore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the code is permitted to add to a store.

Get: AddToStore(self: StorePermissionAttribute) -> bool

Set: AddToStore(self: StorePermissionAttribute) = value
"""

    CreateStore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the code is permitted to create a store.

Get: CreateStore(self: StorePermissionAttribute) -> bool

Set: CreateStore(self: StorePermissionAttribute) = value
"""

    DeleteStore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the code is permitted to delete a store.

Get: DeleteStore(self: StorePermissionAttribute) -> bool

Set: DeleteStore(self: StorePermissionAttribute) = value
"""

    EnumerateCertificates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the code is permitted to enumerate the certificates in a store.

Get: EnumerateCertificates(self: StorePermissionAttribute) -> bool

Set: EnumerateCertificates(self: StorePermissionAttribute) = value
"""

    EnumerateStores = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the code is permitted to enumerate stores.

Get: EnumerateStores(self: StorePermissionAttribute) -> bool

Set: EnumerateStores(self: StorePermissionAttribute) = value
"""

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the store permissions.

Get: Flags(self: StorePermissionAttribute) -> StorePermissionFlags

Set: Flags(self: StorePermissionAttribute) = value
"""

    OpenStore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the code is permitted to open a store.

Get: OpenStore(self: StorePermissionAttribute) -> bool

Set: OpenStore(self: StorePermissionAttribute) = value
"""

    RemoveFromStore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the code is permitted to remove a certificate from a store.

Get: RemoveFromStore(self: StorePermissionAttribute) -> bool

Set: RemoveFromStore(self: StorePermissionAttribute) = value
"""



class StorePermissionFlags(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the permitted access to X.509 certificate stores.
    
    enum (flags) StorePermissionFlags, values: AddToStore (32), AllFlags (247), CreateStore (1), DeleteStore (2), EnumerateCertificates (128), EnumerateStores (4), NoFlags (0), OpenStore (16), RemoveFromStore (64)
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

    AddToStore = None
    AllFlags = None
    CreateStore = None
    DeleteStore = None
    EnumerateCertificates = None
    EnumerateStores = None
    NoFlags = None
    OpenStore = None
    RemoveFromStore = None
    value__ = None


class StrongNameIdentityPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IBuiltInPermission):
    """
    Defines the identity permission for strong names. This class cannot be inherited.
    
    StrongNameIdentityPermission(state: PermissionState)
    StrongNameIdentityPermission(blob: StrongNamePublicKeyBlob, name: str, version: Version)
    """
    def Copy(self):
        """
        Copy(self: StrongNameIdentityPermission) -> IPermission
        
            Creates and returns an identical copy of the current permission.
            Returns: A copy of the current permission.
        """
        pass

    def FromXml(self, e):
        """
        FromXml(self: StrongNameIdentityPermission, e: SecurityElement)
            Reconstructs a permission with a specified state from an XML encoding.
        
            e: The XML encoding to use to reconstruct the permission.
        """
        pass

    def Intersect(self, target):
        """
        Intersect(self: StrongNameIdentityPermission, target: IPermission) -> IPermission
        
            Creates and returns a permission that is the intersection of the current permission and the 
             specified permission.
        
        
            target: A permission to intersect with the current permission. It must be of the same type as the 
             current permission.
        
            Returns: A new permission that represents the intersection of the current permission and the specified 
             permission, or null if the intersection is empty.
        """
        pass

    def IsSubsetOf(self, target):
        """
        IsSubsetOf(self: StrongNameIdentityPermission, target: IPermission) -> bool
        
            Determines whether the current permission is a subset of the specified permission.
        
            target: A permission that is to be tested for the subset relationship. This permission must be of the 
             same type as the current permission.
        
            Returns: true if the current permission is a subset of the specified permission; otherwise, false.
        """
        pass

    def ToXml(self):
        """
        ToXml(self: StrongNameIdentityPermission) -> SecurityElement
        
            Creates an XML encoding of the permission and its current state.
            Returns: An XML encoding of the permission, including any state information.
        """
        pass

    def Union(self, target):
        """
        Union(self: StrongNameIdentityPermission, target: IPermission) -> IPermission
        
            Creates a permission that is the union of the current permission and the specified permission.
        
            target: A permission to combine with the current permission. It must be of the same type as the current 
             permission.
        
            Returns: A new permission that represents the union of the current permission and the specified 
             permission.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, blob: StrongNamePublicKeyBlob, name: str, version: Version)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the simple name portion of the strong name identity.

Get: Name(self: StrongNameIdentityPermission) -> str

Set: Name(self: StrongNameIdentityPermission) = value
"""

    PublicKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the public key blob that defines the strong name identity namespace.

Get: PublicKey(self: StrongNameIdentityPermission) -> StrongNamePublicKeyBlob

Set: PublicKey(self: StrongNameIdentityPermission) = value
"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the version number of the identity.

Get: Version(self: StrongNameIdentityPermission) -> Version

Set: Version(self: StrongNameIdentityPermission) = value
"""



class StrongNameIdentityPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """
    Allows security actions for System.Security.Permissions.StrongNameIdentityPermission to be applied to code using declarative security. This class cannot be inherited.
    
    StrongNameIdentityPermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: StrongNameIdentityPermissionAttribute) -> IPermission
        
            Creates and returns a new System.Security.Permissions.StrongNameIdentityPermission.
            Returns: A System.Security.Permissions.StrongNameIdentityPermission that corresponds to this attribute.
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

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the strong name identity.

Get: Name(self: StrongNameIdentityPermissionAttribute) -> str

Set: Name(self: StrongNameIdentityPermissionAttribute) = value
"""

    PublicKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the public key value of the strong name identity expressed as a hexadecimal string.

Get: PublicKey(self: StrongNameIdentityPermissionAttribute) -> str

Set: PublicKey(self: StrongNameIdentityPermissionAttribute) = value
"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the version of the strong name identity.

Get: Version(self: StrongNameIdentityPermissionAttribute) -> str

Set: Version(self: StrongNameIdentityPermissionAttribute) = value
"""



class StrongNamePublicKeyBlob(object):
    """
    Represents the public key information (called a blob) for a strong name. This class cannot be inherited.
    
    StrongNamePublicKeyBlob(publicKey: Array[Byte])
    """
    def Equals(self, obj):
        """
        Equals(self: StrongNamePublicKeyBlob, obj: object) -> bool
        
            Gets or sets a value indicating whether the current public key blob is equal to the specified 
             public key blob.
        
        
            obj: An object containing a public key blob.
            Returns: true if the public key blob of the current object is equal to the public key blob of the obj 
             parameter; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: StrongNamePublicKeyBlob) -> int
        
            Returns a hash code based on the public key.
            Returns: The hash code based on the public key.
        """
        pass

    def ToString(self):
        """
        ToString(self: StrongNamePublicKeyBlob) -> str
        
            Creates and returns a string representation of the public key blob.
            Returns: A hexadecimal version of the public key blob.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, publicKey):
        """ __new__(cls: type, publicKey: Array[Byte]) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass


class TypeDescriptorPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission):
    """
    Defines partial-trust access to the System.ComponentModel.TypeDescriptor class.
    
    TypeDescriptorPermission(state: PermissionState)
    TypeDescriptorPermission(flag: TypeDescriptorPermissionFlags)
    """
    def Copy(self):
        """
        Copy(self: TypeDescriptorPermission) -> IPermission
            Returns: A copy of the current permission object.
        """
        pass

    def FromXml(self, securityElement):
        """
        FromXml(self: TypeDescriptorPermission, securityElement: SecurityElement)
            securityElement: The XML encoding to use to reconstruct the security object.
        """
        pass

    def Intersect(self, target):
        """
        Intersect(self: TypeDescriptorPermission, target: IPermission) -> IPermission
        
            target: A permission to intersect with the current permission. It must be of the same type as the 
             current permission.
        
            Returns: A new permission that represents the intersection of the current permission and the specified 
             permission. This new permission is null if the intersection is empty.
        """
        pass

    def IsSubsetOf(self, target):
        """
        IsSubsetOf(self: TypeDescriptorPermission, target: IPermission) -> bool
        
            target: A permission that is to be tested for the subset relationship. This permission must be of the 
             same type as the current permission.
        
            Returns: true if the current permission is a subset of the specified permission; otherwise, false.
        """
        pass

    def IsUnrestricted(self):
        """
        IsUnrestricted(self: TypeDescriptorPermission) -> bool
        
            Gets a value that indicates whether the type descriptor may be called from partially trusted 
             code.
        
            Returns: true if the System.Security.Permissions.TypeDescriptorPermission.Flags property is set to 
             System.Security.Permissions.TypeDescriptorPermissionFlags.RestrictedRegistrationAccess; 
             otherwise, false.
        """
        pass

    def ToXml(self):
        """
        ToXml(self: TypeDescriptorPermission) -> SecurityElement
            Returns: An XML encoding of the security object, including any state information.
        """
        pass

    def Union(self, target):
        """
        Union(self: TypeDescriptorPermission, target: IPermission) -> IPermission
        
            target: A permission to combine with the current permission. It must be of the same type as the current 
             permission.
        
            Returns: A new permission that represents the union of the current permission and the specified 
             permission.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, flag: TypeDescriptorPermissionFlags)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Security.Permissions.TypeDescriptorPermissionFlags for the type descriptor.

Get: Flags(self: TypeDescriptorPermission) -> TypeDescriptorPermissionFlags

Set: Flags(self: TypeDescriptorPermission) = value
"""



class TypeDescriptorPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """
    Determines the permission flags that apply to a System.ComponentModel.TypeDescriptor.
    
    TypeDescriptorPermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: TypeDescriptorPermissionAttribute) -> IPermission
            Returns: A serializable permission object.
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

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Security.Permissions.TypeDescriptorPermissionFlags for the System.ComponentModel.TypeDescriptor.

Get: Flags(self: TypeDescriptorPermissionAttribute) -> TypeDescriptorPermissionFlags

Set: Flags(self: TypeDescriptorPermissionAttribute) = value
"""

    RestrictedRegistrationAccess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the type descriptor can be accessed from partial trust.

Get: RestrictedRegistrationAccess(self: TypeDescriptorPermissionAttribute) -> bool

Set: RestrictedRegistrationAccess(self: TypeDescriptorPermissionAttribute) = value
"""



class TypeDescriptorPermissionFlags(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines permission settings for type descriptors.
    
    enum (flags) TypeDescriptorPermissionFlags, values: NoFlags (0), RestrictedRegistrationAccess (1)
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

    NoFlags = None
    RestrictedRegistrationAccess = None
    value__ = None


class UIPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission, IBuiltInPermission):
    """
    Controls the permissions related to user interfaces and the Clipboard. This class cannot be inherited.
    
    UIPermission(state: PermissionState)
    UIPermission(windowFlag: UIPermissionWindow, clipboardFlag: UIPermissionClipboard)
    UIPermission(windowFlag: UIPermissionWindow)
    UIPermission(clipboardFlag: UIPermissionClipboard)
    """
    def Copy(self):
        """
        Copy(self: UIPermission) -> IPermission
        
            Creates and returns an identical copy of the current permission.
            Returns: A copy of the current permission.
        """
        pass

    def FromXml(self, esd):
        """
        FromXml(self: UIPermission, esd: SecurityElement)
            Reconstructs a permission with a specified state from an XML encoding.
        
            esd: The XML encoding used to reconstruct the permission.
        """
        pass

    def Intersect(self, target):
        """
        Intersect(self: UIPermission, target: IPermission) -> IPermission
        
            Creates and returns a permission that is the intersection of the current permission and the 
             specified permission.
        
        
            target: A permission to intersect with the current permission. It must be the same type as the current 
             permission.
        
            Returns: A new permission that represents the intersection of the current permission and the specified 
             permission. This new permission is null if the intersection is empty.
        """
        pass

    def IsSubsetOf(self, target):
        """
        IsSubsetOf(self: UIPermission, target: IPermission) -> bool
        
            Determines whether the current permission is a subset of the specified permission.
        
            target: A permission to test for the subset relationship. This permission must be the same type as the 
             current permission.
        
            Returns: true if the current permission is a subset of the specified permission; otherwise, false.
        """
        pass

    def IsUnrestricted(self):
        """
        IsUnrestricted(self: UIPermission) -> bool
        
            Returns a value indicating whether the current permission is unrestricted.
            Returns: true if the current permission is unrestricted; otherwise, false.
        """
        pass

    def ToXml(self):
        """
        ToXml(self: UIPermission) -> SecurityElement
        
            Creates an XML encoding of the permission and its current state.
            Returns: An XML encoding of the permission, including any state information.
        """
        pass

    def Union(self, target):
        """
        Union(self: UIPermission, target: IPermission) -> IPermission
        
            Creates a permission that is the union of the permission and the specified permission.
        
            target: A permission to combine with the current permission. It must be the same type as the current 
             permission.
        
            Returns: A new permission that represents the union of the current permission and the specified 
             permission.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, windowFlag: UIPermissionWindow, clipboardFlag: UIPermissionClipboard)
        __new__(cls: type, windowFlag: UIPermissionWindow)
        __new__(cls: type, clipboardFlag: UIPermissionClipboard)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Clipboard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Clipboard access represented by the permission.

Get: Clipboard(self: UIPermission) -> UIPermissionClipboard

Set: Clipboard(self: UIPermission) = value
"""

    Window = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the window access represented by the permission.

Get: Window(self: UIPermission) -> UIPermissionWindow

Set: Window(self: UIPermission) = value
"""



class UIPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """
    Allows security actions for System.Security.Permissions.UIPermission to be applied to code using declarative security. This class cannot be inherited.
    
    UIPermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: UIPermissionAttribute) -> IPermission
        
            Creates and returns a new System.Security.Permissions.UIPermission.
            Returns: A System.Security.Permissions.UIPermission that corresponds to this attribute.
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

    Clipboard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type of access to the clipboard that is permitted.

Get: Clipboard(self: UIPermissionAttribute) -> UIPermissionClipboard

Set: Clipboard(self: UIPermissionAttribute) = value
"""

    Window = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type of access to the window resources that is permitted.

Get: Window(self: UIPermissionAttribute) -> UIPermissionWindow

Set: Window(self: UIPermissionAttribute) = value
"""



class UIPermissionClipboard(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of clipboard access that is allowed to the calling code.
    
    enum UIPermissionClipboard, values: AllClipboard (2), NoClipboard (0), OwnClipboard (1)
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

    AllClipboard = None
    NoClipboard = None
    OwnClipboard = None
    value__ = None


class UIPermissionWindow(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of windows that code is allowed to use.
    
    enum UIPermissionWindow, values: AllWindows (3), NoWindows (0), SafeSubWindows (1), SafeTopLevelWindows (2)
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

    AllWindows = None
    NoWindows = None
    SafeSubWindows = None
    SafeTopLevelWindows = None
    value__ = None


class UrlIdentityPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IBuiltInPermission):
    """
    Defines the identity permission for the URL from which the code originates. This class cannot be inherited.
    
    UrlIdentityPermission(state: PermissionState)
    UrlIdentityPermission(site: str)
    """
    def Copy(self):
        """
        Copy(self: UrlIdentityPermission) -> IPermission
        
            Creates and returns an identical copy of the current permission.
            Returns: A copy of the current permission.
        """
        pass

    def FromXml(self, esd):
        """
        FromXml(self: UrlIdentityPermission, esd: SecurityElement)
            Reconstructs a permission with a specified state from an XML encoding.
        
            esd: The XML encoding to use to reconstruct the permission.
        """
        pass

    def Intersect(self, target):
        """
        Intersect(self: UrlIdentityPermission, target: IPermission) -> IPermission
        
            Creates and returns a permission that is the intersection of the current permission and the 
             specified permission.
        
        
            target: A permission to intersect with the current permission. It must be of the same type as the 
             current permission.
        
            Returns: A new permission that represents the intersection of the current permission and the specified 
             permission. This new permission is null if the intersection is empty.
        """
        pass

    def IsSubsetOf(self, target):
        """
        IsSubsetOf(self: UrlIdentityPermission, target: IPermission) -> bool
        
            Determines whether the current permission is a subset of the specified permission.
        
            target: A permission that is to be tested for the subset relationship. This permission must be of the 
             same type as the current permission.
        
            Returns: true if the current permission is a subset of the specified permission; otherwise, false.
        """
        pass

    def ToXml(self):
        """
        ToXml(self: UrlIdentityPermission) -> SecurityElement
        
            Creates an XML encoding of the permission and its current state.
            Returns: An XML encoding of the permission, including any state information.
        """
        pass

    def Union(self, target):
        """
        Union(self: UrlIdentityPermission, target: IPermission) -> IPermission
        
            Creates a permission that is the union of the current permission and the specified permission.
        
            target: A permission to combine with the current permission. It must be of the same type as the current 
             permission.
        
            Returns: A new permission that represents the union of the current permission and the specified 
             permission.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, site: str)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Url = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a URL representing the identity of Internet code.

Get: Url(self: UrlIdentityPermission) -> str

Set: Url(self: UrlIdentityPermission) = value
"""



class UrlIdentityPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """
    Allows security actions for System.Security.Permissions.UrlIdentityPermission to be applied to code using declarative security. This class cannot be inherited.
    
    UrlIdentityPermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: UrlIdentityPermissionAttribute) -> IPermission
        
            Creates and returns a new System.Security.Permissions.UrlIdentityPermission.
            Returns: A System.Security.Permissions.UrlIdentityPermission that corresponds to this attribute.
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

    Url = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the full URL of the calling code.

Get: Url(self: UrlIdentityPermissionAttribute) -> str

Set: Url(self: UrlIdentityPermissionAttribute) = value
"""



class ZoneIdentityPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IBuiltInPermission):
    """
    Defines the identity permission for the zone from which the code originates. This class cannot be inherited.
    
    ZoneIdentityPermission(state: PermissionState)
    ZoneIdentityPermission(zone: SecurityZone)
    """
    def Copy(self):
        """
        Copy(self: ZoneIdentityPermission) -> IPermission
        
            Creates and returns an identical copy of the current permission.
            Returns: A copy of the current permission.
        """
        pass

    def FromXml(self, esd):
        """
        FromXml(self: ZoneIdentityPermission, esd: SecurityElement)
            Reconstructs a permission with a specified state from an XML encoding.
        
            esd: The XML encoding to use to reconstruct the permission.
        """
        pass

    def Intersect(self, target):
        """
        Intersect(self: ZoneIdentityPermission, target: IPermission) -> IPermission
        
            Creates and returns a permission that is the intersection of the current permission and the 
             specified permission.
        
        
            target: A permission to intersect with the current permission. It must be of the same type as the 
             current permission.
        
            Returns: A new permission that represents the intersection of the current permission and the specified 
             permission. This new permission is null if the intersection is empty.
        """
        pass

    def IsSubsetOf(self, target):
        """
        IsSubsetOf(self: ZoneIdentityPermission, target: IPermission) -> bool
        
            Determines whether the current permission is a subset of the specified permission.
        
            target: A permission that is to be tested for the subset relationship. This permission must be of the 
             same type as the current permission.
        
            Returns: true if the current permission is a subset of the specified permission; otherwise, false.
        """
        pass

    def ToXml(self):
        """
        ToXml(self: ZoneIdentityPermission) -> SecurityElement
        
            Creates an XML encoding of the permission and its current state.
            Returns: An XML encoding of the permission, including any state information.
        """
        pass

    def Union(self, target):
        """
        Union(self: ZoneIdentityPermission, target: IPermission) -> IPermission
        
            Creates a permission that is the union of the current permission and the specified permission.
        
            target: A permission to combine with the current permission. It must be of the same type as the current 
             permission.
        
            Returns: A new permission that represents the union of the current permission and the specified 
             permission.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, zone: SecurityZone)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SecurityZone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the zone represented by the current System.Security.Permissions.ZoneIdentityPermission.

Get: SecurityZone(self: ZoneIdentityPermission) -> SecurityZone

Set: SecurityZone(self: ZoneIdentityPermission) = value
"""



class ZoneIdentityPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """
    Allows security actions for System.Security.Permissions.ZoneIdentityPermission to be applied to code using declarative security. This class cannot be inherited.
    
    ZoneIdentityPermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: ZoneIdentityPermissionAttribute) -> IPermission
        
            Creates and returns a new System.Security.Permissions.ZoneIdentityPermission.
            Returns: A System.Security.Permissions.ZoneIdentityPermission that corresponds to this attribute.
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

    Zone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets membership in the content zone specified by the property value.

Get: Zone(self: ZoneIdentityPermissionAttribute) -> SecurityZone

Set: Zone(self: ZoneIdentityPermissionAttribute) = value
"""



