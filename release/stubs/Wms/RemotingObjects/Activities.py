# encoding: utf-8
# module Wms.RemotingObjects.Activities calls itself Activities
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class GetActivityProgressArgs():
    """ GetActivityProgressArgs() """
    CacheKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CacheKey(self: GetActivityProgressArgs) -> CacheKey

Set: CacheKey(self: GetActivityProgressArgs) = value
"""

    GenerateProgressBarDetailImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GenerateProgressBarDetailImage(self: GetActivityProgressArgs) -> bool

Set: GenerateProgressBarDetailImage(self: GetActivityProgressArgs) = value
"""

    GenerateProgressBarImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GenerateProgressBarImage(self: GetActivityProgressArgs) -> bool

Set: GenerateProgressBarImage(self: GetActivityProgressArgs) = value
"""

    ProgressBarType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProgressBarType(self: GetActivityProgressArgs) -> ProgressBarType

Set: ProgressBarType(self: GetActivityProgressArgs) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return GetActivityProgressArgs()

class ProgressBarType:
    """ enum ProgressBarType, values: Mobile (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Mobile = None
    value__ = None

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return ProgressBarType()

