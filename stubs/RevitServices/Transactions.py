# encoding: utf-8
# module RevitServices.Transactions calls itself Transactions
# from RevitServices, Version=1.2.1.3083, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AutomaticTransactionStrategy(object, ITransactionStrategy):
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class DebugTransactionStrategy(object, ITransactionStrategy):
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class FailureDelegate(MulticastDelegate, ICloneable, ISerializable):
    """ FailureDelegate(object: object, method: IntPtr) """
    def BeginInvoke(self, failures, callback, object):
        """ BeginInvoke(self: FailureDelegate, failures: FailuresAccessor, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new 
             delegate.
        
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by 
             the current delegate.-or- null, if the method represented by the current 
             delegate does not require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FailureDelegate, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, failures):
        """ Invoke(self: FailureDelegate, failures: FailuresAccessor) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate 
             that is equal to the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new 
             System.Delegate without value in its invocation list; otherwise, this instance 
             with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
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


