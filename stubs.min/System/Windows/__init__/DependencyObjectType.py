class DependencyObjectType(object):
    """ Implements an underlying type cache for all System.Windows.DependencyObject derived types. """
    @staticmethod
    def FromSystemType(systemType):
        """
        FromSystemType(systemType: Type) -> DependencyObjectType
        
            Returns a System.Windows.DependencyObjectType that represents a given system (CLR) type.
        
            systemType: The system (CLR) type to convert.
            Returns: A System.Windows.DependencyObjectType that represents the system (CLR) type.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DependencyObjectType) -> int
        
            Returns the hash code for this System.Windows.DependencyObjectType.
            Returns: A 32-bit signed integer hash code.
        """
        pass

    def IsInstanceOfType(self, dependencyObject):
        """
        IsInstanceOfType(self: DependencyObjectType, dependencyObject: DependencyObject) -> bool
        
            Determines whether the specified object is an instance of the current System.Windows.DependencyObjectType.
        
            dependencyObject: The object to compare with the current System.Windows.DependencyObjectType.
            Returns: true if the class represented by the current System.Windows.DependencyObjectType is in the inheritance hierarchy of the System.Windows.DependencyObject passed as d; otherwise, false.
        """
        pass

    def IsSubclassOf(self, dependencyObjectType):
        """
        IsSubclassOf(self: DependencyObjectType, dependencyObjectType: DependencyObjectType) -> bool
        
            Determines whether the current System.Windows.DependencyObjectType derives from the specified System.Windows.DependencyObjectType.
        
            dependencyObjectType: The System.Windows.DependencyObjectType to compare.
            Returns: true if the dependencyObjectType parameter and the current System.Windows.DependencyObjectType represent types of classes, and the class represented by the current System.Windows.DependencyObjectType 
             derives from the class represented by dependencyObjectType. Otherwise, false. This method also returns false if dependencyObjectType and the current System.Windows.DependencyObjectType represent the same 
             class.
        """
        pass

    BaseType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.DependencyObjectType of the immediate base class of the current System.Windows.DependencyObjectType.

Get: BaseType(self: DependencyObjectType) -> DependencyObjectType

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a zero-based unique identifier for constant-time array lookup operations.

Get: Id(self: DependencyObjectType) -> int

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the represented common language runtime (CLR) system type.

Get: Name(self: DependencyObjectType) -> str

"""

    SystemType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the common language runtime (CLR) system type represented by this System.Windows.DependencyObjectType.

Get: SystemType(self: DependencyObjectType) -> Type

"""


