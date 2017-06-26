class ElementId(object):
    """
    The ElementId object is used as a unique identification for an element within a
    single project.
    
    ElementId(parameterId: BuiltInParameter)
    ElementId(categoryId: BuiltInCategory)
    ElementId(id: int)
    """
    def Compare(self, id):
        """
        Compare(self: ElementId, id: ElementId) -> int
        
            Compares two element ids.
        
            id: The ElementId to be compared with this ElementId.
            Returns: -1 if this element id is less than id, 0 if equal, 1 if greater.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: ElementId, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to the current 
             System.Object.
        
        
            obj: Another object.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ElementId) -> int
        
            Gets the integer value of the id as hash code
        """
        pass

    def ToString(self):
        """
        ToString(self: ElementId) -> str
        
            Gets a String representation of the integer value of the id.
        """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, parameterId: BuiltInParameter)
        __new__(cls: type, categoryId: BuiltInCategory)
        __new__(cls: type, id: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    IntegerValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides the value of the element id as an integer.

Get: IntegerValue(self: ElementId) -> int

"""


    InvalidElementId = None

