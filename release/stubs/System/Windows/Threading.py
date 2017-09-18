# encoding: utf-8
# module System.Windows.Threading calls itself Threading
# from WindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# functions

def DispatcherOperation(*args, **kwargs): # real signature unknown
    """ Represents an object that is used to interact with an operation that has been posted to the System.Windows.Threading.Dispatcher queue. """
    pass

# classes

class Dispatcher(object):
    """ Provides services for managing the queue of work items for a thread. """
    def BeginInvoke(self, *__args):
        """
        BeginInvoke(self: Dispatcher, method: Delegate, *args: Array[object]) -> DispatcherOperation
        
            Executes the specified delegate asynchronously with the specified arguments on the thread that 
             the System.Windows.Threading.Dispatcher was created on.
        
        
            method: The delegate to a method that takes parameters specified in args, which is pushed onto the 
             System.Windows.Threading.Dispatcher event queue.
        
            args: An array of objects to pass as arguments to the given method. Can be null.
            Returns: An object, which is returned immediately after 
             erload:System.Windows.Threading.Dispatcher.BeginInvoke is called, that can be used to interact 
             with the delegate as it is pending execution in the event queue.
        
        BeginInvoke(self: Dispatcher, method: Delegate, priority: DispatcherPriority, *args: Array[object]) -> DispatcherOperation
        
            Executes the specified delegate asynchronously with the specified arguments, at the specified 
             priority, on the thread that the System.Windows.Threading.Dispatcher was created on.
        
        
            method: The delegate to a method that takes parameters specified in args, which is pushed onto the 
             System.Windows.Threading.Dispatcher event queue.
        
            priority: The priority, relative to the other pending operations in the 
             System.Windows.Threading.Dispatcher event queue, the specified method is invoked.
        
            args: An array of objects to pass as arguments to the given method. Can be null.
            Returns: An object, which is returned immediately after 
             erload:System.Windows.Threading.Dispatcher.BeginInvoke is called, that can be used to interact 
             with the delegate as it is pending execution in the event queue.
        
        BeginInvoke(self: Dispatcher, priority: DispatcherPriority, method: Delegate, arg: object, *args: Array[object]) -> DispatcherOperation
        
            Executes the specified delegate asynchronously at the specified priority and with the specified 
             array of arguments on the thread the System.Windows.Threading.Dispatcher is associated with.
        
        
            priority: The priority, relative to the other pending operations in the 
             System.Windows.Threading.Dispatcher event queue, the specified method is invoked.
        
            method: A delegate to a method that takes multiple arguments, which is pushed onto the 
             System.Windows.Threading.Dispatcher event queue.
        
            arg: The object to pass as an argument to the specified method.
            args: An array of objects to pass as arguments to the specified method.
            Returns: An object, which is returned immediately after 
             erload:System.Windows.Threading.Dispatcher.BeginInvoke is called, that can be used to interact 
             with the delegate as it is pending execution in the System.Windows.Threading.Dispatcher queue.
        
        BeginInvoke(self: Dispatcher, priority: DispatcherPriority, method: Delegate) -> DispatcherOperation
        
            Executes the specified delegate asynchronously at the specified priority on the thread the 
             System.Windows.Threading.Dispatcher is associated with.
        
        
            priority: The priority, relative to the other pending operations in the 
             System.Windows.Threading.Dispatcher event queue, the specified method is invoked.
        
            method: The delegate to a method that takes no arguments, which is pushed onto the 
             System.Windows.Threading.Dispatcher event queue.
        
            Returns: An object, which is returned immediately after 
             erload:System.Windows.Threading.Dispatcher.BeginInvoke is called, that can be used to interact 
             with the delegate as it is pending execution in the event queue.
        
        BeginInvoke(self: Dispatcher, priority: DispatcherPriority, method: Delegate, arg: object) -> DispatcherOperation
        
            Executes the specified delegate asynchronously at the specified priority and with the specified 
             argument on the thread the System.Windows.Threading.Dispatcher is associated with.
        
        
            priority: The priority, relative to the other pending operations in the 
             System.Windows.Threading.Dispatcher event queue, the specified method is invoked.
        
            method: A delegate to a method that takes one argument, which is pushed onto the 
             System.Windows.Threading.Dispatcher event queue.
        
            arg: The object to pass as an argument to the specified method.
            Returns: An object, which is returned immediately after 
             erload:System.Windows.Threading.Dispatcher.BeginInvoke is called, that can be used to interact 
             with the delegate as it is pending execution in the event queue.
        """
        pass

    def BeginInvokeShutdown(self, priority):
        """
        BeginInvokeShutdown(self: Dispatcher, priority: DispatcherPriority)
            Initiates shutdown of the System.Windows.Threading.Dispatcher asynchronously.
        
            priority: The priority at which to begin shutting down the dispatcher.
        """
        pass

    def CheckAccess(self):
        """
        CheckAccess(self: Dispatcher) -> bool
        
            Determines whether the calling thread is the thread associated with this 
             System.Windows.Threading.Dispatcher.
        
            Returns: true if the calling thread is the thread associated with this 
             System.Windows.Threading.Dispatcher; otherwise, false.
        """
        pass

    def DisableProcessing(self):
        """
        DisableProcessing(self: Dispatcher) -> DispatcherProcessingDisabled
        
            Disables processing of the System.Windows.Threading.Dispatcher queue.
            Returns: A structure used to re-enable dispatcher processing.
        """
        pass

    @staticmethod
    def ExitAllFrames():
        """
        ExitAllFrames()
            Requests that all frames exit, including nested frames.
        """
        pass

    @staticmethod
    def FromThread(thread):
        """
        FromThread(thread: Thread) -> Dispatcher
        
            Gets the System.Windows.Threading.Dispatcher for the specified thread.
        
            thread: The thread to obtain the System.Windows.Threading.Dispatcher from.
            Returns: The dispatcher for thread.
        """
        pass

    def Invoke(self, *__args):
        """
        Invoke(self: Dispatcher, priority: DispatcherPriority, timeout: TimeSpan, method: Delegate) -> object
        
            Executes the specified delegate synchronously at the specified priority and with the specified 
             time-out value on the thread the System.Windows.Threading.Dispatcher was created.
        
        
            priority: The priority, relative to the other pending operations in the 
             System.Windows.Threading.Dispatcher event queue, the specified method is invoked.
        
            timeout: The maximum time to wait for the operation to finish.
            method: The delegate to a method that takes no arguments, which is pushed onto the 
             System.Windows.Threading.Dispatcher event queue.
        
            Returns: The return value from the delegate being invoked or null if the delegate has no return value.
        Invoke(self: Dispatcher, priority: DispatcherPriority, timeout: TimeSpan, method: Delegate, arg: object) -> object
        
            Executes the specified delegate at the specified priority with the specified argument 
             synchronously on the thread the System.Windows.Threading.Dispatcher is associated with.
        
        
            priority: The priority, relative to the other pending operations in the 
             System.Windows.Threading.Dispatcher event queue, the specified method is invoked.
        
            timeout: The maximum time to wait for the operation to finish.
            method: A delegate to a method that takes multiple arguments, which is pushed onto the 
             System.Windows.Threading.Dispatcher event queue.
        
            arg: An object to pass as an argument to the given method. This can be null if no arguments are 
             needed.
        
            Returns: The return value from the delegate being invoked or null if the delegate has no return value.
        Invoke(self: Dispatcher, priority: DispatcherPriority, method: Delegate, arg: object) -> object
        
            Executes the specified delegate at the specified priority with the specified argument 
             synchronously on the thread the System.Windows.Threading.Dispatcher is associated with.
        
        
            priority: The priority, relative to the other pending operations in the 
             System.Windows.Threading.Dispatcher event queue, the specified method is invoked.
        
            method: A delegate to a method that takes one argument, which is pushed onto the 
             System.Windows.Threading.Dispatcher event queue.
        
            arg: An object to pass as an argument to the given method.
            Returns: The return value from the delegate being invoked or null if the delegate has no return value.
        Invoke(self: Dispatcher, priority: DispatcherPriority, method: Delegate, arg: object, *args: Array[object]) -> object
        
            Executes the specified delegate at the specified priority with the specified arguments 
             synchronously on the thread the System.Windows.Threading.Dispatcher is associated with.
        
        
            priority: The priority, relative to the other pending operations in the 
             System.Windows.Threading.Dispatcher event queue, the specified method is invoked.
        
            method: A delegate to a method that takes multiple arguments, which is pushed onto the 
             System.Windows.Threading.Dispatcher event queue.
        
            arg: An object to pass as an argument to the given method.
            args: An array of objects to pass as arguments to the given method.
            Returns: The return value from the delegate being invoked or null if the delegate has no return value.
        Invoke(self: Dispatcher, priority: DispatcherPriority, timeout: TimeSpan, method: Delegate, arg: object, *args: Array[object]) -> object
        
            Executes the specified delegate at the specified priority with the specified arguments 
             synchronously on the thread the System.Windows.Threading.Dispatcher is associated with.
        
        
            priority: The priority, relative to the other pending operations in the 
             System.Windows.Threading.Dispatcher event queue, the specified method is invoked.
        
            timeout: The maximum time to wait for the operation to finish.
            method: A delegate to a method that takes multiple arguments, which is pushed onto the 
             System.Windows.Threading.Dispatcher event queue.
        
            arg: An object to pass as an argument to the specified method.
            args: An array of objects to pass as arguments to the specified method.
            Returns: The return value from the delegate being invoked or null if the delegate has no return value.
        Invoke(self: Dispatcher, method: Delegate, timeout: TimeSpan, *args: Array[object]) -> object
        
            Executes the specified delegate within the designated time span at the specified priority with 
             the specified arguments synchronously on the thread the System.Windows.Threading.Dispatcher is 
             associated with.
        
        
            method: A delegate to a method that takes parameters specified in args, which is pushed onto the 
             System.Windows.Threading.Dispatcher event queue.
        
            timeout: The maximum amount of time to wait for the operation to complete.
            args: An array of objects to pass as arguments to the given method. Can be null.
            Returns: The return value from the delegate being invoked or null if the delegate has no return value.
        Invoke(self: Dispatcher, method: Delegate, timeout: TimeSpan, priority: DispatcherPriority, *args: Array[object]) -> object
        
            Executes the specified delegate within the designated time span at the specified priority with 
             the specified arguments synchronously on the thread the System.Windows.Threading.Dispatcher is 
             associated with.
        
        
            method: A delegate to a method that takes parameters specified in args, which is pushed onto the 
             System.Windows.Threading.Dispatcher event queue.
        
            timeout: The maximum amount of time to wait for the operation to complete.
            priority: The priority, relative to the other pending operations in the 
             System.Windows.Threading.Dispatcher event queue, the specified method is invoked.
        
            args: An array of objects to pass as arguments to the given method. Can be null.
            Returns: The return value from the delegate being invoked or null if the delegate has no return value.
        Invoke(self: Dispatcher, method: Delegate, *args: Array[object]) -> object
        
            Executes the specified delegate with the specified arguments synchronously on the thread the 
             System.Windows.Threading.Dispatcher is associated with.
        
        
            method: A delegate to a method that takes parameters specified in args, which is pushed onto the 
             System.Windows.Threading.Dispatcher event queue.
        
            args: An array of objects to pass as arguments to the given method. Can be null.
            Returns: The return value from the delegate being invoked or null if the delegate has no return value.
        Invoke(self: Dispatcher, method: Delegate, priority: DispatcherPriority, *args: Array[object]) -> object
        
            Executes the specified delegate at the specified priority with the specified arguments 
             synchronously on the thread the System.Windows.Threading.Dispatcher is associated with.
        
        
            method: A delegate to a method that takes parameters specified in args, which is pushed onto the 
             System.Windows.Threading.Dispatcher event queue.
        
            priority: The priority, relative to the other pending operations in the 
             System.Windows.Threading.Dispatcher event queue, the specified method is invoked.
        
            args: An array of objects to pass as arguments to the given method. Can be null.
            Returns: The return value from the delegate being invoked or null if the delegate has no return value.
        Invoke(self: Dispatcher, callback: Action, priority: DispatcherPriority, cancellationToken: CancellationToken)Invoke(self: Dispatcher, callback: Action, priority: DispatcherPriority, cancellationToken: CancellationToken, timeout: TimeSpan)Invoke(self: Dispatcher, callback: Action)Invoke(self: Dispatcher, callback: Action, priority: DispatcherPriority)Invoke[TResult](self: Dispatcher, callback: Func[TResult]) -> TResult
        Invoke[TResult](self: Dispatcher, callback: Func[TResult], priority: DispatcherPriority, cancellationToken: CancellationToken, timeout: TimeSpan) -> TResult
        Invoke(self: Dispatcher, priority: DispatcherPriority, method: Delegate) -> object
        
            Executes the specified delegate synchronously at the specified priority on the thread on which 
             the System.Windows.Threading.Dispatcher is associated with.
        
        
            priority: The priority, relative to the other pending operations in the 
             System.Windows.Threading.Dispatcher event queue, the specified method is invoked.
        
            method: A delegate to a method that takes no arguments, which is pushed onto the 
             System.Windows.Threading.Dispatcher event queue.
        
            Returns: The return value from the delegate being invoked or null if the delegate has no return value.
        Invoke[TResult](self: Dispatcher, callback: Func[TResult], priority: DispatcherPriority) -> TResult
        Invoke[TResult](self: Dispatcher, callback: Func[TResult], priority: DispatcherPriority, cancellationToken: CancellationToken) -> TResult
        """
        pass

    def InvokeAsync(self, callback, priority=None, cancellationToken=None):
        """
        InvokeAsync[TResult](self: Dispatcher, callback: Func[TResult]) -> DispatcherOperation[TResult]
        InvokeAsync[TResult](self: Dispatcher, callback: Func[TResult], priority: DispatcherPriority) -> DispatcherOperation[TResult]
        InvokeAsync[TResult](self: Dispatcher, callback: Func[TResult], priority: DispatcherPriority, cancellationToken: CancellationToken) -> DispatcherOperation[TResult]
        InvokeAsync(self: Dispatcher, callback: Action) -> DispatcherOperation
        InvokeAsync(self: Dispatcher, callback: Action, priority: DispatcherPriority) -> DispatcherOperation
        InvokeAsync(self: Dispatcher, callback: Action, priority: DispatcherPriority, cancellationToken: CancellationToken) -> DispatcherOperation
        """
        pass

    def InvokeShutdown(self):
        """
        InvokeShutdown(self: Dispatcher)
            Initiates the shutdown process of the System.Windows.Threading.Dispatcher synchronously.
        """
        pass

    @staticmethod
    def PushFrame(frame):
        """
        PushFrame(frame: DispatcherFrame)
            Enters an execute loop.
        
            frame: The frame for the dispatcher to process.
        """
        pass

    @staticmethod
    def Run():
        """
        Run()
            Pushes the main execution frame on the event queue of the System.Windows.Threading.Dispatcher.
        """
        pass

    @staticmethod
    def ValidatePriority(priority, parameterName):
        """
        ValidatePriority(priority: DispatcherPriority, parameterName: str)
            Determines whether the specified System.Windows.Threading.DispatcherPriority is a valid priority.
        
            priority: The priority to check.
            parameterName: A string that will be returned by the exception that occurs if the priority is invalid.
        """
        pass

    def VerifyAccess(self):
        """
        VerifyAccess(self: Dispatcher)
            Determines whether the calling thread has access to this System.Windows.Threading.Dispatcher.
        """
        pass

    @staticmethod
    def Yield(priority=None):
        """
        Yield(priority: DispatcherPriority) -> DispatcherPriorityAwaitable
        Yield() -> DispatcherPriorityAwaitable
        """
        pass

    HasShutdownFinished = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines whether the System.Windows.Threading.Dispatcher has finished shutting down.

