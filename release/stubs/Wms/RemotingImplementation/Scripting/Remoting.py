# encoding: utf-8
# module Wms.RemotingImplementation.Scripting.Remoting calls itself Remoting
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BaseRemotingSink(BaseChannelObjectWithProperties):
    # no doc
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return BaseRemotingSink()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    def ProcessRequest(self, *args): #cannot find CLR method
        """ ProcessRequest(self: BaseRemotingSink, message: IMessage, headers: ITransportHeaders, stream: Stream, state: object) -> (Stream, object) """
        pass

    def ProcessResponse(self, *args): #cannot find CLR method
        """ ProcessResponse(self: BaseRemotingSink, message: IMessage, headers: ITransportHeaders, stream: Stream, state: object) -> (IMessage, Stream) """
        pass

    def SetNextSink(self, nextSink):
        """ SetNextSink(self: BaseRemotingSink, nextSink: object) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    PerProviderState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class MakePythonTypesSerializeableSink(BaseRemotingSink):
    """ MakePythonTypesSerializeableSink() """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return MakePythonTypesSerializeableSink()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    def ProcessRequest(self, *args): #cannot find CLR method
        """ ProcessRequest(self: BaseRemotingSink, message: IMessage, headers: ITransportHeaders, stream: Stream, state: object) -> (Stream, object) """
        pass

    def ProcessResponse(self, *args): #cannot find CLR method
        """ ProcessResponse(self: MakePythonTypesSerializeableSink, message: IMessage, headers: ITransportHeaders, stream: Stream, state: object) -> (IMessage, Stream) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    PerProviderState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class SinkProviderOf:
    """ SinkProviderOf[T]() """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return SinkProviderOf()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    def CreateSink(self, channel):
        """ CreateSink(self: SinkProviderOf[T], channel: IChannelReceiver) -> IServerChannelSink """
        pass

    def GetChannelData(self, channelData):
        """ GetChannelData(self: SinkProviderOf[T], channelData: IChannelDataStore) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Next(self: SinkProviderOf[T]) -> IServerChannelSinkProvider

Set: Next(self: SinkProviderOf[T]) = value
"""



