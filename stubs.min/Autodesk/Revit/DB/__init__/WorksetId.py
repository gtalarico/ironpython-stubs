class WorksetId(object):
    """
    WorksetId identifies a workset within a single document.
    
    WorksetId(id: int)
    """
    def Compare(self, id):
        """
        Compare(self: WorksetId, id: WorksetId) -> int
        
            Compares two WorksetIds.
        
            id: The WorksetId to be compared with this WorksetId.
            Returns: -1 if this WorksetId is less than id, 0 if equal, 1 if greater.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: WorksetId, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to the current 
             System.Object.
        
        
            obj: Another object.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: WorksetId) -> int
        
            Gets the integer value of the id as hash code
        """
        pass

    def ToString(self):
        """
        ToString(self: WorksetId) -> str
        
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
    def __new__(self, id):
        """ __new__(cls: type, id: int) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    IntegerValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides the value of the WorksetId as an integer.

Get: IntegerValue(self: WorksetId) -> int

"""


    InvalidWorksetId = None

