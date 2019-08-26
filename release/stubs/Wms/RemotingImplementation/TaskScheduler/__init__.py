from System import *
# encoding: utf-8
# module Wms.RemotingImplementation.TaskScheduler calls itself TaskScheduler
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class TaskAlreadyRunningException(Exception):
    """
    TaskAlreadyRunningException()
    TaskAlreadyRunningException(message: str)
    TaskAlreadyRunningException(message: str, innerException: Exception)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None

    Instance = TaskAlreadyRunningException()
    """hardcoded/returns an instance of the class"""

class TaskBase():
    """ TaskBase() """
    def CalculateNextMoment(self):
        """ CalculateNextMoment(self: TaskBase) -> DateTime """
        pass

    def CalculateSchedule(self):
        """ CalculateSchedule(self: TaskBase) -> Array[DateTime] """
        pass

    def Run(self):
        """ Run(self: TaskBase) """
        pass

    def RunAsync(self, *args): #cannot find CLR method
        """ RunAsync(self: TaskBase, token: CancellationToken) -> Task[object] """
        pass

    def StartAsync(self, token, behaviour):
        """ StartAsync(self: TaskBase, token: CancellationToken, behaviour: AlreadyRunningBehaviour) -> Task[object] """
        pass

    def ToCronTabFormat(self):
        """ ToCronTabFormat(self: TaskBase) -> str """
        pass

    Active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Active(self: TaskBase) -> bool

Set: Active(self: TaskBase) = value
"""

    Days = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Days(self: TaskBase) -> str

Set: Days(self: TaskBase) = value
"""

    DaysToExecute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DaysToExecute(self: TaskBase) -> List[str]

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: TaskBase) -> str

Set: Description(self: TaskBase) = value
"""

    Editable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Editable(self: TaskBase) -> bool

Set: Editable(self: TaskBase) = value
"""

    EndDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndDate(self: TaskBase) -> DateTime

Set: EndDate(self: TaskBase) = value
"""

    ExecuteOnFriday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExecuteOnFriday(self: TaskBase) -> bool

Set: ExecuteOnFriday(self: TaskBase) = value
"""

    ExecuteOnMonday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExecuteOnMonday(self: TaskBase) -> bool

Set: ExecuteOnMonday(self: TaskBase) = value
"""

    ExecuteOnSaturday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExecuteOnSaturday(self: TaskBase) -> bool

Set: ExecuteOnSaturday(self: TaskBase) = value
"""

    ExecuteOnSunday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExecuteOnSunday(self: TaskBase) -> bool

Set: ExecuteOnSunday(self: TaskBase) = value
"""

    ExecuteOnThursday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExecuteOnThursday(self: TaskBase) -> bool

Set: ExecuteOnThursday(self: TaskBase) = value
"""

    ExecuteOnTuesday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExecuteOnTuesday(self: TaskBase) -> bool

Set: ExecuteOnTuesday(self: TaskBase) = value
"""

    ExecuteOnWednesday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExecuteOnWednesday(self: TaskBase) -> bool

Set: ExecuteOnWednesday(self: TaskBase) = value
"""

    Hours = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Hours(self: TaskBase) -> str

Set: Hours(self: TaskBase) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: TaskBase) -> int

Set: Id(self: TaskBase) = value
"""

    Interval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Interval(self: TaskBase) -> TimeSpan

Set: Interval(self: TaskBase) = value
"""

    IntervalSpecified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IntervalSpecified(self: TaskBase) -> bool

"""

    IsRunning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRunning(self: TaskBase) -> bool

"""

    LogMessages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LogMessages(self: TaskBase) -> bool

Set: LogMessages(self: TaskBase) = value
"""

    MaximumRuntimeInSeconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumRuntimeInSeconds(self: TaskBase) -> int

Set: MaximumRuntimeInSeconds(self: TaskBase) = value
"""

    Minutes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Minutes(self: TaskBase) -> str

Set: Minutes(self: TaskBase) = value
"""

    Months = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Months(self: TaskBase) -> str

Set: Months(self: TaskBase) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: TaskBase) -> str

Set: Name(self: TaskBase) = value
"""

    NextMoment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NextMoment(self: TaskBase) -> DateTime

Set: NextMoment(self: TaskBase) = value
"""

    PreCheck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreCheck(self: TaskBase) -> bool

Set: PreCheck(self: TaskBase) = value
"""

    RunningTask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RunningTask(self: TaskBase) -> Task[object]

"""

    StartDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartDate(self: TaskBase) -> DateTime

Set: StartDate(self: TaskBase) = value
"""

    TaskStarted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TaskStarted(self: TaskBase) -> DateTime

Set: TaskStarted(self: TaskBase) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: TaskBase) -> TaskType

Set: Type(self: TaskBase) = value
"""


    AlreadyRunningBehaviour = None
    LogCategory = 'Tasks'

    Instance = TaskBase()
    """hardcoded/returns an instance of the class"""

class TaskScheduler():
    # no doc
    def AddDefaultTasks(self):
        """ AddDefaultTasks(self: TaskScheduler) """
        pass

    def AddTask(self, task, findDelegate):
        """ AddTask(self: TaskScheduler, task: TaskBase, findDelegate: Func[TaskBase, bool]) -> int """
        pass

    def IsTaskEnqueued(self, id):
        """ IsTaskEnqueued(self: TaskScheduler, id: int) -> bool """
        pass

    def RemoveTask(self, task):
        """ RemoveTask(self: TaskScheduler, task: TaskBase) """
        pass

    def RemoveTaskByName(self, name):
        """ RemoveTaskByName(self: TaskScheduler, name: str) """
        pass

    def RestartTasksAsync(self):
        """ RestartTasksAsync(self: TaskScheduler) -> Task """
        pass

    def Run(self, *args): #cannot find CLR method
        """ Run(self: TaskScheduler, ct: CancellationToken) -> Task """
        pass

    def RunOnce(self, taskToAdd, findDelegate):
        """ RunOnce(self: TaskScheduler, taskToAdd: TaskBase, findDelegate: Func[TaskBase, bool]) -> Task[object] """
        pass

    def Start(self, ct):
        """ Start(self: TaskScheduler, ct: CancellationToken) -> Task """
        pass

    def Stop(self, waitUntillAllCompleted):
        """ Stop(self: TaskScheduler, waitUntillAllCompleted: bool) -> Task """
        pass

    Tasks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tasks(self: TaskScheduler) -> IEnumerable[TaskBase]

"""


    Instance = None

    Instance = TaskScheduler()
    """hardcoded/returns an instance of the class"""

class TaskType:
    """ enum TaskType, values: Erp (0), General (1), NotificationSummary (3), ScriptTask (2) """
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

    Erp = None
    General = None
    NotificationSummary = None
    ScriptTask = None
    value__ = None

    Instance = TaskType()
    """hardcoded/returns an instance of the class"""

# variables with complex values

