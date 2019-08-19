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


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return AutoDisposeTask()

class NotificationCleanupTask(TaskBase):
    """ NotificationCleanupTask(settings: SystemSettings) """
    def Run(self):
        """ Run(self: NotificationCleanupTask) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, settings):
        """ __new__(cls: type, settings: SystemSettings) """
        pass

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return NotificationCleanupTask()

class NotificationSummaryTask(TaskBase):
    """ NotificationSummaryTask() """
    def Run(self):
        """ Run(self: NotificationSummaryTask) """
        pass

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return NotificationSummaryTask()

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


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return PythonScriptTask()

