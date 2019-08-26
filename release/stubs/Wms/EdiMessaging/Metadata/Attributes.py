# encoding: utf-8
# module Wms.EdiMessaging.Metadata.Attributes calls itself Attributes
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DescriptorAttribute:
    """
    DescriptorAttribute(id: str, friendlyName: str)
    DescriptorAttribute(id: str, friendlyName: str, executeIsolated: bool)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, id, friendlyName, executeIsolated=None):
        """
        __new__(cls: type, id: str, friendlyName: str)
        __new__(cls: type, id: str, friendlyName: str, executeIsolated: bool)
        """
        pass

    ExecuteIsolated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExecuteIsolated(self: DescriptorAttribute) -> bool

"""

    FriendlyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FriendlyName(self: DescriptorAttribute) -> str

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: DescriptorAttribute) -> Guid

"""


    Instance = DescriptorAttribute()
    """hardcoded/returns an instance of the class"""

class HandlerDescriptorAttribute(DescriptorAttribute):
    """
    HandlerDescriptorAttribute(id: str, friendlyName: str)
    HandlerDescriptorAttribute(id: str, friendlyName: str, executeIsolated: bool)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, id, friendlyName, executeIsolated=None):
        """
        __new__(cls: type, id: str, friendlyName: str)
        __new__(cls: type, id: str, friendlyName: str, executeIsolated: bool)
        """
        pass

    Instance = HandlerDescriptorAttribute()
    """hardcoded/returns an instance of the class"""

class PublisherDescriptorAttribute(DescriptorAttribute):
    """
    PublisherDescriptorAttribute(id: str, friendlyName: str)
    PublisherDescriptorAttribute(id: str, friendlyName: str, executeIsolated: bool)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, id, friendlyName, executeIsolated=None):
        """
        __new__(cls: type, id: str, friendlyName: str)
        __new__(cls: type, id: str, friendlyName: str, executeIsolated: bool)
        """
        pass

    Instance = PublisherDescriptorAttribute()
    """hardcoded/returns an instance of the class"""

