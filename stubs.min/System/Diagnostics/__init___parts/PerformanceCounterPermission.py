class PerformanceCounterPermission(ResourcePermissionBase, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission):
    """
    Allows control of code access permissions for System.Diagnostics.PerformanceCounter.
    
    PerformanceCounterPermission()
    PerformanceCounterPermission(state: PermissionState)
    PerformanceCounterPermission(permissionAccess: PerformanceCounterPermissionAccess, machineName: str, categoryName: str)
    PerformanceCounterPermission(permissionAccessEntries: Array[PerformanceCounterPermissionEntry])
    """
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

    def GetPermissionEntries(self, *args): #cannot find CLR method
        """
        GetPermissionEntries(self: ResourcePermissionBase) -> Array[ResourcePermissionBaseEntry]
        
            Returns an array of the System.Security.Permissions.ResourcePermissionBaseEntry objects added to this permission.
            Returns: An array of System.Security.Permissions.ResourcePermissionBaseEntry objects that were added to this permission.
        """
        pass

    def RemovePermissionAccess(self, *args): #cannot find CLR method
        """
        RemovePermissionAccess(self: ResourcePermissionBase, entry: ResourcePermissionBaseEntry)
            Removes a permission entry from the permission.
        
            entry: The System.Security.Permissions.ResourcePermissionBaseEntry to remove.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, permissionAccess: PerformanceCounterPermissionAccess, machineName: str, categoryName: str)
        __new__(cls: type, permissionAccessEntries: Array[PerformanceCounterPermissionEntry])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    PermissionAccessType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an enumeration value that describes the types of access that you are giving the resource.

"""

    PermissionEntries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of permission entries for this permissions request.

Get: PermissionEntries(self: PerformanceCounterPermission) -> PerformanceCounterPermissionEntryCollection

"""

    TagNames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an array of strings that identify the resource you are protecting.

"""


