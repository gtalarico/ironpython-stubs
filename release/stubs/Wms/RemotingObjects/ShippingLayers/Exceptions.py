from System import *
# encoding: utf-8
# module Wms.RemotingObjects.ShippingLayers.Exceptions calls itself Exceptions
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ShipperFatalException(Exception):
    """
    ShipperFatalException(message: str)
    ShipperFatalException(message: str, innerException: Exception)
    """
    Instance = ShipperFatalException
    """hardcoded/returns an instance of the class"""
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message, innerException=None):
        """
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class ShipperCommunicationException(ShipperFatalException):
    """
    ShipperCommunicationException(message: str, shouldRetry: bool)
    ShipperCommunicationException(message: str, innerException: Exception, shouldRetry: bool)
    """
    Instance = ShipperCommunicationException
    """hardcoded/returns an instance of the class"""
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message, *__args):
        """
        __new__(cls: type, message: str, shouldRetry: bool)
        __new__(cls: type, message: str, innerException: Exception, shouldRetry: bool)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ShouldRetry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ShouldRetry(self: ShipperCommunicationException) -> bool

"""


    SerializeObjectState = None


