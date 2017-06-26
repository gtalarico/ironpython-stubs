class ScheduleFieldId(object):
    """
    The ScheduleFieldId object is used as a unique identification for a field in a schedule.
    
    ScheduleFieldId(id: int)
    """
    def Equals(self, obj):
        """
        Equals(self: ScheduleFieldId, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to the current 
             System.Object.
        
        
            obj: The other object to evaluate.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ScheduleFieldId) -> int
        
            Gets the integer value of the id as hash code
        """
        pass

    def ToString(self):
        """
        ToString(self: ScheduleFieldId) -> str
        
            Gets a String representation of the integer value of the id.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, id):
        """ __new__(cls: type, id: int) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    IntegerValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides the value of the ScheduleFieldId as an integer.

Get: IntegerValue(self: ScheduleFieldId) -> int

"""


    InvalidScheduleFieldId = None

