# encoding: utf-8
# module Wms.RemotingImplementation.Logging.NLogExtensions.Targets calls itself Targets
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ExceptionExtensions():
    # no doc
    @staticmethod
    def IsLoggedToInternalLogger(exception):
        """ IsLoggedToInternalLogger(exception: Exception) -> bool """
        pass

    @staticmethod
    def MustBeRethrown(exception):
        """ MustBeRethrown(exception: Exception) -> bool """
        pass

    @staticmethod
    def MustBeRethrownImmediately(exception):
        """ MustBeRethrownImmediately(exception: Exception) -> bool """
        pass

    __all__ = [
        'IsLoggedToInternalLogger',
        'MustBeRethrown',
        'MustBeRethrownImmediately',
    ]

    Instance = ExceptionExtensions()
    """hardcoded/returns an instance of the class"""

class LogLevelExtensions():
    # no doc
    @staticmethod
    def ToSeverity(level):
        """ ToSeverity(level: LogLevel) -> LogSeverity """
        pass

    __all__ = [
        'ToSeverity',
    ]

    Instance = LogLevelExtensions()
    """hardcoded/returns an instance of the class"""

class StackdriverLabel():
    """
    StackdriverLabel()
    StackdriverLabel(parameterName: str, parameterLayout: Layout)
    """
    @staticmethod # known case of __new__
    def __new__(self, parameterName=None, parameterLayout=None):
        """
        __new__(cls: type)
        __new__(cls: type, parameterName: str, parameterLayout: Layout)
        """
        pass

    Layout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Layout(self: StackdriverLabel) -> Layout

Set: Layout(self: StackdriverLabel) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: StackdriverLabel) -> str

Set: Name(self: StackdriverLabel) = value
"""


    Instance = StackdriverLabel()
    """hardcoded/returns an instance of the class"""

class StackDriverLoggingTarget(TargetWithLayout):
    """ StackDriverLoggingTarget() """
    def CloseTarget(self, *args): #cannot find CLR method
        """ CloseTarget(self: StackDriverLoggingTarget) """
        pass

    def Dispose(self):
        """ Dispose(self: Target, disposing: bool) """
        pass

    def FlushAsync(self, *args): #cannot find CLR method
        """ FlushAsync(self: Target, asyncContinuation: AsyncContinuation) """
        pass

    def InitializeTarget(self, *args): #cannot find CLR method
        """ InitializeTarget(self: Target) """
        pass

    def MergeEventProperties(self, *args): #cannot find CLR method
        """ MergeEventProperties(self: Target, logEvent: LogEventInfo) """
        pass

    def RenderLogEvent(self, *args): #cannot find CLR method
        """ RenderLogEvent(self: Target, layout: Layout, logEvent: LogEventInfo) -> str """
        pass

    def Write(self, *args): #cannot find CLR method
        """ Write(self: StackDriverLoggingTarget, logEvent: LogEventInfo)Write(self: StackDriverLoggingTarget, logEvents: Array[AsyncLogEventInfo])Write(self: Target, logEvent: AsyncLogEventInfo)Write(self: Target, logEvents: IList[AsyncLogEventInfo]) """
        pass

    def WriteAsyncThreadSafe(self, *args): #cannot find CLR method
        """ WriteAsyncThreadSafe(self: Target, logEvent: AsyncLogEventInfo)WriteAsyncThreadSafe(self: Target, logEvents: Array[AsyncLogEventInfo])WriteAsyncThreadSafe(self: Target, logEvents: IList[AsyncLogEventInfo]) """
        pass

    def WriteToStackDriver(self, projectId, logId, logEvent):
        """ WriteToStackDriver(self: StackDriverLoggingTarget, projectId: str, logId: str, logEvent: LogEventInfo) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Client = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Client(self: StackDriverLoggingTarget) -> LoggingServiceV2Client

Set: Client(self: StackDriverLoggingTarget) = value
"""

    IsInitialized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Labels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Labels(self: StackDriverLoggingTarget) -> IList[StackdriverLabel]

"""

    LoggingConfiguration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    LogId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LogId(self: StackDriverLoggingTarget) -> str

Set: LogId(self: StackDriverLoggingTarget) = value
"""

    ProjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectId(self: StackDriverLoggingTarget) -> str

Set: ProjectId(self: StackDriverLoggingTarget) = value
"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    Instance = StackDriverLoggingTarget()
    """hardcoded/returns an instance of the class"""

