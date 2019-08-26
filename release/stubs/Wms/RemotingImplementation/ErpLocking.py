from Wms.RemotingImplementation.TaskScheduler import *
# encoding: utf-8
# module Wms.RemotingImplementation.ErpLocking calls itself ErpLocking
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ErpLockingTask(TaskBase):
    """ ErpLockingTask(settings: SystemSettings) """
    def Run(self):
        """ Run(self: ErpLockingTask) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, settings):
        """ __new__(cls: type, settings: SystemSettings) """
        pass

    Settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Settings(self: ErpLockingTask) -> SystemSettings

Set: Settings(self: ErpLockingTask) = value
"""


    Instance = ErpLockingTask()
    """hardcoded/returns an instance of the class"""