Get: HasShutdownFinished(self: Dispatcher) -> bool

"""

    HasShutdownStarted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines whether the System.Windows.Threading.Dispatcher is shutting down.

Get: HasShutdownStarted(self: Dispatcher) -> bool

"""

    Hooks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of hooks that provide additional event information about the System.Windows.Threading.Dispatcher.

Get: Hooks(self: Dispatcher) -> DispatcherHooks

"""

    Thread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the thread this System.Windows.Threading.Dispatcher is associated with.

Get: Thread(self: Dispatcher) -> Thread

"""


    CurrentDispatcher = None
    ShutdownFinished = None
    ShutdownStarted = None
    UnhandledException = None
    UnhandledExceptionFilter = None


class DispatcherEventArgs(EventArgs):
    """ Provides event data for System.Windows.Threading.Dispatcher related events. """
    Dispatcher = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The System.Windows.Threading.Dispatcher associated with this event.

Get: Dispatcher(self: DispatcherEventArgs) -> Dispatcher

"""



class DispatcherObject(object):
    """ Represents an object that is associated with a System.Windows.Threading.Dispatcher. """
    def CheckAccess(self):
        """
        CheckAccess(self: DispatcherObject) -> bool
        
            Determines whether the calling thread has access to this 
             System.Windows.Threading.DispatcherObject.
        
            Returns: true if the calling thread has access to this object; otherwise, false.
        """
        pass

    def VerifyAccess(self):
        """
        VerifyAccess(self: DispatcherObject)
            Enforces that the calling thread has access to this System.Windows.Threading.DispatcherObject.
        """
        pass

    Dispatcher = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Threading.Dispatcher this System.Windows.Threading.DispatcherObject is associated with.

Get: Dispatcher(self: DispatcherObject) -> Dispatcher

"""



