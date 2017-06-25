# encoding: utf-8
# module System.Windows.Input calls itself Input
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, PresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, WindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class AccessKeyEventArgs(EventArgs):
    """ Provides information for access keys events. """
    IsMultiple = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether other elements are invoked by the key.

Get: IsMultiple(self: AccessKeyEventArgs) -> bool

"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the access keys that was pressed.

Get: Key(self: AccessKeyEventArgs) -> str

"""



class AccessKeyManager(object):
    """ Maintains the registration of all access keys and the handling of interop keyboard commands between Windows Forms, Win32,�and Windows Presentation Foundation (WPF). """
    @staticmethod
    def AddAccessKeyPressedHandler(element, handler):
        """
        AddAccessKeyPressedHandler(element: DependencyObject, handler: AccessKeyPressedEventHandler)
            Adds a handler for the System.Windows.Input.AccessKeyManager.AccessKeyPressed�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to be added.
        """
        pass

    @staticmethod
    def IsKeyRegistered(scope, key):
        """
        IsKeyRegistered(scope: object, key: str) -> bool
        
            Indicates whether the specified key is registered as an access keys in the specified scope.
        
            scope: The presentation source to query for key.
            key: The key to query.
            Returns: true if the key is registered; otherwise, false.
        """
        pass

    @staticmethod
    def ProcessKey(scope, key, isMultiple):
        """
        ProcessKey(scope: object, key: str, isMultiple: bool) -> bool
        
            Processes the specified access keys as if a System.Windows.UIElement.KeyDown event for the key was passed to the System.Windows.Input.AccessKeyManager.
        
            scope: The scope for the access key.
            key: The access key.
            isMultiple: Indicates if key has multiple matches.
            Returns: true if there are more keys that match; otherwise, false.
        """
        pass

    @staticmethod
    def Register(key, element):
        """
        Register(key: str, element: IInputElement)
            Associates the specified access keys with the specified element.
        
            key: The access key.
            element: The element to associate key with.
        """
        pass

    @staticmethod
    def RemoveAccessKeyPressedHandler(element, handler):
        """
        RemoveAccessKeyPressedHandler(element: DependencyObject, handler: AccessKeyPressedEventHandler)
            Removes the specified System.Windows.Input.AccessKeyManager.AccessKeyPressed event handler from the specified object.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to be removed.
        """
        pass

    @staticmethod
    def Unregister(key, element):
        """
        Unregister(key: str, element: IInputElement)
            Disassociates the specified access keys from the specified element.
        
            key: The access key.
            element: The element from which to disassociate key.
        """
        pass

    AccessKeyPressedEvent = None


class AccessKeyPressedEventArgs(RoutedEventArgs):
    """
    Provides data for the System.Windows.Input.AccessKeyManager�routed event.
    
    AccessKeyPressedEventArgs()
    AccessKeyPressedEventArgs(key: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, key=None):
        """
        __new__(cls: type)
        __new__(cls: type, key: str)
        """
        pass

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a string representation of the access key that was pressed

Get: Key(self: AccessKeyPressedEventArgs) -> str

"""

    Scope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the scope for the element that raised this event.

Get: Scope(self: AccessKeyPressedEventArgs) -> object

Set: Scope(self: AccessKeyPressedEventArgs) = value
"""

    Target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the target for the event.

Get: Target(self: AccessKeyPressedEventArgs) -> UIElement

Set: Target(self: AccessKeyPressedEventArgs) = value
"""



class AccessKeyPressedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Windows.Input.AccessKeyManager.AccessKeyPressed�attached event.
    
    AccessKeyPressedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: AccessKeyPressedEventHandler, sender: object, e: AccessKeyPressedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null, if the method represented by the current delegate does not require arguments.
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: AccessKeyPressedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: AccessKeyPressedEventHandler, sender: object, e: AccessKeyPressedEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation list.
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


class ApplicationCommands(object):
    """ Provides a standard set of application related commands. """
    CancelPrint = None
    Close = None
    ContextMenu = None
    Copy = None
    CorrectionList = None
    Cut = None
    Delete = None
    Find = None
    Help = None
    New = None
    NotACommand = None
    Open = None
    Paste = None
    Print = None
    PrintPreview = None
    Properties = None
    Redo = None
    Replace = None
    Save = None
    SaveAs = None
    SelectAll = None
    Stop = None
    Undo = None
    __all__ = []


class CanExecuteChangedEventManager(WeakEventManager):
    # no doc
    @staticmethod
    def AddHandler(source, handler):
        """ AddHandler(source: ICommand, handler: EventHandler[EventArgs]) """
        pass

    @staticmethod
    def RemoveHandler(source, handler):
        """ RemoveHandler(source: ICommand, handler: EventHandler[EventArgs]) """
        pass

    ReadLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Establishes a read-lock on the underlying data table, and returns an System.IDisposable.

"""

    WriteLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Establishes a write-lock on the underlying data table, and returns an System.IDisposable.

"""



class CanExecuteRoutedEventArgs(RoutedEventArgs):
    """ Provides data for the System.Windows.Input.CommandBinding.CanExecute and System.Windows.Input.CommandManager.PreviewCanExecute�routed events. """
    CanExecute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the System.Windows.Input.RoutedCommand associated with this event can be executed on the command target.

Get: CanExecute(self: CanExecuteRoutedEventArgs) -> bool

Set: CanExecute(self: CanExecuteRoutedEventArgs) = value
"""

    Command = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the command associated with this event.

Get: Command(self: CanExecuteRoutedEventArgs) -> ICommand

"""

    ContinueRouting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines whether the input routed event that invoked the command should continue to route through the element tree.

Get: ContinueRouting(self: CanExecuteRoutedEventArgs) -> bool

Set: ContinueRouting(self: CanExecuteRoutedEventArgs) = value
"""

    Parameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the command specific data.

Get: Parameter(self: CanExecuteRoutedEventArgs) -> object

"""



class CanExecuteRoutedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Windows.Input.CommandBinding.CanExecute event.
    
    CanExecuteRoutedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: CanExecuteRoutedEventHandler, sender: object, e: CanExecuteRoutedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null, if the method represented by the current delegate does not require arguments.
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: CanExecuteRoutedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: CanExecuteRoutedEventHandler, sender: object, e: CanExecuteRoutedEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation list.
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


class CaptureMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the mouse capture policies.
    
    enum CaptureMode, values: Element (1), None (0), SubTree (2)
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

    Element = None
    None = None
    SubTree = None
    value__ = None


class CommandBinding(object):
    """
    Binds a System.Windows.Input.RoutedCommand to the event handlers that implement the command.
    
    CommandBinding()
    CommandBinding(command: ICommand)
    CommandBinding(command: ICommand, executed: ExecutedRoutedEventHandler)
    CommandBinding(command: ICommand, executed: ExecutedRoutedEventHandler, canExecute: CanExecuteRoutedEventHandler)
    """
    @staticmethod # known case of __new__
    def __new__(self, command=None, executed=None, canExecute=None):
        """
        __new__(cls: type)
        __new__(cls: type, command: ICommand)
        __new__(cls: type, command: ICommand, executed: ExecutedRoutedEventHandler)
        __new__(cls: type, command: ICommand, executed: ExecutedRoutedEventHandler, canExecute: CanExecuteRoutedEventHandler)
        """
        pass

    Command = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Input.ICommand associated with this System.Windows.Input.CommandBinding.

Get: Command(self: CommandBinding) -> ICommand

Set: Command(self: CommandBinding) = value
"""


    CanExecute = None
    Executed = None
    PreviewCanExecute = None
    PreviewExecuted = None


class CommandBindingCollection(object, IList, ICollection, IEnumerable):
    """
    Represents a collection of System.Windows.Input.CommandBinding objects.
    
    CommandBindingCollection()
    CommandBindingCollection(commandBindings: IList)
    """
    def Add(self, commandBinding):
        """
        Add(self: CommandBindingCollection, commandBinding: CommandBinding) -> int
        
            Adds the specified System.Windows.Input.CommandBinding to this System.Windows.Input.CommandBindingCollection.
        
            commandBinding: The binding to add to the collection.
            Returns: 0, if the operation was successful (note that this is not the index of the added item).
        """
        pass

    def AddRange(self, collection):
        """
        AddRange(self: CommandBindingCollection, collection: ICollection)
            Adds the items of the specified System.Collections.ICollection to the end of this System.Windows.Input.CommandBindingCollection.
        
            collection: The collection of items to add to the end of this System.Windows.Input.CommandBindingCollection.
        """
        pass

    def Clear(self):
        """
        Clear(self: CommandBindingCollection)
            Removes all items from this System.Windows.Input.CommandBindingCollection.
        """
        pass

    def Contains(self, commandBinding):
        """
        Contains(self: CommandBindingCollection, commandBinding: CommandBinding) -> bool
        
            Determines whether the specified System.Windows.Input.CommandBinding is in this System.Windows.Input.CommandBindingCollection.
        
            commandBinding: The binding to locate in the collection.
            Returns: true if the specified System.Windows.Input.CommandBinding is in the collection; otherwise, false.
        """
        pass

    def CopyTo(self, commandBindings, index):
        """
        CopyTo(self: CommandBindingCollection, commandBindings: Array[CommandBinding], index: int)
            Copies all of the items in the System.Windows.Input.CommandBindingCollection to the specified one-dimensional array, starting at the specified index of the target array.
        
            commandBindings: The array into which the collection is copied.
            index: The index position in commandBindings at which copying starts.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: CommandBindingCollection) -> IEnumerator
        
            Gets an enumerator that iterates through this System.Windows.Input.CommandBindingCollection.
            Returns: The enumerator for this collection.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: CommandBindingCollection, value: CommandBinding) -> int
        
            Searches for the first occurrence of the specified System.Windows.Input.CommandBinding in this System.Windows.Input.CommandBindingCollection.
        
            value: The binding to locate in the collection.
            Returns: The index of the first occurrence of value, if found; otherwise, -1.
        """
        pass

    def Insert(self, index, commandBinding):
        """
        Insert(self: CommandBindingCollection, index: int, commandBinding: CommandBinding)
            Inserts the specified System.Windows.Input.CommandBinding into this System.Windows.Input.CommandBindingCollection at the specified index.
        
            index: The zero-based index at which to insert commandBinding
            commandBinding: The binding to insert.
        """
        pass

    def Remove(self, commandBinding):
        """
        Remove(self: CommandBindingCollection, commandBinding: CommandBinding)
            Removes the first occurrence of the specified System.Windows.Input.CommandBinding from this System.Windows.Input.CommandBindingCollection.
        
            commandBinding: The binding to remove.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: CommandBindingCollection, index: int)
            Removes the specified System.Windows.Input.CommandBinding at the specified index of this System.Windows.Input.CommandBindingCollection.
        
            index: The zero-based index of the System.Windows.Input.CommandBinding to remove.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: IList, value: object) -> bool
        
            Determines whether the System.Collections.IList contains a specific value.
        
            value: The object to locate in the System.Collections.IList.
            Returns: true if the System.Object is found in the System.Collections.IList; otherwise, false.
        """
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, commandBindings=None):
        """
        __new__(cls: type)
        __new__(cls: type, commandBindings: IList)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of System.Windows.Input.CommandBinding items in this System.Windows.Input.CommandBindingCollection.

Get: Count(self: CommandBindingCollection) -> int

"""

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this System.Windows.Input.CommandBindingCollection has a fixed size.

Get: IsFixedSize(self: CommandBindingCollection) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this System.Windows.Input.CommandBindingCollection is read-only.

Get: IsReadOnly(self: CommandBindingCollection) -> bool

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether access to this System.Windows.Input.CommandBindingCollection is synchronized (thread-safe).

Get: IsSynchronized(self: CommandBindingCollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an object that can be used to synchronize access to the System.Windows.Input.CommandBindingCollection.

Get: SyncRoot(self: CommandBindingCollection) -> object

"""



class CommandConverter(TypeConverter):
    """
    Converts an System.Windows.Input.ICommand object to and from other types.
    
    CommandConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: CommandConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether an object of the specified type can be converted to an instance of System.Windows.Input.ICommand, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            sourceType: The type being evaluated for conversion.
            Returns: true if sourceType is of type System.String; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: CommandConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether an instance of System.Windows.Input.ICommand can be converted to the specified type, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            destinationType: The type being evaluated for conversion.
            Returns: true if destinationType is of type System.String; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: CommandConverter, context: ITypeDescriptorContext, culture: CultureInfo, source: object) -> object
        
            Attempts to convert the specified object to an System.Windows.Input.ICommand, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            culture: Culture specific information.
            source: The object to convert.
            Returns: The converted object, or null if source is an empty string.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: CommandConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Attempts to convert an System.Windows.Input.ICommand to the specified type, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            culture: Culture specific information.
            value: The object to convert.
            destinationType: The type to convert the object to.
            Returns: The converted object, or an empty string.
        """
        pass


class CommandManager(object):
    """ Provides command related utility methods that register System.Windows.Input.CommandBinding and System.Windows.Input.InputBinding objects for class owners and commands, add and remove command event handlers, and provides services for querying the status of a command. """
    @staticmethod
    def AddCanExecuteHandler(element, handler):
        """
        AddCanExecuteHandler(element: UIElement, handler: CanExecuteRoutedEventHandler)
            Attaches the specified System.Windows.Input.CanExecuteRoutedEventHandler to the specified element.
        
            element: The element to attach handler to.
            handler: The can execute handler.
        """
        pass

    @staticmethod
    def AddExecutedHandler(element, handler):
        """
        AddExecutedHandler(element: UIElement, handler: ExecutedRoutedEventHandler)
            Attaches the specified System.Windows.Input.ExecutedRoutedEventHandler to the specified element.
        
            element: The element to attach handler to.
            handler: The executed handler.
        """
        pass

    @staticmethod
    def AddPreviewCanExecuteHandler(element, handler):
        """
        AddPreviewCanExecuteHandler(element: UIElement, handler: CanExecuteRoutedEventHandler)
            Attaches the specified System.Windows.Input.CanExecuteRoutedEventHandler to the specified element.
        
            element: The element to attach handler to.
            handler: The can execute handler.
        """
        pass

    @staticmethod
    def AddPreviewExecutedHandler(element, handler):
        """
        AddPreviewExecutedHandler(element: UIElement, handler: ExecutedRoutedEventHandler)
            Attaches the specified System.Windows.Input.ExecutedRoutedEventHandler to the specified element.
        
            element: The element to attach handler to.
            handler: The can execute handler.
        """
        pass

    @staticmethod
    def InvalidateRequerySuggested():
        """
        InvalidateRequerySuggested()
            Forces the System.Windows.Input.CommandManager to raise the System.Windows.Input.CommandManager.RequerySuggested event.
        """
        pass

    @staticmethod
    def RegisterClassCommandBinding(type, commandBinding):
        """
        RegisterClassCommandBinding(type: Type, commandBinding: CommandBinding)
            Registers a System.Windows.Input.CommandBinding with the specified type.
        
            type: The class with which to register commandBinding.
            commandBinding: The command binding to register.
        """
        pass

    @staticmethod
    def RegisterClassInputBinding(type, inputBinding):
        """
        RegisterClassInputBinding(type: Type, inputBinding: InputBinding)
            Registers the specified System.Windows.Input.InputBinding with the specified type.
        
            type: The type to register inputBinding with.
            inputBinding: The input binding to register.
        """
        pass

    @staticmethod
    def RemoveCanExecuteHandler(element, handler):
        """
        RemoveCanExecuteHandler(element: UIElement, handler: CanExecuteRoutedEventHandler)
            Detaches the specified System.Windows.Input.CanExecuteRoutedEventHandler from the specified element.
        
            element: The element to remove handler from.
            handler: The can execute handler.
        """
        pass

    @staticmethod
    def RemoveExecutedHandler(element, handler):
        """
        RemoveExecutedHandler(element: UIElement, handler: ExecutedRoutedEventHandler)
            Detaches the specified System.Windows.Input.ExecutedRoutedEventHandler from the specified element.
        
            element: The element to remove handler from.
            handler: The executed handler.
        """
        pass

    @staticmethod
    def RemovePreviewCanExecuteHandler(element, handler):
        """
        RemovePreviewCanExecuteHandler(element: UIElement, handler: CanExecuteRoutedEventHandler)
            Detaches the specified System.Windows.Input.CanExecuteRoutedEventHandler from the specified element.
        
            element: The element to remove handler from.
            handler: The can execute handler.
        """
        pass

    @staticmethod
    def RemovePreviewExecutedHandler(element, handler):
        """
        RemovePreviewExecutedHandler(element: UIElement, handler: ExecutedRoutedEventHandler)
            Detaches the specified System.Windows.Input.ExecutedRoutedEventHandler from the specified element.
        
            element: The element to remove handler from.
            handler: The executed handler.
        """
        pass

    CanExecuteEvent = None
    ExecutedEvent = None
    PreviewCanExecuteEvent = None
    PreviewExecutedEvent = None
    RequerySuggested = None


class ComponentCommands(object):
    """ Provides a standard set of component-related commands, which have predefined key input gestures and System.Windows.Input.RoutedUICommand.Text properties. """
    ExtendSelectionDown = None
    ExtendSelectionLeft = None
    ExtendSelectionRight = None
    ExtendSelectionUp = None
    MoveDown = None
    MoveFocusBack = None
    MoveFocusDown = None
    MoveFocusForward = None
    MoveFocusPageDown = None
    MoveFocusPageUp = None
    MoveFocusUp = None
    MoveLeft = None
    MoveRight = None
    MoveToEnd = None
    MoveToHome = None
    MoveToPageDown = None
    MoveToPageUp = None
    MoveUp = None
    ScrollByLine = None
    ScrollPageDown = None
    ScrollPageLeft = None
    ScrollPageRight = None
    ScrollPageUp = None
    SelectToEnd = None
    SelectToHome = None
    SelectToPageDown = None
    SelectToPageUp = None
    __all__ = []


class Cursor(object, IDisposable):
    """
    Represents the image used for the mouse pointer.
    
    Cursor(cursorStream: Stream, scaleWithDpi: bool)
    Cursor(cursorFile: str)
    Cursor(cursorFile: str, scaleWithDpi: bool)
    Cursor(cursorStream: Stream)
    """
    def Dispose(self):
        """
        Dispose(self: Cursor)
            Releases the resources used by the System.Windows.Input.Cursor class.
        """
        pass

    def ToString(self):
        """
        ToString(self: Cursor) -> str
        
            Returns the string representation of the System.Windows.Input.Cursor.
            Returns: The name of the cursor.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cursorFile: str)
        __new__(cls: type, cursorFile: str, scaleWithDpi: bool)
        __new__(cls: type, cursorStream: Stream)
        __new__(cls: type, cursorStream: Stream, scaleWithDpi: bool)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class CursorConverter(TypeConverter):
    """
    Converts a System.Windows.Input.Cursor object to and from other types.
    
    CursorConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: CursorConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether an object of the specified type can be converted to an instance of System.Windows.Input.Cursor, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            sourceType: The type being evaluated for conversion.
            Returns: true if sourceType is of type System.String; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: CursorConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether an instance of System.Windows.Input.Cursor can be converted to the specified type, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            destinationType: The type being evaluated for conversion.
            Returns: true if destinationType is of type System.String; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: CursorConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Attempts to convert the specified object to a System.Windows.Input.Cursor, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            culture: Culture specific information.
            value: The object to convert.
            Returns: The converted object, or null if value is an empty string.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: CursorConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Attempts to convert a System.Windows.Input.Cursor to the specified type, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            culture: Culture specific information.
            value: The object to convert.
            destinationType: The type to convert the object to.
            Returns: The converted object, or an empty string if value is null.
        """
        pass

    def GetStandardValues(self, context=None):
        """
        GetStandardValues(self: CursorConverter, context: ITypeDescriptorContext) -> StandardValuesCollection
        
            Gets a collection of standard cursor values, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            Returns: A collection that holds a standard set of valid values.
        """
        pass

    def GetStandardValuesSupported(self, context=None):
        """
        GetStandardValuesSupported(self: CursorConverter, context: ITypeDescriptorContext) -> bool
        
            Determines whether this object supports a standard set of values that can be picked from a list, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            Returns: Always returns true.
        """
        pass


class Cursors(object):
    """ Defines a set of default cursors. """
    AppStarting = None
    Arrow = None
    ArrowCD = None
    Cross = None
    Hand = None
    Help = None
    IBeam = None
    No = None
    None = None
    Pen = None
    ScrollAll = None
    ScrollE = None
    ScrollN = None
    ScrollNE = None
    ScrollNS = None
    ScrollNW = None
    ScrollS = None
    ScrollSE = None
    ScrollSW = None
    ScrollW = None
    ScrollWE = None
    SizeAll = None
    SizeNESW = None
    SizeNS = None
    SizeNWSE = None
    SizeWE = None
    UpArrow = None
    Wait = None
    __all__ = []


class CursorType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the built in cursor types.
    
    enum CursorType, values: AppStarting (3), Arrow (2), ArrowCD (27), Cross (4), Hand (14), Help (5), IBeam (6), No (1), None (0), Pen (15), ScrollAll (18), ScrollE (22), ScrollN (19), ScrollNE (24), ScrollNS (16), ScrollNW (23), ScrollS (20), ScrollSE (26), ScrollSW (25), ScrollW (21), ScrollWE (17), SizeAll (7), SizeNESW (8), SizeNS (9), SizeNWSE (10), SizeWE (11), UpArrow (12), Wait (13)
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

    AppStarting = None
    Arrow = None
    ArrowCD = None
    Cross = None
    Hand = None
    Help = None
    IBeam = None
    No = None
    None = None
    Pen = None
    ScrollAll = None
    ScrollE = None
    ScrollN = None
    ScrollNE = None
    ScrollNS = None
    ScrollNW = None
    ScrollS = None
    ScrollSE = None
    ScrollSW = None
    ScrollW = None
    ScrollWE = None
    SizeAll = None
    SizeNESW = None
    SizeNS = None
    SizeNWSE = None
    SizeWE = None
    UpArrow = None
    value__ = None
    Wait = None


class ExecutedRoutedEventArgs(RoutedEventArgs):
    """ Provides data for the System.Windows.Input.CommandManager.Executed and System.Windows.Input.CommandManager.PreviewExecuted�routed events. """
    Command = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the command that was invoked.

Get: Command(self: ExecutedRoutedEventArgs) -> ICommand

"""

    Parameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets data parameter of the command.

Get: Parameter(self: ExecutedRoutedEventArgs) -> object

"""



class ExecutedRoutedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Windows.Input.CommandBinding.Executed�and System.Windows.Input.CommandBinding.PreviewExecuted�routed events, as well as related attached events.
    
    ExecutedRoutedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: ExecutedRoutedEventHandler, sender: object, e: ExecutedRoutedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null, if the method represented by the current delegate does not require arguments.
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ExecutedRoutedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ExecutedRoutedEventHandler, sender: object, e: ExecutedRoutedEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation list.
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


class FocusManager(object):
    """ Provides a set of static methods, attached properties, and events for determining and setting focus scopes and for setting the focused element within the scope. """
    @staticmethod
    def AddGotFocusHandler(element, handler):
        """ AddGotFocusHandler(element: DependencyObject, handler: RoutedEventHandler) """
        pass

    @staticmethod
    def AddLostFocusHandler(element, handler):
        """ AddLostFocusHandler(element: DependencyObject, handler: RoutedEventHandler) """
        pass

    @staticmethod
    def GetFocusedElement(element):
        """
        GetFocusedElement(element: DependencyObject) -> IInputElement
        
            Gets the element with logical focus within the specified focus scope.
        
            element: The element with logical focus in the specified focus scope.
            Returns: The element in the specified focus scope with logical focus.
        """
        pass

    @staticmethod
    def GetFocusScope(element):
        """
        GetFocusScope(element: DependencyObject) -> DependencyObject
        
            Determines the closest ancestor of the specified element that has System.Windows.Input.FocusManager.IsFocusScope set to true.
        
            element: The element to get the closest focus scope for.
            Returns: The focus scope for the specified element.
        """
        pass

    @staticmethod
    def GetIsFocusScope(element):
        """
        GetIsFocusScope(element: DependencyObject) -> bool
        
            Determines whether the specified System.Windows.DependencyObject is a focus scope.
        
            element: The element from which to read the attached property.
            Returns: true if System.Windows.Input.FocusManager.IsFocusScope is set to true on the specified element; otherwise, false.
        """
        pass

    @staticmethod
    def RemoveGotFocusHandler(element, handler):
        """ RemoveGotFocusHandler(element: DependencyObject, handler: RoutedEventHandler) """
        pass

    @staticmethod
    def RemoveLostFocusHandler(element, handler):
        """ RemoveLostFocusHandler(element: DependencyObject, handler: RoutedEventHandler) """
        pass

    @staticmethod
    def SetFocusedElement(element, value):
        """
        SetFocusedElement(element: DependencyObject, value: IInputElement)
            Sets logical focus on the specified element.
        
            element: The focus scope in which to make the specified element the System.Windows.Input.FocusManager.FocusedElement.
            value: The element to give logical focus to.
        """
        pass

    @staticmethod
    def SetIsFocusScope(element, value):
        """
        SetIsFocusScope(element: DependencyObject, value: bool)
            Sets the specified System.Windows.DependencyObject as a focus scope.
        
            element: The element to make a focus scope.
            value: true if element is a focus scope; otherwise, false.
        """
        pass

    FocusedElementProperty = None
    GotFocusEvent = None
    IsFocusScopeProperty = None
    LostFocusEvent = None
    __all__ = [
        'AddGotFocusHandler',
        'AddLostFocusHandler',
        'FocusedElementProperty',
        'GetFocusedElement',
        'GetFocusScope',
        'GetIsFocusScope',
        'GotFocusEvent',
        'IsFocusScopeProperty',
        'LostFocusEvent',
        'RemoveGotFocusHandler',
        'RemoveLostFocusHandler',
        'SetFocusedElement',
        'SetIsFocusScope',
    ]


