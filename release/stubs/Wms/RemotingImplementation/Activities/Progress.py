# encoding: utf-8
# module Wms.RemotingImplementation.Activities.Progress calls itself Progress
# from Wms.RemotingImplementation, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ProgressBase:
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


class BatchPackProgress:
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


class BatchPickProgress:
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


class IProgress:
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


class ProgressFactory:
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


class ReceiveProgress:
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


