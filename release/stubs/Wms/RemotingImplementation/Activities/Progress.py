from System import Object
# encoding: utf-8
# module Wms.RemotingImplementation.Activities.Progress calls itself Progress
# from Wms.RemotingImplementation, Version=1.24.1.1, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ProgressBase(Object):
    # no doc
    def GenerateProgressBarImage(self, args, progress):
        """ GenerateProgressBarImage(self: ProgressBase, args: GetActivityProgressArgs, progress: Progress) -> Array[Byte] """
        pass

    def GetActivity(self, args, value):
        """ GetActivity(self: ProgressBase, args: GetActivityProgressArgs, value: object) -> Activity """
        pass

    def GetProgress(self, args, value):
        """ GetProgress(self: ProgressBase, args: GetActivityProgressArgs, value: object) -> Progress """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Instance = ProgressBase()
    """hardcoded/returns an instance of the class"""

class BatchPackProgress(ProgressBase):
    """ BatchPackProgress() """
    def GetActivity(self, args, value):
        """ GetActivity(self: BatchPackProgress, args: GetActivityProgressArgs, value: object) -> Activity """
        pass

    def GetProgress(self, args, value):
        """ GetProgress(self: BatchPackProgress, args: GetActivityProgressArgs, value: object) -> Progress """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Instance = BatchPackProgress()
    """hardcoded/returns an instance of the class"""

class BatchPickProgress(ProgressBase):
    """ BatchPickProgress() """
    def GetActivity(self, args, value):
        """ GetActivity(self: BatchPickProgress, args: GetActivityProgressArgs, value: object) -> Activity """
        pass

    def GetProgress(self, args, value):
        """ GetProgress(self: BatchPickProgress, args: GetActivityProgressArgs, value: object) -> Progress """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Instance = BatchPickProgress()
    """hardcoded/returns an instance of the class"""

class IProgress(Object):
    # no doc
    def GetActivity(self, args, value):
        """ GetActivity(self: IProgress, args: GetActivityProgressArgs, value: object) -> Activity """
        pass

    def GetProgress(self, args, value):
        """ GetProgress(self: IProgress, args: GetActivityProgressArgs, value: object) -> Progress """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Instance = IProgress()
    """hardcoded/returns an instance of the class"""

class ProgressFactory():
    # no doc
    @staticmethod
    def GetActivity(args, value):
        """ GetActivity(args: GetActivityProgressArgs, value: object) -> Activity """
        pass

    @staticmethod
    def GetProgress(args, value):
        """ GetProgress(args: GetActivityProgressArgs, value: object) -> Progress """
        pass

    __all__ = [
        'GetActivity',
        'GetProgress',
    ]

    Instance = ProgressFactory()
    """hardcoded/returns an instance of the class"""

class ReceiveProgress(ProgressBase):
    """ ReceiveProgress() """
    def GetActivity(self, args, value):
        """ GetActivity(self: ReceiveProgress, args: GetActivityProgressArgs, value: object) -> Activity """
        pass

    def GetProgress(self, args, value):
        """ GetProgress(self: ReceiveProgress, args: GetActivityProgressArgs, value: object) -> Progress """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Instance = ReceiveProgress()
    """hardcoded/returns an instance of the class"""
