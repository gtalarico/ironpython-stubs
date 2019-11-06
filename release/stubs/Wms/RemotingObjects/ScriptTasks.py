from System import Object
from Wms.RemotingObjects import FindableList
from Wms.RemotingObjects import DbObject
# encoding: utf-8
# module Wms.RemotingObjects.ScriptTasks calls itself ScriptTasks
# from Wms.RemotingObjects, Version=1.24.1.1, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ScriptTask(DbObject):
    """ ScriptTask() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Active(self: ScriptTask) -> bool

Set: Active(self: ScriptTask) = value
"""

    Days = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Days(self: ScriptTask) -> str

Set: Days(self: ScriptTask) = value
"""

    DaysToExecute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DaysToExecute(self: ScriptTask) -> List[str]

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Description(self: ScriptTask) -> str

Set: Description(self: ScriptTask) = value
"""

    EndDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: EndDate(self: ScriptTask) -> Nullable[DateTime]

Set: EndDate(self: ScriptTask) = value
"""

    ExecuteOnFriday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ExecuteOnFriday(self: ScriptTask) -> bool

Set: ExecuteOnFriday(self: ScriptTask) = value
"""

    ExecuteOnMonday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ExecuteOnMonday(self: ScriptTask) -> bool

Set: ExecuteOnMonday(self: ScriptTask) = value
"""

    ExecuteOnSaturday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ExecuteOnSaturday(self: ScriptTask) -> bool

Set: ExecuteOnSaturday(self: ScriptTask) = value
"""

    ExecuteOnSunday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ExecuteOnSunday(self: ScriptTask) -> bool

Set: ExecuteOnSunday(self: ScriptTask) = value
"""

    ExecuteOnThursday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ExecuteOnThursday(self: ScriptTask) -> bool

Set: ExecuteOnThursday(self: ScriptTask) = value
"""

    ExecuteOnTuesday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ExecuteOnTuesday(self: ScriptTask) -> bool

Set: ExecuteOnTuesday(self: ScriptTask) = value
"""

    ExecuteOnWednesday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ExecuteOnWednesday(self: ScriptTask) -> bool

Set: ExecuteOnWednesday(self: ScriptTask) = value
"""

    Hours = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Hours(self: ScriptTask) -> str

Set: Hours(self: ScriptTask) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Id(self: ScriptTask) -> int

Set: Id(self: ScriptTask) = value
"""

    Interval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Interval(self: ScriptTask) -> int

Set: Interval(self: ScriptTask) = value
"""

    Minutes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Minutes(self: ScriptTask) -> str

Set: Minutes(self: ScriptTask) = value
"""

    Months = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Months(self: ScriptTask) -> str

Set: Months(self: ScriptTask) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Name(self: ScriptTask) -> str

Set: Name(self: ScriptTask) = value
"""

    Priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Priority(self: ScriptTask) -> ScriptTaskPriority

Set: Priority(self: ScriptTask) = value
"""

    Script = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Script(self: ScriptTask) -> str

Set: Script(self: ScriptTask) = value
"""

    StartDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: StartDate(self: ScriptTask) -> DateTime

Set: StartDate(self: ScriptTask) = value
"""

    UserId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the account under wich this task will run.

Get: UserId(self: ScriptTask) -> int

Set: UserId(self: ScriptTask) = value
"""

    ZoneId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the zone on wich this task will run.

Get: ZoneId(self: ScriptTask) -> int

Set: ZoneId(self: ScriptTask) = value
"""


    Instance = ScriptTask()
    """hardcoded/returns an instance of the class"""

class ScriptTaskPriority(Object):
    """ enum ScriptTaskPriority, values: High (3), Low (1), Normal (2) """
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
    Normal = None
    value__ = None

    Instance = ScriptTaskPriority()
    """hardcoded/returns an instance of the class"""

class ScriptTasks(FindableList):
    """ ScriptTasks() """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    DisplayMember = 'Name'
    ValueMember = 'Id'

    Instance = ScriptTasks()
    """hardcoded/returns an instance of the class"""

