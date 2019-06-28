# encoding: utf-8
# module Wms.RemotingImplementation.Logging calls itself Logging
# from Wms.RemotingImplementation, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CleanUpLogTask:
    """ CleanUpLogTask(settings: SystemSettings) """
    def Run(self):
        """ Run(self: CleanUpLogTask) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, settings):
        """ __new__(cls: type, settings: SystemSettings) """
        pass

    Settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Settings(self: CleanUpLogTask) -> SystemSettings

Set: Settings(self: CleanUpLogTask) = value
"""



class NLogLoggingBootstrapper:
    """ NLogLoggingBootstrapper() """
    def Init(self):
        """ Init(self: NLogLoggingBootstrapper) """
        pass


class NLogLoggingService:
    """ NLogLoggingService() """
    def Error(self, *__args):
        """ Error(self: NLogLoggingService, exception: Exception) """
        pass

    def Fatal(self, *__args):
        """ Fatal(self: NLogLoggingService, exception: Exception) """
        pass

    @staticmethod
    def GetLoggingService():
        """ GetLoggingService() -> ILoggingService """
        pass

    def OnLoggerReconfigured(self, *args): #cannot find CLR method
        """
        OnLoggerReconfigured(self: Logger, e: EventArgs)
            Raises the event when the logger is reconfigured.
        
            e: Event arguments
        """
        pass

    def Warn(self, *__args):
        """ Warn(self: NLogLoggingService, exception: Exception) """
        pass

    def Write(self, *__args):
        """ Write(self: NLogLoggingService, message: str)Write(self: NLogLoggingService, message: object)Write(self: NLogLoggingService, message: object, category: str)Write(self: NLogLoggingService, message: object, category: str, level: LogLevel)Write(self: NLogLoggingService, exception: Exception) """
        pass

    def WriteDebug(self, message, category):
        """ WriteDebug(self: NLogLoggingService, message: str, category: str) """
        pass

    def WriteError(self, message, category=None):
        """ WriteError(self: NLogLoggingService, message: str, category: str)WriteError(self: NLogLoggingService, message: object)WriteError(self: NLogLoggingService, message: object, category: str) """
        pass

    def WriteFatal(self, message, category):
        """ WriteFatal(self: NLogLoggingService, message: str, category: str) """
        pass

    def WriteInfo(self, message, category):
        """ WriteInfo(self: NLogLoggingService, message: str, category: str) """
        pass

    def WriteTrace(self, message, category):
        """ WriteTrace(self: NLogLoggingService, message: str, category: str) """
        pass

    def WriteWarn(self, message, category):
        """ WriteWarn(self: NLogLoggingService, message: str, category: str) """
        pass

    def WriteWarning(self, message):
        """ WriteWarning(self: NLogLoggingService, message: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    KeyAccessId = 'bw-accessid'
    KeyBuildEnvironment = 'buildEnvironment'
    KeyCategory = 'bw-category'
    KeyClientName = 'bw-clientname'
    KeyDeviceMacAddress = 'bw-device-macaddress'
    KeyDeviceType = 'bw-devicetype'
    KeyLicenseName = 'bw-licensename'
    KeyUsername = 'bw-username'
    KeyVersion = 'bw-version'
    KeyZoneName = 'bw-zonename'


class NLogTraceLoggingService:
    """ NLogTraceLoggingService() """
    @staticmethod
    def GetTraceLoggingService():
        """ GetTraceLoggingService() -> ITraceLoggingService """
        pass

    def IsTracingEnabled(self):
        """ IsTracingEnabled(self: NLogTraceLoggingService) -> bool """
        pass

    def OnLoggerReconfigured(self, *args): #cannot find CLR method
        """
        OnLoggerReconfigured(self: Logger, e: EventArgs)
            Raises the event when the logger is reconfigured.
        
            e: Event arguments
        """
        pass

    def ToggleEnableTracing(self):
        """ ToggleEnableTracing(self: NLogTraceLoggingService) -> bool """
        pass

    def Trace(self, *__args):
        """ Trace(self: NLogTraceLoggingService, properties: IDictionary[str, object], eventType: TraceType, message: str)Trace(self: NLogTraceLoggingService, properties: IDictionary[str, object], eventType: TraceType, format: str, *args: Array[object]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    KeyCustomTraceActivityId = 'custom-activityid'
    KeyTraceType = 'trace-type'


# variables with complex values

