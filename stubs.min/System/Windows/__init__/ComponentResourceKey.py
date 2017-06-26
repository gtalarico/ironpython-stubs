class ComponentResourceKey(ResourceKey):
    """
    Defines or references resource keys based on class names in external assemblies, as well as an additional identifier.
    
    ComponentResourceKey()
    ComponentResourceKey(typeInTargetAssembly: Type, resourceId: object)
    """
    def Equals(self, o):
        """
        Equals(self: ComponentResourceKey, o: object) -> bool
        
            Determines whether the provided object is equal to the current System.Windows.ComponentResourceKey.
        
            o: Object to compare with the current System.Windows.ComponentResourceKey.
            Returns: true if the objects are equal; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ComponentResourceKey) -> int
        
            Returns a hash code for this System.Windows.ComponentResourceKey.
            Returns: A signed 32-bit integer value.
        """
        pass

    def ToString(self):
        """
        ToString(self: ComponentResourceKey) -> str
        
            Gets the string representation of a System.Windows.ComponentResourceKey.
            Returns: The string representation.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, typeInTargetAssembly=None, resourceId=None):
        """
        __new__(cls: type)
        __new__(cls: type, typeInTargetAssembly: Type, resourceId: object)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Assembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the assembly object that indicates which assembly's dictionary to look in for the value associated with this key.

Get: Assembly(self: ComponentResourceKey) -> Assembly

"""

    ResourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a unique identifier to differentiate this key from others associated with this type.

Get: ResourceId(self: ComponentResourceKey) -> object

Set: ResourceId(self: ComponentResourceKey) = value
"""

    TypeInTargetAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Type that defines the resource key.

Get: TypeInTargetAssembly(self: ComponentResourceKey) -> Type

Set: TypeInTargetAssembly(self: ComponentResourceKey) = value
"""


