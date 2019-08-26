from Wms.RemotingImplementation.TaskScheduler import *
# encoding: utf-8
# module Wms.RemotingImplementation.TaskScheduler.ScriptTasks calls itself ScriptTasks
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AutoDisposeTask(TaskBase):
    """ AutoDisposeTask(settings: SystemSettings) """
    def Run(self):
        """ Run(self: AutoDisposeTask) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, settings):
        """ __new__(cls: type, settings: SystemSettings) """
        pass

    Settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Settings(self: AutoDisposeTask) -> SystemSettings

Set: Settings(self: AutoDisposeTask) = value
"""


    Instance = AutoDisposeTask()
    """hardcoded/returns an instance of the class"""

class NotificationCleanupTask(TaskBase):
    """ NotificationCleanupTask(settings: SystemSettings) """
    def Run(self):
        """ Run(self: NotificationCleanupTask) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, settings):
        """ __new__(cls: type, settings: SystemSettings) """
        pass

    Instance = NotificationCleanupTask()
    """hardcoded/returns an instance of the class"""

class NotificationSummaryTask(TaskBase):
    """ NotificationSummaryTask() """
    def Run(self):
        """ Run(self: NotificationSummaryTask) """
        pass

    Instance = NotificationSummaryTask()
    """hardcoded/returns an instance of the class"""

class PythonScriptTask(TaskBase):
    """
    PythonScriptTask()
    PythonScriptTask(task: ScriptTask)
    """
    @staticmethod # known case of __new__
    def __new__(self, task=None):
        """
        __new__(cls: type)
        __new__(cls: type, task: ScriptTask)
        """
        pass

    InternalId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalId(self: PythonScriptTask) -> int

"""

    Script = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Script(self: PythonScriptTask) -> str

"""


    Instance = PythonScriptTask()
    """hardcoded/returns an instance of the class"""