class DispatcherFrame(DispatcherObject):
    """
    Represents an execution loop in the System.Windows.Threading.Dispatcher.
    
    DispatcherFrame()
    DispatcherFrame(exitWhenRequested: bool)
    """
    @staticmethod # known case of __new__
    def __new__(self, exitWhenRequested=None):
        """
        __new__(cls: type)
        __new__(cls: type, exitWhenRequested: bool)
        """
        pass

    Continue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether this System.Windows.Threading.DispatcherFrame should continue.

Get: Continue(self: DispatcherFrame) -> bool

Set: Continue(self: DispatcherFrame) = value
"""



class DispatcherHookEventArgs(EventArgs):
    """
    Provides event data for System.Windows.Threading.DispatcherHooks events.
    
    DispatcherHookEventArgs(operation: DispatcherOperation)
    """
    @staticmethod # known case of __new__
    def __new__(self, operation):
        """ __new__(cls: type, operation: DispatcherOperation) """
        pass

    Dispatcher = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Threading.Dispatcher associated with this event.

Get: Dispatcher(self: DispatcherHookEventArgs) -> Dispatcher

"""

    Operation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Threading.DispatcherOperation associated with this event.

Get: Operation(self: DispatcherHookEventArgs) -> DispatcherOperation

"""



class DispatcherHookEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle System.Windows.Threading.DispatcherHooks related events.
    
    DispatcherHookEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: DispatcherHookEventHandler, sender: object, e: DispatcherHookEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DispatcherHookEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: DispatcherHookEventHandler, sender: object, e: DispatcherHookEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
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


class DispatcherHooks(object):
    """ Provides additional event information about System.Windows.Threading.Dispatcher processing. """
    DispatcherInactive = None
    OperationAborted = None
    OperationCompleted = None
    OperationPosted = None
    OperationPriorityChanged = None
    OperationStarted = None


class DispatcherOperationCallback(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents a delegate to use for dispatcher operations.
    
    DispatcherOperationCallback(object: object, method: IntPtr)
    """
    def BeginInvoke(self, arg, callback, object):
        """ BeginInvoke(self: DispatcherOperationCallback, arg: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DispatcherOperationCallback, result: IAsyncResult) -> object """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, arg):
        """ Invoke(self: DispatcherOperationCallback, arg: object) -> object """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
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


