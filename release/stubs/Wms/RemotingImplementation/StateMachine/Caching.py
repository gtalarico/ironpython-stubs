from System import Object
# encoding: utf-8
# module Wms.RemotingImplementation.StateMachine.Caching calls itself Caching
# from Wms.RemotingImplementation, Version=1.24.1.1, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class IStateMachineCache(Object):
    # no doc
    def ClearState(self, id):
        """ ClearState(self: IStateMachineCache, id: str) """
        pass

    def GetState(self, id):
        """ GetState(self: IStateMachineCache, id: str) -> object """
        pass

    def SaveState(self, id, state):
        """ SaveState(self: IStateMachineCache, id: str, state: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Instance = IStateMachineCache()
    """hardcoded/returns an instance of the class"""

class StateMachineCacheContainer(Object):
    """ StateMachineCacheContainer() """
    def ClearState(self, id):
        """ ClearState(self: StateMachineCacheContainer, id: str) """
        pass

    def GetState(self, id):
        """ GetState(self: StateMachineCacheContainer, id: str) -> object """
        pass

    def SaveState(self, id, state):
        """ SaveState(self: StateMachineCacheContainer, id: str, state: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Instance = StateMachineCacheContainer()
    """hardcoded/returns an instance of the class"""