class FocusNavigationDirection(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the direction within a user interface (UI) in which a desired focus change request is attempted. The direction is either based on tab order or by relative direction in layout.
    
    enum FocusNavigationDirection, values: Down (7), First (2), Last (3), Left (4), Next (0), Previous (1), Right (5), Up (6)
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

    Down = None
    First = None
    Last = None
    Left = None
    Next = None
    Previous = None
    Right = None
    Up = None
    value__ = None


class ICommand:
    # no doc
    def CanExecute(self, parameter):
        """ CanExecute(self: ICommand, parameter: object) -> bool """
        pass

    def Execute(self, parameter):
        """ Execute(self: ICommand, parameter: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CanExecuteChanged = None


class ICommandSource:
    """ Defines an object that knows how to invoke a command. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Command = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the command that will be executed when the command source is invoked.

Get: Command(self: ICommandSource) -> ICommand

"""

    CommandParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents a user defined data value that can be passed to the command when it is executed.

Get: CommandParameter(self: ICommandSource) -> object

"""

    CommandTarget = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The object that the command is being executed on.

Get: CommandTarget(self: ICommandSource) -> IInputElement

"""



class IInputLanguageSource:
    """ Defines necessary facilities for an object that intends to behave as an input language source. """
    def Initialize(self):
        """
        Initialize(self: IInputLanguageSource)
            Initializes an input language source object.
        """
        pass

    def Uninitialize(self):
        """
        Uninitialize(self: IInputLanguageSource)
            Un-initializes an input language source object.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CurrentInputLanguage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current input language for this input language source object.

Get: CurrentInputLanguage(self: IInputLanguageSource) -> CultureInfo

Set: CurrentInputLanguage(self: IInputLanguageSource) = value
"""

    InputLanguageList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a list of input languages supported by this input language source object.

Get: InputLanguageList(self: IInputLanguageSource) -> IEnumerable

"""



class IManipulator:
    """ Provides the position of input that is needed to create a manipulation. """
    def GetPosition(self, relativeTo):
        """
        GetPosition(self: IManipulator, relativeTo: IInputElement) -> Point
        
            Returns the position of the System.Windows.Input.IManipulator object.
        
            relativeTo: The element to use as the frame of reference for calculating the position of the System.Windows.Input.IManipulator.
            Returns: The position of the System.Windows.Input.IManipulator object.
        """
        pass

    def ManipulationEnded(self, cancel):
        """
        ManipulationEnded(self: IManipulator, cancel: bool)
            Called when the manipulation ends.
        
            cancel: true if the manipulation is canceled; otherwise, false.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a unique identifier for the object.

Get: Id(self: IManipulator) -> int

"""


    Updated = None


class ImeConversionModeValues(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes a mode of input conversion to be performed by an input method.
    
    enum (flags) ImeConversionModeValues, values: Alphanumeric (512), CharCode (16), DoNotCare (-2147483648), Eudc (64), Fixed (256), FullShape (4), Katakana (2), Native (1), NoConversion (32), Roman (8), Symbol (128)
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

    Alphanumeric = None
    CharCode = None
    DoNotCare = None
    Eudc = None
    Fixed = None
    FullShape = None
    Katakana = None
    Native = None
    NoConversion = None
    Roman = None
    Symbol = None
    value__ = None


class ImeSentenceModeValues(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the mode of sentence conversion performed by an input method.
    
    enum (flags) ImeSentenceModeValues, values: Automatic (4), Conversation (16), DoNotCare (-2147483648), None (0), PhrasePrediction (8), PluralClause (1), SingleConversion (2)
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

    Automatic = None
    Conversation = None
    DoNotCare = None
    None = None
    PhrasePrediction = None
    PluralClause = None
    SingleConversion = None
    value__ = None


class InertiaExpansionBehavior(object):
    """
    Controls the deceleration of a resizing manipulation during inertia.
    
    InertiaExpansionBehavior()
    """
    DesiredDeceleration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the rate that resizing slows in device-independent units (1/96th inch per unit) per square milliseconds.

Get: DesiredDeceleration(self: InertiaExpansionBehavior) -> float

Set: DesiredDeceleration(self: InertiaExpansionBehavior) = value
"""

    DesiredExpansion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the amount the element resizes at the end of inertia.

Get: DesiredExpansion(self: InertiaExpansionBehavior) -> Vector

Set: DesiredExpansion(self: InertiaExpansionBehavior) = value
"""

    InitialRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the initial average radius.

Get: InitialRadius(self: InertiaExpansionBehavior) -> float

Set: InitialRadius(self: InertiaExpansionBehavior) = value
"""

    InitialVelocity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the initial rate the element resizes at the start of inertia.

Get: InitialVelocity(self: InertiaExpansionBehavior) -> Vector

Set: InitialVelocity(self: InertiaExpansionBehavior) = value
"""



class InertiaRotationBehavior(object):
    """
    Controls the deceleration of a rotation manipulation during inertia.
    
    InertiaRotationBehavior()
    """
    DesiredDeceleration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the rate the rotation slows in degrees per squared millisecond.

Get: DesiredDeceleration(self: InertiaRotationBehavior) -> float

Set: DesiredDeceleration(self: InertiaRotationBehavior) = value
"""

    DesiredRotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the rotation, in degrees, at the end of the inertial movement.

Get: DesiredRotation(self: InertiaRotationBehavior) -> float

Set: DesiredRotation(self: InertiaRotationBehavior) = value
"""

    InitialVelocity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the initial rate of the rotation at the start of the inertia phase.

Get: InitialVelocity(self: InertiaRotationBehavior) -> float

Set: InitialVelocity(self: InertiaRotationBehavior) = value
"""



class InertiaTranslationBehavior(object):
    """
    Controls deceleration on a translation manipulation during inertia.
    
    InertiaTranslationBehavior()
    """
    DesiredDeceleration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the rate the linear movement slows in device-independent units (1/96th inch per unit) per squared millisecond.

Get: DesiredDeceleration(self: InertiaTranslationBehavior) -> float

Set: DesiredDeceleration(self: InertiaTranslationBehavior) = value
"""

    DesiredDisplacement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the linear movement of the manipulation at the end of inertia.

Get: DesiredDisplacement(self: InertiaTranslationBehavior) -> float

Set: DesiredDisplacement(self: InertiaTranslationBehavior) = value
"""

    InitialVelocity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the initial rate of linear movement at the start of the inertia phase.

Get: InitialVelocity(self: InertiaTranslationBehavior) -> Vector

Set: InitialVelocity(self: InertiaTranslationBehavior) = value
"""



class InputBinding(Freezable, ISealable, ICommandSource):
    """
    Represents a binding between an System.Windows.Input.InputGesture and a command. The command is potentially a System.Windows.Input.RoutedCommand.
    
    InputBinding(command: ICommand, gesture: InputGesture)
    """
    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: InputBinding, sourceFreezable: Freezable)
            Copies the base (non-animated) values of the properties of the specified object.
        
            sourceFreezable: The object to clone.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: InputBinding, sourceFreezable: Freezable)
            Copies the current values of the properties of the specified object.
        
            sourceFreezable: The object to clone.
        """
        pass

    def CreateInstance(self, *args): #cannot find CLR method
        """
        CreateInstance(self: Freezable) -> Freezable
        
            Initializes a new instance of the System.Windows.Freezable class.
            Returns: The new instance.
        """
        pass

    def CreateInstanceCore(self, *args): #cannot find CLR method
        """
        CreateInstanceCore(self: InputBinding) -> Freezable
        
            Creates an instance of an System.Windows.Input.InputBinding.
            Returns: The new object.
        """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: Freezable, isChecking: bool) -> bool
        
            Makes the System.Windows.Freezable object unmodifiable or tests whether it can be made unmodifiable.
        
            isChecking: true to return an indication of whether the object can be frozen (without actually freezing it); false to actually freeze the object.
            Returns: If isChecking is true, this method returns true if the System.Windows.Freezable can be made unmodifiable, or false if it cannot be made unmodifiable. If isChecking is false, this method returns true if the 
             if the specified System.Windows.Freezable is now unmodifiable, or false if it cannot be made unmodifiable.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: InputBinding, sourceFreezable: Freezable)
            Makes the instance a frozen clone of the specified System.Windows.Freezable by using base (non-animated) property values.
        
            sourceFreezable: The object to clone.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: InputBinding, sourceFreezable: Freezable)
            Makes the current instance a frozen clone of the specified System.Windows.Freezable. If the object has animated dependency properties, their current animated values are copied.
        
            sourceFreezable: The object to clone.
        """
        pass

    def OnChanged(self, *args): #cannot find CLR method
        """
        OnChanged(self: Freezable)
            Called when the current System.Windows.Freezable object is modified.
        """
        pass

    def OnFreezablePropertyChanged(self, *args): #cannot find CLR method
        """
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject, property: DependencyProperty)
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not intended to be used directly from your code.
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a System.Windows.DependencyObjectType data member that has just been set.
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventArgs) to also invoke any 
             System.Windows.Freezable.Changed handlers in response to a changing dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of System.Windows.Freezable must call this method at the beginning of any API that reads data members that are 
             not dependency properties.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for the provided dependency property.
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable should call 
             this method at the end of any API that modifies class members that are not stored as dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a valid threading context. System.Windows.Freezable inheritors should call this method at the beginning of any 
             API that writes to data members that are not dependency properties.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, command, gesture):
        """
        __new__(cls: type)
        __new__(cls: type, command: ICommand, gesture: InputGesture)
        """
        pass

    Command = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Input.ICommand associated with this input binding.

Get: Command(self: InputBinding) -> ICommand

Set: Command(self: InputBinding) = value
"""

    CommandParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the command-specific data for a particular command.

Get: CommandParameter(self: InputBinding) -> object

Set: CommandParameter(self: InputBinding) = value
"""

    CommandTarget = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the target element of the command.

Get: CommandTarget(self: InputBinding) -> IInputElement

Set: CommandTarget(self: InputBinding) = value
"""

    Gesture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Input.InputGesture associated with this input binding.

Get: Gesture(self: InputBinding) -> InputGesture

Set: Gesture(self: InputBinding) = value
"""


    CommandParameterProperty = None
    CommandProperty = None
    CommandTargetProperty = None


class InputBindingCollection(object, IList, ICollection, IEnumerable):
    """
    Represents an ordered collection of System.Windows.Input.InputBinding objects.
    
    InputBindingCollection()
    InputBindingCollection(inputBindings: IList)
    """
    def Add(self, inputBinding):
        """
        Add(self: InputBindingCollection, inputBinding: InputBinding) -> int
        
            Adds the specified System.Windows.Input.InputBinding to this System.Windows.Input.InputBindingCollection.
        
            inputBinding: The binding to add to the collection.
            Returns: Always returns 0. This deviates from the standard System.Collections.IList implementation for Add, which should return the index where the new item was added to the collection.
        """
        pass

    def AddRange(self, collection):
        """
        AddRange(self: InputBindingCollection, collection: ICollection)
            Adds the items of the specified System.Collections.ICollection to the end of this System.Windows.Input.InputBindingCollection
        
            collection: The collection of items to add to the end of this System.Windows.Input.InputBindingCollection.
        """
        pass

    def Clear(self):
        """
        Clear(self: InputBindingCollection)
            Removes all items from this System.Windows.Input.InputBindingCollection.
        """
        pass

    def Contains(self, key):
        """
        Contains(self: InputBindingCollection, key: InputBinding) -> bool
        
            Determines whether the specified System.Windows.Input.InputBinding is in this System.Windows.Input.InputBindingCollection
        
            key: The binding to locate in the collection.
            Returns: true if the specified System.Windows.Input.InputBinding is in the collection; otherwise, false.
        """
        pass

    def CopyTo(self, inputBindings, index):
        """
        CopyTo(self: InputBindingCollection, inputBindings: Array[InputBinding], index: int)
            Copies all of the items in the System.Windows.Input.InputBindingCollection to the specified one-dimensional array, starting at the specified index of the target array.
        
            inputBindings: The array into which the collection is copied.
            index: The index position in inputBindings at which copying starts.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: InputBindingCollection) -> IEnumerator
        
            Gets an enumerator that iterates through this System.Windows.Input.InputBindingCollection.
            Returns: The enumerator for this collection.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: InputBindingCollection, value: InputBinding) -> int
        
            Searches for the first occurrence of the specified System.Windows.Input.InputBinding in his System.Windows.Input.InputBindingCollection.
        
            value: The object to locate in the collection.
                """
        pass

    def Insert(self, index, inputBinding):
        """
        Insert(self: InputBindingCollection, index: int, inputBinding: InputBinding)
            Inserts the specified System.Windows.Input.InputBinding into this System.Windows.Input.InputBindingCollection at the specified index.
        
            index: The zero-based index at which to insert inputBinding.
            inputBinding: The binding to insert.
        """
        pass

    def Remove(self, inputBinding):
        """
        Remove(self: InputBindingCollection, inputBinding: InputBinding)
            Removes the first occurrence of the specified System.Windows.Input.InputBinding from this System.Windows.Input.InputBindingCollection.
        
            inputBinding: The binding to remove.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: InputBindingCollection, index: int)
            Removes the specified System.Windows.Input.InputBinding at the specified index of this System.Windows.Input.InputBindingCollection.
        
            index: The zero-based index of the System.Windows.Input.InputBinding to remove.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: IList, value: object) -> bool
        
            Determines whether the System.Collections.IList contains a specific value.
        
            value: The object to locate in the System.Collections.IList.
            Returns: true if the System.Object is found in the System.Collections.IList; otherwise, false.
        """
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, inputBindings=None):
        """
        __new__(cls: type)
        __new__(cls: type, inputBindings: IList)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of System.Windows.Input.InputBinding items in this collection.

Get: Count(self: InputBindingCollection) -> int

"""

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this System.Windows.Input.InputBindingCollection has a fixed size.

Get: IsFixedSize(self: InputBindingCollection) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this System.Windows.Input.InputBindingCollection is read-only.

Get: IsReadOnly(self: InputBindingCollection) -> bool

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether access to this System.Windows.Input.InputBindingCollection is synchronized (thread-safe).

Get: IsSynchronized(self: InputBindingCollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an object that can be used to synchronize access to the System.Windows.Input.InputBindingCollection.

Get: SyncRoot(self: InputBindingCollection) -> object

"""



class InputDevice(DispatcherObject):
    """ Abstract class that describes an input devices. """
    ActiveSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the System.Windows.PresentationSource that is reporting input for this device.

Get: ActiveSource(self: InputDevice) -> PresentationSource

"""

    Target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the element that receives input from this device.

Get: Target(self: InputDevice) -> IInputElement

"""



class InputEventArgs(RoutedEventArgs):
    """
    Provides data for input related events.
    
    InputEventArgs(inputDevice: InputDevice, timestamp: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, inputDevice, timestamp):
        """ __new__(cls: type, inputDevice: InputDevice, timestamp: int) """
        pass

    Device = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the input device that initiated this event.

Get: Device(self: InputEventArgs) -> InputDevice

"""

    Timestamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time when this event occurred.

Get: Timestamp(self: InputEventArgs) -> int

"""



class InputEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that handles input related routed events.
    
    InputEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: InputEventHandler, sender: object, e: InputEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null, if the method represented by the current delegate does not require arguments.
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: InputEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: InputEventHandler, sender: object, e: InputEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation list.
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


class InputGesture(object):
    """ Abstract class that describes input device gestures. """
    def Matches(self, targetElement, inputEventArgs):
        """
        Matches(self: InputGesture, targetElement: object, inputEventArgs: InputEventArgs) -> bool
        
            When overridden in a derived class, determines whether the specified System.Windows.Input.InputGesture matches the input associated with the specified System.Windows.Input.InputEventArgs object.
        
            targetElement: The target of the command.
            inputEventArgs: The input event data to compare this gesture to.
            Returns: true if the gesture matches the input; otherwise, false.
        """
        pass


class InputGestureCollection(object, IList, ICollection, IEnumerable):
    """
    Represents an ordered collection of System.Windows.Input.InputGesture objects.
    
    InputGestureCollection()
    InputGestureCollection(inputGestures: IList)
    """
    def Add(self, inputGesture):
        """
        Add(self: InputGestureCollection, inputGesture: InputGesture) -> int
        
            Adds the specified System.Windows.Input.InputGesture to this System.Windows.Input.InputGestureCollection.
        
            inputGesture: The gesture to add to the collection.
            Returns: 0, if the operation was successful (note that this is not the index of the added item).
        """
        pass

    def AddRange(self, collection):
        """
        AddRange(self: InputGestureCollection, collection: ICollection)
            Adds the elements of the specified System.Collections.ICollection to the end of this System.Windows.Input.InputGestureCollection.
        
            collection: The collection of items to add to the end of this System.Windows.Input.InputGestureCollection.
        """
        pass

    def Clear(self):
        """
        Clear(self: InputGestureCollection)
            Removes all elements from the System.Windows.Input.InputGestureCollection.
        """
        pass

    def Contains(self, key):
        """
        Contains(self: InputGestureCollection, key: InputGesture) -> bool
        
            Determines whether the specified System.Windows.Input.InputGesture is in the collection.
        
            key: The gesture to locate in the collection.
            Returns: true if the gesture is in the collection; otherwise, false.
        """
        pass

    def CopyTo(self, inputGestures, index):
        """
        CopyTo(self: InputGestureCollection, inputGestures: Array[InputGesture], index: int)
            Copies all of the items in the System.Windows.Input.InputGestureCollection to the specified one-dimensional array, starting at the specified index of the target array.
        
            inputGestures: An array into which the collection is copied.
            index: The index position in the inputGestures at which copying begins.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: InputGestureCollection) -> IEnumerator
        
            Gets an enumerator that iterates through this System.Windows.Input.InputGestureCollection.
            Returns: The enumerator for this collection.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: InputGestureCollection, value: InputGesture) -> int
        
            Searches for the first occurrence of the specified System.Windows.Input.InputGesture in this System.Windows.Input.InputGestureCollection.
        
            value: The gesture to locate in the collection.
            Returns: The index of the first occurrence of value, if found; otherwise, -1.
        """
        pass

    def Insert(self, index, inputGesture):
        """
        Insert(self: InputGestureCollection, index: int, inputGesture: InputGesture)
            Inserts the specified System.Windows.Input.InputGesture into this System.Windows.Input.InputGestureCollection at the specified index.
        
            index: Index at which to insert inputGesture.
            inputGesture: The gesture to insert.
        """
        pass

    def Remove(self, inputGesture):
        """
        Remove(self: InputGestureCollection, inputGesture: InputGesture)
            Removes the first occurrence of the specified System.Windows.Input.InputGesture from this System.Windows.Input.InputGestureCollection.
        
            inputGesture: The gesture to remove.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: InputGestureCollection, index: int)
            Removes the specified System.Windows.Input.InputGesture at the specified index of this System.Windows.Input.InputGestureCollection.
        
            index: The zero-based index of the gesture to remove.
        """
        pass

    def Seal(self):
        """
        Seal(self: InputGestureCollection)
            Sets this System.Windows.Input.InputGestureCollection to read-only.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: IList, value: object) -> bool
        
            Determines whether the System.Collections.IList contains a specific value.
        
            value: The object to locate in the System.Collections.IList.
            Returns: true if the System.Object is found in the System.Collections.IList; otherwise, false.
        """
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, inputGestures=None):
        """
        __new__(cls: type)
        __new__(cls: type, inputGestures: IList)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of System.Windows.Input.InputGesture items in this System.Windows.Input.InputGestureCollection.

Get: Count(self: InputGestureCollection) -> int

"""

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this System.Windows.Input.InputGestureCollection has a fixed size.

Get: IsFixedSize(self: InputGestureCollection) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this System.Windows.Input.InputGestureCollection is read-only.  The default value is false.

Get: IsReadOnly(self: InputGestureCollection) -> bool

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this System.Windows.Input.InputGestureCollection is synchronized (thread safe).

Get: IsSynchronized(self: InputGestureCollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an object that can be used to synchronize access to this System.Windows.Input.InputGestureCollection.

Get: SyncRoot(self: InputGestureCollection) -> object

"""



class InputLanguageEventArgs(EventArgs):
    """ Provides a base class for arguments for events dealing with a change in input language. """
    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, newLanguageId: CultureInfo, previousLanguageId: CultureInfo) """
        pass

    NewLanguage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Globalization.CultureInfo object representing the new current input language.

Get: NewLanguage(self: InputLanguageEventArgs) -> CultureInfo

"""

    PreviousLanguage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Globalization.CultureInfo object representing the previous current input language.

Get: PreviousLanguage(self: InputLanguageEventArgs) -> CultureInfo

"""



class InputLanguageChangedEventArgs(InputLanguageEventArgs):
    """
    Contains arguments associated with the System.Windows.Input.InputLanguageManager.InputLanguageChanged event.
    
    InputLanguageChangedEventArgs(newLanguageId: CultureInfo, previousLanguageId: CultureInfo)
    """
    @staticmethod # known case of __new__
    def __new__(self, newLanguageId, previousLanguageId):
        """ __new__(cls: type, newLanguageId: CultureInfo, previousLanguageId: CultureInfo) """
        pass


class InputLanguageChangingEventArgs(InputLanguageEventArgs):
    """
    Contains arguments associated with the System.Windows.Input.InputLanguageManager.InputLanguageChanging event.
    
    InputLanguageChangingEventArgs(newLanguageId: CultureInfo, previousLanguageId: CultureInfo)
    """
    @staticmethod # known case of __new__
    def __new__(self, newLanguageId, previousLanguageId):
        """ __new__(cls: type, newLanguageId: CultureInfo, previousLanguageId: CultureInfo) """
        pass

    Rejected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the initiated change of input language should be accepted or rejected.

Get: Rejected(self: InputLanguageChangingEventArgs) -> bool

Set: Rejected(self: InputLanguageChangingEventArgs) = value
"""



class InputLanguageEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Windows.Input.InputLanguageManager.InputLanguageChanged and System.Windows.Input.InputLanguageManager.InputLanguageChanging events.
    
    InputLanguageEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: InputLanguageEventHandler, sender: object, e: InputLanguageEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null, if the method represented by the current delegate does not require arguments.
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: InputLanguageEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: InputLanguageEventHandler, sender: object, e: InputLanguageEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation list.
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


class InputLanguageManager(DispatcherObject):
    """ Provides facilities for managing input languages in Windows Presentation Foundation (WPF). """
    @staticmethod
    def GetInputLanguage(target):
        """
        GetInputLanguage(target: DependencyObject) -> CultureInfo
        
            Returns the value of the System.Windows.Input.InputLanguageManager.InputLanguage �attached property for a specified dependency object.
        
            target: The dependency object for which to retrieve the input language.
            Returns: A System.Globalization.CultureInfo object representing the input language for the specified dependency object.
        """
        pass

    @staticmethod
    def GetRestoreInputLanguage(target):
        """
        GetRestoreInputLanguage(target: DependencyObject) -> bool
        
            Returns the value of System.Windows.Input.InputLanguageManager.RestoreInputLanguage �attached property for a specified dependency object.
        
            target: The dependency object for which to retrieve the value of System.Windows.Input.InputLanguageManager.RestoreInputLanguage.
            Returns: The current value of System.Windows.Input.InputLanguageManager.RestoreInputLanguage for the specified dependency object.
        """
        pass

    def RegisterInputLanguageSource(self, inputLanguageSource):
        """
        RegisterInputLanguageSource(self: InputLanguageManager, inputLanguageSource: IInputLanguageSource)
            Registers an input language source with the System.Windows.Input.InputLanguageManager.
        
            inputLanguageSource: An object that specifies the input language to register.  This object must implement the System.Windows.Input.IInputLanguageSource interface.
        """
        pass

    def ReportInputLanguageChanged(self, newLanguageId, previousLanguageId):
        """
        ReportInputLanguageChanged(self: InputLanguageManager, newLanguageId: CultureInfo, previousLanguageId: CultureInfo)
            Report the completion of a change of input language to the System.Windows.Input.InputLanguageManager.
        
            newLanguageId: A System.Globalization.CultureInfo object representing the new input language.
            previousLanguageId: A System.Globalization.CultureInfo object representing the previous input language.
        """
        pass

    def ReportInputLanguageChanging(self, newLanguageId, previousLanguageId):
        """
        ReportInputLanguageChanging(self: InputLanguageManager, newLanguageId: CultureInfo, previousLanguageId: CultureInfo) -> bool
        
            Report the initiation of a change of input language to the System.Windows.Input.InputLanguageManager.
        
            newLanguageId: A System.Globalization.CultureInfo object representing the new input language.
            previousLanguageId: A System.Globalization.CultureInfo object representing the previous input language.
            Returns: true to indicate that the reported change of input language was accepted; otherwise, false.
        """
        pass

    @staticmethod
    def SetInputLanguage(target, inputLanguage):
        """
        SetInputLanguage(target: DependencyObject, inputLanguage: CultureInfo)
            Sets the value of the System.Windows.Input.InputLanguageManager.InputLanguage attached property on the specified dependency object.
        
            target: The dependency object on which to set the System.Windows.Input.InputLanguageManager.InputLanguage attached property.
            inputLanguage: A System.Globalization.CultureInfo object representing the new value for the System.Windows.Input.InputLanguageManager.InputLanguage attached property.
        """
        pass

    @staticmethod
    def SetRestoreInputLanguage(target, restore):
        """
        SetRestoreInputLanguage(target: DependencyObject, restore: bool)
            Sets the value of the System.Windows.Input.InputLanguageManager.RestoreInputLanguage dependency property on the specified dependency object.
        
            target: The dependency object for which to set the value of System.Windows.Input.InputLanguageManager.RestoreInputLanguage.
            restore: A Boolean value to set the System.Windows.Input.InputLanguageManager.RestoreInputLanguage attached property to.
        """
        pass

    AvailableInputLanguages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an enumerator for currently available input languages.

Get: AvailableInputLanguages(self: InputLanguageManager) -> IEnumerable

"""

    CurrentInputLanguage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current input language.

Get: CurrentInputLanguage(self: InputLanguageManager) -> CultureInfo

Set: CurrentInputLanguage(self: InputLanguageManager) = value
"""


    Current = None
    InputLanguageChanged = None
    InputLanguageChanging = None
    InputLanguageProperty = None
    RestoreInputLanguageProperty = None


class InputManager(DispatcherObject):
    """ Manages all the input systems in Windows Presentation Foundation (WPF). """
    def PopMenuMode(self, menuSite):
        """
        PopMenuMode(self: InputManager, menuSite: PresentationSource)
            Called by components to leave menu mode.
        
            menuSite: The menu to leave.
        """
        pass

    def ProcessInput(self, input):
        """
        ProcessInput(self: InputManager, input: InputEventArgs) -> bool
        
            Processes the specified input synchronously.
        
            input: The input to process.
            Returns: true if all input events were handled; otherwise, false.
        """
        pass

    def PushMenuMode(self, menuSite):
        """
        PushMenuMode(self: InputManager, menuSite: PresentationSource)
            Called by components to enter menu mode.
        
            menuSite: The menu to enter.
        """
        pass

    InputProviders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of System.Windows.Input.InputManager.InputProviders registered with the System.Windows.Input.InputManager.

Get: InputProviders(self: InputManager) -> ICollection

"""

    IsInMenuMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this System.Windows.Interop.ComponentDispatcher is in menu mode.

Get: IsInMenuMode(self: InputManager) -> bool

"""

    MostRecentInputDevice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that represents the input device associated with the most recent input event.

Get: MostRecentInputDevice(self: InputManager) -> InputDevice

"""

    PrimaryKeyboardDevice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the primary keyboard device.

Get: PrimaryKeyboardDevice(self: InputManager) -> KeyboardDevice

"""

    PrimaryMouseDevice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the primary mouse device.

Get: PrimaryMouseDevice(self: InputManager) -> MouseDevice

"""


    Current = None
    EnterMenuMode = None
    HitTestInvalidatedAsync = None
    LeaveMenuMode = None
    PostNotifyInput = None
    PostProcessInput = None
    PreNotifyInput = None
    PreProcessInput = None


class InputMethod(DispatcherObject):
    """ Provides facilities for managing and interacting with the Text Services Framework, which provides support for alternate text input methods such as speech and handwriting. """
    @staticmethod
    def GetInputScope(target):
        """
        GetInputScope(target: DependencyObject) -> InputScope
        
            Returns the value of the System.Windows.Input.InputMethod.InputScope �attached property for a specified dependency object.
        
            target: The dependency object for which to retrieve the input scope.
            Returns: An System.Windows.Input.InputScope object representing the current input scope for the specified dependency object.
        """
        pass

    @staticmethod
    def GetIsInputMethodEnabled(target):
        """
        GetIsInputMethodEnabled(target: DependencyObject) -> bool
        
            Returns the value of the System.Windows.Input.InputMethod.IsInputMethodEnabled �attached property for a specified dependency object.
        
            target: The dependency object for which to retrieve the value of System.Windows.Input.InputMethod.IsInputMethodEnabled.
            Returns: The current value of System.Windows.Input.InputMethod.IsInputMethodEnabled for the specified dependency object.
        """
        pass

    @staticmethod
    def GetIsInputMethodSuspended(target):
        """
        GetIsInputMethodSuspended(target: DependencyObject) -> bool
        
            Returns the value of the System.Windows.Input.InputMethod.IsInputMethodSuspended �attached property for a specified dependency object.
        
            target: The dependency object for which to retrieve the value of System.Windows.Input.InputMethod.IsInputMethodSuspended.
            Returns: The current value of System.Windows.Input.InputMethod.IsInputMethodSuspended for the specified dependency object.
        """
        pass

    @staticmethod
    def GetPreferredImeConversionMode(target):
        """
        GetPreferredImeConversionMode(target: DependencyObject) -> ImeConversionModeValues
        
            Returns the value of the System.Windows.Input.InputMethod.PreferredImeConversionMode �attached property for a specified dependency object.
        
            target: The dependency object for which to retrieve the value of System.Windows.Input.InputMethod.PreferredImeConversionMode.
            Returns: A member of the System.Windows.Input.ImeConversionModeValues enumeration specifying the current System.Windows.Input.InputMethod.PreferredImeConversionMode for the specified dependency object.
        """
        pass

    @staticmethod
    def GetPreferredImeSentenceMode(target):
        """
        GetPreferredImeSentenceMode(target: DependencyObject) -> ImeSentenceModeValues
        
            Returns the value of the System.Windows.Input.InputMethod.PreferredImeSentenceMode �attached property for a specified dependency object.
        
            target: The dependency object for which to retrieve the value of System.Windows.Input.InputMethod.PreferredImeSentenceMode.
            Returns: A member of the System.Windows.Input.ImeSentenceModeValues enumeration specifying the current System.Windows.Input.InputMethod.PreferredImeSentenceMode for the specified dependency object.
        """
        pass

    @staticmethod
    def GetPreferredImeState(target):
        """
        GetPreferredImeState(target: DependencyObject) -> InputMethodState
        
            Returns the value of the System.Windows.Input.InputMethod.PreferredImeState �attached property for a specified dependency object.
        
            target: The dependency object for which to retrieve the value of System.Windows.Input.InputMethod.PreferredImeState.
            Returns: A member of the System.Windows.Input.InputMethodState enumeration specifying the current System.Windows.Input.InputMethod.PreferredImeState for the specified dependency object.
        """
        pass

    @staticmethod
    def SetInputScope(target, value):
        """
        SetInputScope(target: DependencyObject, value: InputScope)
            Sets the value of the System.Windows.Input.InputMethod.InputScope attached property on the specified dependency object.
        
            target: The dependency object on which to set the System.Windows.Input.InputMethod.InputScope attached property.
            value: An System.Windows.Input.InputScope object representing the new value for the System.Windows.Input.InputMethod.InputScope attached property.
        """
        pass

    @staticmethod
    def SetIsInputMethodEnabled(target, value):
        """
        SetIsInputMethodEnabled(target: DependencyObject, value: bool)
            Sets the value of the System.Windows.Input.InputMethod.IsInputMethodEnabled attached property on the specified dependency object.
        
            target: The dependency object on which to set the System.Windows.Input.InputMethod.IsInputMethodEnabled attached property.
            value: The new value for the System.Windows.Input.InputMethod.IsInputMethodEnabled attached property.
        """
        pass

    @staticmethod
    def SetIsInputMethodSuspended(target, value):
        """
        SetIsInputMethodSuspended(target: DependencyObject, value: bool)
            Sets the value of the System.Windows.Input.InputMethod.IsInputMethodSuspended attached property on the specified dependency object.
        
            target: The dependency object on which to set the System.Windows.Input.InputMethod.IsInputMethodSuspended attached property.
            value: The new value for the System.Windows.Input.InputMethod.IsInputMethodSuspended attached property.
        """
        pass

    @staticmethod
    def SetPreferredImeConversionMode(target, value):
        """
        SetPreferredImeConversionMode(target: DependencyObject, value: ImeConversionModeValues)
            Sets the value of the System.Windows.Input.InputMethod.PreferredImeConversionMode attached property on the specified dependency object.
        
            target: The dependency object on which to set the System.Windows.Input.InputMethod.PreferredImeConversionMode attached property.
            value: A member of the System.Windows.Input.ImeConversionModeValues enumeration representing the new value for the System.Windows.Input.InputMethod.PreferredImeConversionMode attached property.
        """
        pass

    @staticmethod
    def SetPreferredImeSentenceMode(target, value):
        """
        SetPreferredImeSentenceMode(target: DependencyObject, value: ImeSentenceModeValues)
            Sets the value of the System.Windows.Input.InputMethod.PreferredImeSentenceMode attached property on the specified dependency object.
        
            target: The dependency object on which to set the System.Windows.Input.InputMethod.PreferredImeSentenceMode attached property.
            value: A member of the System.Windows.Input.ImeConversionModeValues enumeration representing the new value for the System.Windows.Input.InputMethod.PreferredImeSentenceMode attached property.
        """
        pass

    @staticmethod
    def SetPreferredImeState(target, value):
        """
        SetPreferredImeState(target: DependencyObject, value: InputMethodState)
            Sets the value of the System.Windows.Input.InputMethod.PreferredImeState attached property on the specified dependency object.
        
            target: The dependency object on which to set the System.Windows.Input.InputMethod.PreferredImeState attached property.
            value: A member of the System.Windows.Input.ImeConversionModeValues enumeration representing the new value for the System.Windows.Input.InputMethod.PreferredImeState attached property.
        """
        pass

    def ShowConfigureUI(self, element=None):
        """
        ShowConfigureUI(self: InputMethod, element: UIElement)
            Displays configuration user interface (UI) associated with the currently active keyboard text service, using a specified System.Windows.UIElement as the parent element for the configuration UI.
        
            element: A System.Windows.UIElement that will be used as the parent element for the configuration UI.  This parameter can be null.
        ShowConfigureUI(self: InputMethod)
            Displays configuration user interface (UI) associated with the currently active keyboard text service.
        """
        pass

    def ShowRegisterWordUI(self, *__args):
        """
        ShowRegisterWordUI(self: InputMethod, element: UIElement, registeredText: str)
            Displays word registration user interface (UI) associated with the currently active keyboard text service.  Accepts a specified string as the default value to register, and a specified 
             System.Windows.UIElement as the parent element for the configuration UI.
        
        
            element: A System.Windows.UIElement that will be used as the parent element for the word registration UI.  This parameter can be null.
            registeredText: A string that specifies a value to register.
        ShowRegisterWordUI(self: InputMethod, registeredText: str)
            Displays word registration user interface (UI) associated with the currently active keyboard text service.  Accepts a specified string as the default value to register.
        
            registeredText: A string that specifies a value to register.
        ShowRegisterWordUI(self: InputMethod)
            Displays word registration user interface (UI) associated with the currently active keyboard text service.
        """
        pass

    CanShowConfigurationUI = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether or not this input method can display configuration user interface (UI).

Get: CanShowConfigurationUI(self: InputMethod) -> bool

"""

    CanShowRegisterWordUI = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this input method can display word registration user interface (UI).

Get: CanShowRegisterWordUI(self: InputMethod) -> bool

"""

    HandwritingState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current state of handwriting input for this input method.

Get: HandwritingState(self: InputMethod) -> InputMethodState

Set: HandwritingState(self: InputMethod) = value
"""

    ImeConversionMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current conversion mode for the input method editor associated with this input method.

Get: ImeConversionMode(self: InputMethod) -> ImeConversionModeValues

Set: ImeConversionMode(self: InputMethod) = value
"""

    ImeSentenceMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current sentence mode for the input method editor associated with this input method.

Get: ImeSentenceMode(self: InputMethod) -> ImeSentenceModeValues

Set: ImeSentenceMode(self: InputMethod) = value
"""

    ImeState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current state of the input method editor associated with this input method.

Get: ImeState(self: InputMethod) -> InputMethodState

Set: ImeState(self: InputMethod) = value
"""

    MicrophoneState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current state of microphone input for this input method.

Get: MicrophoneState(self: InputMethod) -> InputMethodState

Set: MicrophoneState(self: InputMethod) = value
"""

    SpeechMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the speech mode for this input method.

Get: SpeechMode(self: InputMethod) -> SpeechMode