class DispatcherOperationStatus(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes the possible values for the status of a System.Windows.Threading.DispatcherOperation.
    
    enum DispatcherOperationStatus, values: Aborted (1), Completed (2), Executing (3), Pending (0)
    """
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

    Aborted = None
    Completed = None
    Executing = None
    Pending = None
    value__ = None


class DispatcherPriority(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes the priorities at which operations can be invoked by way of the System.Windows.Threading.Dispatcher.
    
    enum DispatcherPriority, values: ApplicationIdle (2), Background (4), ContextIdle (3), DataBind (8), Inactive (0), Input (5), Invalid (-1), Loaded (6), Normal (9), Render (7), Send (10), SystemIdle (1)
    """
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

    ApplicationIdle = None
    Background = None
    ContextIdle = None
    DataBind = None
    Inactive = None
    Input = None
    Invalid = None
    Loaded = None
    Normal = None
    Render = None
    Send = None
    SystemIdle = None
    value__ = None


class DispatcherPriorityAwaitable(object):
    # no doc
    def GetAwaiter(self):
        """ GetAwaiter(self: DispatcherPriorityAwaitable) -> DispatcherPriorityAwaiter """
        pass


class DispatcherPriorityAwaiter(object, INotifyCompletion):
    # no doc
    def GetResult(self):
        """ GetResult(self: DispatcherPriorityAwaiter) """
        pass

    def OnCompleted(self, continuation):
        """ OnCompleted(self: DispatcherPriorityAwaiter, continuation: Action) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsCompleted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCompleted(self: DispatcherPriorityAwaiter) -> bool

"""



class DispatcherProcessingDisabled(object, IDisposable):
    """ Represents the Dispatcher when it is in a disable state and provides a means to re-enable dispatcher processing. """
    def Dispose(self):
        """
        Dispose(self: DispatcherProcessingDisabled)
            Re-enables dispatcher processing.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: DispatcherProcessingDisabled, obj: object) -> bool
        
            Determines whether the specified System.Windows.Threading.DispatcherProcessingDisabled object is 
             equal to this System.Windows.Threading.DispatcherProcessingDisabled object.
        
        
            obj: The object to evaluate for equality.
            Returns: true if the specified object is equal to this 
             System.Windows.Threading.DispatcherProcessingDisabled object; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DispatcherProcessingDisabled) -> int
        
            Gets a hash code for this instance.
            Returns: A signed 32-bit integer hash code.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class DispatcherSynchronizationContext(SynchronizationContext):
    """
    Provides a synchronization context for Windows Presentation Foundation (WPF).
    
    DispatcherSynchronizationContext()
    DispatcherSynchronizationContext(dispatcher: Dispatcher)
    DispatcherSynchronizationContext(dispatcher: Dispatcher, priority: DispatcherPriority)
    """
    def CreateCopy(self):
        """
        CreateCopy(self: DispatcherSynchronizationContext) -> SynchronizationContext
        
            Creates a copy of this System.Windows.Threading.DispatcherSynchronizationContext.
            Returns: The copy of this synchronization context.
        """
        pass

    def Post(self, d, state):
        """
        Post(self: DispatcherSynchronizationContext, d: SendOrPostCallback, state: object)
            Invokes the callback in the synchronization context asynchronously.
        
            d: The delegate to call.
            state: The object passed to the delegate.
        """
        pass

    def Send(self, d, state):
        """
        Send(self: DispatcherSynchronizationContext, d: SendOrPostCallback, state: object)
            Invokes the callback in the synchronization context synchronously.
        
            d: The delegate to call.
            state: The object passed to the delegate.
        """
        pass

    def Wait(self, waitHandles, waitAll, millisecondsTimeout):
        """
        Wait(self: DispatcherSynchronizationContext, waitHandles: Array[IntPtr], waitAll: bool, millisecondsTimeout: int) -> int
        
            Waits for any or all the elements in the specified array to receive a signal.
        
            waitHandles: An array that contains the native operating system handles.
            waitAll: true to wait for all handles; false to wait for any handle.
            millisecondsTimeout: The number of milliseconds to wait, or System.Threading.Timeout.Infinite (-1) to wait 
             indefinitely.
        
            Returns: The array index of the object that satisfied the wait.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, dispatcher=None, priority=None):
        """
        __new__(cls: type)
        __new__(cls: type, dispatcher: Dispatcher)
        __new__(cls: type, dispatcher: Dispatcher, priority: DispatcherPriority)
        """
        pass


