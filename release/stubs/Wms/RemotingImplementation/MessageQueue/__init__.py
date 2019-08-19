from Wms.RemotingImplementation.TaskScheduler import *
# encoding: utf-8
# module Wms.RemotingImplementation.MessageQueue calls itself MessageQueue
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
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


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return CleanupMessageQueueTask()

# variables with complex values