Set: SpeechMode(self: InputMethod) = value
"""


    Current = None
    InputScopeProperty = None
    IsInputMethodEnabledProperty = None
    IsInputMethodSuspendedProperty = None
    PreferredImeConversionModeProperty = None
    PreferredImeSentenceModeProperty = None
    PreferredImeStateProperty = None
    StateChanged = None


class InputMethodState(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes the state of an System.Windows.Input.InputMethod.
    
    enum InputMethodState, values: DoNotCare (2), Off (0), On (1)
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

    DoNotCare = None
    Off = None
    On = None
    value__ = None


class InputMethodStateChangedEventArgs(EventArgs):
    """ Contains arguments associated with the System.Windows.Input.InputMethod.StateChanged event. """
    IsHandwritingStateChanged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether or not the System.Windows.Input.InputMethod.HandwritingState property changed.

Get: IsHandwritingStateChanged(self: InputMethodStateChangedEventArgs) -> bool

"""

    IsImeConversionModeChanged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether or not the System.Windows.Input.InputMethod.ImeConversionMode property changed.

Get: IsImeConversionModeChanged(self: InputMethodStateChangedEventArgs) -> bool

"""

    IsImeSentenceModeChanged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether or not the System.Windows.Input.InputMethod.ImeSentenceMode property changed.

Get: IsImeSentenceModeChanged(self: InputMethodStateChangedEventArgs) -> bool

"""

    IsImeStateChanged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether or not the System.Windows.Input.InputMethod.ImeState property changed.

Get: IsImeStateChanged(self: InputMethodStateChangedEventArgs) -> bool

"""

    IsMicrophoneStateChanged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether or not the System.Windows.Input.InputMethod.MicrophoneState property changed.

Get: IsMicrophoneStateChanged(self: InputMethodStateChangedEventArgs) -> bool

"""

    IsSpeechModeChanged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether or not the System.Windows.Input.InputMethod.SpeechMode property changed.

Get: IsSpeechModeChanged(self: InputMethodStateChangedEventArgs) -> bool

"""



class InputMethodStateChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Windows.Input.InputMethod.StateChanged event.
    
    InputMethodStateChangedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: InputMethodStateChangedEventHandler, sender: object, e: InputMethodStateChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null, if the method represented by the current delegate does not require arguments.
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: InputMethodStateChangedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: InputMethodStateChangedEventHandler, sender: object, e: InputMethodStateChangedEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation list.
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


class InputMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the possible values for the input mode.
    
    enum InputMode, values: Foreground (0), Sink (1)
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

    Foreground = None
    Sink = None
    value__ = None


class InputScope(object):
    """
    Represents information related to the scope of data provided by an input method.
    
    InputScope()
    """
    Names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the input scope name.

Get: Names(self: InputScope) -> IList

"""

    PhraseList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of phrases to be used as suggested input patterns by input processors.

Get: PhraseList(self: InputScope) -> IList

"""

    RegularExpression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a regular expression to be used as a suggested text input pattern by input processors.

Get: RegularExpression(self: InputScope) -> str

Set: RegularExpression(self: InputScope) = value
"""

    SrgsMarkup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a string that specifies any Speech Recognition Grammar Specification (SRGS) markup to be used as a suggested input pattern by input processors.

Get: SrgsMarkup(self: InputScope) -> str

Set: SrgsMarkup(self: InputScope) = value
"""



class InputScopeConverter(TypeConverter):
    """
    Converts a System.Windows.Input.InputScope to and from other types.
    
    InputScopeConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: InputScopeConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether an System.Windows.Input.InputScope object can be converted from an object of a specified type.
        
            context: An object that describes any type descriptor context.  This object must implement the System.ComponentModel.ITypeDescriptorContext interface.  This parameter may be null.
            sourceType: A System.Type to check for conversion compatibility.
            Returns: true if sourceType is type System.String; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: InputScopeConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether an System.Windows.Input.InputScope object can be converted to an object of a specified type.
        
            context: An object that describes any type descriptor context.  This object must implement the System.ComponentModel.ITypeDescriptorContext interface.  This parameter may be null.
            destinationType: A System.Type to check for conversion compatibility.
            Returns: true if destinationType is type System.String; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: InputScopeConverter, context: ITypeDescriptorContext, culture: CultureInfo, source: object) -> object
        
            Converts a source object (string) into an System.Windows.Input.InputScope object.
        
            context: An object that describes any type descriptor context.  This object must implement the System.ComponentModel.ITypeDescriptorContext interface.  This parameter may be null.
            culture: A System.Globalization.CultureInfo object containing any cultural context for the conversion.  This parameter may be null.
            source: A source object to convert from.  This object must be a string.
            Returns: An System.Windows.Input.InputScope object converted from the specified source object.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: InputScopeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts an System.Windows.Input.InputScope object into a specified object type (string).
        
            context: An object that describes any type descriptor context.  This object must implement the System.ComponentModel.ITypeDescriptorContext interface.  This parameter may be null.
            culture: A System.Globalization.CultureInfo object containing any cultural context for the conversion.  This parameter may be null.
            value: An object to convert from.  This object must be of type System.Windows.Input.InputScope.
            destinationType: A destination type to convert type.  This type must be string.
            Returns: A new object of the specified type (string) converted from the given System.Windows.Input.InputScope object.
        """
        pass


class InputScopeName(object, IAddChild):
    """
    Defines a name for text input patterns.
    
    InputScopeName()
    InputScopeName(nameValue: InputScopeNameValue)
    """
    def AddChild(self, value):
        """
        AddChild(self: InputScopeName, value: object)
            Adds a child object to this System.Windows.Input.InputScopeName.
        
            value: The object to be added as the child of this System.Windows.Input.InputScopeName.
        """
        pass

    def AddText(self, name):
        """
        AddText(self: InputScopeName, name: str)
            Adds a text string as a child of this System.Windows.Input.InputScopeName.
        
            name: The text added to the System.Windows.Input.InputScopeName.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, nameValue=None):
        """
        __new__(cls: type)
        __new__(cls: type, nameValue: InputScopeNameValue)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    NameValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the input scope name value which modifies how input from alternative input methods is interpreted.

Get: NameValue(self: InputScopeName) -> InputScopeNameValue

Set: NameValue(self: InputScopeName) = value
"""



class InputScopeNameConverter(TypeConverter):
    """
    Converts instances of System.Windows.Input.InputScopeName to and from other data types.
    
    InputScopeNameConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: InputScopeNameConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Indicates whether an object can be converted from a given type to an instance of a System.Windows.Input.InputScopeName.
        
            context: Describes the context information of a type.
            sourceType: The source System.Type that is being queried for conversion support.
            Returns: true if sourceType is type System.String; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: InputScopeNameConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether instances of System.Windows.Input.InputScopeName can be converted to the specified type.
        
            context: Describes the context information of a type.
            destinationType: The desired type this System.Windows.Input.InputScopeName is being evaluated to be converted to.
            Returns: true if destinationType is type System.String; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: InputScopeNameConverter, context: ITypeDescriptorContext, culture: CultureInfo, source: object) -> object
        
            Converts the specified object to a System.Windows.Input.InputScopeName.
        
            context: Describes the context information of a type.
            culture: Describes the System.Globalization.CultureInfo of the type being converted.
            source: The object being converted.
            Returns: The System.Windows.Input.InputScopeName created from converting source.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: InputScopeNameConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the specified System.Windows.Input.InputScopeName to the specified type.
        
            context: Describes the context information of a type.
            culture: Describes the System.Globalization.CultureInfo of the type being converted.
            value: The System.Windows.Input.InputScopeName to convert.
            destinationType: The type to convert the System.Windows.Input.InputScopeName to.
            Returns: The object created from converting this System.Windows.Input.InputScopeName.
        """
        pass


class InputScopeNameValue(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the input scope name which modifies how input from alternative input methods is interpreted.
    
    enum InputScopeNameValue, values: AddressCity (17), AddressCountryName (18), AddressCountryShortName (19), AddressStateOrProvince (16), AddressStreet (15), AlphanumericFullWidth (41), AlphanumericHalfWidth (40), Bopomofo (43), CurrencyAmount (21), CurrencyAmountAndSymbol (20), CurrencyChinese (42), Date (22), DateDay (24), DateDayName (27), DateMonth (23), DateMonthName (26), DateYear (25), Default (0), Digits (28), EmailSmtpAddress (5), EmailUserName (4), FileName (3), FullFilePath (2), Hanja (47), Hiragana (44), KatakanaFullWidth (46), KatakanaHalfWidth (45), LogOnName (6), Number (29), NumberFullWidth (39), OneChar (30), Password (31), PersonalFullName (7), PersonalGivenName (9), PersonalMiddleName (10), PersonalNamePrefix (8), PersonalNameSuffix (12), PersonalSurname (11), PhraseList (-1), PostalAddress (13), PostalCode (14), RegularExpression (-2), Srgs (-3), TelephoneAreaCode (34), TelephoneCountryCode (33), TelephoneLocalNumber (35), TelephoneNumber (32), Time (36), TimeHour (37), TimeMinorSec (38), Url (1), Xml (-4)
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

    AddressCity = None
    AddressCountryName = None
    AddressCountryShortName = None
    AddressStateOrProvince = None
    AddressStreet = None
    AlphanumericFullWidth = None
    AlphanumericHalfWidth = None
    Bopomofo = None
    CurrencyAmount = None
    CurrencyAmountAndSymbol = None
    CurrencyChinese = None
    Date = None
    DateDay = None
    DateDayName = None
    DateMonth = None
    DateMonthName = None
    DateYear = None
    Default = None
    Digits = None
    EmailSmtpAddress = None
    EmailUserName = None
    FileName = None
    FullFilePath = None
    Hanja = None
    Hiragana = None
    KatakanaFullWidth = None
    KatakanaHalfWidth = None
    LogOnName = None
    Number = None
    NumberFullWidth = None
    OneChar = None
    Password = None
    PersonalFullName = None
    PersonalGivenName = None
    PersonalMiddleName = None
    PersonalNamePrefix = None
    PersonalNameSuffix = None
    PersonalSurname = None
    PhraseList = None
    PostalAddress = None
    PostalCode = None
    RegularExpression = None
    Srgs = None
    TelephoneAreaCode = None
    TelephoneCountryCode = None
    TelephoneLocalNumber = None
    TelephoneNumber = None
    Time = None
    TimeHour = None
    TimeMinorSec = None
    Url = None
    value__ = None
    Xml = None


class InputScopePhrase(object, IAddChild):
    """
    Represents a suggested input text pattern.
    
    InputScopePhrase()
    InputScopePhrase(name: str)
    """
    def AddChild(self, value):
        """
        AddChild(self: InputScopePhrase, value: object)
            This type or member supports the Windows Presentation Foundation (WPF) infrastructure and is not intended to be used directly from your code.
        
            value: An object to add as a child.
        """
        pass

    def AddText(self, name):
        """
        AddText(self: InputScopePhrase, name: str)
            This type or member supports the Windows Presentation Foundation (WPF) infrastructure and is not intended to be used directly from your code.
        
            name: A string to add.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a descriptive name associated with the text input pattern for this System.Windows.Input.InputScopePhrase.

Get: Name(self: InputScopePhrase) -> str

Set: Name(self: InputScopePhrase) = value
"""



class InputType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the possible types of input being reported.
    
    enum InputType, values: Command (5), Hid (3), Keyboard (0), Mouse (1), Stylus (2), Text (4)
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

    Command = None
    Hid = None
    Keyboard = None
    Mouse = None
    Stylus = None
    Text = None
    value__ = None


class Key(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the possible key values on a keyboard.
    
    enum Key, values: A (44), AbntC1 (147), AbntC2 (148), Add (85), Apps (72), Attn (163), B (45), Back (2), BrowserBack (122), BrowserFavorites (127), BrowserForward (123), BrowserHome (128), BrowserRefresh (124), BrowserSearch (126), BrowserStop (125), C (46), Cancel (1), Capital (8), CapsLock (8), Clear (5), CrSel (164), D (47), D0 (34), D1 (35), D2 (36), D3 (37), D4 (38), D5 (39), D6 (40), D7 (41), D8 (42), D9 (43), DbeAlphanumeric (157), DbeCodeInput (167), DbeDbcsChar (161), DbeDetermineString (169), DbeEnterDialogConversionMode (170), DbeEnterImeConfigureMode (165), DbeEnterWordRegisterMode (164), DbeFlushString (166), DbeHiragana (159), DbeKatakana (158), DbeNoCodeInput (168), DbeNoRoman (163), DbeRoman (162), DbeSbcsChar (160), DeadCharProcessed (172), Decimal (88), Delete (32), Divide (89), Down (26), E (48), End (21), Enter (6), EraseEof (166), Escape (13), Execute (29), ExSel (165), F (49), F1 (90), F10 (99), F11 (100), F12 (101), F13 (102), F14 (103), F15 (104), F16 (105), F17 (106), F18 (107), F19 (108), F2 (91), F20 (109), F21 (110), F22 (111), F23 (112), F24 (113), F3 (92), F4 (93), F5 (94), F6 (95), F7 (96), F8 (97), F9 (98), FinalMode (11), G (50), H (51), HangulMode (9), HanjaMode (12), Help (33), Home (22), I (52), ImeAccept (16), ImeConvert (14), ImeModeChange (17), ImeNonConvert (15), ImeProcessed (155), Insert (31), J (53), JunjaMode (10), K (54), KanaMode (9), KanjiMode (12), L (55), LaunchApplication1 (138), LaunchApplication2 (139), LaunchMail (136), Left (23), LeftAlt (120), LeftCtrl (118), LeftShift (116), LineFeed (4), LWin (70), M (56), MediaNextTrack (132), MediaPlayPause (135), MediaPreviousTrack (133), MediaStop (134), Multiply (84), N (57), Next (20), NoName (169), None (0), NumLock (114), NumPad0 (74), NumPad1 (75), NumPad2 (76), NumPad3 (77), NumPad4 (78), NumPad5 (79), NumPad6 (80), NumPad7 (81), NumPad8 (82), NumPad9 (83), O (58), Oem1 (140), Oem102 (154), Oem2 (145), Oem3 (146), Oem4 (149), Oem5 (150), Oem6 (151), Oem7 (152), Oem8 (153), OemAttn (157), OemAuto (160), OemBackslash (154), OemBackTab (162), OemClear (171), OemCloseBrackets (151), OemComma (142), OemCopy (159), OemEnlw (161), OemFinish (158), OemMinus (143), OemOpenBrackets (149), OemPeriod (144), OemPipe (150), OemPlus (141), OemQuestion (145), OemQuotes (152), OemSemicolon (140), OemTilde (146), P (59), Pa1 (170), PageDown (20), PageUp (19), Pause (7), Play (167), Print (28), PrintScreen (30), Prior (19), Q (60), R (61), Return (6), Right (25), RightAlt (121), RightCtrl (119), RightShift (117), RWin (71), S (62), Scroll (115), Select (27), SelectMedia (137), Separator (86), Sleep (73), Snapshot (30), Space (18), Subtract (87), System (156), T (63), Tab (3), U (64), Up (24), V (65), VolumeDown (130), VolumeMute (129), VolumeUp (131), W (66), X (67), Y (68), Z (69), Zoom (168)
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

    A = None
    AbntC1 = None
    AbntC2 = None
    Add = None
    Apps = None
    Attn = None
    B = None
    Back = None
    BrowserBack = None
    BrowserFavorites = None
    BrowserForward = None
    BrowserHome = None
    BrowserRefresh = None
    BrowserSearch = None
    BrowserStop = None
    C = None
    Cancel = None
    Capital = None
    CapsLock = None
    Clear = None
    CrSel = None
    D = None
    D0 = None
    D1 = None
    D2 = None
    D3 = None
    D4 = None
    D5 = None
    D6 = None
    D7 = None
    D8 = None
    D9 = None
    DbeAlphanumeric = None
    DbeCodeInput = None
    DbeDbcsChar = None
    DbeDetermineString = None
    DbeEnterDialogConversionMode = None
    DbeEnterImeConfigureMode = None
    DbeEnterWordRegisterMode = None
    DbeFlushString = None
    DbeHiragana = None
    DbeKatakana = None
    DbeNoCodeInput = None
    DbeNoRoman = None
    DbeRoman = None
    DbeSbcsChar = None
    DeadCharProcessed = None
    Decimal = None
    Delete = None
    Divide = None
    Down = None
    E = None
    End = None
    Enter = None
    EraseEof = None
    Escape = None
    Execute = None
    ExSel = None
    F = None
    F1 = None
    F10 = None
    F11 = None
    F12 = None
    F13 = None
    F14 = None
    F15 = None
    F16 = None
    F17 = None
    F18 = None
    F19 = None
    F2 = None
    F20 = None
    F21 = None
    F22 = None
    F23 = None
    F24 = None
    F3 = None
    F4 = None
    F5 = None
    F6 = None
    F7 = None
    F8 = None
    F9 = None
    FinalMode = None
    G = None
    H = None
    HangulMode = None
    HanjaMode = None
    Help = None
    Home = None
    I = None
    ImeAccept = None
    ImeConvert = None
    ImeModeChange = None
    ImeNonConvert = None
    ImeProcessed = None
    Insert = None
    J = None
    JunjaMode = None
    K = None
    KanaMode = None
    KanjiMode = None
    L = None
    LaunchApplication1 = None
    LaunchApplication2 = None
    LaunchMail = None
    Left = None
    LeftAlt = None
    LeftCtrl = None
    LeftShift = None
    LineFeed = None
    LWin = None
    M = None
    MediaNextTrack = None
    MediaPlayPause = None
    MediaPreviousTrack = None
    MediaStop = None
    Multiply = None
    N = None
    Next = None
    NoName = None
    None = None
    NumLock = None
    NumPad0 = None
    NumPad1 = None
    NumPad2 = None
    NumPad3 = None
    NumPad4 = None
    NumPad5 = None
    NumPad6 = None
    NumPad7 = None
    NumPad8 = None
    NumPad9 = None
    O = None
    Oem1 = None
    Oem102 = None
    Oem2 = None
    Oem3 = None
    Oem4 = None
    Oem5 = None
    Oem6 = None
    Oem7 = None
    Oem8 = None
    OemAttn = None
    OemAuto = None
    OemBackslash = None
    OemBackTab = None
    OemClear = None
    OemCloseBrackets = None
    OemComma = None
    OemCopy = None
    OemEnlw = None
    OemFinish = None
    OemMinus = None
    OemOpenBrackets = None
    OemPeriod = None
    OemPipe = None
    OemPlus = None
    OemQuestion = None
    OemQuotes = None
    OemSemicolon = None
    OemTilde = None
    P = None
    Pa1 = None
    PageDown = None
    PageUp = None
    Pause = None
    Play = None
    Print = None
    PrintScreen = None
    Prior = None
    Q = None
    R = None
    Return = None
    Right = None
    RightAlt = None
    RightCtrl = None
    RightShift = None
    RWin = None
    S = None
    Scroll = None
    Select = None
    SelectMedia = None
    Separator = None
    Sleep = None
    Snapshot = None
    Space = None
    Subtract = None
    System = None
    T = None
    Tab = None
    U = None
    Up = None
    V = None
    value__ = None
    VolumeDown = None
    VolumeMute = None
    VolumeUp = None
    W = None
    X = None
    Y = None
    Z = None
    Zoom = None


class KeyBinding(InputBinding, ISealable, ICommandSource):
    """
    Binds a System.Windows.Input.KeyGesture to a System.Windows.Input.RoutedCommand (or another  System.Windows.Input.ICommand implementation).
    
    KeyBinding()
    KeyBinding(command: ICommand, gesture: KeyGesture)
    KeyBinding(command: ICommand, key: Key, modifiers: ModifierKeys)
    """
    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: InputBinding, sourceFreezable: Freezable)
            Copies the base (non-animated) values of the properties of the specified object.
        
            sourceFreezable: The object to clone.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: InputBinding, sourceFreezable: Freezable)
            Copies the current values of the properties of the specified object.
        
            sourceFreezable: The object to clone.
        """
        pass

    def CreateInstance(self, *args): #cannot find CLR method
        """
        CreateInstance(self: Freezable) -> Freezable
        
            Initializes a new instance of the System.Windows.Freezable class.
            Returns: The new instance.
        """
        pass

    def CreateInstanceCore(self, *args): #cannot find CLR method
        """
        CreateInstanceCore(self: KeyBinding) -> Freezable
        
            Creates an instance of a System.Windows.Input.KeyBinding.
            Returns: The new object.
        """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: Freezable, isChecking: bool) -> bool
        
            Makes the System.Windows.Freezable object unmodifiable or tests whether it can be made unmodifiable.
        
            isChecking: true to return an indication of whether the object can be frozen (without actually freezing it); false to actually freeze the object.
            Returns: If isChecking is true, this method returns true if the System.Windows.Freezable can be made unmodifiable, or false if it cannot be made unmodifiable. If isChecking is false, this method returns true if the 
             if the specified System.Windows.Freezable is now unmodifiable, or false if it cannot be made unmodifiable.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: InputBinding, sourceFreezable: Freezable)
            Makes the instance a frozen clone of the specified System.Windows.Freezable by using base (non-animated) property values.
        
            sourceFreezable: The object to clone.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: InputBinding, sourceFreezable: Freezable)
            Makes the current instance a frozen clone of the specified System.Windows.Freezable. If the object has animated dependency properties, their current animated values are copied.
        
            sourceFreezable: The object to clone.
        """
        pass

    def OnChanged(self, *args): #cannot find CLR method
        """
        OnChanged(self: Freezable)
            Called when the current System.Windows.Freezable object is modified.
        """
        pass

    def OnFreezablePropertyChanged(self, *args): #cannot find CLR method
        """
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject, property: DependencyProperty)
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not intended to be used directly from your code.
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a System.Windows.DependencyObjectType data member that has just been set.
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventArgs) to also invoke any 
             System.Windows.Freezable.Changed handlers in response to a changing dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of System.Windows.Freezable must call this method at the beginning of any API that reads data members that are 
             not dependency properties.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for the provided dependency property.
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable should call 
             this method at the end of any API that modifies class members that are not stored as dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a valid threading context. System.Windows.Freezable inheritors should call this method at the beginning of any 
             API that writes to data members that are not dependency properties.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, command=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, command: ICommand, gesture: KeyGesture)
        __new__(cls: type, command: ICommand, key: Key, modifiers: ModifierKeys)
        """
        pass

    Gesture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the gesture associated with this System.Windows.Input.KeyBinding.

Get: Gesture(self: KeyBinding) -> InputGesture

Set: Gesture(self: KeyBinding) = value
"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Input.Key of the System.Windows.Input.KeyGesture associated with this System.Windows.Input.KeyBinding.

Get: Key(self: KeyBinding) -> Key

Set: Key(self: KeyBinding) = value
"""

    Modifiers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Input.ModifierKeys of the System.Windows.Input.KeyGesture associated with this System.Windows.Input.KeyBinding.

Get: Modifiers(self: KeyBinding) -> ModifierKeys

Set: Modifiers(self: KeyBinding) = value
"""


    KeyProperty = None
    ModifiersProperty = None


class Keyboard(object):
    """ Represents the keyboard device. """
    @staticmethod
    def AddGotKeyboardFocusHandler(element, handler):
        """
        AddGotKeyboardFocusHandler(element: DependencyObject, handler: KeyboardFocusChangedEventHandler)
            Adds a handler for the System.Windows.Input.Keyboard.GotKeyboardFocus�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to be added.
        """
        pass

    @staticmethod
    def AddKeyboardInputProviderAcquireFocusHandler(element, handler):
        """
        AddKeyboardInputProviderAcquireFocusHandler(element: DependencyObject, handler: KeyboardInputProviderAcquireFocusEventHandler)
            Adds a handler for the System.Windows.Input.Keyboard.KeyboardInputProviderAcquireFocus�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to be added.
        """
        pass

    @staticmethod
    def AddKeyDownHandler(element, handler):
        """
        AddKeyDownHandler(element: DependencyObject, handler: KeyEventHandler)
            Adds a handler for the System.Windows.Input.Keyboard.KeyDown�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to be added.
        """
        pass

    @staticmethod
    def AddKeyUpHandler(element, handler):
        """
        AddKeyUpHandler(element: DependencyObject, handler: KeyEventHandler)
            Adds a handler for the System.Windows.Input.Keyboard.KeyUp�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to be added.
        """
        pass

    @staticmethod
    def AddLostKeyboardFocusHandler(element, handler):
        """
        AddLostKeyboardFocusHandler(element: DependencyObject, handler: KeyboardFocusChangedEventHandler)
            Adds a handler for the System.Windows.Input.Keyboard.LostKeyboardFocus�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to be added.
        """
        pass

    @staticmethod
    def AddPreviewGotKeyboardFocusHandler(element, handler):
        """
        AddPreviewGotKeyboardFocusHandler(element: DependencyObject, handler: KeyboardFocusChangedEventHandler)
            Adds a handler for the System.Windows.Input.Keyboard.PreviewGotKeyboardFocus�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to be added.
        """
        pass

    @staticmethod
    def AddPreviewKeyboardInputProviderAcquireFocusHandler(element, handler):
        """
        AddPreviewKeyboardInputProviderAcquireFocusHandler(element: DependencyObject, handler: KeyboardInputProviderAcquireFocusEventHandler)
            Adds a handler for the System.Windows.Input.Keyboard.PreviewKeyboardInputProviderAcquireFocus�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to be added.
        """
        pass

    @staticmethod
    def AddPreviewKeyDownHandler(element, handler):
        """
        AddPreviewKeyDownHandler(element: DependencyObject, handler: KeyEventHandler)
            Adds a handler for the System.Windows.Input.Keyboard.PreviewKeyDown�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to be added.
        """
        pass

    @staticmethod
    def AddPreviewKeyUpHandler(element, handler):
        """
        AddPreviewKeyUpHandler(element: DependencyObject, handler: KeyEventHandler)
            Adds a handler for the System.Windows.Input.Keyboard.PreviewKeyUp�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to be added.
        """
        pass

    @staticmethod
    def AddPreviewLostKeyboardFocusHandler(element, handler):
        """
        AddPreviewLostKeyboardFocusHandler(element: DependencyObject, handler: KeyboardFocusChangedEventHandler)
            Adds a handler for the System.Windows.Input.Keyboard.PreviewLostKeyboardFocus�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to be added.
        """
        pass

    @staticmethod
    def ClearFocus():
        """
        ClearFocus()
            Clears focus.
        """
        pass

    @staticmethod
    def Focus(element):
        """
        Focus(element: IInputElement) -> IInputElement
        
            Sets keyboard focus on the specified element.
        
            element: The element on which to set keyboard focus.
            Returns: The element with keyboard focus.
        """
        pass

    @staticmethod
    def GetKeyStates(key):
        """
        GetKeyStates(key: Key) -> KeyStates
        
            Gets the set of key states for the specified key.
        
            key: The specified key.
            Returns: A bitwise combination of the System.Windows.Input.KeyStates values.
        """
        pass

    @staticmethod
    def IsKeyDown(key):
        """
        IsKeyDown(key: Key) -> bool
        
            Determines whether the specified key is pressed.
        
            key: The specified key.
            Returns: true if key is in the down state; otherwise, false.
        """
        pass

    @staticmethod
    def IsKeyToggled(key):
        """
        IsKeyToggled(key: Key) -> bool
        
            Determines whether the specified key is toggled.
        
            key: The specified key.
            Returns: true if key is in the toggled state; otherwise, false.
        """
        pass

    @staticmethod
    def IsKeyUp(key):
        """
        IsKeyUp(key: Key) -> bool
        
            Determines whether the specified key is released.
        
            key: The key to check.
            Returns: true if key is in the up state; otherwise, false.
        """
        pass

    @staticmethod
    def RemoveGotKeyboardFocusHandler(element, handler):
        """
        RemoveGotKeyboardFocusHandler(element: DependencyObject, handler: KeyboardFocusChangedEventHandler)
            Removes a handler for the System.Windows.Input.Keyboard.GotKeyboardFocus�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to be removed.
        """
        pass

    @staticmethod
    def RemoveKeyboardInputProviderAcquireFocusHandler(element, handler):
        """
        RemoveKeyboardInputProviderAcquireFocusHandler(element: DependencyObject, handler: KeyboardInputProviderAcquireFocusEventHandler)
            Removes a handler for the System.Windows.Input.Keyboard.KeyboardInputProviderAcquireFocus�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to be removed.
        """
        pass

    @staticmethod
    def RemoveKeyDownHandler(element, handler):
        """
        RemoveKeyDownHandler(element: DependencyObject, handler: KeyEventHandler)
            Removes a handler for the System.Windows.Input.Keyboard.KeyDown�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to be removed.
        """
        pass

    @staticmethod
    def RemoveKeyUpHandler(element, handler):
        """
        RemoveKeyUpHandler(element: DependencyObject, handler: KeyEventHandler)
            Removes a handler for the System.Windows.Input.Keyboard.KeyUp�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to be removed.
        """
        pass

    @staticmethod
    def RemoveLostKeyboardFocusHandler(element, handler):
        """
        RemoveLostKeyboardFocusHandler(element: DependencyObject, handler: KeyboardFocusChangedEventHandler)
            Removes a handler for the System.Windows.Input.Keyboard.LostKeyboardFocus�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to be removed.
        """
        pass

    @staticmethod
    def RemovePreviewGotKeyboardFocusHandler(element, handler):
        """
        RemovePreviewGotKeyboardFocusHandler(element: DependencyObject, handler: KeyboardFocusChangedEventHandler)
            Removes a handler for the System.Windows.Input.Keyboard.PreviewGotKeyboardFocus�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to be removed.
        """
        pass

    @staticmethod
    def RemovePreviewKeyboardInputProviderAcquireFocusHandler(element, handler):
        """
        RemovePreviewKeyboardInputProviderAcquireFocusHandler(element: DependencyObject, handler: KeyboardInputProviderAcquireFocusEventHandler)
            Removes a handler for the System.Windows.Input.Keyboard.PreviewKeyboardInputProviderAcquireFocus�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to be removed.
        """
        pass

    @staticmethod
    def RemovePreviewKeyDownHandler(element, handler):
        """
        RemovePreviewKeyDownHandler(element: DependencyObject, handler: KeyEventHandler)
            Removes a handler for the System.Windows.Input.Keyboard.PreviewKeyDown�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to be removed.
        """
        pass

    @staticmethod
    def RemovePreviewKeyUpHandler(element, handler):
        """
        RemovePreviewKeyUpHandler(element: DependencyObject, handler: KeyEventHandler)
            Removes a handler for the System.Windows.Input.Keyboard.PreviewKeyUp�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to be removed.
        """
        pass

    @staticmethod
    def RemovePreviewLostKeyboardFocusHandler(element, handler):
        """
        RemovePreviewLostKeyboardFocusHandler(element: DependencyObject, handler: KeyboardFocusChangedEventHandler)
            Removes a handler for the System.Windows.Input.Keyboard.PreviewLostKeyboardFocus�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to be removed.
        """
        pass

    DefaultRestoreFocusMode = None
    FocusedElement = None
    GotKeyboardFocusEvent = None
    KeyboardInputProviderAcquireFocusEvent = None
    KeyDownEvent = None
    KeyUpEvent = None
    LostKeyboardFocusEvent = None
    Modifiers = None
    PreviewGotKeyboardFocusEvent = None
    PreviewKeyboardInputProviderAcquireFocusEvent = None
    PreviewKeyDownEvent = None
    PreviewKeyUpEvent = None
    PreviewLostKeyboardFocusEvent = None
    PrimaryDevice = None
    __all__ = [
        'AddGotKeyboardFocusHandler',
        'AddKeyboardInputProviderAcquireFocusHandler',
        'AddKeyDownHandler',
        'AddKeyUpHandler',
        'AddLostKeyboardFocusHandler',
        'AddPreviewGotKeyboardFocusHandler',
        'AddPreviewKeyboardInputProviderAcquireFocusHandler',
        'AddPreviewKeyDownHandler',
        'AddPreviewKeyUpHandler',
        'AddPreviewLostKeyboardFocusHandler',
        'ClearFocus',
        'Focus',
        'GetKeyStates',
        'GotKeyboardFocusEvent',
        'IsKeyDown',
        'IsKeyToggled',
        'IsKeyUp',
        'KeyboardInputProviderAcquireFocusEvent',
        'KeyDownEvent',
        'KeyUpEvent',
        'LostKeyboardFocusEvent',
        'PreviewGotKeyboardFocusEvent',
        'PreviewKeyboardInputProviderAcquireFocusEvent',
        'PreviewKeyDownEvent',
        'PreviewKeyUpEvent',
        'PreviewLostKeyboardFocusEvent',
        'RemoveGotKeyboardFocusHandler',
        'RemoveKeyboardInputProviderAcquireFocusHandler',
        'RemoveKeyDownHandler',
        'RemoveKeyUpHandler',
        'RemoveLostKeyboardFocusHandler',
        'RemovePreviewGotKeyboardFocusHandler',
        'RemovePreviewKeyboardInputProviderAcquireFocusHandler',
        'RemovePreviewKeyDownHandler',
        'RemovePreviewKeyUpHandler',
        'RemovePreviewLostKeyboardFocusHandler',
    ]