class DispatcherTimer(object):
    """
    A timer that is integrated into the System.Windows.Threading.Dispatcher queue which is processed at a specified interval of time and at a specified priority.
    
    DispatcherTimer()
    DispatcherTimer(priority: DispatcherPriority)
    DispatcherTimer(priority: DispatcherPriority, dispatcher: Dispatcher)
    DispatcherTimer(interval: TimeSpan, priority: DispatcherPriority, callback: EventHandler, dispatcher: Dispatcher)
    """
    def Start(self):
        """
        Start(self: DispatcherTimer)
            Starts the System.Windows.Threading.DispatcherTimer.
        """
        pass

    def Stop(self):
        """
        Stop(self: DispatcherTimer)
            Stops the System.Windows.Threading.DispatcherTimer.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, priority: DispatcherPriority)
        __new__(cls: type, priority: DispatcherPriority, dispatcher: Dispatcher)
        __new__(cls: type, interval: TimeSpan, priority: DispatcherPriority, callback: EventHandler, dispatcher: Dispatcher)
        """
        pass

    Dispatcher = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Threading.Dispatcher associated with this System.Windows.Threading.DispatcherTimer.

Get: Dispatcher(self: DispatcherTimer) -> Dispatcher

"""

    Interval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the period of time between timer ticks.

Get: Interval(self: DispatcherTimer) -> TimeSpan

Set: Interval(self: DispatcherTimer) = value
"""

    IsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the timer is running.

