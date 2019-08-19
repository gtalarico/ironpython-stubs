# encoding: utf-8
# module Wms.RemotingImplementation.Activities.Progress calls itself Progress
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
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

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return ProgressBase()

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

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return BatchPackProgress()

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

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return BatchPickProgress()

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

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return IProgress()

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

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return ProgressFactory()

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

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return ReceiveProgress()