class KeyboardDevice(InputDevice):
    """ Abstract class that represents a keyboard device. """
    def ClearFocus(self):
        """
        ClearFocus(self: KeyboardDevice)
            Clears focus.
        """
        pass

    def Focus(self, element):
        """
        Focus(self: KeyboardDevice, element: IInputElement) -> IInputElement
        
            Sets keyboard focus on the specified System.Windows.IInputElement.
        
            element: The element to move focus to.
            Returns: The element that has keyboard focus.
        """
        pass

    def GetKeyStates(self, key):
        """
        GetKeyStates(self: KeyboardDevice, key: Key) -> KeyStates
        
            Gets the set of key states for the specified System.Windows.Input.Key.
        
            key: The key to check.
            Returns: The set of key states for the specified key.
        """
        pass

    def GetKeyStatesFromSystem(self, *args): #cannot find CLR method
        """
        GetKeyStatesFromSystem(self: KeyboardDevice, key: Key) -> KeyStates
        
            When overridden in a derived class, obtains the System.Windows.Input.KeyStates for the specified System.Windows.Input.Key.
        
            key: The key to check.
            Returns: The set of key states for the specified key.
        """
        pass

    def IsKeyDown(self, key):
        """
        IsKeyDown(self: KeyboardDevice, key: Key) -> bool
        
            Determines whether the specified System.Windows.Input.Key is in the down state.
        
            key: The key to check.
            Returns: true if key is in the down state; otherwise, false.
        """
        pass

    def IsKeyToggled(self, key):
        """
        IsKeyToggled(self: KeyboardDevice, key: Key) -> bool
        
            Determines whether the specified System.Windows.Input.Key is in the toggled state.
        
            key: The key to check.
            Returns: true if key is in the toggled state; otherwise, false.
        """
        pass

    def IsKeyUp(self, key):
        """
        IsKeyUp(self: KeyboardDevice, key: Key) -> bool
        
            Determines whether the specified System.Windows.Input.Key is in the up state.
        
            key: The key to check.
            Returns: true if key is in the up state; otherwise, false.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, inputManager: InputManager) """
        pass

    ActiveSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.PresentationSource that is reporting input for this device.

Get: ActiveSource(self: KeyboardDevice) -> PresentationSource

"""

    DefaultRestoreFocusMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the behavior of Windows Presentation Foundation (WPF) when restoring focus.

Get: DefaultRestoreFocusMode(self: KeyboardDevice) -> RestoreFocusMode

Set: DefaultRestoreFocusMode(self: KeyboardDevice) = value
"""

    FocusedElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the element that has keyboard focus.

Get: FocusedElement(self: KeyboardDevice) -> IInputElement

"""

    Modifiers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the set of System.Windows.Input.ModifierKeys which are currently pressed.

Get: Modifiers(self: KeyboardDevice) -> ModifierKeys

"""

    Target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the specified System.Windows.IInputElement that input from this device is sent to.

Get: Target(self: KeyboardDevice) -> IInputElement

"""



class KeyboardEventArgs(InputEventArgs):
    """
    Provides data for keyboard-related events.
    
    KeyboardEventArgs(keyboard: KeyboardDevice, timestamp: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, keyboard, timestamp):
        """ __new__(cls: type, keyboard: KeyboardDevice, timestamp: int) """
        pass

    KeyboardDevice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the keyboard device associated with the input event.

Get: KeyboardDevice(self: KeyboardEventArgs) -> KeyboardDevice

"""



class KeyboardEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle keyboard-related routed events.
    
    KeyboardEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: KeyboardEventHandler, sender: object, e: KeyboardEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null, if the method represented by the current delegate does not require arguments.
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: KeyboardEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: KeyboardEventHandler, sender: object, e: KeyboardEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation list.
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


class KeyboardFocusChangedEventArgs(KeyboardEventArgs):
    """
    Provides data for System.Windows.UIElement.LostKeyboardFocus and System.Windows.UIElement.GotKeyboardFocus�routed events, as well as related attached and Preview events.
    
    KeyboardFocusChangedEventArgs(keyboard: KeyboardDevice, timestamp: int, oldFocus: IInputElement, newFocus: IInputElement)
    """
    @staticmethod # known case of __new__
    def __new__(self, keyboard, timestamp, oldFocus, newFocus):
        """ __new__(cls: type, keyboard: KeyboardDevice, timestamp: int, oldFocus: IInputElement, newFocus: IInputElement) """
        pass

    NewFocus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the element that focus has moved to.

Get: NewFocus(self: KeyboardFocusChangedEventArgs) -> IInputElement

"""

    OldFocus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the element that previously had focus.

Get: OldFocus(self: KeyboardFocusChangedEventArgs) -> IInputElement

"""



class KeyboardFocusChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Windows.UIElement.LostKeyboardFocus and System.Windows.UIElement.GotKeyboardFocus�routed events, as well as related attached and Preview events.
    
    KeyboardFocusChangedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: KeyboardFocusChangedEventHandler, sender: object, e: KeyboardFocusChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null, if the method represented by the current delegate does not require arguments.
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: KeyboardFocusChangedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: KeyboardFocusChangedEventHandler, sender: object, e: KeyboardFocusChangedEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation list.
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


class KeyboardInputProviderAcquireFocusEventArgs(KeyboardEventArgs):
    """
    Provides data for the System.Windows.Input.Keyboard.KeyboardInputProviderAcquireFocus event.
    
    KeyboardInputProviderAcquireFocusEventArgs(keyboard: KeyboardDevice, timestamp: int, focusAcquired: bool)
    """
    @staticmethod # known case of __new__
    def __new__(self, keyboard, timestamp, focusAcquired):
        """ __new__(cls: type, keyboard: KeyboardDevice, timestamp: int, focusAcquired: bool) """
        pass

    FocusAcquired = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether interoperation focus was acquired.

Get: FocusAcquired(self: KeyboardInputProviderAcquireFocusEventArgs) -> bool

"""



class KeyboardInputProviderAcquireFocusEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Windows.Input.Keyboard.KeyboardInputProviderAcquireFocus event
    
    KeyboardInputProviderAcquireFocusEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: KeyboardInputProviderAcquireFocusEventHandler, sender: object, e: KeyboardInputProviderAcquireFocusEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null, if the method represented by the current delegate does not require arguments.
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: KeyboardInputProviderAcquireFocusEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: KeyboardInputProviderAcquireFocusEventHandler, sender: object, e: KeyboardInputProviderAcquireFocusEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation list.
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


class KeyboardNavigation(object):
    """ Provides logical and directional navigation between focusable objects. """
    @staticmethod
    def GetAcceptsReturn(element):
        """
        GetAcceptsReturn(element: DependencyObject) -> bool
        
            Gets the value of the System.Windows.Input.KeyboardNavigation.AcceptsReturn�attached property for the specified element.
        
            element: The element from which to read the attached property.
            Returns: The value of the System.Windows.Input.KeyboardNavigation.AcceptsReturn property.
        """
        pass

    @staticmethod
    def GetControlTabNavigation(element):
        """
        GetControlTabNavigation(element: DependencyObject) -> KeyboardNavigationMode
        
            Gets the value of the System.Windows.Input.KeyboardNavigation.ControlTabNavigation�attached property for the specified element.
        
            element: Element from which to get the attached property.
            Returns: The value of the System.Windows.Input.KeyboardNavigation.ControlTabNavigation property.
        """
        pass

    @staticmethod
    def GetDirectionalNavigation(element):
        """
        GetDirectionalNavigation(element: DependencyObject) -> KeyboardNavigationMode
        
            Gets the value of the System.Windows.Input.KeyboardNavigation.DirectionalNavigation�attached property for the specified element.
        
            element: Element from which to get the attached property.
            Returns: The value of the System.Windows.Input.KeyboardNavigation.DirectionalNavigation property.
        """
        pass

    @staticmethod
    def GetIsTabStop(element):
        """
        GetIsTabStop(element: DependencyObject) -> bool
        
            Gets the value of the System.Windows.Input.KeyboardNavigation.IsTabStop�attached property for the specified element.
        
            element: The element from which to read the attached property.
            Returns: The value of the System.Windows.Input.KeyboardNavigation.IsTabStop property.
        """
        pass

    @staticmethod
    def GetTabIndex(element):
        """
        GetTabIndex(element: DependencyObject) -> int
        
            Gets the value of the System.Windows.Input.KeyboardNavigation.TabIndex �attached property for the specified element.
        
            element: The element from which to read the attached property.
            Returns: The value of the System.Windows.Input.KeyboardNavigation.TabIndex property.
        """
        pass

    @staticmethod
    def GetTabNavigation(element):
        """
        GetTabNavigation(element: DependencyObject) -> KeyboardNavigationMode
        
            Gets the value of the System.Windows.Input.KeyboardNavigation.TabNavigation�attached property for the specified element.
        
            element: Element from which to get the attached property.
            Returns: The value of the System.Windows.Input.KeyboardNavigation.TabNavigation property.
        """
        pass

    @staticmethod
    def SetAcceptsReturn(element, enabled):
        """
        SetAcceptsReturn(element: DependencyObject, enabled: bool)
            Sets the value of the System.Windows.Input.KeyboardNavigation.AcceptsReturn �attached property for the specified element.
        
            element: The element to write the attached property to.
            enabled: The property value to set.
        """
        pass

    @staticmethod
    def SetControlTabNavigation(element, mode):
        """
        SetControlTabNavigation(element: DependencyObject, mode: KeyboardNavigationMode)
            Sets the value of the System.Windows.Input.KeyboardNavigation.ControlTabNavigation�attached property for the specified element.
        
            element: Element on which to set the attached property.
            mode: The property value to set
        """
        pass

    @staticmethod
    def SetDirectionalNavigation(element, mode):
        """
        SetDirectionalNavigation(element: DependencyObject, mode: KeyboardNavigationMode)
            Sets the value of the System.Windows.Input.KeyboardNavigation.DirectionalNavigation�attached property for the specified element.
        
            element: Element on which to set the attached property.
            mode: Property value to set.
        """
        pass

    @staticmethod
    def SetIsTabStop(element, isTabStop):
        """
        SetIsTabStop(element: DependencyObject, isTabStop: bool)
            Sets the value of the System.Windows.Input.KeyboardNavigation.IsTabStop�attached property for the specified element.
        
            element: The element to which to write the attached property.
            isTabStop: The property value to set.
        """
        pass

    @staticmethod
    def SetTabIndex(element, index):
        """
        SetTabIndex(element: DependencyObject, index: int)
            Set the value of the System.Windows.Input.KeyboardNavigation.TabIndex�attached property for the specified element.
        
            element: The element on which to set the attached property to.
            index: The property value to set.
        """
        pass

    @staticmethod
    def SetTabNavigation(element, mode):
        """
        SetTabNavigation(element: DependencyObject, mode: KeyboardNavigationMode)
            Sets the value of the System.Windows.Input.KeyboardNavigation.TabNavigation�attached property for the specified element.
        
            element: Element on which to set the attached property.
            mode: Property value to set.
        """
        pass

    AcceptsReturnProperty = None
    ControlTabNavigationProperty = None
    DirectionalNavigationProperty = None
    IsTabStopProperty = None
    TabIndexProperty = None
    TabNavigationProperty = None


class KeyboardNavigationMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the possible values for changes in focus when logical and directional navigation occurs.
    
    enum KeyboardNavigationMode, values: Contained (4), Continue (0), Cycle (2), Local (5), None (3), Once (1)
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

    Contained = None
    Continue = None
    Cycle = None
    Local = None
    None = None
    Once = None
    value__ = None


class KeyConverter(TypeConverter):
    """
    Converts a System.Windows.Input.Key object to and from other types.
    
    KeyConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: KeyConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether an object of the specified type can be converted to an instance of System.Windows.Input.Key, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            sourceType: The type being evaluated for conversion.
            Returns: true if sourceType is of type System.String; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: KeyConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether an instance of System.Windows.Input.Key can be converted to the specified type, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            destinationType: The type being evaluated for conversion.
            Returns: true if destinationType is of type System.String; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: KeyConverter, context: ITypeDescriptorContext, culture: CultureInfo, source: object) -> object
        
            Attempts to convert the specified object to a System.Windows.Input.Key, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            culture: Culture specific information.
            source: The object to convert.
            Returns: The converted object.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: KeyConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Attempts to convert a System.Windows.Input.Key to the specified type, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            culture: Culture specific information.
            value: The object to convert.
            destinationType: The type to convert the object to.
            Returns: The converted object.
        """
        pass


class KeyEventArgs(KeyboardEventArgs):
    """
    Provides data for the System.Windows.UIElement.KeyUp and System.Windows.UIElement.KeyDown�routed events, as well as related attached and Preview events.
    
    KeyEventArgs(keyboard: KeyboardDevice, inputSource: PresentationSource, timestamp: int, key: Key)
    """
    @staticmethod # known case of __new__
    def __new__(self, keyboard, inputSource, timestamp, key):
        """ __new__(cls: type, keyboard: KeyboardDevice, inputSource: PresentationSource, timestamp: int, key: Key) """
        pass

    DeadCharProcessedKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the key that is part of dead key composition to create a single combined character.

Get: DeadCharProcessedKey(self: KeyEventArgs) -> Key

"""

    ImeProcessedKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the keyboard key referenced by the event, if the key will be processed by an Input Method Editor (IME).

Get: ImeProcessedKey(self: KeyEventArgs) -> Key

"""

    InputSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the input source that provided this input.

Get: InputSource(self: KeyEventArgs) -> PresentationSource

"""

    IsDown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the key referenced by the event is in the down state.

Get: IsDown(self: KeyEventArgs) -> bool

"""

    IsRepeat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the keyboard key referenced by the event is a repeated key.

Get: IsRepeat(self: KeyEventArgs) -> bool

"""

    IsToggled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the key referenced by the event is in the toggled state.

Get: IsToggled(self: KeyEventArgs) -> bool

"""

    IsUp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the key referenced by the event is in the up state.

Get: IsUp(self: KeyEventArgs) -> bool

"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the keyboard key associated with the event.

Get: Key(self: KeyEventArgs) -> Key

"""

    KeyStates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the state of the keyboard key associated with this event.

Get: KeyStates(self: KeyEventArgs) -> KeyStates

"""

    SystemKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the keyboard key referenced by the event, if the key will be processed by the system.

Get: SystemKey(self: KeyEventArgs) -> Key

"""



class KeyEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Windows.UIElement.KeyUp and System.Windows.UIElement.KeyDown�routed events, as well as related attached and Preview events.
    
    KeyEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: KeyEventHandler, sender: object, e: KeyEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null, if the method represented by the current delegate does not require arguments.
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: KeyEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: KeyEventHandler, sender: object, e: KeyEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation list.
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


class KeyGesture(InputGesture):
    """
    Defines a keyboard combination that can be used to invoke a command.
    
    KeyGesture(key: Key)
    KeyGesture(key: Key, modifiers: ModifierKeys)
    KeyGesture(key: Key, modifiers: ModifierKeys, displayString: str)
    """
    def GetDisplayStringForCulture(self, culture):
        """
        GetDisplayStringForCulture(self: KeyGesture, culture: CultureInfo) -> str
        
            Returns a string that can be used to display the System.Windows.Input.KeyGesture.
        
            culture: The culture specific information.
            Returns: The string to display
        """
        pass

    def Matches(self, targetElement, inputEventArgs):
        """
        Matches(self: KeyGesture, targetElement: object, inputEventArgs: InputEventArgs) -> bool
        
            Determines whether this System.Windows.Input.KeyGesture matches the input associated with the specified System.Windows.Input.InputEventArgs object.
        
            targetElement: The target.
            inputEventArgs: The input event data to compare this gesture to.
            Returns: true if the event data matches this System.Windows.Input.KeyGesture; otherwise, false.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, key, modifiers=None, displayString=None):
        """
        __new__(cls: type, key: Key)
        __new__(cls: type, key: Key, modifiers: ModifierKeys)
        __new__(cls: type, key: Key, modifiers: ModifierKeys, displayString: str)
        """
        pass

    DisplayString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a string representation of this System.Windows.Input.KeyGesture.

Get: DisplayString(self: KeyGesture) -> str

"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the key associated with this System.Windows.Input.KeyGesture.

Get: Key(self: KeyGesture) -> Key

"""

    Modifiers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the modifier keys associated with this System.Windows.Input.KeyGesture.

Get: Modifiers(self: KeyGesture) -> ModifierKeys

"""



class KeyGestureConverter(TypeConverter):
    """
    Converts a System.Windows.Input.KeyGesture object to and from other types.
    
    KeyGestureConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: KeyGestureConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether an object of the specified type can be converted to an instance of System.Windows.Input.KeyGesture, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            sourceType: The type being evaluated for conversion.
            Returns: true if sourceType is type System.String; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: KeyGestureConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether an instance of System.Windows.Input.KeyGesture can be converted to the specified type, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            destinationType: The type being evaluated for conversion.
            Returns: true if destinationType is type System.String; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: KeyGestureConverter, context: ITypeDescriptorContext, culture: CultureInfo, source: object) -> object
        
            Attempts to convert the specified object to a System.Windows.Input.KeyGesture, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            culture: Culture specific information.
            source: The object to convert.
            Returns: The converted object.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: KeyGestureConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Attempts to convert a System.Windows.Input.KeyGesture to the specified type, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            culture: Culture specific information.
            value: The object to convert.
            destinationType: The type to convert the object to.
            Returns: The converted object, or an empty string if value is null.
        """
        pass


class KeyGestureValueSerializer(ValueSerializer):
    """
    Converts instances of System.String to and from instances of System.Windows.Input.KeyGesture.
    
    KeyGestureValueSerializer()
    """
    def CanConvertFromString(self, value, context):
        """
        CanConvertFromString(self: KeyGestureValueSerializer, value: str, context: IValueSerializerContext) -> bool
        
            Determines if the specified System.String can be convert to an instance of System.Windows.Input.KeyGesture.
        
            value: String to evaluate for conversion.
            context: Context information that is used for conversion.
            Returns: Always returns true.
        """
        pass

    def CanConvertToString(self, value, context):
        """
        CanConvertToString(self: KeyGestureValueSerializer, value: object, context: IValueSerializerContext) -> bool
        
            Determines if the specified System.Windows.Input.KeyGesture can be converted to a System.String.
        
            value: The gesture to evaluate for conversion.
            context: Context information that is used for conversion.
            Returns: true if value can be converted into a System.String; otherwise, false.
        """
        pass

    def ConvertFromString(self, value, context):
        """
        ConvertFromString(self: KeyGestureValueSerializer, value: str, context: IValueSerializerContext) -> object
        
            Converts a System.String into a System.Windows.Input.KeyGesture.
        
            value: The string to convert into a System.Windows.Input.KeyGesture.
            context: Context information that is used for conversion.
            Returns: A new instance of System.Windows.Input.KeyGesture based on the supplied value.
        """
        pass

    def ConvertToString(self, value, context):
        """
        ConvertToString(self: KeyGestureValueSerializer, value: object, context: IValueSerializerContext) -> str
        
            Converts an instance of System.Windows.Input.KeyGesture to a System.String.
        
            value: The gesture to convert into a string.
            context: Context information that is used for conversion.
            Returns: An invariant string representation of the specified System.Windows.Input.KeyGesture.
        """
        pass


class KeyInterop(object):
    """ Provides static methods to convert between Win32 Virtual-Keys and the WPF�System.Windows.Input.Key enumeration. """
    @staticmethod
    def KeyFromVirtualKey(virtualKey):
        """
        KeyFromVirtualKey(virtualKey: int) -> Key
        
            Converts a Win32 Virtual-Key into WPF�System.Windows.Input.Key.
        
            virtualKey: The virtual key to convert.
            Returns: The WPF key.
        """
        pass

    @staticmethod
    def VirtualKeyFromKey(key):
        """
        VirtualKeyFromKey(key: Key) -> int
        
            Converts a WPF�System.Windows.Input.Key into a�Win32 Virtual-Key.
        
            key: The WPF to convert.
            Returns: The Win32 Virtual-Key.
        """
        pass

    __all__ = [
        'KeyFromVirtualKey',
        'VirtualKeyFromKey',
    ]