Get: IsEnabled(self: DispatcherTimer) -> bool

Set: IsEnabled(self: DispatcherTimer) = value
"""

    Tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a user-defined data object.

Get: Tag(self: DispatcherTimer) -> object

Set: Tag(self: DispatcherTimer) = value
"""


    Tick = None


class DispatcherUnhandledExceptionEventArgs(DispatcherEventArgs):
    """ Provides data for the System.Windows.Threading.Dispatcher�System.Windows.Threading.Dispatcher.UnhandledException event. """
    Exception = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the exception that was raised when executing code by way of the dispatcher.

Get: Exception(self: DispatcherUnhandledExceptionEventArgs) -> Exception

"""

    Handled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether the exception event has been handled.

Get: Handled(self: DispatcherUnhandledExceptionEventArgs) -> bool

Set: Handled(self: DispatcherUnhandledExceptionEventArgs) = value
"""



class DispatcherUnhandledExceptionEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Windows.Threading.Dispatcher.UnhandledException event.
    
    DispatcherUnhandledExceptionEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: DispatcherUnhandledExceptionEventHandler, sender: object, e: DispatcherUnhandledExceptionEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DispatcherUnhandledExceptionEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: DispatcherUnhandledExceptionEventHandler, sender: object, e: DispatcherUnhandledExceptionEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
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


class DispatcherUnhandledExceptionFilterEventArgs(DispatcherEventArgs):
    """ Provides data for the System.Windows.Threading.Dispatcher�System.Windows.Threading.Dispatcher.UnhandledExceptionFilter event. """
    Exception = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the exception that was raised when executing code by way of the dispatcher.

Get: Exception(self: DispatcherUnhandledExceptionFilterEventArgs) -> Exception

"""

    RequestCatch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether the exception should be caught and the event handlers called.

Get: RequestCatch(self: DispatcherUnhandledExceptionFilterEventArgs) -> bool

Set: RequestCatch(self: DispatcherUnhandledExceptionFilterEventArgs) = value
"""



class DispatcherUnhandledExceptionFilterEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Windows.Threading.Dispatcher.UnhandledExceptionFilter event.
    
    DispatcherUnhandledExceptionFilterEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: DispatcherUnhandledExceptionFilterEventHandler, sender: object, e: DispatcherUnhandledExceptionFilterEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DispatcherUnhandledExceptionFilterEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: DispatcherUnhandledExceptionFilterEventHandler, sender: object, e: DispatcherUnhandledExceptionFilterEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
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


