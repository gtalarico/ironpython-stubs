# encoding: utf-8
# module Wms.EdiMessaging.Extensions calls itself Extensions
# from Wms.EdiMessaging, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class MessageExtensions():
    # no doc
    @staticmethod
    def AppendLogLine(message, line):
        """ AppendLogLine(message: IMessage, line: str) """
        pass

    @staticmethod
    def GetBodyAsAscii(message):
        """ GetBodyAsAscii(message: IMessage) -> str """
        pass

    @staticmethod
    def GetBodyAsUnicode(message):
        """ GetBodyAsUnicode(message: IMessage) -> str """
        pass

    @staticmethod
    def GetBodyAsUtf8(message):
        """ GetBodyAsUtf8(message: IMessage) -> str """
        pass

    @staticmethod
    def GetBodyAsXDocument(message):
        """ GetBodyAsXDocument(message: IMessage) -> XDocument """
        pass

    @staticmethod
    def GetBodyAsXmlDocument(message):
        """ GetBodyAsXmlDocument(message: IMessage) -> XmlDocument """
        pass

    @staticmethod
    def GetUtf8BodyAsXmlDocument(message):
        """ GetUtf8BodyAsXmlDocument(message: IMessage) -> XmlDocument """
        pass

    @staticmethod
    def SetBodyAsAscii(message, content):
        """ SetBodyAsAscii(message: IMessage, content: str) """
        pass

    @staticmethod
    def SetBodyAsUnicode(message, content):
        """ SetBodyAsUnicode(message: IMessage, content: str) """
        pass

    @staticmethod
    def SetBodyAsUtf8(message, content):
        """ SetBodyAsUtf8(message: IMessage, content: str) """
        pass

    @staticmethod
    def SetBodyAsXDocument(message, xdoc):
        """ SetBodyAsXDocument(message: IMessage, xdoc: XDocument) """
        pass

    @staticmethod
    def SetBodyAsXmlDocument(message, doc):
        """ SetBodyAsXmlDocument(message: IMessage, doc: XmlDocument) """
        pass

    __all__ = [
        'AppendLogLine',
        'GetBodyAsAscii',
        'GetBodyAsUnicode',
        'GetBodyAsUtf8',
        'GetBodyAsXDocument',
        'GetBodyAsXmlDocument',
        'GetUtf8BodyAsXmlDocument',
        'SetBodyAsAscii',
        'SetBodyAsUnicode',
        'SetBodyAsUtf8',
        'SetBodyAsXDocument',
        'SetBodyAsXmlDocument',
    ]

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return MessageExtensions()

