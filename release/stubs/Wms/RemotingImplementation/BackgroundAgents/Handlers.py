from Wms.EdiMessaging import MessageHandlerBase
# encoding: utf-8
# module Wms.RemotingImplementation.BackgroundAgents.Handlers calls itself Handlers
# from Wms.RemotingImplementation, Version=1.24.1.1, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class PingHandler(MessageHandlerBase):
    """ PingHandler(agentHealthMonitor: IBackgroundAgentHealthMonitor) """
    def Handle(self, message):
        """ Handle(self: PingHandler, message: PingMessage) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, agentHealthMonitor):
        """ __new__(cls: type, agentHealthMonitor: IBackgroundAgentHealthMonitor) """
        pass

    Instance = PingHandler()
    """hardcoded/returns an instance of the class"""

