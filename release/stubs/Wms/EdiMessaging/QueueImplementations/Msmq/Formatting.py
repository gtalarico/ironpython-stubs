# encoding: utf-8
# module Wms.EdiMessaging.QueueImplementations.Msmq.Formatting calls itself Formatting
# from Wms.EdiMessaging, Version=1.24.1.1, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class MessageSerialization():
    # no doc
    @staticmethod
    def Deserialize(stream):
        """ Deserialize(stream: Stream) -> IMessage """
        pass

    @staticmethod
    def Serialize(message):
        """ Serialize(message: IMessage) -> Stream """
        pass

    __all__ = [
        'Deserialize',
        'Serialize',
    ]

    Instance = MessageSerialization()
    """hardcoded/returns an instance of the class"""