class KeyStates(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies constants that define the state of a key.
    
    enum (flags) KeyStates, values: Down (1), None (0), Toggled (2)
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

    Down = None
    None = None
    Toggled = None
    value__ = None


class KeyValueSerializer(ValueSerializer):
    """
    Converts instances of System.String to and from instances of System.Windows.Input.Key.
    
    KeyValueSerializer()
    """
    def CanConvertFromString(self, value, context):
        """
        CanConvertFromString(self: KeyValueSerializer, value: str, context: IValueSerializerContext) -> bool
        
            Determines if the specified System.String can be convert to an instance of System.Windows.Input.Key.
        
            value: String to evaluate for conversion.
            context: Context information that is used for conversion.
            Returns: Always returns true.
        """
        pass

    def CanConvertToString(self, value, context):
        """
        CanConvertToString(self: KeyValueSerializer, value: object, context: IValueSerializerContext) -> bool
        
            Determines if the specified System.Windows.Input.Key can be converted to a System.String.
        
            value: The key to evaluate for conversion.
            context: Context information that is used for conversion.
            Returns: true if value can be converted into a System.String; otherwise, false.
        """
        pass

    def ConvertFromString(self, value, context):
        """
        ConvertFromString(self: KeyValueSerializer, value: str, context: IValueSerializerContext) -> object
        
            Converts a System.String into a System.Windows.Input.Key.
        
            value: The string to convert into a System.Windows.Input.Key.
            context: Context information that is used for conversion.
            Returns: A new instance of System.Windows.Input.Key based on the supplied value.
        """
        pass

    def ConvertToString(self, value, context):
        """
        ConvertToString(self: KeyValueSerializer, value: object, context: IValueSerializerContext) -> str
        
            Converts an instance of System.Windows.Input.Key to a System.String.
        
            value: The key to convert into a string.
            context: Context information that is used for conversion.
            Returns: An invariant string representation of the specified System.Windows.Input.Key.
        """
        pass


class Manipulation(object):
    """ Contains methods to get and update information about a manipulation. """
    @staticmethod
    def AddManipulator(element, manipulator):
        """
        AddManipulator(element: UIElement, manipulator: IManipulator)
            Associates a System.Windows.Input.IManipulator object with the specified element.
        
            element: The element to associate the manipulator with.
            manipulator: The object that provides the position of the input that creates or is added to a manipulation.
        """
        pass

    @staticmethod
    def CompleteManipulation(element):
        """
        CompleteManipulation(element: UIElement)
            Completes the active manipulation on the specified element. When called, manipulation input is no longer tracked and inertia on the specified element stops.
        
            element: The element on which to complete manipulation.
        """
        pass

    @staticmethod
    def GetManipulationContainer(element):
        """
        GetManipulationContainer(element: UIElement) -> IInputElement
        
            Gets the container that defines the coordinates for the manipulation.
        
            element: The element on which there is an active manipulation.
            Returns: The container that defines the coordinate space.
        """
        pass

    @staticmethod
    def GetManipulationMode(element):
        """
        GetManipulationMode(element: UIElement) -> ManipulationModes
        
            Gets the System.Windows.Input.ManipulationModes for the specified element.
        
            element: The element for which to get the manipulation mode.
            Returns: One of the enumeration values.
        """
        pass

    @staticmethod
    def GetManipulationPivot(element):
        """
        GetManipulationPivot(element: UIElement) -> ManipulationPivot
        
            Returns an object that describes how a rotation occurs with one point of user input.
        
            element: The element on which there is a manipulation.
            Returns: An object that describes how a rotation occurs with one point of user input.
        """
        pass

    @staticmethod
    def IsManipulationActive(element):
        """
        IsManipulationActive(element: UIElement) -> bool
        
            Gets a value that indicates whether a manipulation is associated with the specified element.
        
            element: The element to check.
            Returns: true if a manipulation is associated with the specified element; otherwise, false.
        """
        pass

    @staticmethod
    def RemoveManipulator(element, manipulator):
        """
        RemoveManipulator(element: UIElement, manipulator: IManipulator)
            Removes the association between the specified System.Windows.Input.IManipulator object and the element.
        
            element: The element to remove the associated manipulator from.
            manipulator: The object that provides the position of the input.
        """
        pass

    @staticmethod
    def SetManipulationContainer(element, container):
        """
        SetManipulationContainer(element: UIElement, container: IInputElement)
            Sets the element that defines the coordinates for the manipulation of the specified element.
        
            element: The element with which the manipulation is associated.
            container: The container that defines the coordinate space.
        """
        pass

    @staticmethod
    def SetManipulationMode(element, mode):
        """
        SetManipulationMode(element: UIElement, mode: ManipulationModes)
            Sets the mode of manipulation for the specified element.
        
            element: The element on which to set the manipulation mode.
            mode: The new manipulation mode.
        """
        pass

    @staticmethod
    def SetManipulationParameter(element, parameter):
        """
        SetManipulationParameter(element: UIElement, parameter: ManipulationParameters2D)
            Adds parameters to the manipulation of the specified element.
        
            element: The element that has the manipulation that the parameter is added to.
            parameter: The parameter to add.
        """
        pass

    @staticmethod
    def SetManipulationPivot(element, pivot):
        """
        SetManipulationPivot(element: UIElement, pivot: ManipulationPivot)
            Sets the pivot of the single-point manipulation of the specified element.
        
            element: The element that has an active manipulation.
            pivot: An object that describes the pivot.
        """
        pass

    @staticmethod
    def StartInertia(element):
        """
        StartInertia(element: UIElement)
            Stops the manipulation and begins inertia on the specified element.
        
            element: The element on which to begin inertia.
        """
        pass

    __all__ = [
        'AddManipulator',
        'CompleteManipulation',
        'GetManipulationContainer',
        'GetManipulationMode',
        'GetManipulationPivot',
        'IsManipulationActive',
        'RemoveManipulator',
        'SetManipulationContainer',
        'SetManipulationMode',
        'SetManipulationParameter',
        'SetManipulationPivot',
        'StartInertia',
    ]


class ManipulationBoundaryFeedbackEventArgs(InputEventArgs):
    """ Provides data for the System.Windows.UIElement.ManipulationBoundaryFeedback event. """
    BoundaryFeedback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the unused portion of the direct manipulation.

Get: BoundaryFeedback(self: ManipulationBoundaryFeedbackEventArgs) -> ManipulationDelta

"""

    ManipulationContainer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the container that the System.Windows.Input.ManipulationBoundaryFeedbackEventArgs.BoundaryFeedback property is relative to.

Get: ManipulationContainer(self: ManipulationBoundaryFeedbackEventArgs) -> IInputElement

"""

    Manipulators = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of objects that represents the touch contacts for the manipulation.

Get: Manipulators(self: ManipulationBoundaryFeedbackEventArgs) -> IEnumerable[IManipulator]

"""



class ManipulationCompletedEventArgs(InputEventArgs):
    """ Provides data for the System.Windows.UIElement.ManipulationCompleted event. """
    def Cancel(self):
        """
        Cancel(self: ManipulationCompletedEventArgs) -> bool
        
            Cancels the manipulation.
            Returns: true if the manipulation was successfully canceled; otherwise, false.
        """
        pass

    FinalVelocities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the velocities that are used for the manipulation.

Get: FinalVelocities(self: ManipulationCompletedEventArgs) -> ManipulationVelocities

"""

    IsInertial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.Windows.UIElement.ManipulationCompleted event occurs during inertia.

Get: IsInertial(self: ManipulationCompletedEventArgs) -> bool

"""

    ManipulationContainer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the container that defines the coordinates for the manipulation.

Get: ManipulationContainer(self: ManipulationCompletedEventArgs) -> IInputElement

"""

    ManipulationOrigin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the point from which the manipulation originated.

Get: ManipulationOrigin(self: ManipulationCompletedEventArgs) -> Point

"""

    Manipulators = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of objects that represents the touch contacts for the manipulation.

Get: Manipulators(self: ManipulationCompletedEventArgs) -> IEnumerable[IManipulator]

"""

    TotalManipulation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the total transformation that occurs during the current manipulation.

Get: TotalManipulation(self: ManipulationCompletedEventArgs) -> ManipulationDelta

"""



class ManipulationDelta(object):
    """
    Contains transformation data that is accumulated when manipulation events occur.
    
    ManipulationDelta(translation: Vector, rotation: float, scale: Vector, expansion: Vector)
    """
    @staticmethod # known case of __new__
    def __new__(self, translation, rotation, scale, expansion):
        """ __new__(cls: type, translation: Vector, rotation: float, scale: Vector, expansion: Vector) """
        pass

    Expansion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the amount the manipulation has resized in device-independent units (1/96th inch per unit).

Get: Expansion(self: ManipulationDelta) -> Vector

"""

    Rotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the rotation of the manipulation in degrees.

Get: Rotation(self: ManipulationDelta) -> float

"""

    Scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the amount the manipulation has resized as a multiplier.

Get: Scale(self: ManipulationDelta) -> Vector

"""

    Translation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the linear motion of the manipulation.

Get: Translation(self: ManipulationDelta) -> Vector

"""



class ManipulationDeltaEventArgs(InputEventArgs):
    """ Provides data for the System.Windows.UIElement.ManipulationDelta event. """
    def Cancel(self):
        """
        Cancel(self: ManipulationDeltaEventArgs) -> bool
        
            Cancels the manipulation.
            Returns: true if the manipulation was successfully canceled; otherwise, false.
        """
        pass

    def Complete(self):
        """
        Complete(self: ManipulationDeltaEventArgs)
            Completes the manipulation without inertia.
        """
        pass

    def ReportBoundaryFeedback(self, unusedManipulation):
        """
        ReportBoundaryFeedback(self: ManipulationDeltaEventArgs, unusedManipulation: ManipulationDelta)
            Specifies that the manipulation has gone beyond certain boundaries.
        
            unusedManipulation: The portion of the manipulation that represents moving beyond the boundary.
        """
        pass

    def StartInertia(self):
        """
        StartInertia(self: ManipulationDeltaEventArgs)
            Starts inertia on the manipulation by ignoring subsequent contact movements and raising the System.Windows.UIElement.ManipulationInertiaStarting event.
        """
        pass

    CumulativeManipulation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the cumulated changes of the current manipulation.

Get: CumulativeManipulation(self: ManipulationDeltaEventArgs) -> ManipulationDelta

"""

    DeltaManipulation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recent changes of the current manipulation.

Get: DeltaManipulation(self: ManipulationDeltaEventArgs) -> ManipulationDelta

"""

    IsInertial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.Windows.UIElement.ManipulationDelta event occurs during inertia.

Get: IsInertial(self: ManipulationDeltaEventArgs) -> bool

"""

    ManipulationContainer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the container that defines the coordinates for the manipulation.

Get: ManipulationContainer(self: ManipulationDeltaEventArgs) -> IInputElement

"""

    ManipulationOrigin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the point from which the manipulation originated.

Get: ManipulationOrigin(self: ManipulationDeltaEventArgs) -> Point

"""

    Manipulators = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of objects that represents the touch contacts for the manipulation.

Get: Manipulators(self: ManipulationDeltaEventArgs) -> IEnumerable[IManipulator]

"""

    Velocities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the rates of the most recent changes to the manipulation.

Get: Velocities(self: ManipulationDeltaEventArgs) -> ManipulationVelocities

"""



class ManipulationInertiaStartingEventArgs(InputEventArgs):
    """ Provides data for the System.Windows.UIElement.ManipulationInertiaStarting event. """
    def Cancel(self):
        """
        Cancel(self: ManipulationInertiaStartingEventArgs) -> bool
        
            Cancels the manipulation.
            Returns: true if the manipulation was successfully canceled; otherwise, false.
        """
        pass

    def SetInertiaParameter(self, parameter):
        """
        SetInertiaParameter(self: ManipulationInertiaStartingEventArgs, parameter: InertiaParameters2D)
            Specifies the behavior of a manipulation during inertia.
        
            parameter: The object that specifies the behavior of a manipulation during inertia.
        """
        pass

    ExpansionBehavior = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or sets the rate of slowdown of expansion inertial movement.

Get: ExpansionBehavior(self: ManipulationInertiaStartingEventArgs) -> InertiaExpansionBehavior

Set: ExpansionBehavior(self: ManipulationInertiaStartingEventArgs) = value
"""

    InitialVelocities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the rates of changes to the manipulation that occur before inertia starts.

Get: InitialVelocities(self: ManipulationInertiaStartingEventArgs) -> ManipulationVelocities

"""

    ManipulationContainer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the container that the System.Windows.Input.ManipulationStartedEventArgs.ManipulationOrigin property is relative to.

Get: ManipulationContainer(self: ManipulationInertiaStartingEventArgs) -> IInputElement

"""

    ManipulationOrigin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the point from which the manipulation originated.

Get: ManipulationOrigin(self: ManipulationInertiaStartingEventArgs) -> Point

Set: ManipulationOrigin(self: ManipulationInertiaStartingEventArgs) = value
"""

    Manipulators = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of objects that represents the touch contacts for the manipulation.

Get: Manipulators(self: ManipulationInertiaStartingEventArgs) -> IEnumerable[IManipulator]

"""

    RotationBehavior = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the rate of slowdown of rotational inertial movement.

Get: RotationBehavior(self: ManipulationInertiaStartingEventArgs) -> InertiaRotationBehavior

Set: RotationBehavior(self: ManipulationInertiaStartingEventArgs) = value
"""

    TranslationBehavior = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets and sets the rate of slowdown of linear inertial movement.

Get: TranslationBehavior(self: ManipulationInertiaStartingEventArgs) -> InertiaTranslationBehavior

Set: TranslationBehavior(self: ManipulationInertiaStartingEventArgs) = value
"""



class ManipulationModes(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies how manipulation events are interpreted.
    
    enum (flags) ManipulationModes, values: All (15), None (0), Rotate (4), Scale (8), Translate (3), TranslateX (1), TranslateY (2)
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

    All = None
    None = None
    Rotate = None
    Scale = None
    Translate = None
    TranslateX = None
    TranslateY = None
    value__ = None


class ManipulationPivot(object):
    """
    Specifies how a rotation occurs with one point of user input.
    
    ManipulationPivot()
    ManipulationPivot(center: Point, radius: float)
    """
    @staticmethod # known case of __new__
    def __new__(self, center=None, radius=None):
        """
        __new__(cls: type)
        __new__(cls: type, center: Point, radius: float)
        """
        pass

    Center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the center of a single-point manipulation.

Get: Center(self: ManipulationPivot) -> Point

Set: Center(self: ManipulationPivot) = value
"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the area around the pivot that is used to determine how much rotation and translation occurs when a single point of contact initiates the manipulation.

Get: Radius(self: ManipulationPivot) -> float

Set: Radius(self: ManipulationPivot) = value
"""



class ManipulationStartedEventArgs(InputEventArgs):
    """ Provides data for the System.Windows.UIElement.ManipulationStarted event. """
    def Cancel(self):
        """
        Cancel(self: ManipulationStartedEventArgs) -> bool
        
            Cancels the manipulation.
            Returns: true if manipulation was successfully, otherwise, false.
        """
        pass

    def Complete(self):
        """
        Complete(self: ManipulationStartedEventArgs)
            Completes the manipulation without inertia.
        """
        pass

    ManipulationContainer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the container that the System.Windows.Input.ManipulationStartedEventArgs.ManipulationOrigin property is relative to.

Get: ManipulationContainer(self: ManipulationStartedEventArgs) -> IInputElement

"""

    ManipulationOrigin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the point from which the manipulation originated.

Get: ManipulationOrigin(self: ManipulationStartedEventArgs) -> Point

"""

    Manipulators = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of objects that represents the touch contacts for the manipulation.

Get: Manipulators(self: ManipulationStartedEventArgs) -> IEnumerable[IManipulator]

"""



class ManipulationStartingEventArgs(InputEventArgs):
    """ Provides data for the System.Windows.UIElement.ManipulationStarting, event. """
    def Cancel(self):
        """
        Cancel(self: ManipulationStartingEventArgs) -> bool
        
            Cancels the manipulation and promotes touch to mouse events.
            Returns: true if touch was successfully promoted to mouse events, otherwise, false.
        """
        pass

    def SetManipulationParameter(self, parameter):
        """
        SetManipulationParameter(self: ManipulationStartingEventArgs, parameter: ManipulationParameters2D)
            Adds parameters to the current manipulation of the specified element.
        
            parameter: The parameter to add.
        """
        pass

    IsSingleTouchEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether one finger can start a manipulation.

Get: IsSingleTouchEnabled(self: ManipulationStartingEventArgs) -> bool

Set: IsSingleTouchEnabled(self: ManipulationStartingEventArgs) = value
"""

    ManipulationContainer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the container that all manipulation events and calculations are relative to.

Get: ManipulationContainer(self: ManipulationStartingEventArgs) -> IInputElement

Set: ManipulationContainer(self: ManipulationStartingEventArgs) = value
"""

    Manipulators = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of objects that represents the touch contacts for the manipulation.

Get: Manipulators(self: ManipulationStartingEventArgs) -> IEnumerable[IManipulator]

"""

    Mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets which types of manipulations are possible.

Get: Mode(self: ManipulationStartingEventArgs) -> ManipulationModes

Set: Mode(self: ManipulationStartingEventArgs) = value
"""

    Pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an object that describes the pivot for a single-point manipulation.

Get: Pivot(self: ManipulationStartingEventArgs) -> ManipulationPivot

Set: Pivot(self: ManipulationStartingEventArgs) = value
"""



class ManipulationVelocities(object):
    """
    Describes the speed at which manipulations occurs.
    
    ManipulationVelocities(linearVelocity: Vector, angularVelocity: float, expansionVelocity: Vector)
    """
    @staticmethod # known case of __new__
    def __new__(self, linearVelocity, angularVelocity, expansionVelocity):
        """ __new__(cls: type, linearVelocity: Vector, angularVelocity: float, expansionVelocity: Vector) """
        pass

    AngularVelocity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the speed of rotation.

Get: AngularVelocity(self: ManipulationVelocities) -> float

"""

    ExpansionVelocity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the rate at which the manipulation is resized.

Get: ExpansionVelocity(self: ManipulationVelocities) -> Vector

"""

    LinearVelocity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the speed of linear motion.

Get: LinearVelocity(self: ManipulationVelocities) -> Vector

"""



class MediaCommands(object):
    """ Provides a standard set of media related commands. """
    BoostBass = None
    ChannelDown = None
    ChannelUp = None
    DecreaseBass = None
    DecreaseMicrophoneVolume = None
    DecreaseTreble = None
    DecreaseVolume = None
    FastForward = None
    IncreaseBass = None
    IncreaseMicrophoneVolume = None
    IncreaseTreble = None
    IncreaseVolume = None
    MuteMicrophoneVolume = None
    MuteVolume = None
    NextTrack = None
    Pause = None
    Play = None
    PreviousTrack = None
    Record = None
    Rewind = None
    Select = None
    Stop = None
    ToggleMicrophoneOnOff = None
    TogglePlayPause = None
    __all__ = []


class ModifierKeys(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the set of modifier keys.
    
    enum (flags) ModifierKeys, values: Alt (1), Control (2), None (0), Shift (4), Windows (8)
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

    Alt = None
    Control = None
    None = None
    Shift = None
    value__ = None
    Windows = None


class ModifierKeysConverter(TypeConverter):
    """
    Converts a System.Windows.Input.ModifierKeys object to and from other types.
    
    ModifierKeysConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: ModifierKeysConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether an object of the specified type can be converted to an instance of System.Windows.Input.ModifierKeys, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            sourceType: The type being evaluated for conversion.
            Returns: true if sourceType is type System.String; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: ModifierKeysConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether an instance of System.Windows.Input.ModifierKeys can be converted to the specified type, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            destinationType: The type being evaluated for conversion.
            Returns: true if destinationType is type System.String; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: ModifierKeysConverter, context: ITypeDescriptorContext, culture: CultureInfo, source: object) -> object
        
            Attempts to convert the specified object to a System.Windows.Input.ModifierKeys, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            culture: Culture specific information.
            source: The object to convert.
            Returns: The converted object.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: ModifierKeysConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Attempts to convert a System.Windows.Input.ModifierKeys to the specified type, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            culture: Culture specific information.
            value: The object to convert.
            destinationType: The type to convert the object to.
            Returns: The converted object.
        """
        pass

    @staticmethod
    def IsDefinedModifierKeys(modifierKeys):
        """
        IsDefinedModifierKeys(modifierKeys: ModifierKeys) -> bool
        
            Determines whether the specified value is a valid System.Windows.Input.ModifierKeys value.
        
            modifierKeys: The value to check for validity.
            Returns: true if input is a valid System.Windows.Input.ModifierKeys value; otherwise, false.
        """
        pass


class ModifierKeysValueSerializer(ValueSerializer):
    """
    Converts instances of System.String to and from instances of System.Windows.Input.ModifierKeys.
    
    ModifierKeysValueSerializer()
    """
    def CanConvertFromString(self, value, context):
        """
        CanConvertFromString(self: ModifierKeysValueSerializer, value: str, context: IValueSerializerContext) -> bool
        
            Determines if the specified System.String can be convert to an instance of System.Windows.Input.ModifierKeys.
        
            value: String to evaluate for conversion.
            context: Context information that is used for conversion.
            Returns: Always returns true.
        """
        pass

    def CanConvertToString(self, value, context):
        """
        CanConvertToString(self: ModifierKeysValueSerializer, value: object, context: IValueSerializerContext) -> bool
        
            Determines if the specified System.Windows.Input.ModifierKeys can be converted to a System.String.
        
            value: The modifier keys to evaluate for conversion.
            context: Context information that is used for conversion.
            Returns: true if value can be converted into a System.String; otherwise, false.
        """
        pass

    def ConvertFromString(self, value, context):
        """
        ConvertFromString(self: ModifierKeysValueSerializer, value: str, context: IValueSerializerContext) -> object
        
            Converts a System.String into a System.Windows.Input.ModifierKeys value.
        
            value: The string to convert into a System.Windows.Input.ModifierKeys.
            context: Context information that is used for conversion.
            Returns: A new instance of System.Windows.Input.ModifierKeys based on the supplied value.
        """
        pass

    def ConvertToString(self, value, context):
        """
        ConvertToString(self: ModifierKeysValueSerializer, value: object, context: IValueSerializerContext) -> str
        
            Converts an instance of System.Windows.Input.ModifierKeys to a System.String.
        
            value: The key to convert into a string.
            context: Context information that is used for conversion.
            Returns: An invariant string representation of the specified System.Windows.Input.ModifierKeys value.
        """
        pass


class Mouse(object):
    """ Represents the mouse device to a specific thread. """
    @staticmethod
    def AddGotMouseCaptureHandler(element, handler):
        """
        AddGotMouseCaptureHandler(element: DependencyObject, handler: MouseEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.GotMouseCapture�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def AddLostMouseCaptureHandler(element, handler):
        """
        AddLostMouseCaptureHandler(element: DependencyObject, handler: MouseEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.LostMouseCapture�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def AddMouseDownHandler(element, handler):
        """
        AddMouseDownHandler(element: DependencyObject, handler: MouseButtonEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.MouseDown�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def AddMouseEnterHandler(element, handler):
        """
        AddMouseEnterHandler(element: DependencyObject, handler: MouseEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.MouseEnter�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def AddMouseLeaveHandler(element, handler):
        """
        AddMouseLeaveHandler(element: DependencyObject, handler: MouseEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.MouseLeave�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def AddMouseMoveHandler(element, handler):
        """
        AddMouseMoveHandler(element: DependencyObject, handler: MouseEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.MouseMove�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def AddMouseUpHandler(element, handler):
        """
        AddMouseUpHandler(element: DependencyObject, handler: MouseButtonEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.MouseUp�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def AddMouseWheelHandler(element, handler):
        """
        AddMouseWheelHandler(element: DependencyObject, handler: MouseWheelEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.MouseWheel�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def AddPreviewMouseDownHandler(element, handler):
        """
        AddPreviewMouseDownHandler(element: DependencyObject, handler: MouseButtonEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.PreviewMouseDown�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def AddPreviewMouseDownOutsideCapturedElementHandler(element, handler):
        """
        AddPreviewMouseDownOutsideCapturedElementHandler(element: DependencyObject, handler: MouseButtonEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.PreviewMouseDownOutsideCapturedElement�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def AddPreviewMouseMoveHandler(element, handler):
        """
        AddPreviewMouseMoveHandler(element: DependencyObject, handler: MouseEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.PreviewMouseMove�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def AddPreviewMouseUpHandler(element, handler):
        """
        AddPreviewMouseUpHandler(element: DependencyObject, handler: MouseButtonEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.PreviewMouseUp�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def AddPreviewMouseUpOutsideCapturedElementHandler(element, handler):
        """
        AddPreviewMouseUpOutsideCapturedElementHandler(element: DependencyObject, handler: MouseButtonEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.PreviewMouseUpOutsideCapturedElement�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def AddPreviewMouseWheelHandler(element, handler):
        """
        AddPreviewMouseWheelHandler(element: DependencyObject, handler: MouseWheelEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.PreviewMouseWheel�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def AddQueryCursorHandler(element, handler):
        """
        AddQueryCursorHandler(element: DependencyObject, handler: QueryCursorEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.QueryCursor�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def Capture(element, captureMode=None):
        """
        Capture(element: IInputElement, captureMode: CaptureMode) -> bool
        
            Captures mouse input to the specified element using the specified System.Windows.Input.CaptureMode.
        
            element: The element to capture the mouse.
            captureMode: The capture policy to use.
            Returns: true if the element was able to capture the mouse; otherwise, false.
        Capture(element: IInputElement) -> bool
        
            Captures mouse input to the specified element.
        
            element: The element to capture the mouse.
            Returns: true if the element was able to capture the mouse; otherwise, false.
        """
        pass

    @staticmethod
    def GetIntermediatePoints(relativeTo, points):
        """
        GetIntermediatePoints(relativeTo: IInputElement, points: Array[Point]) -> int
        
            Retrieves up to 64 previous coordinates of the mouse pointer since the last mouse move event.
        
            relativeTo: The elements points are in relation to.
            points: An array of objects.
            Returns: The number of points returned.
        """
        pass

    @staticmethod
    def GetPosition(relativeTo):
        """
        GetPosition(relativeTo: IInputElement) -> Point
        
            Gets the position of the mouse relative to a specified element.
        
            relativeTo: The coordinate space in which to calculate the position of the mouse.
            Returns: The position of the mouse relative to the parameter relativeTo.
        """
        pass

    @staticmethod
    def RemoveGotMouseCaptureHandler(element, handler):
        """
        RemoveGotMouseCaptureHandler(element: DependencyObject, handler: MouseEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.GotMouseCapture�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def RemoveLostMouseCaptureHandler(element, handler):
        """
        RemoveLostMouseCaptureHandler(element: DependencyObject, handler: MouseEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.LostMouseCapture�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def RemoveMouseDownHandler(element, handler):
        """
        RemoveMouseDownHandler(element: DependencyObject, handler: MouseButtonEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.MouseDown�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def RemoveMouseEnterHandler(element, handler):
        """
        RemoveMouseEnterHandler(element: DependencyObject, handler: MouseEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.MouseEnter�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def RemoveMouseLeaveHandler(element, handler):
        """
        RemoveMouseLeaveHandler(element: DependencyObject, handler: MouseEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.MouseLeave�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def RemoveMouseMoveHandler(element, handler):
        """
        RemoveMouseMoveHandler(element: DependencyObject, handler: MouseEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.MouseMove�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def RemoveMouseUpHandler(element, handler):
        """
        RemoveMouseUpHandler(element: DependencyObject, handler: MouseButtonEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.MouseUp�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def RemoveMouseWheelHandler(element, handler):
        """
        RemoveMouseWheelHandler(element: DependencyObject, handler: MouseWheelEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.MouseWheel�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def RemovePreviewMouseDownHandler(element, handler):
        """
        RemovePreviewMouseDownHandler(element: DependencyObject, handler: MouseButtonEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.PreviewMouseDown�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def RemovePreviewMouseDownOutsideCapturedElementHandler(element, handler):
        """
        RemovePreviewMouseDownOutsideCapturedElementHandler(element: DependencyObject, handler: MouseButtonEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.PreviewMouseDownOutsideCapturedElement�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def RemovePreviewMouseMoveHandler(element, handler):
        """
        RemovePreviewMouseMoveHandler(element: DependencyObject, handler: MouseEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.PreviewMouseMove�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def RemovePreviewMouseUpHandler(element, handler):
        """
        RemovePreviewMouseUpHandler(element: DependencyObject, handler: MouseButtonEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.PreviewMouseUp�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def RemovePreviewMouseUpOutsideCapturedElementHandler(element, handler):
        """
        RemovePreviewMouseUpOutsideCapturedElementHandler(element: DependencyObject, handler: MouseButtonEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.PreviewMouseUpOutsideCapturedElement�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def RemovePreviewMouseWheelHandler(element, handler):
        """
        RemovePreviewMouseWheelHandler(element: DependencyObject, handler: MouseWheelEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.PreviewMouseWheel�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def RemoveQueryCursorHandler(element, handler):
        """
        RemoveQueryCursorHandler(element: DependencyObject, handler: QueryCursorEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.QueryCursor�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def SetCursor(cursor):
        """
        SetCursor(cursor: Cursor) -> bool
        
            Sets the mouse pointer to the specified System.Windows.Input.Cursor.
        
            cursor: The cursor to set the mouse pointer to.
            Returns: true, if the cursor was set; otherwise, false.
        """
        pass

    @staticmethod
    def Synchronize():
        """
        Synchronize()
            Forces the mouse to resynchronize.
        """
        pass

    @staticmethod
    def UpdateCursor():
        """
        UpdateCursor()
            Forces the mouse cursor to be updated.
        """
        pass

    Captured = None
    DirectlyOver = None
    GotMouseCaptureEvent = None
    LeftButton = None
    LostMouseCaptureEvent = None
    MiddleButton = None
    MouseDownEvent = None
    MouseEnterEvent = None
    MouseLeaveEvent = None
    MouseMoveEvent = None
    MouseUpEvent = None
    MouseWheelDeltaForOneLine = 120
    MouseWheelEvent = None
    OverrideCursor = None
    PreviewMouseDownEvent = None
    PreviewMouseDownOutsideCapturedElementEvent = None
    PreviewMouseMoveEvent = None
    PreviewMouseUpEvent = None
    PreviewMouseUpOutsideCapturedElementEvent = None
    PreviewMouseWheelEvent = None
    PrimaryDevice = None
    QueryCursorEvent = None
    RightButton = None
    XButton1 = None
    XButton2 = None
    __all__ = [
        'AddGotMouseCaptureHandler',
        'AddLostMouseCaptureHandler',
        'AddMouseDownHandler',
        'AddMouseEnterHandler',
        'AddMouseLeaveHandler',
        'AddMouseMoveHandler',
        'AddMouseUpHandler',
        'AddMouseWheelHandler',
        'AddPreviewMouseDownHandler',
        'AddPreviewMouseDownOutsideCapturedElementHandler',
        'AddPreviewMouseMoveHandler',
        'AddPreviewMouseUpHandler',
        'AddPreviewMouseUpOutsideCapturedElementHandler',
        'AddPreviewMouseWheelHandler',
        'AddQueryCursorHandler',
        'Capture',
        'GetIntermediatePoints',
        'GetPosition',
        'GotMouseCaptureEvent',
        'LostMouseCaptureEvent',
        'MouseDownEvent',
        'MouseEnterEvent',
        'MouseLeaveEvent',
        'MouseMoveEvent',
        'MouseUpEvent',
        'MouseWheelDeltaForOneLine',
        'MouseWheelEvent',
        'PreviewMouseDownEvent',
        'PreviewMouseDownOutsideCapturedElementEvent',
        'PreviewMouseMoveEvent',
        'PreviewMouseUpEvent',
        'PreviewMouseUpOutsideCapturedElementEvent',
        'PreviewMouseWheelEvent',
        'QueryCursorEvent',
        'RemoveGotMouseCaptureHandler',
        'RemoveLostMouseCaptureHandler',
        'RemoveMouseDownHandler',
        'RemoveMouseEnterHandler',
        'RemoveMouseLeaveHandler',
        'RemoveMouseMoveHandler',
        'RemoveMouseUpHandler',
        'RemoveMouseWheelHandler',
        'RemovePreviewMouseDownHandler',
        'RemovePreviewMouseDownOutsideCapturedElementHandler',
        'RemovePreviewMouseMoveHandler',
        'RemovePreviewMouseUpHandler',
        'RemovePreviewMouseUpOutsideCapturedElementHandler',
        'RemovePreviewMouseWheelHandler',
        'RemoveQueryCursorHandler',
        'SetCursor',
        'Synchronize',
        'UpdateCursor',
    ]


class MouseAction(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies constants that define actions performed by the mouse.
    
    enum MouseAction, values: LeftClick (1), LeftDoubleClick (5), MiddleClick (3), MiddleDoubleClick (7), None (0), RightClick (2), RightDoubleClick (6), WheelClick (4)
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

    LeftClick = None
    LeftDoubleClick = None
    MiddleClick = None
    MiddleDoubleClick = None
    None = None
    RightClick = None
    RightDoubleClick = None
    value__ = None
    WheelClick = None


class MouseActionConverter(TypeConverter):
    """
    Converts a System.Windows.Input.MouseAction object to and from other types.
    
    MouseActionConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: MouseActionConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether an object of the specified type can be converted to an instance of System.Windows.Input.MouseAction,using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            sourceType: The type being evaluated for conversion.
            Returns: true if this converter can perform the operation; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: MouseActionConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether an instance of System.Windows.Input.MouseAction can be converted to the specified type, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            destinationType: The type being evaluated for conversion.
            Returns: true if this converter can perform the operation; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: MouseActionConverter, context: ITypeDescriptorContext, culture: CultureInfo, source: object) -> object
        
            Attempts to convert the specified object to a System.Windows.Input.MouseAction, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            culture: Culture specific information.
            source: The object to convert.
            Returns: The converted object.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: MouseActionConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Attempts to convert a System.Windows.Input.MouseAction to the specified type, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            culture: Culture specific information.
            value: The object to convert.
            destinationType: The type to convert the object to.
            Returns: The converted object.
        """
        pass


class MouseActionValueSerializer(ValueSerializer):
    """
    Converts instances of System.String to and from instances of System.Windows.Input.MouseAction.
    
    MouseActionValueSerializer()
    """
    def CanConvertFromString(self, value, context):
        """
        CanConvertFromString(self: MouseActionValueSerializer, value: str, context: IValueSerializerContext) -> bool
        
            Determines if the specified System.String can be convert to an instance of System.Windows.Input.MouseAction.
        
            value: String to evaluate for conversion.
            context: Context information that is used for conversion.
            Returns: Always returns true.
        """
        pass

    def CanConvertToString(self, value, context):
        """
        CanConvertToString(self: MouseActionValueSerializer, value: object, context: IValueSerializerContext) -> bool
        
            Determines if the specified System.Windows.Input.MouseAction can be converted to a System.String.
        
            value: The modifier keys to evaluate for conversion.
            context: Context information that is used for conversion.
            Returns: true if value can be converted into a System.String; otherwise, false.
        """
        pass

    def ConvertFromString(self, value, context):
        """
        ConvertFromString(self: MouseActionValueSerializer, value: str, context: IValueSerializerContext) -> object
        
            Converts a System.String into a System.Windows.Input.MouseAction.
        
            value: The string to convert into a System.Windows.Input.MouseAction.
            context: Context information that is used for conversion.
            Returns: A new instance of System.Windows.Input.MouseAction based on the supplied value.
        """
        pass

    def ConvertToString(self, value, context):
        """
        ConvertToString(self: MouseActionValueSerializer, value: object, context: IValueSerializerContext) -> str
        
            Converts an instance of System.Windows.Input.MouseAction to a System.String.
        
            value: The key to convert into a string.
            context: Context information that is used for conversion.
            Returns: An invariant string representation of the specified System.Windows.Input.MouseAction.
        """
        pass


class MouseBinding(InputBinding, ISealable, ICommandSource):
    """
    Binds a System.Windows.Input.MouseGesture to a System.Windows.Input.RoutedCommand (or another System.Windows.Input.ICommand implementation).
    
    MouseBinding()
    MouseBinding(command: ICommand, gesture: MouseGesture)
    """
    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: MouseBinding, sourceFreezable: Freezable)
            Copies the base (non-animated) values of the properties of the specified object.
        
            sourceFreezable: The object to clone.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: MouseBinding, sourceFreezable: Freezable)
            Copies the current values of the properties of the specified object.
        
            sourceFreezable: The object to clone.
        """
        pass

    def CreateInstance(self, *args): #cannot find CLR method
        """
        CreateInstance(self: Freezable) -> Freezable
        
            Initializes a new instance of the System.Windows.Freezable class.
            Returns: The new instance.
        """
        pass

    def CreateInstanceCore(self, *args): #cannot find CLR method
        """
        CreateInstanceCore(self: MouseBinding) -> Freezable
        
            Creates an instance of an System.Windows.Input.MouseBinding.
            Returns: The new object.
        """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: Freezable, isChecking: bool) -> bool
        
            Makes the System.Windows.Freezable object unmodifiable or tests whether it can be made unmodifiable.
        
            isChecking: true to return an indication of whether the object can be frozen (without actually freezing it); false to actually freeze the object.
            Returns: If isChecking is true, this method returns true if the System.Windows.Freezable can be made unmodifiable, or false if it cannot be made unmodifiable. If isChecking is false, this method returns true if the 
             if the specified System.Windows.Freezable is now unmodifiable, or false if it cannot be made unmodifiable.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: MouseBinding, sourceFreezable: Freezable)
            Creates the instance a frozen clone of the specified System.Windows.Freezable by using base (non-animated) property values.
        
            sourceFreezable: The object to clone.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: MouseBinding, sourceFreezable: Freezable)
            Creates the current instance a frozen clone of the specified System.Windows.Freezable. If the object has animated dependency properties, their current animated values are copied.
        
            sourceFreezable: The object to clone.
        """
        pass

    def OnChanged(self, *args): #cannot find CLR method
        """
        OnChanged(self: Freezable)
            Called when the current System.Windows.Freezable object is modified.
        """
        pass

    def OnFreezablePropertyChanged(self, *args): #cannot find CLR method
        """
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject, property: DependencyProperty)
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not intended to be used directly from your code.
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a System.Windows.DependencyObjectType data member that has just been set.
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventArgs) to also invoke any 
             System.Windows.Freezable.Changed handlers in response to a changing dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of System.Windows.Freezable must call this method at the beginning of any API that reads data members that are 
             not dependency properties.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for the provided dependency property.
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable should call 
             this method at the end of any API that modifies class members that are not stored as dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a valid threading context. System.Windows.Freezable inheritors should call this method at the beginning of any 
             API that writes to data members that are not dependency properties.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, command=None, gesture=None):
        """
        __new__(cls: type)
        __new__(cls: type, command: ICommand, gesture: MouseGesture)
        """
        pass

    Gesture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the gesture associated with this System.Windows.Input.MouseBinding.

Get: Gesture(self: MouseBinding) -> InputGesture

Set: Gesture(self: MouseBinding) = value
"""

    MouseAction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Input.MouseAction associated with this System.Windows.Input.MouseBinding.

Get: MouseAction(self: MouseBinding) -> MouseAction

Set: MouseAction(self: MouseBinding) = value
"""


    MouseActionProperty = None


class MouseButton(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines values that specify the buttons on a mouse device.
    
    enum MouseButton, values: Left (0), Middle (1), Right (2), XButton1 (3), XButton2 (4)
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

    Left = None
    Middle = None
    Right = None
    value__ = None
    XButton1 = None
    XButton2 = None


class MouseEventArgs(InputEventArgs):
    """
    Provides data for mouse related routed events that do not specifically involve mouse buttons or the mouse wheel, for example System.Windows.UIElement.MouseMove.
    
    MouseEventArgs(mouse: MouseDevice, timestamp: int)
    MouseEventArgs(mouse: MouseDevice, timestamp: int, stylusDevice: StylusDevice)
    """
    def GetPosition(self, relativeTo):
        """
        GetPosition(self: MouseEventArgs, relativeTo: IInputElement) -> Point
        
            Returns the position of the mouse pointer relative to the specified element.
        
            relativeTo: The element to use as the frame of reference for calculating the position of the mouse pointer.
            Returns: The x- and y-coordinates of the mouse pointer position relative to the specified object.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, mouse, timestamp, stylusDevice=None):
        """
        __new__(cls: type, mouse: MouseDevice, timestamp: int)
        __new__(cls: type, mouse: MouseDevice, timestamp: int, stylusDevice: StylusDevice)
        """
        pass

    LeftButton = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current state of the left mouse button.

Get: LeftButton(self: MouseEventArgs) -> MouseButtonState

"""

    MiddleButton = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current state of the middle mouse button.

Get: MiddleButton(self: MouseEventArgs) -> MouseButtonState

"""

    MouseDevice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the mouse device associated with this event.

Get: MouseDevice(self: MouseEventArgs) -> MouseDevice

"""

    RightButton = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current state of the right mouse button.

Get: RightButton(self: MouseEventArgs) -> MouseButtonState

"""

    StylusDevice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the stylus device associated with this event.

Get: StylusDevice(self: MouseEventArgs) -> StylusDevice

"""

    XButton1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current state of the first extended mouse button.

Get: XButton1(self: MouseEventArgs) -> MouseButtonState

"""

    XButton2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the state of the second extended mouse button.

Get: XButton2(self: MouseEventArgs) -> MouseButtonState

"""



class MouseButtonEventArgs(MouseEventArgs):
    """
    Provides data for mouse button related events.
    
    MouseButtonEventArgs(mouse: MouseDevice, timestamp: int, button: MouseButton)
    MouseButtonEventArgs(mouse: MouseDevice, timestamp: int, button: MouseButton, stylusDevice: StylusDevice)
    """
    @staticmethod # known case of __new__
    def __new__(self, mouse, timestamp, button, stylusDevice=None):
        """
        __new__(cls: type, mouse: MouseDevice, timestamp: int, button: MouseButton)
        __new__(cls: type, mouse: MouseDevice, timestamp: int, button: MouseButton, stylusDevice: StylusDevice)
        """
        pass

    ButtonState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the state of the button associated with the event.

Get: ButtonState(self: MouseButtonEventArgs) -> MouseButtonState

"""

    ChangedButton = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the button associated with the event.

Get: ChangedButton(self: MouseButtonEventArgs) -> MouseButton

"""

    ClickCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of times the button was clicked.

Get: ClickCount(self: MouseButtonEventArgs) -> int

"""



class MouseButtonEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle mouse button related routed events, for example System.Windows.UIElement.MouseLeftButtonDown.
    
    MouseButtonEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: MouseButtonEventHandler, sender: object, e: MouseButtonEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null, if the method represented by the current delegate does not require arguments.
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: MouseButtonEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: MouseButtonEventHandler, sender: object, e: MouseButtonEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation list.
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


class MouseButtonState(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the possible states of a mouse button.
    
    enum MouseButtonState, values: Pressed (1), Released (0)
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

    Pressed = None
    Released = None
    value__ = None


class MouseDevice(InputDevice):
    """ Represents a mouse device. """
    def Capture(self, element, captureMode=None):
        """
        Capture(self: MouseDevice, element: IInputElement, captureMode: CaptureMode) -> bool
        
            Captures mouse input to the specified element using the specified System.Windows.Input.CaptureMode.
        
            element: The element to capture the mouse..
            captureMode: The capture policy to use.
            Returns: true if the element was able to capture the mouse; otherwise, false.
        Capture(self: MouseDevice, element: IInputElement) -> bool
        
            Captures mouse events to the specified element.
        
            element: The element to capture the mouse.
            Returns: true if the element was able to capture the mouse; otherwise, false.
        """
        pass

    def GetButtonState(self, *args): #cannot find CLR method
        """
        GetButtonState(self: MouseDevice, mouseButton: MouseButton) -> MouseButtonState
        
            Gets the state of the specified mouse button.
        
            mouseButton: The button which is being queried.
            Returns: The state of the button.
        """
        pass

    def GetClientPosition(self, *args): #cannot find CLR method
        """
        GetClientPosition(self: MouseDevice, presentationSource: PresentationSource) -> Point
        
            Calculates the position of the mouse pointer, in client coordinates, in the specified System.Windows.PresentationSource.
        
            presentationSource: The source in which to obtain the mouse position.
            Returns: The position of the mouse pointer, in client coordinates, in the specified System.Windows.PresentationSource.
        GetClientPosition(self: MouseDevice) -> Point
        
            Calculates the position of the mouse pointer, in client coordinates.
            Returns: The position of the mouse pointer, in client coordinates.
        """
        pass

    def GetPosition(self, relativeTo):
        """
        GetPosition(self: MouseDevice, relativeTo: IInputElement) -> Point
        
            Gets the position of the mouse relative to a specified element.
        
            relativeTo: The frame of reference in which to calculate the position of the mouse.
            Returns: The position of the mouse relative to the parameter relativeTo.
        """
        pass

    def GetScreenPosition(self, *args): #cannot find CLR method
        """
        GetScreenPosition(self: MouseDevice) -> Point
        
            Calculates the screen position of the mouse pointer.
            Returns: The position of the mouse pointer.
        """
        pass

    def SetCursor(self, cursor):
        """
        SetCursor(self: MouseDevice, cursor: Cursor) -> bool
        
            Sets the mouse pointer to the specified System.Windows.Input.Cursor
        
            cursor: The cursor to set the mouse pointer to.
            Returns: true if the mouse cursor is set; otherwise, false.
        """
        pass

    def Synchronize(self):
        """
        Synchronize(self: MouseDevice)
            Forces the mouse to resynchronize.
        """
        pass

    def UpdateCursor(self):
        """
        UpdateCursor(self: MouseDevice)
            Forces the mouse cursor to update.
        """
        pass

    ActiveSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.PresentationSource that is reporting input for this device.

Get: ActiveSource(self: MouseDevice) -> PresentationSource

"""

    Captured = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.IInputElement that is captured by the mouse.

Get: Captured(self: MouseDevice) -> IInputElement

"""

    DirectlyOver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the element that the mouse pointer is directly over.

Get: DirectlyOver(self: MouseDevice) -> IInputElement

"""

    LeftButton = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the state of the left mouse button of this mouse device.

Get: LeftButton(self: MouseDevice) -> MouseButtonState

"""

    MiddleButton = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The state of the middle button of this mouse device.

Get: MiddleButton(self: MouseDevice) -> MouseButtonState

"""

    OverrideCursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the cursor for the entire application.

Get: OverrideCursor(self: MouseDevice) -> Cursor

Set: OverrideCursor(self: MouseDevice) = value
"""

    RightButton = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the state of the right button of this mouse device.

Get: RightButton(self: MouseDevice) -> MouseButtonState

"""

    Target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.IInputElement that the input from this mouse device is sent to.

Get: Target(self: MouseDevice) -> IInputElement

"""

    XButton1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the state of the first extended button on this mouse device.

Get: XButton1(self: MouseDevice) -> MouseButtonState

"""

    XButton2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the state of the second extended button of this mouse device.

Get: XButton2(self: MouseDevice) -> MouseButtonState

"""



class MouseEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle mouse related routed events that do not specifically involve mouse buttons or the mouse wheel; for example, System.Windows.UIElement.MouseMove.
    
    MouseEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: MouseEventHandler, sender: object, e: MouseEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null, if the method represented by the current delegate does not require arguments.
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: MouseEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: MouseEventHandler, sender: object, e: MouseEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation list.
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


class MouseGesture(InputGesture):
    """
    Defines a mouse input gesture that can be used to invoke a command.
    
    MouseGesture()
    MouseGesture(mouseAction: MouseAction)
    MouseGesture(mouseAction: MouseAction, modifiers: ModifierKeys)
    """
    def Matches(self, targetElement, inputEventArgs):
        """
        Matches(self: MouseGesture, targetElement: object, inputEventArgs: InputEventArgs) -> bool
        
            Determines whether System.Windows.Input.MouseGesture matches the input associated with the specified System.Windows.Input.InputEventArgs object.
        
            targetElement: The target.
            inputEventArgs: The input event data to compare with this gesture.
            Returns: true if the event data matches this System.Windows.Input.MouseGesture; otherwise, false.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, mouseAction=None, modifiers=None):
        """
        __new__(cls: type)
        __new__(cls: type, mouseAction: MouseAction)
        __new__(cls: type, mouseAction: MouseAction, modifiers: ModifierKeys)
        """
        pass

    Modifiers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the modifier keys associated with this System.Windows.Input.MouseGesture.

Get: Modifiers(self: MouseGesture) -> ModifierKeys

Set: Modifiers(self: MouseGesture) = value
"""

    MouseAction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Input.MouseAction associated with this gesture.

Get: MouseAction(self: MouseGesture) -> MouseAction

Set: MouseAction(self: MouseGesture) = value
"""



class MouseGestureConverter(TypeConverter):
    """
    Converts a System.Windows.Input.MouseGesture object to and from other types.
    
    MouseGestureConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: MouseGestureConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether an object of the specified type can be converted to an instance of System.Windows.Input.MouseGesture, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            sourceType: The type being evaluated for conversion.
            Returns: true if sourceType is of type System.String; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: MouseGestureConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether an instance of System.Windows.Input.MouseGesture can be converted to the specified type, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            destinationType: The type being evaluated for conversion.
            Returns: true if destinationType is of type System.String; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: MouseGestureConverter, context: ITypeDescriptorContext, culture: CultureInfo, source: object) -> object
        
            Attempts to convert the specified object to a System.Windows.Input.MouseGesture, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            culture: Culture specific information.
            source: The object to convert.
            Returns: The converted object.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: MouseGestureConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Attempts to convert a System.Windows.Input.MouseGesture to the specified type, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            culture: A format context that provides information about the environment from which this converter is being invoked.
            value: The object to convert.
            destinationType: The type to convert the object to.
            Returns: The converted object.
        """
        pass


class MouseGestureValueSerializer(ValueSerializer):
    """
    Converts instances of System.String to and from instances of System.Windows.Input.ModifierKeys.
    
    MouseGestureValueSerializer()
    """
    def CanConvertFromString(self, value, context):
        """
        CanConvertFromString(self: MouseGestureValueSerializer, value: str, context: IValueSerializerContext) -> bool
        
            Determines if the specified System.String can be convert to an instance of System.Windows.Input.ModifierKeys.
        
            value: String to evaluate for conversion.
            context: Context information that is used for conversion.
            Returns: Always returns true.
        """
        pass

    def CanConvertToString(self, value, context):
        """
        CanConvertToString(self: MouseGestureValueSerializer, value: object, context: IValueSerializerContext) -> bool
        
            Determines if the specified System.Windows.Input.ModifierKeys can be converted to a System.String.
        
            value: The modifier keys to evaluate for conversion.
            context: Context information that is used for conversion.
            Returns: true if value can be converted into a System.String; otherwise, false.
        """
        pass

    def ConvertFromString(self, value, context):
        """
        ConvertFromString(self: MouseGestureValueSerializer, value: str, context: IValueSerializerContext) -> object
        
            Converts a System.String into a System.Windows.Input.ModifierKeys.
        
            value: The string to convert into a System.Windows.Input.ModifierKeys.
            context: Context information that is used for conversion.
            Returns: A new instance of System.Windows.Input.ModifierKeys based on the supplied value.
        """
        pass

    def ConvertToString(self, value, context):
        """
        ConvertToString(self: MouseGestureValueSerializer, value: object, context: IValueSerializerContext) -> str
        
            Converts an instance of System.Windows.Input.ModifierKeys to a System.String.
        
            value: The key to convert into a string.
            context: Context information that is used for conversion.
            Returns: A string representation of the specified System.Windows.Input.ModifierKeys.
        """
        pass


class MouseWheelEventArgs(MouseEventArgs):
    """
    Provides data for various events that report changes to the mouse wheel delta value of a mouse device.
    
    MouseWheelEventArgs(mouse: MouseDevice, timestamp: int, delta: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, mouse, timestamp, delta):
        """ __new__(cls: type, mouse: MouseDevice, timestamp: int, delta: int) """
        pass

    Delta = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates the amount that the mouse wheel has changed.

Get: Delta(self: MouseWheelEventArgs) -> int

"""



class MouseWheelEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Windows.UIElement.MouseWheel and System.Windows.ContentElement.MouseWheel routed events, as well as related attached and Preview events.
    
    MouseWheelEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: MouseWheelEventHandler, sender: object, e: MouseWheelEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null, if the method represented by the current delegate does not require arguments.
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: MouseWheelEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: MouseWheelEventHandler, sender: object, e: MouseWheelEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation list.
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


class NavigationCommands(object):
    """ Provides a standard set of navigation-related commands. """
    BrowseBack = None
    BrowseForward = None
    BrowseHome = None
    BrowseStop = None
    DecreaseZoom = None
    Favorites = None
    FirstPage = None
    GoToPage = None
    IncreaseZoom = None
    LastPage = None
    NavigateJournal = None
    NextPage = None
    PreviousPage = None
    Refresh = None
    Search = None
    Zoom = None
    __all__ = []


class NotifyInputEventArgs(EventArgs):
    """ Provides data for raw input being processed by the System.Windows.Input.NotifyInputEventArgs.InputManager. """
    InputManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the input manager processing the input event.

Get: InputManager(self: NotifyInputEventArgs) -> InputManager

"""

    StagingItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the staging area input item being processed by the input manager.

Get: StagingItem(self: NotifyInputEventArgs) -> StagingAreaInputItem

"""



class NotifyInputEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle System.Windows.Input.InputManager.PreNotifyInput and System.Windows.Input.InputManager.PostNotifyInput events.
    
    NotifyInputEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: NotifyInputEventHandler, sender: object, e: NotifyInputEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null, if the method represented by the current delegate does not require arguments.
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: NotifyInputEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: NotifyInputEventHandler, sender: object, e: NotifyInputEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation list.
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


class ProcessInputEventArgs(NotifyInputEventArgs):
    """ Provides data for postprocess input events. """
    def PeekInput(self):
        """
        PeekInput(self: ProcessInputEventArgs) -> StagingAreaInputItem
        
            Gets, but does not pop, the input event on the top of the staging area stack.
            Returns: The input event that is on the top of the staging area stack.
        """
        pass

    def PopInput(self):
        """
        PopInput(self: ProcessInputEventArgs) -> StagingAreaInputItem
        
            Removes the input event off the top of the staging area stack.
            Returns: The input event that was on the top of the staging area stack. This will be null if the staging area is empty.
        """
        pass

    def PushInput(self, input, promote=None):
        """
        PushInput(self: ProcessInputEventArgs, input: StagingAreaInputItem) -> StagingAreaInputItem
        
            Puts the specified input event onto the top of the staging area stack.
        
            input: The input event to put on the staging area stack.
            Returns: The staging area input item.
        PushInput(self: ProcessInputEventArgs, input: InputEventArgs, promote: StagingAreaInputItem) -> StagingAreaInputItem
        
            Puts the specified input event onto the top of the specified staging area stack.
        
            input: The input event to put on the staging area stack.
            promote: An existing staging area item to promote the state from.
            Returns: The staging area input item that wraps the specified input.
        """
        pass


class PreProcessInputEventArgs(ProcessInputEventArgs):
    """ Provides data for preprocess input events. """
    def Cancel(self):
        """
        Cancel(self: PreProcessInputEventArgs)
            Cancels the processing of the input event.
        """
        pass

    Canceled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines whether processing of the input event was canceled.

Get: Canceled(self: PreProcessInputEventArgs) -> bool

"""



class PreProcessInputEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Windows.Input.InputManager.PreProcessInput event.
    
    PreProcessInputEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: PreProcessInputEventHandler, sender: object, e: PreProcessInputEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null, if the method represented by the current delegate does not require arguments.
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PreProcessInputEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PreProcessInputEventHandler, sender: object, e: PreProcessInputEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation list.
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


class ProcessInputEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Windows.Input.InputManager.PostProcessInput event.
    
    ProcessInputEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: ProcessInputEventHandler, sender: object, e: ProcessInputEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null, if the method represented by the current delegate does not require arguments.
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ProcessInputEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ProcessInputEventHandler, sender: object, e: ProcessInputEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation list.
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


class QueryCursorEventArgs(MouseEventArgs):
    """
    Provides data for the System.Windows.Input.Mouse.QueryCursor event.
    
    QueryCursorEventArgs(mouse: MouseDevice, timestamp: int)
    QueryCursorEventArgs(mouse: MouseDevice, timestamp: int, stylusDevice: StylusDevice)
    """
    @staticmethod # known case of __new__
    def __new__(self, mouse, timestamp, stylusDevice=None):
        """
        __new__(cls: type, mouse: MouseDevice, timestamp: int)
        __new__(cls: type, mouse: MouseDevice, timestamp: int, stylusDevice: StylusDevice)
        """
        pass

    Cursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the cursor associated with this event.

Get: Cursor(self: QueryCursorEventArgs) -> Cursor

Set: Cursor(self: QueryCursorEventArgs) = value
"""



class QueryCursorEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Windows.UIElement.QueryCursor and System.Windows.ContentElement.QueryCursor events, as well as the System.Windows.Input.Mouse.QueryCursor attached event.
    
    QueryCursorEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: QueryCursorEventHandler, sender: object, e: QueryCursorEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null, if the method represented by the current delegate does not require arguments.
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: QueryCursorEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: QueryCursorEventHandler, sender: object, e: QueryCursorEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation list.
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


class RestoreFocusMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies how Windows Presentation Foundation (WPF) restores focus to the window.
    
    enum RestoreFocusMode, values: Auto (0), None (1)
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

    Auto = None
    None = None
    value__ = None


class RoutedCommand(object, ICommand):
    """
    Defines a command that implements System.Windows.Input.ICommand and is routed through the element tree.
    
    RoutedCommand()
    RoutedCommand(name: str, ownerType: Type)
    RoutedCommand(name: str, ownerType: Type, inputGestures: InputGestureCollection)
    """
    def CanExecute(self, parameter, target):
        """
        CanExecute(self: RoutedCommand, parameter: object, target: IInputElement) -> bool
        
            Determines whether this System.Windows.Input.RoutedCommand can execute in its current state.
        
            parameter: A user defined data type.
            target: The command target.
            Returns: true if the command can execute on the current command target; otherwise, false.
        """
        pass

    def Execute(self, parameter, target):
        """
        Execute(self: RoutedCommand, parameter: object, target: IInputElement)
            Executes the System.Windows.Input.RoutedCommand on the current command target.
        
            parameter: User defined parameter to be passed to the handler.
            target: Element at which to begin looking for command handlers.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name=None, ownerType=None, inputGestures=None):
        """
        __new__(cls: type)
        __new__(cls: type, name: str, ownerType: Type)
        __new__(cls: type, name: str, ownerType: Type, inputGestures: InputGestureCollection)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    InputGestures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of System.Windows.Input.InputGesture objects that are associated with this command.

Get: InputGestures(self: RoutedCommand) -> InputGestureCollection

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the command.

Get: Name(self: RoutedCommand) -> str

"""

    OwnerType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type that is registered with the command.

Get: OwnerType(self: RoutedCommand) -> Type

"""


    CanExecuteChanged = None


class RoutedUICommand(RoutedCommand, ICommand):
    """
    Defines an System.Windows.Input.ICommand that is routed through the element tree and contains a text property.
    
    RoutedUICommand()
    RoutedUICommand(text: str, name: str, ownerType: Type)
    RoutedUICommand(text: str, name: str, ownerType: Type, inputGestures: InputGestureCollection)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, text=None, name=None, ownerType=None, inputGestures=None):
        """
        __new__(cls: type)
        __new__(cls: type, text: str, name: str, ownerType: Type)
        __new__(cls: type, text: str, name: str, ownerType: Type, inputGestures: InputGestureCollection)
        """
        pass

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the text that describes this command.

Get: Text(self: RoutedUICommand) -> str

Set: Text(self: RoutedUICommand) = value
"""



class SpeechMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the mode of interpretation for speech input.
    
    enum SpeechMode, values: Command (1), Dictation (0), Indeterminate (2)
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

    Command = None
    Dictation = None
    Indeterminate = None
    value__ = None


class StagingAreaInputItem(object):
    """ Encapsulates an input event when it is being processed by the input manager. """
    def GetData(self, key):
        """
        GetData(self: StagingAreaInputItem, key: object) -> object
        
            Gets the input data associated with the specified key.
        
            key: An arbitrary key for the data. This cannot be null.
            Returns: The data for this key, or null.
        """
        pass

    def SetData(self, key, value):
        """
        SetData(self: StagingAreaInputItem, key: object, value: object)
            Creates a dictionary entry by using the specified key and the specified data.
        
            key: An arbitrary key for the data. This cannot be null.
            value: The data to set for this key. This can be null.
        """
        pass

    Input = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the input event data associated with this System.Windows.Input.StagingAreaInputItem object

Get: Input(self: StagingAreaInputItem) -> InputEventArgs

"""



class Stylus(object):
    """ Provides access to general information about a tablet pen. """
    @staticmethod
    def AddGotStylusCaptureHandler(element, handler):
        """
        AddGotStylusCaptureHandler(element: DependencyObject, handler: StylusEventHandler)
            Adds a handler for the System.Windows.Input.Stylus.GotStylusCapture�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to add.
        """
        pass

    @staticmethod
    def AddLostStylusCaptureHandler(element, handler):
        """
        AddLostStylusCaptureHandler(element: DependencyObject, handler: StylusEventHandler)
            Adds a handler for the System.Windows.Input.Stylus.LostStylusCapture�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to add.
        """
        pass

    @staticmethod
    def AddPreviewStylusButtonDownHandler(element, handler):
        """
        AddPreviewStylusButtonDownHandler(element: DependencyObject, handler: StylusButtonEventHandler)
            Adds a handler for the System.Windows.Input.Stylus.PreviewStylusButtonDown�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to add.
        """
        pass

    @staticmethod
    def AddPreviewStylusButtonUpHandler(element, handler):
        """
        AddPreviewStylusButtonUpHandler(element: DependencyObject, handler: StylusButtonEventHandler)
            Adds a handler for the System.Windows.Input.Stylus.PreviewStylusButtonUp�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to add.
        """
        pass

    @staticmethod
    def AddPreviewStylusDownHandler(element, handler):
        """
        AddPreviewStylusDownHandler(element: DependencyObject, handler: StylusDownEventHandler)
            Adds a handler for the System.Windows.Input.Stylus.PreviewStylusDown�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to add.
        """
        pass

    @staticmethod
    def AddPreviewStylusInAirMoveHandler(element, handler):
        """
        AddPreviewStylusInAirMoveHandler(element: DependencyObject, handler: StylusEventHandler)
            Adds a handler for the System.Windows.Input.Stylus.PreviewStylusInAirMove�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to add.
        """
        pass

    @staticmethod
    def AddPreviewStylusInRangeHandler(element, handler):
        """
        AddPreviewStylusInRangeHandler(element: DependencyObject, handler: StylusEventHandler)
            Adds a handler for the System.Windows.Input.Stylus.PreviewStylusInRange�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to add.
        """
        pass

    @staticmethod
    def AddPreviewStylusMoveHandler(element, handler):
        """
        AddPreviewStylusMoveHandler(element: DependencyObject, handler: StylusEventHandler)
            Adds a handler for the System.Windows.Input.Stylus.PreviewStylusMove�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to add.
        """
        pass

    @staticmethod
    def AddPreviewStylusOutOfRangeHandler(element, handler):
        """
        AddPreviewStylusOutOfRangeHandler(element: DependencyObject, handler: StylusEventHandler)
            Adds a handler for the System.Windows.Input.Stylus.PreviewStylusOutOfRange�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to add.
        """
        pass

    @staticmethod
    def AddPreviewStylusSystemGestureHandler(element, handler):
        """
        AddPreviewStylusSystemGestureHandler(element: DependencyObject, handler: StylusSystemGestureEventHandler)
            Adds a handler for the System.Windows.Input.Stylus.PreviewStylusSystemGesture�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to add.
        """
        pass

    @staticmethod
    def AddPreviewStylusUpHandler(element, handler):
        """
        AddPreviewStylusUpHandler(element: DependencyObject, handler: StylusEventHandler)
            Adds a handler for the System.Windows.Input.Stylus.PreviewStylusUp�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to add.
        """
        pass

    @staticmethod
    def AddStylusButtonDownHandler(element, handler):
        """
        AddStylusButtonDownHandler(element: DependencyObject, handler: StylusButtonEventHandler)
            Adds a handler for the System.Windows.Input.Stylus.StylusButtonDown�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to add.
        """
        pass

    @staticmethod
    def AddStylusButtonUpHandler(element, handler):
        """
        AddStylusButtonUpHandler(element: DependencyObject, handler: StylusButtonEventHandler)
            Adds a handler for the System.Windows.Input.Stylus.StylusButtonUp�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to add.
        """
        pass

    @staticmethod
    def AddStylusDownHandler(element, handler):
        """
        AddStylusDownHandler(element: DependencyObject, handler: StylusDownEventHandler)
            Adds a handler for the System.Windows.Input.Stylus.StylusDown�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to add.
        """
        pass

    @staticmethod
    def AddStylusEnterHandler(element, handler):
        """
        AddStylusEnterHandler(element: DependencyObject, handler: StylusEventHandler)
            Adds a handler for the System.Windows.Input.Stylus.StylusEnter�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to add.
        """
        pass

    @staticmethod
    def AddStylusInAirMoveHandler(element, handler):
        """
        AddStylusInAirMoveHandler(element: DependencyObject, handler: StylusEventHandler)
            Adds a handler for the System.Windows.Input.Stylus.StylusInAirMove�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to add.
        """
        pass

    @staticmethod
    def AddStylusInRangeHandler(element, handler):
        """
        AddStylusInRangeHandler(element: DependencyObject, handler: StylusEventHandler)
            Adds a handler for the System.Windows.Input.Stylus.StylusInRange�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to add.
        """
        pass

    @staticmethod
    def AddStylusLeaveHandler(element, handler):
        """
        AddStylusLeaveHandler(element: DependencyObject, handler: StylusEventHandler)
            Adds a handler for the System.Windows.Input.Stylus.StylusLeave�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to add.
        """
        pass

    @staticmethod
    def AddStylusMoveHandler(element, handler):
        """
        AddStylusMoveHandler(element: DependencyObject, handler: StylusEventHandler)
            Adds a handler for the System.Windows.Input.Stylus.StylusMove�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to add.
        """
        pass

    @staticmethod
    def AddStylusOutOfRangeHandler(element, handler):
        """
        AddStylusOutOfRangeHandler(element: DependencyObject, handler: StylusEventHandler)
            Adds a handler for the System.Windows.Input.Stylus.StylusOutOfRange�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to add.
        """
        pass

    @staticmethod
    def AddStylusSystemGestureHandler(element, handler):
        """
        AddStylusSystemGestureHandler(element: DependencyObject, handler: StylusSystemGestureEventHandler)
            Adds a handler for the System.Windows.Input.Stylus.StylusSystemGesture�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to add.
        """
        pass

    @staticmethod
    def AddStylusUpHandler(element, handler):
        """
        AddStylusUpHandler(element: DependencyObject, handler: StylusEventHandler)
            Adds a handler for the System.Windows.Input.Stylus.StylusUp�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to add.
        """
        pass

    @staticmethod
    def Capture(element, captureMode=None):
        """
        Capture(element: IInputElement, captureMode: CaptureMode) -> bool
        
            Captures the stylus to the specified element.
        
            element: The element to capture the stylus to.
            captureMode: One of the System.Windows.Input.CaptureMode values.
            Returns: true if the stylus is captured to element; otherwise, false.
        Capture(element: IInputElement) -> bool
        
            Captures the stylus to the specified element.
        
            element: The element to capture the stylus to.
            Returns: true if the stylus is captured to element; otherwise, false.
        """
        pass

    @staticmethod
    def GetIsFlicksEnabled(element):
        """
        GetIsFlicksEnabled(element: DependencyObject) -> bool
        
            Gets the value of the System.Windows.Input.Stylus.IsFlicksEnabled�attached property on the specified element.
        
            element: A System.Windows.UIElement or System.Windows.ContentElement on which to determine whether flicks are enabled.
            Returns: true if the specified element has flicks enabled; otherwise, false.
        """
        pass

    @staticmethod
    def GetIsPressAndHoldEnabled(element):
        """
        GetIsPressAndHoldEnabled(element: DependencyObject) -> bool
        
            Gets the value of the System.Windows.Input.Stylus.IsPressAndHoldEnabled�attached property on the specified element.
        
            element: A System.Windows.UIElement or System.Windows.ContentElement on which to determine whether press and hold is enabled.
            Returns: true if the specified element has press and hold enabled; otherwise, false;
        """
        pass

    @staticmethod
    def GetIsTapFeedbackEnabled(element):
        """
        GetIsTapFeedbackEnabled(element: DependencyObject) -> bool
        
            Gets the value of the System.Windows.Input.Stylus.IsTapFeedbackEnabled�attached property on the specified element.
        
            element: A System.Windows.UIElement or System.Windows.ContentElement on which to determine whether tap feedback enabled.
            Returns: true if the specified element has tap feedback enabled; otherwise, false.
        """
        pass

    @staticmethod
    def GetIsTouchFeedbackEnabled(element):
        """
        GetIsTouchFeedbackEnabled(element: DependencyObject) -> bool
        
            Gets the value of the System.Windows.Input.Stylus.IsTouchFeedbackEnabled�attached property on the specified element.
        
            element: A System.Windows.UIElement or System.Windows.ContentElement on which to determine whether touch input feedback enabled.
            Returns: true if touch input feedback is enabled, otherwise false.
        """
        pass

    @staticmethod
    def RemoveGotStylusCaptureHandler(element, handler):
        """
        RemoveGotStylusCaptureHandler(element: DependencyObject, handler: StylusEventHandler)
            Removes a handler for the System.Windows.Input.Stylus.GotStylusCapture�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to remove.
        """
        pass

    @staticmethod
    def RemoveLostStylusCaptureHandler(element, handler):
        """
        RemoveLostStylusCaptureHandler(element: DependencyObject, handler: StylusEventHandler)
            Removes a handler for the System.Windows.Input.Stylus.LostStylusCapture�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to remove.
        """
        pass

    @staticmethod
    def RemovePreviewStylusButtonDownHandler(element, handler):
        """
        RemovePreviewStylusButtonDownHandler(element: DependencyObject, handler: StylusButtonEventHandler)
            Removes a handler for the System.Windows.Input.Stylus.PreviewStylusButtonDown�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to remove.
        """
        pass

    @staticmethod
    def RemovePreviewStylusButtonUpHandler(element, handler):
        """
        RemovePreviewStylusButtonUpHandler(element: DependencyObject, handler: StylusButtonEventHandler)
            Removes a handler for the System.Windows.Input.Stylus.PreviewStylusButtonUp�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to remove.
        """
        pass

    @staticmethod
    def RemovePreviewStylusDownHandler(element, handler):
        """
        RemovePreviewStylusDownHandler(element: DependencyObject, handler: StylusDownEventHandler)
            Removes a handler for the System.Windows.Input.Stylus.PreviewStylusDown�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to remove.
        """
        pass

    @staticmethod
    def RemovePreviewStylusInAirMoveHandler(element, handler):
        """
        RemovePreviewStylusInAirMoveHandler(element: DependencyObject, handler: StylusEventHandler)
            Removes a handler for the System.Windows.Input.Stylus.PreviewStylusInAirMove�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to remove.
        """
        pass

    @staticmethod
    def RemovePreviewStylusInRangeHandler(element, handler):
        """
        RemovePreviewStylusInRangeHandler(element: DependencyObject, handler: StylusEventHandler)
            Removes a handler for the System.Windows.Input.Stylus.PreviewStylusInRange�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to remove.
        """
        pass

    @staticmethod
    def RemovePreviewStylusMoveHandler(element, handler):
        """
        RemovePreviewStylusMoveHandler(element: DependencyObject, handler: StylusEventHandler)
            Removes a handler for the System.Windows.Input.Stylus.PreviewStylusMove�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to remove.
        """
        pass

    @staticmethod
    def RemovePreviewStylusOutOfRangeHandler(element, handler):
        """
        RemovePreviewStylusOutOfRangeHandler(element: DependencyObject, handler: StylusEventHandler)
            Removes a handler for the System.Windows.Input.Stylus.PreviewStylusOutOfRange�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to remove.
        """
        pass

    @staticmethod
    def RemovePreviewStylusSystemGestureHandler(element, handler):
        """
        RemovePreviewStylusSystemGestureHandler(element: DependencyObject, handler: StylusSystemGestureEventHandler)
            Removes a handler for the System.Windows.Input.Stylus.PreviewStylusSystemGesture�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to remove.
        """
        pass

    @staticmethod
    def RemovePreviewStylusUpHandler(element, handler):
        """
        RemovePreviewStylusUpHandler(element: DependencyObject, handler: StylusEventHandler)
            Removes a handler for the System.Windows.Input.Stylus.PreviewStylusUp�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to remove.
        """
        pass

    @staticmethod
    def RemoveStylusButtonDownHandler(element, handler):
        """
        RemoveStylusButtonDownHandler(element: DependencyObject, handler: StylusButtonEventHandler)
            Removes a handler for the System.Windows.Input.Stylus.StylusButtonDown�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to remove.
        """
        pass

    @staticmethod
    def RemoveStylusButtonUpHandler(element, handler):
        """
        RemoveStylusButtonUpHandler(element: DependencyObject, handler: StylusButtonEventHandler)
            Removes a handler for the System.Windows.Input.Stylus.StylusButtonUp�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to remove.
        """
        pass

    @staticmethod
    def RemoveStylusDownHandler(element, handler):
        """
        RemoveStylusDownHandler(element: DependencyObject, handler: StylusDownEventHandler)
            Removes a handler for the System.Windows.Input.Stylus.StylusDown�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to remove.
        """
        pass

    @staticmethod
    def RemoveStylusEnterHandler(element, handler):
        """
        RemoveStylusEnterHandler(element: DependencyObject, handler: StylusEventHandler)
            Removes a handler for the System.Windows.Input.Stylus.StylusEnter�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to remove.
        """
        pass

    @staticmethod
    def RemoveStylusInAirMoveHandler(element, handler):
        """
        RemoveStylusInAirMoveHandler(element: DependencyObject, handler: StylusEventHandler)
            Removes a handler for the System.Windows.Input.Stylus.StylusInAirMove�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to remove.
        """
        pass

    @staticmethod
    def RemoveStylusInRangeHandler(element, handler):
        """
        RemoveStylusInRangeHandler(element: DependencyObject, handler: StylusEventHandler)
            Removes a handler for the System.Windows.Input.Stylus.StylusInRange�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to remove.
        """
        pass

    @staticmethod
    def RemoveStylusLeaveHandler(element, handler):
        """
        RemoveStylusLeaveHandler(element: DependencyObject, handler: StylusEventHandler)
            Removes a handler for the System.Windows.Input.Stylus.StylusLeave�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to remove.
        """
        pass

    @staticmethod
    def RemoveStylusMoveHandler(element, handler):
        """
        RemoveStylusMoveHandler(element: DependencyObject, handler: StylusEventHandler)
            Removes a handler for the System.Windows.Input.Stylus.StylusMove�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to remove.
        """
        pass

    @staticmethod
    def RemoveStylusOutOfRangeHandler(element, handler):
        """
        RemoveStylusOutOfRangeHandler(element: DependencyObject, handler: StylusEventHandler)
            Removes a handler for the System.Windows.Input.Stylus.StylusOutOfRange�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to remove.
        """
        pass

    @staticmethod
    def RemoveStylusSystemGestureHandler(element, handler):
        """
        RemoveStylusSystemGestureHandler(element: DependencyObject, handler: StylusSystemGestureEventHandler)
            Removes a handler for the System.Windows.Input.Stylus.StylusSystemGesture�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to remove.
        """
        pass

    @staticmethod
    def RemoveStylusUpHandler(element, handler):
        """
        RemoveStylusUpHandler(element: DependencyObject, handler: StylusEventHandler)
            Removes a handler for the System.Windows.Input.Stylus.StylusUp�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to remove.
        """
        pass

    @staticmethod
    def SetIsFlicksEnabled(element, enabled):
        """
        SetIsFlicksEnabled(element: DependencyObject, enabled: bool)
            Gets the value of the System.Windows.Input.Stylus.IsFlicksEnabled�attached property on the specified element.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement on which to enable flicks.
            enabled: true to enable flicks; false to disable flicks.
        """
        pass

    @staticmethod
    def SetIsPressAndHoldEnabled(element, enabled):
        """
        SetIsPressAndHoldEnabled(element: DependencyObject, enabled: bool)
            Sets the value of the System.Windows.Input.Stylus.IsPressAndHoldEnabled�attached property on the specified element.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement on which to enable press and hold.
            enabled: true to enable press and hold; false to disable press and hold.
        """
        pass

    @staticmethod
    def SetIsTapFeedbackEnabled(element, enabled):
        """
        SetIsTapFeedbackEnabled(element: DependencyObject, enabled: bool)
            Sets the value of the System.Windows.Input.Stylus.IsTapFeedbackEnabled�attached property on the specified element.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement on which to enable tap feedback.
            enabled: true to enable tap feedback; false to disable tap feedback.
        """
        pass

    @staticmethod
    def SetIsTouchFeedbackEnabled(element, enabled):
        """
        SetIsTouchFeedbackEnabled(element: DependencyObject, enabled: bool)
            Sets the value of the System.Windows.Input.Stylus.IsTouchFeedbackEnabled�attached property on the specified element.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement on which to enable tap feedback.
            enabled: true to enable touch input feedback; false to disable touch input feedback.
        """
        pass

    @staticmethod
    def Synchronize():
        """
        Synchronize()
            Synchronizes the cursor and the user interface.
        """
        pass

    Captured = None
    CurrentStylusDevice = None
    DirectlyOver = None
    GotStylusCaptureEvent = None
    IsFlicksEnabledProperty = None
    IsPressAndHoldEnabledProperty = None
    IsTapFeedbackEnabledProperty = None
    IsTouchFeedbackEnabledProperty = None
    LostStylusCaptureEvent = None
    PreviewStylusButtonDownEvent = None
    PreviewStylusButtonUpEvent = None
    PreviewStylusDownEvent = None
    PreviewStylusInAirMoveEvent = None
    PreviewStylusInRangeEvent = None
    PreviewStylusMoveEvent = None
    PreviewStylusOutOfRangeEvent = None
    PreviewStylusSystemGestureEvent = None
    PreviewStylusUpEvent = None
    StylusButtonDownEvent = None
    StylusButtonUpEvent = None
    StylusDownEvent = None
    StylusEnterEvent = None
    StylusInAirMoveEvent = None
    StylusInRangeEvent = None
    StylusLeaveEvent = None
    StylusMoveEvent = None
    StylusOutOfRangeEvent = None
    StylusSystemGestureEvent = None
    StylusUpEvent = None
    __all__ = [
        'AddGotStylusCaptureHandler',
        'AddLostStylusCaptureHandler',
        'AddPreviewStylusButtonDownHandler',
        'AddPreviewStylusButtonUpHandler',
        'AddPreviewStylusDownHandler',
        'AddPreviewStylusInAirMoveHandler',
        'AddPreviewStylusInRangeHandler',
        'AddPreviewStylusMoveHandler',
        'AddPreviewStylusOutOfRangeHandler',
        'AddPreviewStylusSystemGestureHandler',
        'AddPreviewStylusUpHandler',
        'AddStylusButtonDownHandler',
        'AddStylusButtonUpHandler',
        'AddStylusDownHandler',
        'AddStylusEnterHandler',
        'AddStylusInAirMoveHandler',
        'AddStylusInRangeHandler',
        'AddStylusLeaveHandler',
        'AddStylusMoveHandler',
        'AddStylusOutOfRangeHandler',
        'AddStylusSystemGestureHandler',
        'AddStylusUpHandler',
        'Capture',
        'GetIsFlicksEnabled',
        'GetIsPressAndHoldEnabled',
        'GetIsTapFeedbackEnabled',
        'GetIsTouchFeedbackEnabled',
        'GotStylusCaptureEvent',
        'IsFlicksEnabledProperty',
        'IsPressAndHoldEnabledProperty',
        'IsTapFeedbackEnabledProperty',
        'IsTouchFeedbackEnabledProperty',
        'LostStylusCaptureEvent',
        'PreviewStylusButtonDownEvent',
        'PreviewStylusButtonUpEvent',
        'PreviewStylusDownEvent',
        'PreviewStylusInAirMoveEvent',
        'PreviewStylusInRangeEvent',
        'PreviewStylusMoveEvent',
        'PreviewStylusOutOfRangeEvent',
        'PreviewStylusSystemGestureEvent',
        'PreviewStylusUpEvent',
        'RemoveGotStylusCaptureHandler',
        'RemoveLostStylusCaptureHandler',
        'RemovePreviewStylusButtonDownHandler',
        'RemovePreviewStylusButtonUpHandler',
        'RemovePreviewStylusDownHandler',
        'RemovePreviewStylusInAirMoveHandler',
        'RemovePreviewStylusInRangeHandler',
        'RemovePreviewStylusMoveHandler',
        'RemovePreviewStylusOutOfRangeHandler',
        'RemovePreviewStylusSystemGestureHandler',
        'RemovePreviewStylusUpHandler',
        'RemoveStylusButtonDownHandler',
        'RemoveStylusButtonUpHandler',
        'RemoveStylusDownHandler',
        'RemoveStylusEnterHandler',
        'RemoveStylusInAirMoveHandler',
        'RemoveStylusInRangeHandler',
        'RemoveStylusLeaveHandler',
        'RemoveStylusMoveHandler',
        'RemoveStylusOutOfRangeHandler',
        'RemoveStylusSystemGestureHandler',
        'RemoveStylusUpHandler',
        'SetIsFlicksEnabled',
        'SetIsPressAndHoldEnabled',
        'SetIsTapFeedbackEnabled',
        'SetIsTouchFeedbackEnabled',
        'StylusButtonDownEvent',
        'StylusButtonUpEvent',
        'StylusDownEvent',
        'StylusEnterEvent',
        'StylusInAirMoveEvent',
        'StylusInRangeEvent',
        'StylusLeaveEvent',
        'StylusMoveEvent',
        'StylusOutOfRangeEvent',
        'StylusSystemGestureEvent',
        'StylusUpEvent',
        'Synchronize',
    ]


class StylusButton(object):
    """ Represents a button on a stylus. """
    def ToString(self):
        """
        ToString(self: StylusButton) -> str
        
            Creates a string representation of the System.Windows.Input.StylusButton.
        """
        pass

    Guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Guid that represents the stylus button.

Get: Guid(self: StylusButton) -> Guid

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the stylus button.

Get: Name(self: StylusButton) -> str

"""

    StylusButtonState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the state of the stylus button.

Get: StylusButtonState(self: StylusButton) -> StylusButtonState

"""

    StylusDevice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the stylus that this button belongs to.

Get: StylusDevice(self: StylusButton) -> StylusDevice

"""



class StylusButtonCollection(ReadOnlyCollection[StylusButton], IList[StylusButton], ICollection[StylusButton], IEnumerable[StylusButton], IEnumerable, IList, ICollection, IReadOnlyList[StylusButton], IReadOnlyCollection[StylusButton]):
    """ Contains a collection of System.Windows.Input.StylusButton objects. """
    def GetStylusButtonByGuid(self, guid):
        """
        GetStylusButtonByGuid(self: StylusButtonCollection, guid: Guid) -> StylusButton
        
            Gets the System.Windows.Input.StylusButton that the specified GUID identifies.
        
            guid: The System.Guid that specifies the desired System.Windows.Input.StylusButton.
            Returns: The System.Windows.Input.StylusButton of the specified GUID.
        """
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

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the System.Collections.Generic.IList that the System.Collections.ObjectModel.ReadOnlyCollection wraps.

"""



class StylusEventArgs(InputEventArgs):
    """
    Provides data for several of the events that are associated with the System.Windows.Input.Stylus class.
    
    StylusEventArgs(stylus: StylusDevice, timestamp: int)
    """
    def GetPosition(self, relativeTo):
        """
        GetPosition(self: StylusEventArgs, relativeTo: IInputElement) -> Point
        
            Gets the position of the stylus.
        
            relativeTo: The System.Windows.IInputElement that the (x,y) coordinates are mapped to.
            Returns: A System.Windows.Point that represents the position of the stylus, based on the coordinates of relativeTo.
        """
        pass

    def GetStylusPoints(self, relativeTo, subsetToReformatTo=None):
        """
        GetStylusPoints(self: StylusEventArgs, relativeTo: IInputElement, subsetToReformatTo: StylusPointDescription) -> StylusPointCollection
        
            Returns a System.Windows.Input.StylusPointCollection that uses the specified System.Windows.Input.StylusPointDescription and contains System.Windows.Input.StylusPoint objects relating to the specified 
             input element.
        
        
            relativeTo: The System.Windows.IInputElement to which the (x,y) coordinates in the System.Windows.Input.StylusPointCollection are mapped.
            subsetToReformatTo: The System.Windows.Input.StylusPointDescription to be used by the System.Windows.Input.StylusPointCollection.
            Returns: A System.Windows.Input.StylusPointCollection that contains System.Windows.Input.StylusPoint objects collected during an event.
        GetStylusPoints(self: StylusEventArgs, relativeTo: IInputElement) -> StylusPointCollection
        
            Returns a System.Windows.Input.StylusPointCollection that contains System.Windows.Input.StylusPoint objects relative to the specified input element.
        
            relativeTo: The System.Windows.IInputElement to which the (x,y) coordinates in the System.Windows.Input.StylusPointCollection are mapped.
            Returns: A System.Windows.Input.StylusPointCollection that contains System.Windows.Input.StylusPoint objects collected in the event.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, stylus, timestamp):
        """ __new__(cls: type, stylus: StylusDevice, timestamp: int) """
        pass

    InAir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the stylus is in proximity to, but not touching, the digitizer.

Get: InAir(self: StylusEventArgs) -> bool

"""

    Inverted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the stylus in inverted.

Get: Inverted(self: StylusEventArgs) -> bool

"""

    StylusDevice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Input.StylusDevice that represents the stylus.

Get: StylusDevice(self: StylusEventArgs) -> StylusDevice

"""



class StylusButtonEventArgs(StylusEventArgs):
    """
    Provides data for the System.Windows.UIElement.StylusButtonDown and System.Windows.UIElement.StylusButtonUp events.
    
    StylusButtonEventArgs(stylusDevice: StylusDevice, timestamp: int, button: StylusButton)
    """
    @staticmethod # known case of __new__
    def __new__(self, stylusDevice, timestamp, button):
        """ __new__(cls: type, stylusDevice: StylusDevice, timestamp: int, button: StylusButton) """
        pass

    StylusButton = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Input.StylusButton that raises this event.

Get: StylusButton(self: StylusButtonEventArgs) -> StylusButton

"""



class StylusButtonEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that handles either the System.Windows.UIElement.StylusButtonDown event or the System.Windows.UIElement.StylusButtonUp event of a System.Windows.UIElement.
    
    StylusButtonEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: StylusButtonEventHandler, sender: object, e: StylusButtonEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null, if the method represented by the current delegate does not require arguments.
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: StylusButtonEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: StylusButtonEventHandler, sender: object, e: StylusButtonEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation list.
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


class StylusButtonState(Enum, IComparable, IFormattable, IConvertible):
    """
    Represents the state of a System.Windows.Input.StylusButton.
    
    enum StylusButtonState, values: Down (1), Up (0)
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

    Down = None
    Up = None
    value__ = None


class StylusDevice(InputDevice):
    """ Represents a tablet pen used with a Tablet PC. """
    def Capture(self, element, captureMode=None):
        """
        Capture(self: StylusDevice, element: IInputElement) -> bool
        
            Binds input from the stylus to the specified element.
        
            element: The element to which the stylus is bound.
            Returns: true if the input element is captured successfully; otherwise, false. The default is false.
        Capture(self: StylusDevice, element: IInputElement, captureMode: CaptureMode) -> bool
        
            Binds the stylus to the specified element.
        
            captureMode: One of the System.Windows.Input.CaptureMode values.
            Returns: true if the input element is captured successfully; otherwise, false. The default is false.
        """
        pass

    def GetPosition(self, relativeTo):
        """
        GetPosition(self: StylusDevice, relativeTo: IInputElement) -> Point
        
            Gets the position of the stylus.
        
            relativeTo: The System.Windows.IInputElement to which the (x,y) coordinates are mapped.
            Returns: A System.Windows.Point that represents the position of the stylus, in relation to relativeTo.
        """
        pass

    def GetStylusPoints(self, relativeTo, subsetToReformatTo=None):
        """
        GetStylusPoints(self: StylusDevice, relativeTo: IInputElement, subsetToReformatTo: StylusPointDescription) -> StylusPointCollection
        
            Returns a System.Windows.Input.StylusPointCollection that contains System.Windows.Input.StylusPoint objects collected from the stylus. Uses the specified System.Windows.Input.StylusPointDescription.
        
            relativeTo: The System.Windows.IInputElement to which the (x y) coordinates in the System.Windows.Input.StylusPointCollection are mapped.
            subsetToReformatTo: The System.Windows.Input.StylusPointDescription to be used by the System.Windows.Input.StylusPointCollection.
            Returns: A System.Windows.Input.StylusPointCollection that contains System.Windows.Input.StylusPoint objects collected from the stylus.
        GetStylusPoints(self: StylusDevice, relativeTo: IInputElement) -> StylusPointCollection
        
            Returns a System.Windows.Input.StylusPointCollection that contains System.Windows.Input.StylusPoint objects collected from the stylus.
        
            relativeTo: The System.Windows.IInputElement to which the (x,y) coordinates in the System.Windows.Input.StylusPointCollection are mapped.
            Returns: A System.Windows.Input.StylusPointCollection that contains System.Windows.Input.StylusPoint objects that the stylus collected.
        """
        pass

    def Synchronize(self):
        """
        Synchronize(self: StylusDevice)
            Synchronizes the cursor and the user interface.
        """
        pass

    def ToString(self):
        """
        ToString(self: StylusDevice) -> str
        
            Returns the name of the stylus device.
            Returns: The name of the System.Windows.Input.StylusDevice.
        """
        pass

    ActiveSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.PresentationSource that reports current input for the stylus.

Get: ActiveSource(self: StylusDevice) -> PresentationSource

"""

    Captured = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the element that captured the stylus.

Get: Captured(self: StylusDevice) -> IInputElement

"""

    DirectlyOver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.IInputElement that the pointer is positioned over.

Get: DirectlyOver(self: StylusDevice) -> IInputElement

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the identifier for the stylus device.

Get: Id(self: StylusDevice) -> int

"""

    InAir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether the tablet pen is positioned above, yet not in contact with, the digitizer.

Get: InAir(self: StylusDevice) -> bool

"""

    InRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the tablet pen is in range of the digitizer.

Get: InRange(self: StylusDevice) -> bool

"""

    Inverted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the secondary tip of the stylus is in use.

Get: Inverted(self: StylusDevice) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: StylusDevice) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the stylus.

Get: Name(self: StylusDevice) -> str

"""

    StylusButtons = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the stylus buttons on the stylus.

Get: StylusButtons(self: StylusDevice) -> StylusButtonCollection

"""

    TabletDevice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Input.TabletDevice representing the digitizer associated with the current System.Windows.Input.StylusDevice.

Get: TabletDevice(self: StylusDevice) -> TabletDevice

"""

    Target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the element that receives input.

Get: Target(self: StylusDevice) -> IInputElement

"""



class StylusDeviceCollection(ReadOnlyCollection[StylusDevice], IList[StylusDevice], ICollection[StylusDevice], IEnumerable[StylusDevice], IEnumerable, IList, ICollection, IReadOnlyList[StylusDevice], IReadOnlyCollection[StylusDevice]):
    """ Contains the System.Windows.Input.StylusDevice objects that represent a Tablet PC's stylus devices. """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the System.Collections.Generic.IList that the System.Collections.ObjectModel.ReadOnlyCollection wraps.

"""



class StylusDownEventArgs(StylusEventArgs):
    """
    Provides data for the System.Windows.UIElement.StylusDown event.
    
    StylusDownEventArgs(stylusDevice: StylusDevice, timestamp: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, stylusDevice, timestamp):
        """ __new__(cls: type, stylusDevice: StylusDevice, timestamp: int) """
        pass

    TapCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of times the tablet pen was tapped.

Get: TapCount(self: StylusDownEventArgs) -> int

"""



class StylusDownEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that handles the System.Windows.Input.Stylus.StylusDown event, as well as several variations, including the corresponding Preview event. Also re-exposes the event in the base element classes.
    
    StylusDownEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: StylusDownEventHandler, sender: object, e: StylusDownEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null, if the method represented by the current delegate does not require arguments.
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: StylusDownEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: StylusDownEventHandler, sender: object, e: StylusDownEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation list.
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


class StylusEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that handles a stylus event for a class that the implements the System.Windows.IInputElement interface.
    
    StylusEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: StylusEventHandler, sender: object, e: StylusEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null, if the method represented by the current delegate does not require arguments.
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: StylusEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: StylusEventHandler, sender: object, e: StylusEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation list.
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


class StylusPoint(object, IEquatable[StylusPoint]):
    """
    Represents a single data point collected from the digitizer and stylus.
    
    StylusPoint(x: float, y: float)
    StylusPoint(x: float, y: float, pressureFactor: Single)
    StylusPoint(x: float, y: float, pressureFactor: Single, stylusPointDescription: StylusPointDescription, additionalValues: Array[int])
    """
    @staticmethod
    def Equals(*__args):
        """
        Equals(self: StylusPoint, value: StylusPoint) -> bool
        
            Returns a Boolean value that indicates whether the specified System.Windows.Input.StylusPoint is equal to the current System.Windows.Input.StylusPoint.
        
            value: The System.Windows.Input.StylusPoint to compare to the current System.Windows.Input.StylusPoint.
            Returns: true if the System.Windows.Input.StylusPoint objects are equal; otherwise, false.
        Equals(self: StylusPoint, o: object) -> bool
        
            Returns a value indicating whether the specified object is equal to the System.Windows.Input.StylusPoint.
        
            o: The System.Windows.Input.StylusPoint to compare to the current System.Windows.Input.StylusPoint.
            Returns: true if the objects are equal; otherwise, false.
        Equals(stylusPoint1: StylusPoint, stylusPoint2: StylusPoint) -> bool
        
            Returns a Boolean value that indicates whether the two specified System.Windows.Input.StylusPoint objects are equal.
        
            stylusPoint1: The first System.Windows.Input.StylusPoint to compare.
            stylusPoint2: The second System.Windows.Input.StylusPoint to compare.
            Returns: true if the System.Windows.Input.StylusPoint objects are equal; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: StylusPoint) -> int """
        pass

    def GetPropertyValue(self, stylusPointProperty):
        """
        GetPropertyValue(self: StylusPoint, stylusPointProperty: StylusPointProperty) -> int
        
            Returns the value of the specified property.
        
            stylusPointProperty: The System.Windows.Input.StylusPointProperty that specifies which property value to get.
            Returns: The value of the specified System.Windows.Input.StylusPointProperty.
        """
        pass

    def HasProperty(self, stylusPointProperty):
        """
        HasProperty(self: StylusPoint, stylusPointProperty: StylusPointProperty) -> bool
        
            Returns whether the current System.Windows.Input.StylusPoint contains the specified property.
        
            stylusPointProperty: The System.Windows.Input.StylusPointProperty to check for in the System.Windows.Input.StylusPoint.
            Returns: true if the specified System.Windows.Input.StylusPointProperty is in the current System.Windows.Input.StylusPoint; otherwise, false.
        """
        pass

    def SetPropertyValue(self, stylusPointProperty, value):
        """
        SetPropertyValue(self: StylusPoint, stylusPointProperty: StylusPointProperty, value: int)
            Sets the specified property to the specified value.
        
            stylusPointProperty: The System.Windows.Input.StylusPointProperty that specifies which property value to set.
            value: The value of the property.
        """
        pass

    def ToPoint(self):
        """
        ToPoint(self: StylusPoint) -> Point
        
            Converts a System.Windows.Input.StylusPoint to a System.Windows.Point.
            Returns: A System.Windows.Point structure.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, x, y, pressureFactor=None, stylusPointDescription=None, additionalValues=None):
        """
        __new__[StylusPoint]() -> StylusPoint
        
        __new__(cls: type, x: float, y: float)
        __new__(cls: type, x: float, y: float, pressureFactor: Single)
        __new__(cls: type, x: float, y: float, pressureFactor: Single, stylusPointDescription: StylusPointDescription, additionalValues: Array[int])
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Input.StylusPointDescription that specifies the properties stored in the System.Windows.Input.StylusPoint.

Get: Description(self: StylusPoint) -> StylusPointDescription

"""

    PressureFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value between 0 and 1 that reflects the amount of pressure the stylus applies to the digitizer's surface when the System.Windows.Input.StylusPoint is created.

Get: PressureFactor(self: StylusPoint) -> Single

Set: PressureFactor(self: StylusPoint) = value
"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value for the x-coordinate of the System.Windows.Input.StylusPoint.

Get: X(self: StylusPoint) -> float

Set: X(self: StylusPoint) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the y-coordinate of the System.Windows.Input.StylusPoint.

Get: Y(self: StylusPoint) -> float

Set: Y(self: StylusPoint) = value
"""


    MaxXY = 81164736.283464298
    MinXY = -81164736.321259603


class StylusPointCollection(Collection[StylusPoint], IList[StylusPoint], ICollection[StylusPoint], IEnumerable[StylusPoint], IEnumerable, IList, ICollection, IReadOnlyList[StylusPoint], IReadOnlyCollection[StylusPoint]):
    """
    Contains a collection of System.Windows.Input.StylusPoint objects.
    
    StylusPointCollection()
    StylusPointCollection(initialCapacity: int)
    StylusPointCollection(stylusPointDescription: StylusPointDescription)
    StylusPointCollection(stylusPointDescription: StylusPointDescription, initialCapacity: int)
    StylusPointCollection(stylusPoints: IEnumerable[StylusPoint])
    StylusPointCollection(points: IEnumerable[Point])
    """
    def Add(self, *__args):
        """
        Add(self: StylusPointCollection, stylusPoints: StylusPointCollection)
            Adds the specified System.Windows.Input.StylusPointCollection to the current System.Windows.Input.StylusPointCollection.
        
            stylusPoints: The System.Windows.Input.StylusPointCollection to add to the current System.Windows.Input.StylusPointCollection.
        """
        pass

    def ClearItems(self, *args): #cannot find CLR method
        """
        ClearItems(self: StylusPointCollection)
            Removes all System.Windows.Input.StylusPoint objects from the System.Windows.Input.StylusPointCollection.
        """
        pass

    def Clone(self):
        """
        Clone(self: StylusPointCollection) -> StylusPointCollection
        
            Copies the System.Windows.Input.StylusPointCollection.
            Returns: A new System.Windows.Input.StylusPointCollection that contains copies of the System.Windows.Input.StylusPoint objects in the current System.Windows.Input.StylusPointCollection.
        """
        pass

    def InsertItem(self, *args): #cannot find CLR method
        """
        InsertItem(self: StylusPointCollection, index: int, stylusPoint: StylusPoint)
            Inserts the specified System.Windows.Input.StylusPoint into the System.Windows.Input.StylusPointCollection at the specified position.
        
            index: The position at which to insert the System.Windows.Input.StylusPoint.
            stylusPoint: The System.Windows.Input.StylusPoint to insert into the System.Windows.Input.StylusPointCollection.
        """
        pass

    def OnChanged(self, *args): #cannot find CLR method
        """
        OnChanged(self: StylusPointCollection, e: EventArgs)
            Raises the System.Windows.Input.StylusPointCollection.Changed event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def Reformat(self, subsetToReformatTo):
        """
        Reformat(self: StylusPointCollection, subsetToReformatTo: StylusPointDescription) -> StylusPointCollection
        
            Finds the intersection of the specified System.Windows.Input.StylusPointDescription and the System.Windows.Input.StylusPointCollection.Description property.
        
            subsetToReformatTo: A System.Windows.Input.StylusPointDescription to intersect with the System.Windows.Input.StylusPointDescription of the current System.Windows.Input.StylusPointCollection.
            Returns: A System.Windows.Input.StylusPointCollection that has a System.Windows.Input.StylusPointDescription that is a subset of the specified System.Windows.Input.StylusPointDescription and the 
             System.Windows.Input.StylusPointDescription that the current System.Windows.Input.StylusPointCollection uses.
        """
        pass

    def RemoveItem(self, *args): #cannot find CLR method
        """
        RemoveItem(self: StylusPointCollection, index: int)
            Removes the System.Windows.Input.StylusPoint at the specified position from the System.Windows.Input.StylusPointCollection.
        
            index: The position at which to remove the System.Windows.Input.StylusPoint.
        """
        pass

    def SetItem(self, *args): #cannot find CLR method
        """
        SetItem(self: StylusPointCollection, index: int, stylusPoint: StylusPoint)
            Sets the specified System.Windows.Input.StylusPoint at the specified position.
        
            index: The position at which to set the System.Windows.Input.StylusPoint.
            stylusPoint: The System.Windows.Input.StylusPoint to set at the specified position.
        """
        pass

    def ToHiMetricArray(self):
        """
        ToHiMetricArray(self: StylusPointCollection) -> Array[int]
        
            Converts the property values of the System.Windows.Input.StylusPoint objects into a 32-bit signed integer array.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, initialCapacity: int)
        __new__(cls: type, stylusPointDescription: StylusPointDescription)
        __new__(cls: type, stylusPointDescription: StylusPointDescription, initialCapacity: int)
        __new__(cls: type, stylusPoints: IEnumerable[StylusPoint])
        __new__(cls: type, points: IEnumerable[Point])
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Input.StylusPointDescription that is associated with the System.Windows.Input.StylusPoint objects in the System.Windows.Input.StylusPointCollection.

Get: Description(self: StylusPointCollection) -> StylusPointDescription

"""

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Collections.Generic.IList wrapper around the System.Collections.ObjectModel.Collection.

"""


    Changed = None


class StylusPointDescription(object):
    """
    Specifies the properties that are in a System.Windows.Input.StylusPoint.
    
    StylusPointDescription()
    StylusPointDescription(stylusPointPropertyInfos: IEnumerable[StylusPointPropertyInfo])
    """
    @staticmethod
    def AreCompatible(stylusPointDescription1, stylusPointDescription2):
        """
        AreCompatible(stylusPointDescription1: StylusPointDescription, stylusPointDescription2: StylusPointDescription) -> bool
        
            Returns a value that indicates whether the specified System.Windows.Input.StylusPointDescription objects are identical.
        
            stylusPointDescription1: The first System.Windows.Input.StylusPointDescription to check.
            stylusPointDescription2: The second System.Windows.Input.StylusPointDescription to check.
            Returns: true if the System.Windows.Input.StylusPointDescription objects are identical; otherwise, false.
        """
        pass

    @staticmethod
    def GetCommonDescription(stylusPointDescription, stylusPointDescriptionPreserveInfo):
        """
        GetCommonDescription(stylusPointDescription: StylusPointDescription, stylusPointDescriptionPreserveInfo: StylusPointDescription) -> StylusPointDescription
        
            Returns the intersection of the specified System.Windows.Input.StylusPointDescription objects.
        
            stylusPointDescriptionPreserveInfo: The second System.Windows.Input.StylusPointDescription to intersect.
            Returns: A System.Windows.Input.StylusPointDescription that contains the properties that are present if both of the specified System.Windows.Input.StylusPointDescription objects.
        """
        pass

    def GetPropertyInfo(self, stylusPointProperty):
        """
        GetPropertyInfo(self: StylusPointDescription, stylusPointProperty: StylusPointProperty) -> StylusPointPropertyInfo
        
            Gets the System.Windows.Input.StylusPointPropertyInfo for the specified property.
        
            stylusPointProperty: The System.Windows.Input.StylusPointProperty that specifies the property of the desired System.Windows.Input.StylusPointPropertyInfo.
            Returns: The System.Windows.Input.StylusPointPropertyInfo for the specified System.Windows.Input.StylusPointProperty.
        """
        pass

    def GetStylusPointProperties(self):
        """
        GetStylusPointProperties(self: StylusPointDescription) -> ReadOnlyCollection[StylusPointPropertyInfo]
        
            Gets all the properties of the System.Windows.Input.StylusPointDescription.
            Returns: A collection that contains all of the System.Windows.Input.StylusPointPropertyInfo objects in the System.Windows.Input.StylusPointDescription.
        """
        pass

    def HasProperty(self, stylusPointProperty):
        """
        HasProperty(self: StylusPointDescription, stylusPointProperty: StylusPointProperty) -> bool
        
            Returns a value that indicates whether the current System.Windows.Input.StylusPointDescription has the specified property.
        
            stylusPointProperty: The System.Windows.Input.StylusPointProperty to check for in the System.Windows.Input.StylusPointDescription.
            Returns: true if the System.Windows.Input.StylusPointDescription has the specified System.Windows.Input.StylusPointProperty; otherwise, false.
        """
        pass

    def IsSubsetOf(self, stylusPointDescriptionSuperset):
        """
        IsSubsetOf(self: StylusPointDescription, stylusPointDescriptionSuperset: StylusPointDescription) -> bool
        
            Returns a value that indicates whether the current System.Windows.Input.StylusPointDescription is a subset of the specified System.Windows.Input.StylusPointDescription.
        
            stylusPointDescriptionSuperset: The System.Windows.Input.StylusPointDescription against which to check whether the current System.Windows.Input.StylusPointDescription is a subset.
            Returns: true if the current System.Windows.Input.StylusPointDescription is a subset of the specified System.Windows.Input.StylusPointDescription; otherwise, false.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, stylusPointPropertyInfos=None):
        """
        __new__(cls: type)
        __new__(cls: type, stylusPointPropertyInfos: IEnumerable[StylusPointPropertyInfo])
        """
        pass

    PropertyCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of properties in the System.Windows.Input.StylusPointDescription.

Get: PropertyCount(self: StylusPointDescription) -> int

"""



class StylusPointProperties(object):
    """ Contains a System.Windows.Input.StylusPointProperty for each property that the WPF supports. """
    AltitudeOrientation = None
    AzimuthOrientation = None
    BarrelButton = None
    ButtonPressure = None
    Height = None
    NormalPressure = None
    PacketStatus = None
    PitchRotation = None
    RollRotation = None
    SecondaryTipButton = None
    SerialNumber = None
    SystemTouch = None
    TangentPressure = None
    TipButton = None
    TwistOrientation = None
    Width = None
    X = None
    XTiltOrientation = None
    Y = None
    YawRotation = None
    YTiltOrientation = None
    Z = None
    __all__ = [
        'AltitudeOrientation',
        'AzimuthOrientation',
        'BarrelButton',
        'ButtonPressure',
        'Height',
        'NormalPressure',
        'PacketStatus',
        'PitchRotation',
        'RollRotation',
        'SecondaryTipButton',
        'SerialNumber',
        'SystemTouch',
        'TangentPressure',
        'TipButton',
        'TwistOrientation',
        'Width',
        'X',
        'XTiltOrientation',
        'Y',
        'YawRotation',
        'YTiltOrientation',
        'Z',
    ]


class StylusPointProperty(object):
    """
    Represents a property stored in a System.Windows.Input.StylusPoint.
    
    StylusPointProperty(identifier: Guid, isButton: bool)
    """
    def ToString(self):
        """ ToString(self: StylusPointProperty) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, identifier, isButton):
        """
        __new__(cls: type, identifier: Guid, isButton: bool)
        __new__(cls: type, stylusPointProperty: StylusPointProperty)
        """
        pass

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the GUID for the current System.Windows.Input.StylusPointProperty.

Get: Id(self: StylusPointProperty) -> Guid

"""

    IsButton = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether the System.Windows.Input.StylusPointProperty represents a button on the stylus.

Get: IsButton(self: StylusPointProperty) -> bool

"""



class StylusPointPropertyInfo(StylusPointProperty):
    """
    Specifies the constraints of a property in a System.Windows.Input.StylusPoint.
    
    StylusPointPropertyInfo(stylusPointProperty: StylusPointProperty)
    StylusPointPropertyInfo(stylusPointProperty: StylusPointProperty, minimum: int, maximum: int, unit: StylusPointPropertyUnit, resolution: Single)
    """
    @staticmethod # known case of __new__
    def __new__(self, stylusPointProperty, minimum=None, maximum=None, unit=None, resolution=None):
        """
        __new__(cls: type, stylusPointProperty: StylusPointProperty)
        __new__(cls: type, stylusPointProperty: StylusPointProperty, minimum: int, maximum: int, unit: StylusPointPropertyUnit, resolution: Single)
        """
        pass

    Maximum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the maximum value accepted for the System.Windows.Input.StylusPoint property.

Get: Maximum(self: StylusPointPropertyInfo) -> int

"""

    Minimum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the minimum value accepted for the System.Windows.Input.StylusPoint property.

Get: Minimum(self: StylusPointPropertyInfo) -> int

"""

    Resolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the scale that converts a System.Windows.Input.StylusPoint property value into units.

Get: Resolution(self: StylusPointPropertyInfo) -> Single

"""

    Unit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of measurement that is used by System.Windows.Input.StylusPoint property.

Get: Unit(self: StylusPointPropertyInfo) -> StylusPointPropertyUnit

"""



class StylusPointPropertyUnit(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the unit of measurement for a System.Windows.Input.StylusPoint property.
    
    enum StylusPointPropertyUnit, values: Centimeters (2), Degrees (3), Grams (7), Inches (1), None (0), Pounds (6), Radians (4), Seconds (5)
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

    Centimeters = None
    Degrees = None
    Grams = None
    Inches = None
    None = None
    Pounds = None
    Radians = None
    Seconds = None
    value__ = None


class StylusSystemGestureEventArgs(StylusEventArgs):
    """
    Provides data for the System.Windows.UIElement.StylusSystemGesture event.
    
    StylusSystemGestureEventArgs(stylusDevice: StylusDevice, timestamp: int, systemGesture: SystemGesture)
    """
    @staticmethod # known case of __new__
    def __new__(self, stylusDevice, timestamp, systemGesture):
        """ __new__(cls: type, stylusDevice: StylusDevice, timestamp: int, systemGesture: SystemGesture) """
        pass

    SystemGesture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Input.SystemGesture that raises the event.

Get: SystemGesture(self: StylusSystemGestureEventArgs) -> SystemGesture

"""



class StylusSystemGestureEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that handles the System.Windows.UIElement.StylusSystemGesture event of a System.Windows.UIElement.
    
    StylusSystemGestureEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: StylusSystemGestureEventHandler, sender: object, e: StylusSystemGestureEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null, if the method represented by the current delegate does not require arguments.
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: StylusSystemGestureEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: StylusSystemGestureEventHandler, sender: object, e: StylusSystemGestureEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation list.
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


class SystemGesture(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines the available system gestures.
    
    enum SystemGesture, values: Drag (19), Flick (31), HoldEnter (21), HoldLeave (22), HoverEnter (23), HoverLeave (24), None (0), RightDrag (20), RightTap (18), Tap (16), TwoFingerTap (4352)
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

    Drag = None
    Flick = None
    HoldEnter = None
    HoldLeave = None
    HoverEnter = None
    HoverLeave = None
    None = None
    RightDrag = None
    RightTap = None
    Tap = None
    TwoFingerTap = None
    value__ = None


class Tablet(object):
    """ Provides access to static methods that return the tablet devices attached to the system. """
    CurrentTabletDevice = None
    TabletDevices = None
    __all__ = []


class TabletDevice(InputDevice):
    """ Represents the digitizer device of a Tablet PC. """
    def ToString(self):
        """
        ToString(self: TabletDevice) -> str
        
            Returns the name of the tablet device.
            Returns: A System.String that contains the name of the System.Windows.Input.TabletDevice.
        """
        pass

    ActiveSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.PresentationSource that reports current input for the tablet device.

Get: ActiveSource(self: TabletDevice) -> PresentationSource

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the unique identifier for the tablet device on the system.

Get: Id(self: TabletDevice) -> int

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the tablet device.

Get: Name(self: TabletDevice) -> str

"""

    ProductId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the product identifier for the tablet device.

Get: ProductId(self: TabletDevice) -> str

"""

    StylusDevices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Input.StylusDeviceCollection associated with the tablet device.

Get: StylusDevices(self: TabletDevice) -> StylusDeviceCollection

"""

    SupportedStylusPointProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of System.Windows.Input.StylusPointProperty objects that the System.Windows.Input.TabletDevice supports.

Get: SupportedStylusPointProperties(self: TabletDevice) -> ReadOnlyCollection[StylusPointProperty]

"""

    TabletHardwareCapabilities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Input.TabletHardwareCapabilities for the tablet device.

Get: TabletHardwareCapabilities(self: TabletDevice) -> TabletHardwareCapabilities

"""

    Target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.IInputElement that provides basic input processing for the tablet device.

Get: Target(self: TabletDevice) -> IInputElement

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Input.TabletDeviceType of the tablet device.

Get: Type(self: TabletDevice) -> TabletDeviceType

"""



class TabletDeviceCollection(object, ICollection, IEnumerable):
    """ Contains the System.Windows.Input.TabletDevice objects that represent the digitizer devices of a tablet device. """
    def CopyTo(self, array, index):
        """
        CopyTo(self: TabletDeviceCollection, array: Array[TabletDevice], index: int)
            Copies all elements in the current collection to the specified one-dimensional array, starting at the specified destination array index.
        
            array: The one-dimensional array that is the destination of elements copied from the collection. The array must have zero-based indexing.
            index: The zero-based index in the array parameter where copying begins.
        """
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of System.Windows.Input.TabletDevice objects in the collection.

Get: Count(self: TabletDeviceCollection) -> int

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether access to the collection is synchronized (thread safe).

Get: IsSynchronized(self: TabletDeviceCollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an object that can be used to synchronize access to the collection.

Get: SyncRoot(self: TabletDeviceCollection) -> object

"""



class TabletDeviceType(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines values for the type of devices the tablet device uses.
    
    enum TabletDeviceType, values: Stylus (0), Touch (1)
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

    Stylus = None
    Touch = None
    value__ = None


class TabletHardwareCapabilities(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines values that specify the hardware capabilities of a tablet device, including desktop digitizers and mice.
    
    enum (flags) TabletHardwareCapabilities, values: HardProximity (4), Integrated (1), None (0), StylusHasPhysicalIds (8), StylusMustTouch (2), SupportsPressure (1073741824)
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

    HardProximity = None
    Integrated = None
    None = None
    StylusHasPhysicalIds = None
    StylusMustTouch = None
    SupportsPressure = None
    value__ = None


class TextComposition(DispatcherObject):
    """
    Represents a composition related to text input which includes the composition text itself, any related control or system text, and a state of completion for the composition.
    
    TextComposition(inputManager: InputManager, source: IInputElement, resultText: str)
    TextComposition(inputManager: InputManager, source: IInputElement, resultText: str, autoComplete: TextCompositionAutoComplete)
    """
    def Complete(self):
        """
        Complete(self: TextComposition)
            Completes this text composition.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, inputManager, source, resultText, autoComplete=None):
        """
        __new__(cls: type, inputManager: InputManager, source: IInputElement, resultText: str)
        __new__(cls: type, inputManager: InputManager, source: IInputElement, resultText: str, autoComplete: TextCompositionAutoComplete)
        """
        pass

    AutoComplete = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the auto-complete setting for this text composition.

Get: AutoComplete(self: TextComposition) -> TextCompositionAutoComplete

"""

    CompositionText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the composition text for this text composition.

Get: CompositionText(self: TextComposition) -> str

"""

    ControlText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets any control text associated with this text composition.

Get: ControlText(self: TextComposition) -> str

"""

    SystemCompositionText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the system composition text for this text composition.

Get: SystemCompositionText(self: TextComposition) -> str

"""

    SystemText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the system text for this text composition.

Get: SystemText(self: TextComposition) -> str

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current text for this text composition.

Get: Text(self: TextComposition) -> str

"""



class TextCompositionAutoComplete(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines a set of states for the handling of automatic completion of a text composition.
    
    enum TextCompositionAutoComplete, values: Off (0), On (1)
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

    Off = None
    On = None
    value__ = None


class TextCompositionEventArgs(InputEventArgs):
    """
    Contains arguments associated with changes to a System.Windows.Input.TextComposition.
    
    TextCompositionEventArgs(inputDevice: InputDevice, composition: TextComposition)
    """
    @staticmethod # known case of __new__
    def __new__(self, inputDevice, composition):
        """ __new__(cls: type, inputDevice: InputDevice, composition: TextComposition) """
        pass

    ControlText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets control text associated with a System.Windows.Input.TextComposition event.

Get: ControlText(self: TextCompositionEventArgs) -> str

"""

    SystemText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets system text associated with a System.Windows.Input.TextComposition event.

Get: SystemText(self: TextCompositionEventArgs) -> str

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets input text associated with a System.Windows.Input.TextComposition event.

Get: Text(self: TextCompositionEventArgs) -> str

"""

    TextComposition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Input.TextComposition associated with a System.Windows.Input.TextComposition event.

Get: TextComposition(self: TextCompositionEventArgs) -> TextComposition

"""



class TextCompositionEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the routed events related to the System.Windows.Input.TextComposition and System.Windows.Input.TextCompositionManager classes, for example System.Windows.UIElement.TextInput.
    
    TextCompositionEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: TextCompositionEventHandler, sender: object, e: TextCompositionEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null, if the method represented by the current delegate does not require arguments.
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: TextCompositionEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: TextCompositionEventHandler, sender: object, e: TextCompositionEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation list.
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


class TextCompositionManager(DispatcherObject):
    """ Provides facilities for managing events related to input and text compositions. """
    @staticmethod
    def AddPreviewTextInputHandler(element, handler):
        """
        AddPreviewTextInputHandler(element: DependencyObject, handler: TextCompositionEventHandler)
            Adds a handler for the System.Windows.Input.TextCompositionManager.PreviewTextInput � attached event.
        
            element: A dependency object to add the event handler to.  The dependency object must be a System.Windows.UIElement or a System.Windows.ContentElement.
            handler: A delegate that designates the handler to add.
        """
        pass

    @staticmethod
    def AddPreviewTextInputStartHandler(element, handler):
        """
        AddPreviewTextInputStartHandler(element: DependencyObject, handler: TextCompositionEventHandler)
            Adds a handler for the System.Windows.Input.TextCompositionManager.PreviewTextInputStart � attached event.
        
            element: A dependency object to add the event handler to.  The dependency object must be a System.Windows.UIElement or a System.Windows.ContentElement.
            handler: A delegate that designates the handler to add.
        """
        pass

    @staticmethod
    def AddPreviewTextInputUpdateHandler(element, handler):
        """
        AddPreviewTextInputUpdateHandler(element: DependencyObject, handler: TextCompositionEventHandler)
            Adds a handler for the System.Windows.Input.TextCompositionManager.PreviewTextInputUpdate � attached event.
        
            element: A dependency object to add the event handler to.  The dependency object must be a System.Windows.UIElement or a System.Windows.ContentElement.
            handler: A delegate that designates the handler to add.
        """
        pass

    @staticmethod
    def AddTextInputHandler(element, handler):
        """
        AddTextInputHandler(element: DependencyObject, handler: TextCompositionEventHandler)
            Adds a handler for the System.Windows.Input.TextCompositionManager.TextInput � attached event.
        
            element: A dependency object to add the event handler to.  The dependency object must be a System.Windows.UIElement or a System.Windows.ContentElement.
            handler: A delegate that designates the handler to add.
        """
        pass

    @staticmethod
    def AddTextInputStartHandler(element, handler):
        """
        AddTextInputStartHandler(element: DependencyObject, handler: TextCompositionEventHandler)
            Adds a handler for the System.Windows.Input.TextCompositionManager.TextInputStart � attached event.
        
            element: A dependency object to add the event handler to.  The dependency object must be a System.Windows.UIElement or a System.Windows.ContentElement.
            handler: A delegate that designates the handler to add.
        """
        pass

    @staticmethod
    def AddTextInputUpdateHandler(element, handler):
        """
        AddTextInputUpdateHandler(element: DependencyObject, handler: TextCompositionEventHandler)
            Adds a handler for the System.Windows.Input.TextCompositionManager.TextInputUpdate � attached event.
        
            element: A dependency object to add the event handler to.  The dependency object must be a System.Windows.UIElement or a System.Windows.ContentElement.
            handler: A delegate that designates the handler to add.
        """
        pass

    @staticmethod
    def CompleteComposition(composition):
        """
        CompleteComposition(composition: TextComposition) -> bool
        
            Completes a specified text composition.
        
            composition: A System.Windows.Input.TextComposition object to complete.
            Returns: true if the text composition was successfully completed; otherwise, false.
        """
        pass

    @staticmethod
    def RemovePreviewTextInputHandler(element, handler):
        """
        RemovePreviewTextInputHandler(element: DependencyObject, handler: TextCompositionEventHandler)
            Removes a handler for the System.Windows.Input.TextCompositionManager.PreviewTextInput � attached event.
        
            element: A dependency object to remove the event handler from.  The dependency object must be a System.Windows.UIElement or a System.Windows.ContentElement.
            handler: A delegate that designates the handler to remove.
        """
        pass

    @staticmethod
    def RemovePreviewTextInputStartHandler(element, handler):
        """
        RemovePreviewTextInputStartHandler(element: DependencyObject, handler: TextCompositionEventHandler)
            Removes a handler for the System.Windows.Input.TextCompositionManager.TextInputStart � attached event.
        
            element: A dependency object to remove the event handler from.  The dependency object must be a System.Windows.UIElement or a System.Windows.ContentElement.
            handler: A delegate that designates the handler to remove.
        """
        pass

    @staticmethod
    def RemovePreviewTextInputUpdateHandler(element, handler):
        """
        RemovePreviewTextInputUpdateHandler(element: DependencyObject, handler: TextCompositionEventHandler)
            Removes a handler for the System.Windows.Input.TextCompositionManager.PreviewTextInputUpdate � attached event.
        
            element: A dependency object to remove the event handler from.  The dependency object must be a System.Windows.UIElement or a System.Windows.ContentElement.
            handler: A delegate that designates the handler to remove.
        """
        pass

    @staticmethod
    def RemoveTextInputHandler(element, handler):
        """
        RemoveTextInputHandler(element: DependencyObject, handler: TextCompositionEventHandler)
            Removes a handler for the System.Windows.Input.TextCompositionManager.TextInput � attached event.
        
            element: A dependency object to remove the event handler from.  The dependency object must be a System.Windows.UIElement or a System.Windows.ContentElement.
            handler: A delegate that designates the handler to remove.
        """
        pass

    @staticmethod
    def RemoveTextInputStartHandler(element, handler):
        """
        RemoveTextInputStartHandler(element: DependencyObject, handler: TextCompositionEventHandler)
            Removes a handler for the System.Windows.Input.TextCompositionManager.TextInputStart � attached event.
        
            element: A dependency object to remove the event handler from.  The dependency object must be a System.Windows.UIElement or a System.Windows.ContentElement.
            handler: A delegate that designates the handler to remove.
        """
        pass

    @staticmethod
    def RemoveTextInputUpdateHandler(element, handler):
        """
        RemoveTextInputUpdateHandler(element: DependencyObject, handler: TextCompositionEventHandler)
            Removes a handler for the System.Windows.Input.TextCompositionManager.TextInputUpdate � attached event.
        
            element: A dependency object to remove the event handler from.  The dependency object must be a System.Windows.UIElement or a System.Windows.ContentElement.
            handler: A delegate that designates the handler to remove.
        """
        pass

    @staticmethod
    def StartComposition(composition):
        """
        StartComposition(composition: TextComposition) -> bool
        
            Starts a specified text composition.
        
            composition: A System.Windows.Input.TextComposition object to start.
            Returns: true if the text composition was successfully started; otherwise, false.
        """
        pass

    @staticmethod
    def UpdateComposition(composition):
        """
        UpdateComposition(composition: TextComposition) -> bool
        
            Updates a specified text composition.
        
            composition: A System.Windows.Input.TextComposition object to update.
            Returns: true if the text composition was successfully updated; otherwise, false.
        """
        pass

    PreviewTextInputEvent = None
    PreviewTextInputStartEvent = None
    PreviewTextInputUpdateEvent = None
    TextInputEvent = None
    TextInputStartEvent = None
    TextInputUpdateEvent = None


class Touch(object):
    """ Provides an application-level service that processes multitouch input from the operating system and raises the System.Windows.Input.Touch.FrameReported event. """
    FrameReported = None
    __all__ = [
        'FrameReported',
    ]


class TouchAction(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes the action of a specific touch point.
    
    enum TouchAction, values: Down (0), Move (1), Up (2)
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

    Down = None
    Move = None
    Up = None
    value__ = None


class TouchDevice(InputDevice, IManipulator):
    """ Represents a single touch input produced by a finger on a touchscreen. """
    def Activate(self, *args): #cannot find CLR method
        """
        Activate(self: TouchDevice)
            Adds the System.Windows.Input.TouchDevice to the input messaging system.
        """
        pass

    def Capture(self, element, captureMode=None):
        """
        Capture(self: TouchDevice, element: IInputElement, captureMode: CaptureMode) -> bool
        
            Captures a touch to the specified element by using the specified System.Windows.Input.CaptureMode.
        
            element: The element that captures the touch.
            captureMode: The capture policy to use.
            Returns: true if the element was able to capture the touch; otherwise, false.
        Capture(self: TouchDevice, element: IInputElement) -> bool
        
            Captures a touch to the specified element by using the System.Windows.Input.CaptureMode.Element capture mode.
        
            element: The element that captures the touch input.
            Returns: true if the element was able to capture the touch; otherwise, false.
        """
        pass

    def Deactivate(self, *args): #cannot find CLR method
        """
        Deactivate(self: TouchDevice)
            Removes the System.Windows.Input.TouchDevice from the input messaging system.
        """
        pass

    def GetIntermediateTouchPoints(self, relativeTo):
        """
        GetIntermediateTouchPoints(self: TouchDevice, relativeTo: IInputElement) -> TouchPointCollection
        
            When overridden in a derived class, returns all touch points that are collected between the most recent and previous touch events.
        
            relativeTo: The element that defines the coordinate space.
            Returns: All touch points that were collected between the most recent and previous touch events.
        """
        pass

    def GetTouchPoint(self, relativeTo):
        """
        GetTouchPoint(self: TouchDevice, relativeTo: IInputElement) -> TouchPoint
        
            Returns the current position of the touch device relative to the specified element.
        
            relativeTo: The element that defines the coordinate space.
            Returns: The current position of the touch device relative to the specified element.
        """
        pass

    def OnCapture(self, *args): #cannot find CLR method
        """
        OnCapture(self: TouchDevice, element: IInputElement, captureMode: CaptureMode)
            Called when a touch is captured to an element.
        
            element: The element that captures the touch input.
            captureMode: The capture policy.
        """
        pass

    def OnManipulationEnded(self, *args): #cannot find CLR method
        """
        OnManipulationEnded(self: TouchDevice, cancel: bool)
            Called when a manipulation has ended.
        
            cancel: true to cancel the action; otherwise, false.
        """
        pass

    def OnManipulationStarted(self, *args): #cannot find CLR method
        """
        OnManipulationStarted(self: TouchDevice)
            Called when a manipulation is started.
        """
        pass

    def ReportDown(self, *args): #cannot find CLR method
        """
        ReportDown(self: TouchDevice) -> bool
        
            Reports that a touch is pressed on an element.
            Returns: true if the System.Windows.UIElement.TouchDown event was handled; otherwise, false.
        """
        pass

    def ReportMove(self, *args): #cannot find CLR method
        """
        ReportMove(self: TouchDevice) -> bool
        
            Reports that a touch is moving across an element.
            Returns: true if the System.Windows.UIElement.TouchMove event was handled; otherwise, false.
        """
        pass

    def ReportUp(self, *args): #cannot find CLR method
        """
        ReportUp(self: TouchDevice) -> bool
        
            Reports that a touch was lifted from an element.
            Returns: true if the System.Windows.UIElement.TouchUp event was handled; otherwise, false.
        """
        pass

    def SetActiveSource(self, *args): #cannot find CLR method
        """
        SetActiveSource(self: TouchDevice, activeSource: PresentationSource)
            Sets the System.Windows.PresentationSource that is reporting input for this device.
        
            activeSource: The source that reports input for this device.
        """
        pass

    def Synchronize(self):
        """
        Synchronize(self: TouchDevice)
            Forces the System.Windows.Input.TouchDevice to synchronize the user interface with underlying touch points.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, deviceId: int) """
        pass

    ActiveSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.PresentationSource that is reporting input for this device.

Get: ActiveSource(self: TouchDevice) -> PresentationSource

"""

    Captured = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the element that captured the System.Windows.Input.TouchDevice.

Get: Captured(self: TouchDevice) -> IInputElement

"""

    CaptureMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the capture policy of the System.Windows.Input.TouchDevice.

Get: CaptureMode(self: TouchDevice) -> CaptureMode

"""

    DirectlyOver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the element that the touch contact point is directly over.

Get: DirectlyOver(self: TouchDevice) -> IInputElement

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the unique identifier of the System.Windows.Input.TouchDevice, as provided by the operating system.

Get: Id(self: TouchDevice) -> int

"""

    IsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the device is active.

Get: IsActive(self: TouchDevice) -> bool

"""

    Target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the element that receives input from the System.Windows.Input.TouchDevice.

Get: Target(self: TouchDevice) -> IInputElement

"""


    Activated = None
    Deactivated = None
    Updated = None


class TouchEventArgs(InputEventArgs):
    """
    Provides data for touch input events.
    
    TouchEventArgs(touchDevice: TouchDevice, timestamp: int)
    """
    def GetIntermediateTouchPoints(self, relativeTo):
        """
        GetIntermediateTouchPoints(self: TouchEventArgs, relativeTo: IInputElement) -> TouchPointCollection
        
            Returns all touch points that were collected between the most recent and previous touch events.
        
            relativeTo: The element that defines the coordinate space.
            Returns: All touch points that were collected between the most recent and previous touch events.
        """
        pass

    def GetTouchPoint(self, relativeTo):
        """
        GetTouchPoint(self: TouchEventArgs, relativeTo: IInputElement) -> TouchPoint
        
            Returns the current position of the touch device relative to the specified element.
        
            relativeTo: The element that defines the coordinate space.
            Returns: The current position of the touch device relative to the specified element.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, touchDevice, timestamp):
        """ __new__(cls: type, touchDevice: TouchDevice, timestamp: int) """
        pass

    TouchDevice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the touch that generated the event.

Get: TouchDevice(self: TouchEventArgs) -> TouchDevice

"""



class TouchFrameEventArgs(EventArgs):
    """ Provides data for the System.Windows.Input.Touch.FrameReported event. """
    def GetPrimaryTouchPoint(self, relativeTo):
        """
        GetPrimaryTouchPoint(self: TouchFrameEventArgs, relativeTo: IInputElement) -> TouchPoint
        
            Returns the current touch point of the primary touch device relative to the specified element.
        
            relativeTo: The element that defines the coordinate space. To use WPF absolute coordinates, specify relativeTo as null.
            Returns: The current position of the primary System.Windows.Input.TouchDevice relative to the specified element; or null if the primary System.Windows.Input.TouchDevice is not active.
        """
        pass

    def GetTouchPoints(self, relativeTo):
        """
        GetTouchPoints(self: TouchFrameEventArgs, relativeTo: IInputElement) -> TouchPointCollection
        
            Returns a collection that contains the current touch point for each active touch device relative to the specified element.
        
            relativeTo: The element that defines the coordinate space. To use WPF absolute coordinates, specify relativeTo as null.
            Returns: A collection that contains the current System.Windows.Input.TouchPoint for each active System.Windows.Input.TouchDevice.
        """
        pass

    def SuspendMousePromotionUntilTouchUp(self):
        """
        SuspendMousePromotionUntilTouchUp(self: TouchFrameEventArgs)
            This member is not implemented.
        """
        pass

    Timestamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time stamp for this event.

Get: Timestamp(self: TouchFrameEventArgs) -> int

"""



class TouchFrameEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Windows.Input.Touch.FrameReported event of a System.Windows.Input.Touch.
    
    TouchFrameEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: TouchFrameEventHandler, sender: object, e: TouchFrameEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null, if the method represented by the current delegate does not require arguments.
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: TouchFrameEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: TouchFrameEventHandler, sender: object, e: TouchFrameEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation list.
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


class TouchPoint(object, IEquatable[TouchPoint]):
    """
    Represents a single touch point from a multitouch message source.
    
    TouchPoint(device: TouchDevice, position: Point, bounds: Rect, action: TouchAction)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, device, position, bounds, action):
        """ __new__(cls: type, device: TouchDevice, position: Point, bounds: Rect, action: TouchAction) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the last action that occurred at this location.

Get: Action(self: TouchPoint) -> TouchAction

"""

    Bounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the bounds of the area that the finger has in contact with the screen.

Get: Bounds(self: TouchPoint) -> Rect

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the location of the touch point.

Get: Position(self: TouchPoint) -> Point

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size of the System.Windows.Input.TouchPoint.Bounds property.

Get: Size(self: TouchPoint) -> Size

"""

    TouchDevice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the touch device that generated this System.Windows.Input.TouchPoint.

Get: TouchDevice(self: TouchPoint) -> TouchDevice

"""



class TouchPointCollection(Collection[TouchPoint], IList[TouchPoint], ICollection[TouchPoint], IEnumerable[TouchPoint], IEnumerable, IList, ICollection, IReadOnlyList[TouchPoint], IReadOnlyCollection[TouchPoint]):
    """
    Contains a collection of System.Windows.Input.TouchPoint objects.
    
    TouchPointCollection()
    """
    def ClearItems(self, *args): #cannot find CLR method
        """
        ClearItems(self: Collection[TouchPoint])
            Removes all elements from the System.Collections.ObjectModel.Collection.
        """
        pass

    def InsertItem(self, *args): #cannot find CLR method
        """ InsertItem(self: Collection[TouchPoint], index: int, item: TouchPoint) """
        pass

    def RemoveItem(self, *args): #cannot find CLR method
        """
        RemoveItem(self: Collection[TouchPoint], index: int)
            Removes the element at the specified index of the System.Collections.ObjectModel.Collection.
        
            index: The zero-based index of the element to remove.
        """
        pass

    def SetItem(self, *args): #cannot find CLR method
        """ SetItem(self: Collection[TouchPoint], index: int, item: TouchPoint) """
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

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Collections.Generic.IList wrapper around the System.Collections.ObjectModel.Collection.

"""



class TraversalRequest(object):
    """
    Represents a request to move focus to another control.
    
    TraversalRequest(focusNavigationDirection: FocusNavigationDirection)
    """
    @staticmethod # known case of __new__
    def __new__(self, focusNavigationDirection):
        """ __new__(cls: type, focusNavigationDirection: FocusNavigationDirection) """
        pass

    FocusNavigationDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the traversal direction.

Get: FocusNavigationDirection(self: TraversalRequest) -> FocusNavigationDirection

"""

    Wrapped = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether focus traversal has reached the end of child elements that can have focus.

Get: Wrapped(self: TraversalRequest) -> bool

Set: Wrapped(self: TraversalRequest) = value
"""



# variables with complex values

