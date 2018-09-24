class EventHandlerWrapper(MarshalByRefObject):
 """ EventHandlerWrapper(Instance: IEventHandler,Functionality: WrapperFunctionalityBase) """
 def AddListener(self,EventListener):
  """ AddListener(self: EventHandlerWrapper,EventListener: Events) """
  pass
 def RemoveListener(self,EventListener):
  """ RemoveListener(self: EventHandlerWrapper,EventListener: Events) """
  pass
 @staticmethod
 def __new__(self,Instance,Functionality):
  """ __new__(cls: type,Instance: IEventHandler,Functionality: WrapperFunctionalityBase) """
  pass
 Functionality=None
 Instance=None

