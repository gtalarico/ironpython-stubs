# encoding: utf-8
# module Wms.RemotingObjects.BackgroundAgents calls itself BackgroundAgents
# from Wms.RemotingObjects, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BackgroundAgent:
    """ BackgroundAgent() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    BackgroundAgentPk = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackgroundAgentPk(self: BackgroundAgent) -> int

Set: BackgroundAgentPk(self: BackgroundAgent) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: BackgroundAgent) -> str

Set: Id(self: BackgroundAgent) = value
"""

    IsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsActive(self: BackgroundAgent) -> bool

"""

    IsAuthorized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAuthorized(self: BackgroundAgent) -> bool

Set: IsAuthorized(self: BackgroundAgent) = value
"""

    LastSeen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LastSeen(self: BackgroundAgent) -> DateTime

Set: LastSeen(self: BackgroundAgent) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: BackgroundAgent) -> str

Set: Name(self: BackgroundAgent) = value
"""

    OS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OS(self: BackgroundAgent) -> str

Set: OS(self: BackgroundAgent) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: BackgroundAgent) -> BackgroundAgentType

Set: Type(self: BackgroundAgent) = value
"""



class BackgroundAgents:
    """ BackgroundAgents() """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass


class BackgroundAgentStatus:
    """ BackgroundAgentStatus() """
    ActiveAgents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveAgents(self: BackgroundAgentStatus) -> int

Set: ActiveAgents(self: BackgroundAgentStatus) = value
"""

    InactiveAgents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InactiveAgents(self: BackgroundAgentStatus) -> int

Set: InactiveAgents(self: BackgroundAgentStatus) = value
"""



class BackgroundAgentType:
    """ enum BackgroundAgentType, values: PrintAgent (1), Unknown (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    PrintAgent = None
    Unknown = None
    value__ = None


class PingMessage:
    """ PingMessage() """
    AgentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AgentType(self: PingMessage) -> BackgroundAgentType

Set: AgentType(self: PingMessage) = value
"""

    CreatedAt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreatedAt(self: PingMessage) -> DateTime

Set: CreatedAt(self: PingMessage) = value
"""

    ListenerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ListenerId(self: PingMessage) -> str

Set: ListenerId(self: PingMessage) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: PingMessage) -> str

Set: Name(self: PingMessage) = value
"""

    OS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OS(self: PingMessage) -> str

Set: OS(self: PingMessage) = value
"""



