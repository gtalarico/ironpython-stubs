# encoding: utf-8
# module RevitServices.Transactions calls itself Transactions
# from RevitServices, Version=1.2.1.3083, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AutomaticTransactionStrategy(object):
    """ AutomaticTransactionStrategy() """
    def EnsureInTransaction(self, wrapper, document):
        """ EnsureInTransaction(self: AutomaticTransactionStrategy, wrapper: TransactionWrapper, document: Document) -> TransactionHandle """
        pass

    def ForceCloseTransaction(self, handle):
        """ ForceCloseTransaction(self: AutomaticTransactionStrategy, handle: TransactionHandle) """
        pass

    def TransactionTaskDone(self, handle):
        """ TransactionTaskDone(self: AutomaticTransactionStrategy, handle: TransactionHandle) """
        pass


class DebugTransactionStrategy(object):
    """ DebugTransactionStrategy() """
    def EnsureInTransaction(self, wrapper, document):
        """ EnsureInTransaction(self: DebugTransactionStrategy, wrapper: TransactionWrapper, document: Document) -> TransactionHandle """
        pass

    def ForceCloseTransaction(self, handle):
        """ ForceCloseTransaction(self: DebugTransactionStrategy, handle: TransactionHandle) """
        pass

    def TransactionTaskDone(self, handle):
        """ TransactionTaskDone(self: DebugTransactionStrategy, handle: TransactionHandle) """
        pass


class FailureDelegate(MulticastDelegate):
    """ FailureDelegate(object: object, method: IntPtr) """
    def BeginInvoke(self, failures, callback, object):
        """ BeginInvoke(self: FailureDelegate, failures: FailuresAccessor, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FailureDelegate, result: IAsyncResult) """
        pass

    def Invoke(self, failures):
        """ Invoke(self: FailureDelegate, failures: FailuresAccessor) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class ITransactionStrategy:
    # no doc
    def EnsureInTransaction(self, wrapper, document):
        """ EnsureInTransaction(self: ITransactionStrategy, wrapper: TransactionWrapper, document: Document) -> TransactionHandle """
        pass

    def ForceCloseTransaction(self, handle):
        """ ForceCloseTransaction(self: ITransactionStrategy, handle: TransactionHandle) """
        pass

    def TransactionTaskDone(self, handle):
        """ TransactionTaskDone(self: ITransactionStrategy, handle: TransactionHandle) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class TransactionHandle(object):
    # no doc
    def CancelTransaction(self):
        """ CancelTransaction(self: TransactionHandle) -> TransactionStatus """
        pass

    def CommitTransaction(self):
        """ CommitTransaction(self: TransactionHandle) -> TransactionStatus """
        pass

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: TransactionHandle) -> TransactionStatus

"""



class TransactionManager(object):
    # no doc
    def EnsureInTransaction(self, document):
        """ EnsureInTransaction(self: TransactionManager, document: Document) """
        pass

    def ForceCloseTransaction(self):
        """ ForceCloseTransaction(self: TransactionManager) """
        pass

    @staticmethod
    def SetupManager(strategy=None):
        """ SetupManager(strategy: ITransactionStrategy)SetupManager() """
        pass

    def TransactionTaskDone(self):
        """ TransactionTaskDone(self: TransactionManager) """
        pass

    DoAssertInIdleThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DoAssertInIdleThread(self: TransactionManager) -> bool

Set: DoAssertInIdleThread(self: TransactionManager) = value
"""

    Strategy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Strategy(self: TransactionManager) -> ITransactionStrategy

Set: Strategy(self: TransactionManager) = value
"""

    TransactionWrapper = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransactionWrapper(self: TransactionManager) -> TransactionWrapper

"""


    Instance = None
    OnLog = None


class TransactionWrapper(object):
    # no doc
    def StartTransaction(self, document):
        """ StartTransaction(self: TransactionWrapper, document: Document) -> TransactionHandle """
        pass

    TransactionActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransactionActive(self: TransactionWrapper) -> bool

"""


    FailuresRaised = None
    TransactionCancelled = None
    TransactionCommitted = None
    TransactionName = 'Dynamo-51297CB5 Script'
    TransactionStarted = None


