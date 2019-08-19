# encoding: utf-8
# module Wms.EdiMessaging.Metadata calls itself Metadata
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# functions

def MessageHandlerDescriptor(handlerType, createInstance, IMessageHandler): # real signature unknown; restored from __doc__
    """ MessageHandlerDescriptor(handlerType: Type, createInstance: Func[IMessageHandler]) """
    pass

def MessagePublisherDescriptor(handlerType, createInstance, IMessagePublisher): # real signature unknown; restored from __doc__
    """ MessagePublisherDescriptor(handlerType: Type, createInstance: Func[IMessagePublisher]) """
    pass

# classes

class ObjectDescriptor():
    # no doc
    def ExtractAttribute(self):
        """ ExtractAttribute(self: ObjectDescriptor) -> DescriptorAttribute """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, handlerType: Type) """
        pass

    ExecuteIsolated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExecuteIsolated(self: ObjectDescriptor) -> bool

"""

    FriendlyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FriendlyName(self: ObjectDescriptor) -> str

"""

    Fullname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fullname(self: ObjectDescriptor) -> str

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: ObjectDescriptor) -> Guid

"""


    HandlerType = None

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return ObjectDescriptor()

# variables with complex values

