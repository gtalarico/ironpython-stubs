from Wms.RemotingImplementation.TaskScheduler import TaskBase
# encoding: utf-8
# module Wms.RemotingImplementation.MessageQueue calls itself MessageQueue
# from Wms.RemotingImplementation, Version=1.24.1.1, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CleanupMessageQueueTask(TaskBase):
    """ CleanupMessageQueueTask(settings: SystemSettings) """
    def Run(self):
        """ Run(self: CleanupMessageQueueTask) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, settings):
        """ __new__(cls: type, settings: SystemSettings) """
        pass

    Settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Settings(self: CleanupMessageQueueTask) -> SystemSettings

Set: Settings(self: CleanupMessageQueueTask) = value
"""


    Instance = CleanupMessageQueueTask()
    """hardcoded/returns an instance of the class"""

# variables with complex values

