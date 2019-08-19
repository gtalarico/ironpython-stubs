from Wms.RemotingObjects import *
# encoding: utf-8
# module Wms.RemotingObjects.Exceptions calls itself Exceptions
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class RemotingInvalidVersionException(RemotingException):
    """
    RemotingInvalidVersionException()
    RemotingInvalidVersionException(message: str)
    RemotingInvalidVersionException(message: str, innerEx: Exception)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, innerEx=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerEx: Exception)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return RemotingInvalidVersionException()

