# encoding: utf-8
# module System.ComponentModel.Design calls itself Design
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class ActiveDesignerEventArgs(EventArgs):
    """
    Provides data for the System.ComponentModel.Design.IDesignerEventService.ActiveDesigner event.
    
    ActiveDesignerEventArgs(oldDesigner: IDesignerHost, newDesigner: IDesignerHost)
    """
    @staticmethod # known case of __new__
    def __new__(self, oldDesigner, newDesigner):
        """ __new__(cls: type, oldDesigner: IDesignerHost, newDesigner: IDesignerHost) """
        pass

    NewDesigner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the document that is gaining activation.

Get: NewDesigner(self: ActiveDesignerEventArgs) -> IDesignerHost

"""

    OldDesigner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the document that is losing activation.

Get: OldDesigner(self: ActiveDesignerEventArgs) -> IDesignerHost

"""



class ActiveDesignerEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.ComponentModel.Design.IDesignerEventService.ActiveDesignerChanged event.
    
    ActiveDesignerEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: ActiveDesignerEventHandler, sender: object, e: ActiveDesignerEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: ActiveDesignerEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ActiveDesignerEventHandler, sender: object, e: ActiveDesignerEventArgs) """
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


class CheckoutException(ExternalException, ISerializable, _Exception):
    """
    The exception that is thrown when an attempt to check out a file that is checked into a source code management program is canceled or fails.
    
    CheckoutException()
    CheckoutException(message: str)
    CheckoutException(message: str, errorCode: int)
    CheckoutException(message: str, innerException: Exception)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, errorCode: int)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, message: str, innerException: Exception)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Canceled = None


class CommandID(object):
    """
    Represents a unique command identifier that consists of a numeric command ID and a GUID menu group identifier.
    
    CommandID(menuGroup: Guid, commandID: int)
    """
    def Equals(self, obj):
        """
        Equals(self: CommandID, obj: object) -> bool
        
            Determines whether two System.ComponentModel.Design.CommandID instances are equal.
        
            obj: The object to compare.
            Returns: true if the specified object is equivalent to this one; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: CommandID) -> int
            Returns: A hash code for the current System.Object.
        """
        pass

    def ToString(self):
        """
        ToString(self: CommandID) -> str
        
            Returns a System.String that represents the current object.
            Returns: A string that contains the command ID information, both the GUID and integer identifier.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, menuGroup, commandID):
        """ __new__(cls: type, menuGroup: Guid, commandID: int) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the GUID of the menu group that the menu command identified by this System.ComponentModel.Design.CommandID belongs to.

Get: Guid(self: CommandID) -> Guid

"""

    ID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the numeric command ID.

Get: ID(self: CommandID) -> int

"""



class ComponentChangedEventArgs(EventArgs):
    """
    Provides data for the System.ComponentModel.Design.IComponentChangeService.ComponentChanged event. This class cannot be inherited.
    
    ComponentChangedEventArgs(component: object, member: MemberDescriptor, oldValue: object, newValue: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, component, member, oldValue, newValue):
        """ __new__(cls: type, component: object, member: MemberDescriptor, oldValue: object, newValue: object) """
        pass

    Component = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the component that was modified.

Get: Component(self: ComponentChangedEventArgs) -> object

"""

    Member = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the member that has been changed.

Get: Member(self: ComponentChangedEventArgs) -> MemberDescriptor

"""

    NewValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the new value of the changed member.

Get: NewValue(self: ComponentChangedEventArgs) -> object

"""

    OldValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the old value of the changed member.

Get: OldValue(self: ComponentChangedEventArgs) -> object

"""



class ComponentChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle a System.ComponentModel.Design.IComponentChangeService.ComponentChanged event.
    
    ComponentChangedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: ComponentChangedEventHandler, sender: object, e: ComponentChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: ComponentChangedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ComponentChangedEventHandler, sender: object, e: ComponentChangedEventArgs) """
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


class ComponentChangingEventArgs(EventArgs):
    """
    Provides data for the System.ComponentModel.Design.IComponentChangeService.ComponentChanging event. This class cannot be inherited.
    
    ComponentChangingEventArgs(component: object, member: MemberDescriptor)
    """
    @staticmethod # known case of __new__
    def __new__(self, component, member):
        """ __new__(cls: type, component: object, member: MemberDescriptor) """
        pass

    Component = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the component that is about to be changed or the component that is the parent container of the member that is about to be changed.

Get: Component(self: ComponentChangingEventArgs) -> object

"""

    Member = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the member that is about to be changed.

Get: Member(self: ComponentChangingEventArgs) -> MemberDescriptor

"""



class ComponentChangingEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle a System.ComponentModel.Design.IComponentChangeService.ComponentChanging event.
    
    ComponentChangingEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: ComponentChangingEventHandler, sender: object, e: ComponentChangingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: ComponentChangingEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ComponentChangingEventHandler, sender: object, e: ComponentChangingEventArgs) """
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


class ComponentEventArgs(EventArgs):
    """
    Provides data for the System.ComponentModel.Design.IComponentChangeService.ComponentAdded, System.ComponentModel.Design.IComponentChangeService.ComponentAdding, System.ComponentModel.Design.IComponentChangeService.ComponentRemoved, and System.ComponentModel.Design.IComponentChangeService.ComponentRemoving events.
    
    ComponentEventArgs(component: IComponent)
    """
    @staticmethod # known case of __new__
    def __new__(self, component):
        """ __new__(cls: type, component: IComponent) """
        pass

    Component = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the component associated with the event.

Get: Component(self: ComponentEventArgs) -> IComponent

"""



class ComponentEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.ComponentModel.Design.IComponentChangeService.ComponentAdding, System.ComponentModel.Design.IComponentChangeService.ComponentAdded, System.ComponentModel.Design.IComponentChangeService.ComponentRemoving, and System.ComponentModel.Design.IComponentChangeService.ComponentRemoved events raised for component-level events.
    
    ComponentEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: ComponentEventHandler, sender: object, e: ComponentEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: ComponentEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ComponentEventHandler, sender: object, e: ComponentEventArgs) """
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


class ComponentRenameEventArgs(EventArgs):
    """
    Provides data for the System.ComponentModel.Design.IComponentChangeService.ComponentRename event.
    
    ComponentRenameEventArgs(component: object, oldName: str, newName: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, component, oldName, newName):
        """ __new__(cls: type, component: object, oldName: str, newName: str) """
        pass

    Component = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the component that is being renamed.

Get: Component(self: ComponentRenameEventArgs) -> object

"""

    NewName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the component after the rename event.

Get: NewName(self: ComponentRenameEventArgs) -> str

"""

    OldName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the component before the rename event.

Get: OldName(self: ComponentRenameEventArgs) -> str

"""



class ComponentRenameEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle a System.ComponentModel.Design.IComponentChangeService.ComponentRename event.
    
    ComponentRenameEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: ComponentRenameEventHandler, sender: object, e: ComponentRenameEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: ComponentRenameEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ComponentRenameEventHandler, sender: object, e: ComponentRenameEventArgs) """
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


class DesignerCollection(object, ICollection, IEnumerable):
    """
    Represents a collection of designers.
    
    DesignerCollection(designers: Array[IDesignerHost])
    DesignerCollection(designers: IList)
    """
    def GetEnumerator(self):
        """
        GetEnumerator(self: DesignerCollection) -> IEnumerator
        
            Gets a new enumerator for this collection.
            Returns: An System.Collections.IEnumerator that enumerates the collection.
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
    def __new__(self, designers):
        """
        __new__(cls: type, designers: Array[IDesignerHost])
        __new__(cls: type, designers: IList)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of designers in the collection.

Get: Count(self: DesignerCollection) -> int

"""



class DesignerEventArgs(EventArgs):
    """
    Provides data for the System.ComponentModel.Design.IDesignerEventService.DesignerCreated and System.ComponentModel.Design.IDesignerEventService.DesignerDisposed events.
    
    DesignerEventArgs(host: IDesignerHost)
    """
    @staticmethod # known case of __new__
    def __new__(self, host):
        """ __new__(cls: type, host: IDesignerHost) """
        pass

    Designer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the host of the document.

Get: Designer(self: DesignerEventArgs) -> IDesignerHost

"""



class DesignerEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.ComponentModel.Design.IDesignerEventService.DesignerCreated and System.ComponentModel.Design.IDesignerEventService.DesignerDisposed events that are raised when a document is created or disposed of.
    
    DesignerEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: DesignerEventHandler, sender: object, e: DesignerEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: DesignerEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: DesignerEventHandler, sender: object, e: DesignerEventArgs) """
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


class IDesignerOptionService:
    """ Provides access to the designer options located on the Tools menu under the Options command in the Visual Studio development environment. """
    def GetOptionValue(self, pageName, valueName):
        """
        GetOptionValue(self: IDesignerOptionService, pageName: str, valueName: str) -> object
        
            Gets the value of the specified Windows Forms Designer option.
        
            pageName: The name of the page that defines the option.
            valueName: The name of the option property.
            Returns: The value of the specified option.
        """
        pass

    def SetOptionValue(self, pageName, valueName, value):
        """
        SetOptionValue(self: IDesignerOptionService, pageName: str, valueName: str, value: object)
            Sets the value of the specified Windows Forms Designer option.
        
            pageName: The name of the page that defines the option.
            valueName: The name of the option property.
            value: The new value.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class DesignerOptionService(object, IDesignerOptionService):
    """ Provides a base class for getting and setting option values for a designer. """
    def CreateOptionCollection(self, *args): #cannot find CLR method
        """ CreateOptionCollection(self: DesignerOptionService, parent: DesignerOptionCollection, name: str, value: object) -> DesignerOptionCollection """
        pass

    def PopulateOptionCollection(self, *args): #cannot find CLR method
        """ PopulateOptionCollection(self: DesignerOptionService, options: DesignerOptionCollection) """
        pass

    def ShowDialog(self, *args): #cannot find CLR method
        """ ShowDialog(self: DesignerOptionService, options: DesignerOptionCollection, optionObject: object) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the options collection for this service.

Get: Options(self: DesignerOptionService) -> DesignerOptionCollection

"""


    DesignerOptionCollection = None


class DesignerTransaction(object, IDisposable):
    """ Provides a way to group a series of design-time actions to improve performance and enable most types of changes to be undone. """
    def Cancel(self):
        """
        Cancel(self: DesignerTransaction)
            Cancels the transaction and attempts to roll back the changes made by the events of the 
             transaction.
        """
        pass

    def Commit(self):
        """
        Commit(self: DesignerTransaction)
            Commits this transaction.
        """
        pass

    def Dispose(self, *args): #cannot find CLR method
        """
        Dispose(self: DesignerTransaction, disposing: bool)
            Releases the unmanaged resources used by the System.ComponentModel.Design.DesignerTransaction 
             and optionally releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def OnCancel(self, *args): #cannot find CLR method
        """
        OnCancel(self: DesignerTransaction)
            Raises the Cancel event.
        """
        pass

    def OnCommit(self, *args): #cannot find CLR method
        """
        OnCommit(self: DesignerTransaction)
            Performs the actual work of committing a transaction.
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
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, description: str)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Canceled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the transaction was canceled.

Get: Canceled(self: DesignerTransaction) -> bool

"""

    Committed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the transaction was committed.

Get: Committed(self: DesignerTransaction) -> bool

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a description for the transaction.

Get: Description(self: DesignerTransaction) -> str

"""



class DesignerTransactionCloseEventArgs(EventArgs):
    """
    Provides data for the System.ComponentModel.Design.IDesignerHost.TransactionClosed and System.ComponentModel.Design.IDesignerHost.TransactionClosing events.
    
    DesignerTransactionCloseEventArgs(commit: bool)
    DesignerTransactionCloseEventArgs(commit: bool, lastTransaction: bool)
    """
    @staticmethod # known case of __new__
    def __new__(self, commit, lastTransaction=None):
        """
        __new__(cls: type, commit: bool)
        __new__(cls: type, commit: bool, lastTransaction: bool)
        """
        pass

    LastTransaction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this is the last transaction to close.

Get: LastTransaction(self: DesignerTransactionCloseEventArgs) -> bool

"""

    TransactionCommitted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether the designer called System.ComponentModel.Design.DesignerTransaction.Commit on the transaction.

Get: TransactionCommitted(self: DesignerTransactionCloseEventArgs) -> bool

"""



class DesignerTransactionCloseEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that handles the System.ComponentModel.Design.IDesignerHost.TransactionClosed and System.ComponentModel.Design.IDesignerHost.TransactionClosing events of a designer.
    
    DesignerTransactionCloseEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: DesignerTransactionCloseEventHandler, sender: object, e: DesignerTransactionCloseEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: DesignerTransactionCloseEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: DesignerTransactionCloseEventHandler, sender: object, e: DesignerTransactionCloseEventArgs) """
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


class MenuCommand(object):
    """
    Represents a Windows menu or toolbar command item.
    
    MenuCommand(handler: EventHandler, command: CommandID)
    """
    def Invoke(self, arg=None):
        """
        Invoke(self: MenuCommand, arg: object)
            Invokes the command with the given parameter.
        
            arg: An optional argument for use by the command.
        Invoke(self: MenuCommand)
            Invokes the command.
        """
        pass

    def OnCommandChanged(self, *args): #cannot find CLR method
        """
        OnCommandChanged(self: MenuCommand, e: EventArgs)
            Raises the System.ComponentModel.Design.MenuCommand.CommandChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def ToString(self):
        """
        ToString(self: MenuCommand) -> str
        
            Returns a string representation of this menu command.
            Returns: A string containing the value of the System.ComponentModel.Design.MenuCommand.CommandID property 
             appended with the names of any flags that are set, separated by pipe bars (|). These flag 
             properties include System.ComponentModel.Design.MenuCommand.Checked, 
             System.ComponentModel.Design.MenuCommand.Enabled, 
             System.ComponentModel.Design.MenuCommand.Supported, and 
             System.ComponentModel.Design.MenuCommand.Visible.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, handler, command):
        """ __new__(cls: type, handler: EventHandler, command: CommandID) """
        pass

    Checked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether this menu item is checked.

Get: Checked(self: MenuCommand) -> bool

Set: Checked(self: MenuCommand) = value
"""

    CommandID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.ComponentModel.Design.CommandID associated with this menu command.

Get: CommandID(self: MenuCommand) -> CommandID

"""

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this menu item is available.

Get: Enabled(self: MenuCommand) -> bool

Set: Enabled(self: MenuCommand) = value
"""

    OleStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the OLE command status code for this menu item.

Get: OleStatus(self: MenuCommand) -> int

"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the public properties associated with the System.ComponentModel.Design.MenuCommand.

Get: Properties(self: MenuCommand) -> IDictionary

"""

    Supported = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether this menu item is supported.

Get: Supported(self: MenuCommand) -> bool

Set: Supported(self: MenuCommand) = value
"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether this menu item is visible.

Get: Visible(self: MenuCommand) -> bool

Set: Visible(self: MenuCommand) = value
"""


    CommandChanged = None


class DesignerVerb(MenuCommand):
    """
    Represents a verb that can be invoked from a designer.
    
    DesignerVerb(text: str, handler: EventHandler)
    DesignerVerb(text: str, handler: EventHandler, startCommandID: CommandID)
    """
    def ToString(self):
        """
        ToString(self: DesignerVerb) -> str
        
            Overrides System.Object.ToString.
            Returns: The verb's text, or an empty string ("") if the text field is empty.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, text, handler, startCommandID=None):
        """
        __new__(cls: type, text: str, handler: EventHandler)
        __new__(cls: type, text: str, handler: EventHandler, startCommandID: CommandID)
        """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the description of the menu item for the verb.

Get: Description(self: DesignerVerb) -> str

Set: Description(self: DesignerVerb) = value
"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the text description for the verb command on the menu.

Get: Text(self: DesignerVerb) -> str

"""



class DesignerVerbCollection(CollectionBase, IList, ICollection, IEnumerable):
    """
    Represents a collection of System.ComponentModel.Design.DesignerVerb objects.
    
    DesignerVerbCollection()
    DesignerVerbCollection(value: Array[DesignerVerb])
    """
    def Add(self, value):
        """
        Add(self: DesignerVerbCollection, value: DesignerVerb) -> int
        
            Adds the specified System.ComponentModel.Design.DesignerVerb to the collection.
        
            value: The System.ComponentModel.Design.DesignerVerb to add to the collection.
            Returns: The index in the collection at which the verb was added.
        """
        pass

    def AddRange(self, value):
        """
        AddRange(self: DesignerVerbCollection, value: DesignerVerbCollection)
            Adds the specified collection of designer verbs to the collection.
        
            value: A System.ComponentModel.Design.DesignerVerbCollection to add to the collection.
        AddRange(self: DesignerVerbCollection, value: Array[DesignerVerb])
            Adds the specified set of designer verbs to the collection.
        
            value: An array of System.ComponentModel.Design.DesignerVerb objects to add to the collection.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: DesignerVerbCollection, value: DesignerVerb) -> bool
        
            Gets a value indicating whether the specified System.ComponentModel.Design.DesignerVerb exists 
             in the collection.
        
        
            value: The System.ComponentModel.Design.DesignerVerb to search for in the collection.
            Returns: true if the specified object exists in the collection; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: DesignerVerbCollection, array: Array[DesignerVerb], index: int)
            Copies the collection members to the specified System.ComponentModel.Design.DesignerVerb array 
             beginning at the specified destination index.
        
        
            array: The array to copy collection members to.
            index: The destination index to begin copying to.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: DesignerVerbCollection, value: DesignerVerb) -> int
        
            Gets the index of the specified System.ComponentModel.Design.DesignerVerb.
        
            value: The System.ComponentModel.Design.DesignerVerb whose index to get in the collection.
            Returns: The index of the specified object if it is found in the list; otherwise, -1.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: DesignerVerbCollection, index: int, value: DesignerVerb)
            Inserts the specified System.ComponentModel.Design.DesignerVerb at the specified index.
        
            index: The index in the collection at which to insert the verb.
            value: The System.ComponentModel.Design.DesignerVerb to insert in the collection.
        """
        pass

    def OnClear(self, *args): #cannot find CLR method
        """
        OnClear(self: DesignerVerbCollection)
            Raises the Clear event.
        """
        pass

    def OnClearComplete(self, *args): #cannot find CLR method
        """
        OnClearComplete(self: CollectionBase)
            Performs additional custom processes after clearing the contents of the 
             System.Collections.CollectionBase instance.
        """
        pass

    def OnInsert(self, *args): #cannot find CLR method
        """
        OnInsert(self: DesignerVerbCollection, index: int, value: object)
            Raises the Insert event.
        
            index: The index at which to insert an item.
            value: The object to insert.
        """
        pass

    def OnInsertComplete(self, *args): #cannot find CLR method
        """
        OnInsertComplete(self: CollectionBase, index: int, value: object)
            Performs additional custom processes after inserting a new element into the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which to insert value.
            value: The new value of the element at index.
        """
        pass

    def OnRemove(self, *args): #cannot find CLR method
        """
        OnRemove(self: DesignerVerbCollection, index: int, value: object)
            Raises the Remove event.
        
            index: The index at which to remove the item.
            value: The object to remove.
        """
        pass

    def OnRemoveComplete(self, *args): #cannot find CLR method
        """
        OnRemoveComplete(self: CollectionBase, index: int, value: object)
            Performs additional custom processes after removing an element from the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which value can be found.
            value: The value of the element to remove from index.
        """
        pass

    def OnSet(self, *args): #cannot find CLR method
        """
        OnSet(self: DesignerVerbCollection, index: int, oldValue: object, newValue: object)
            Raises the Set event.
        
            index: The index at which to set the item.
            oldValue: The old object.
            newValue: The new object.
        """
        pass

    def OnSetComplete(self, *args): #cannot find CLR method
        """
        OnSetComplete(self: CollectionBase, index: int, oldValue: object, newValue: object)
            Performs additional custom processes after setting a value in the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which oldValue can be found.
            oldValue: The value to replace with newValue.
            newValue: The new value of the element at index.
        """
        pass

    def OnValidate(self, *args): #cannot find CLR method
        """
        OnValidate(self: DesignerVerbCollection, value: object)
            Raises the Validate event.
        
            value: The object to validate.
        """
        pass

    def Remove(self, value):
        """
        Remove(self: DesignerVerbCollection, value: DesignerVerb)
            Removes the specified System.ComponentModel.Design.DesignerVerb from the collection.
        
            value: The System.ComponentModel.Design.DesignerVerb to remove from the collection.
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
    def __new__(self, value=None):
        """
        __new__(cls: type)
        __new__(cls: type, value: Array[DesignerVerb])
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""



class DesigntimeLicenseContext(LicenseContext, IServiceProvider):
    """
    Represents a design-time license context that can support a license provider at design time.
    
    DesigntimeLicenseContext()
    """
    def GetSavedLicenseKey(self, type, resourceAssembly):
        """
        GetSavedLicenseKey(self: DesigntimeLicenseContext, type: Type, resourceAssembly: Assembly) -> str
        
            Gets a saved license key.
        
            type: The type of the license key.
            resourceAssembly: The assembly to get the key from.
            Returns: The saved license key that matches the specified type.
        """
        pass

    def SetSavedLicenseKey(self, type, key):
        """
        SetSavedLicenseKey(self: DesigntimeLicenseContext, type: Type, key: str)
            Sets a saved license key.
        
            type: The type of the license key.
            key: The license key.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    UsageMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the license usage mode.

Get: UsageMode(self: DesigntimeLicenseContext) -> LicenseUsageMode

"""



class DesigntimeLicenseContextSerializer(object):
    """ Provides support for design-time license context serialization. """
    @staticmethod
    def Serialize(o, cryptoKey, context):
        """
        Serialize(o: Stream, cryptoKey: str, context: DesigntimeLicenseContext)
            Serializes the licenses within the specified design-time license context using the specified key 
             and output stream.
        
        
            o: The stream to output to.
            cryptoKey: The key to use for encryption.
            context: A System.ComponentModel.Design.DesigntimeLicenseContext indicating the license context.
        """
        pass


class HelpContextType(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines identifiers that indicate information about the context in which a request for Help information originated.
    
    enum HelpContextType, values: Ambient (0), Selection (2), ToolWindowSelection (3), Window (1)
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

    Ambient = None
    Selection = None
    ToolWindowSelection = None
    value__ = None
    Window = None


class HelpKeywordAttribute(Attribute, _Attribute):
    """
    Specifies the context keyword for a class or member. This class cannot be inherited.
    
    HelpKeywordAttribute()
    HelpKeywordAttribute(keyword: str)
    HelpKeywordAttribute(t: Type)
    """
    def Equals(self, obj):
        """
        Equals(self: HelpKeywordAttribute, obj: object) -> bool
        
            Determines whether two System.ComponentModel.Design.HelpKeywordAttribute instances are equal.
        
            obj: The System.ComponentModel.Design.HelpKeywordAttribute to compare with the current 
             System.ComponentModel.Design.HelpKeywordAttribute.
        
            Returns: true if the specified System.ComponentModel.Design.HelpKeywordAttribute is equal to the current 
             System.ComponentModel.Design.HelpKeywordAttribute; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: HelpKeywordAttribute) -> int
        
            Returns the hash code for this instance.
            Returns: A hash code for the current System.ComponentModel.Design.HelpKeywordAttribute.
        """
        pass

    def IsDefaultAttribute(self):
        """
        IsDefaultAttribute(self: HelpKeywordAttribute) -> bool
        
            Determines whether the Help keyword is null.
            Returns: true if the Help keyword is null; otherwise, false.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, keyword: str)
        __new__(cls: type, t: Type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    HelpKeyword = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Help keyword supplied by this attribute.

Get: HelpKeyword(self: HelpKeywordAttribute) -> str

"""


    Default = None


class HelpKeywordType(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines identifiers that indicate the type of a Help keyword.
    
    enum HelpKeywordType, values: F1Keyword (0), FilterKeyword (2), GeneralKeyword (1)
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

    F1Keyword = None
    FilterKeyword = None
    GeneralKeyword = None
    value__ = None


class IComponentChangeService:
    """ Provides an interface to add and remove the event handlers for events that add, change, remove or rename components, and provides methods to raise a System.ComponentModel.Design.IComponentChangeService.ComponentChanged or System.ComponentModel.Design.IComponentChangeService.ComponentChanging event. """
    def OnComponentChanged(self, component, member, oldValue, newValue):
        """
        OnComponentChanged(self: IComponentChangeService, component: object, member: MemberDescriptor, oldValue: object, newValue: object)
            Announces to the component change service that a particular component has changed.
        
            component: The component that has changed.
            member: The member that has changed. This is null if this change is not related to a single member.
            oldValue: The old value of the member. This is valid only if the member is not null.
            newValue: The new value of the member. This is valid only if the member is not null.
        """
        pass

    def OnComponentChanging(self, component, member):
        """
        OnComponentChanging(self: IComponentChangeService, component: object, member: MemberDescriptor)
            Announces to the component change service that a particular component is changing.
        
            component: The component that is about to change.
            member: The member that is changing. This is null if this change is not related to a single member.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentAdded = None
    ComponentAdding = None
    ComponentChanged = None
    ComponentChanging = None
    ComponentRemoved = None
    ComponentRemoving = None
    ComponentRename = None


class IComponentDiscoveryService:
    """ Enables enumeration of components at design time. """
    def GetComponentTypes(self, designerHost, baseType):
        """
        GetComponentTypes(self: IComponentDiscoveryService, designerHost: IDesignerHost, baseType: Type) -> ICollection
        
            Gets the list of available component types.
        
            designerHost: The designer host providing design-time services. Can be null.
            baseType: The base type specifying the components to retrieve. Can be null.
            Returns: The list of available component types.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IComponentInitializer:
    """ Provides a set of recommended default values during component creation. """
    def InitializeExistingComponent(self, defaultValues):
        """
        InitializeExistingComponent(self: IComponentInitializer, defaultValues: IDictionary)
            Restores an instance of a component to its default state.
        
            defaultValues: A dictionary of default property values, which are name/value pairs, with which to reset the 
             component's state.
        """
        pass

    def InitializeNewComponent(self, defaultValues):
        """
        InitializeNewComponent(self: IComponentInitializer, defaultValues: IDictionary)
            Initializes a new component using a set of recommended values.
        
            defaultValues: A dictionary of default property values, which are name/value pairs, with which to initialize 
             the component's state.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IDesigner(IDisposable):
    """ Provides the basic framework for building a custom designer. """
    def DoDefaultAction(self):
        """
        DoDefaultAction(self: IDesigner)
            Performs the default action for this designer.
        """
        pass

    def Initialize(self, component):
        """
        Initialize(self: IDesigner, component: IComponent)
            Initializes the designer with the specified component.
        
            component: The component to associate with this designer.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Component = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the base component that this designer is designing.

Get: Component(self: IDesigner) -> IComponent

"""

    Verbs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of the design-time verbs supported by the designer.

Get: Verbs(self: IDesigner) -> DesignerVerbCollection

"""



class IDesignerEventService:
    """ Provides event notifications when root designers are added and removed, when a selected component changes, and when the current root designer changes. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ActiveDesigner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the root designer for the currently active document.

Get: ActiveDesigner(self: IDesignerEventService) -> IDesignerHost

"""

    Designers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of root designers for design documents that are currently active in the development environment.

Get: Designers(self: IDesignerEventService) -> DesignerCollection

"""


    ActiveDesignerChanged = None
    DesignerCreated = None
    DesignerDisposed = None
    SelectionChanged = None


class IDesignerFilter:
    """ Provides an interface that enables a designer to access and filter the dictionaries of a System.ComponentModel.TypeDescriptor that stores the property, attribute, and event descriptors that a component designer can expose to the design-time environment. """
    def PostFilterAttributes(self, attributes):
        """
        PostFilterAttributes(self: IDesignerFilter, attributes: IDictionary)
            When overridden in a derived class, allows a designer to change or remove items from the set of 
             attributes that it exposes through a System.ComponentModel.TypeDescriptor.
        
        
            attributes: The System.Attribute objects for the class of the component. The keys in the dictionary of 
             attributes are the System.Attribute.TypeId values of the attributes.
        """
        pass

    def PostFilterEvents(self, events):
        """
        PostFilterEvents(self: IDesignerFilter, events: IDictionary)
            When overridden in a derived class, allows a designer to change or remove items from the set of 
             events that it exposes through a System.ComponentModel.TypeDescriptor.
        
        
            events: The System.ComponentModel.EventDescriptor objects that represent the events of the class of the 
             component. The keys in the dictionary of events are event names.
        """
        pass

    def PostFilterProperties(self, properties):
        """
        PostFilterProperties(self: IDesignerFilter, properties: IDictionary)
            When overridden in a derived class, allows a designer to change or remove items from the set of 
             properties that it exposes through a System.ComponentModel.TypeDescriptor.
        
        
            properties: The System.ComponentModel.PropertyDescriptor objects that represent the properties of the class 
             of the component. The keys in the dictionary of properties are property names.
        """
        pass

    def PreFilterAttributes(self, attributes):
        """
        PreFilterAttributes(self: IDesignerFilter, attributes: IDictionary)
            When overridden in a derived class, allows a designer to add items to the set of attributes that 
             it exposes through a System.ComponentModel.TypeDescriptor.
        
        
            attributes: The System.Attribute objects for the class of the component. The keys in the dictionary of 
             attributes are the System.Attribute.TypeId values of the attributes.
        """
        pass

    def PreFilterEvents(self, events):
        """
        PreFilterEvents(self: IDesignerFilter, events: IDictionary)
            When overridden in a derived class, allows a designer to add items to the set of events that it 
             exposes through a System.ComponentModel.TypeDescriptor.
        
        
            events: The System.ComponentModel.EventDescriptor objects that represent the events of the class of the 
             component. The keys in the dictionary of events are event names.
        """
        pass

    def PreFilterProperties(self, properties):
        """
        PreFilterProperties(self: IDesignerFilter, properties: IDictionary)
            When overridden in a derived class, allows a designer to add items to the set of properties that 
             it exposes through a System.ComponentModel.TypeDescriptor.
        
        
            properties: The System.ComponentModel.PropertyDescriptor objects that represent the properties of the class 
             of the component. The keys in the dictionary of properties are property names.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IServiceContainer(IServiceProvider):
    """ Provides a container for services. """
    def AddService(self, serviceType, *__args):
        """
        AddService(self: IServiceContainer, serviceType: Type, callback: ServiceCreatorCallback)
            Adds the specified service to the service container.
        
            serviceType: The type of service to add.
            callback: A callback object that is used to create the service. This allows a service to be declared as 
             available, but delays the creation of the object until the service is requested.
        
        AddService(self: IServiceContainer, serviceType: Type, callback: ServiceCreatorCallback, promote: bool)
            Adds the specified service to the service container, and optionally promotes the service to 
             parent service containers.
        
        
            serviceType: The type of service to add.
            callback: A callback object that is used to create the service. This allows a service to be declared as 
             available, but delays the creation of the object until the service is requested.
        
            promote: true to promote this request to any parent service containers; otherwise, false.
        AddService(self: IServiceContainer, serviceType: Type, serviceInstance: object)
            Adds the specified service to the service container.
        
            serviceType: The type of service to add.
            serviceInstance: An instance of the service type to add. This object must implement or inherit from the type 
             indicated by the serviceType parameter.
        
        AddService(self: IServiceContainer, serviceType: Type, serviceInstance: object, promote: bool)
            Adds the specified service to the service container, and optionally promotes the service to any 
             parent service containers.
        
        
            serviceType: The type of service to add.
            serviceInstance: An instance of the service type to add. This object must implement or inherit from the type 
             indicated by the serviceType parameter.
        
            promote: true to promote this request to any parent service containers; otherwise, false.
        """
        pass

    def RemoveService(self, serviceType, promote=None):
        """
        RemoveService(self: IServiceContainer, serviceType: Type, promote: bool)
            Removes the specified service type from the service container, and optionally promotes the 
             service to parent service containers.
        
        
            serviceType: The type of service to remove.
            promote: true to promote this request to any parent service containers; otherwise, false.
        RemoveService(self: IServiceContainer, serviceType: Type)
            Removes the specified service type from the service container.
        
            serviceType: The type of service to remove.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IDesignerHost(IServiceContainer, IServiceProvider):
    """ Provides an interface for managing designer transactions and components. """
    def Activate(self):
        """
        Activate(self: IDesignerHost)
            Activates the designer that this host is hosting.
        """
        pass

    def CreateComponent(self, componentClass, name=None):
        """
        CreateComponent(self: IDesignerHost, componentClass: Type, name: str) -> IComponent
        
            Creates a component of the specified type and name, and adds it to the design document.
        
            componentClass: The type of the component to create.
            name: The name for the component.
            Returns: The newly created component.
        CreateComponent(self: IDesignerHost, componentClass: Type) -> IComponent
        
            Creates a component of the specified type and adds it to the design document.
        
            componentClass: The type of the component to create.
            Returns: The newly created component.
        """
        pass

    def CreateTransaction(self, description=None):
        """
        CreateTransaction(self: IDesignerHost, description: str) -> DesignerTransaction
        
            Creates a System.ComponentModel.Design.DesignerTransaction that can encapsulate event sequences 
             to improve performance and enable undo and redo support functionality, using the specified 
             transaction description.
        
        
            description: A title or description for the newly created transaction.
            Returns: A new System.ComponentModel.Design.DesignerTransaction. When you have completed the steps in 
             your transaction, you should call System.ComponentModel.Design.DesignerTransaction.Commit on 
             this object.
        
        CreateTransaction(self: IDesignerHost) -> DesignerTransaction
        
            Creates a System.ComponentModel.Design.DesignerTransaction that can encapsulate event sequences 
             to improve performance and enable undo and redo support functionality.
        
            Returns: A new instance of System.ComponentModel.Design.DesignerTransaction. When you complete the steps 
             in your transaction, you should call System.ComponentModel.Design.DesignerTransaction.Commit on 
             this object.
        """
        pass

    def DestroyComponent(self, component):
        """
        DestroyComponent(self: IDesignerHost, component: IComponent)
            Destroys the specified component and removes it from the designer container.
        
            component: The component to destroy.
        """
        pass

    def GetDesigner(self, component):
        """
        GetDesigner(self: IDesignerHost, component: IComponent) -> IDesigner
        
            Gets the designer instance that contains the specified component.
        
            component: The System.ComponentModel.IComponent to retrieve the designer for.
            Returns: An System.ComponentModel.Design.IDesigner, or null if there is no designer for the specified 
             component.
        """
        pass

    def GetType(self, typeName):
        """
        GetType(self: IDesignerHost, typeName: str) -> Type
        
            Gets an instance of the specified, fully qualified type name.
        
            typeName: The name of the type to load.
            Returns: The type object for the specified type name, or null if the type cannot be found.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Container = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the container for this designer host.

Get: Container(self: IDesignerHost) -> IContainer

"""

    InTransaction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the designer host is currently in a transaction.

Get: InTransaction(self: IDesignerHost) -> bool

"""

    Loading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the designer host is currently loading the document.

Get: Loading(self: IDesignerHost) -> bool

"""

    RootComponent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the instance of the base class used as the root component for the current design.

Get: RootComponent(self: IDesignerHost) -> IComponent

"""

    RootComponentClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the fully qualified name of the class being designed.

Get: RootComponentClassName(self: IDesignerHost) -> str

"""

    TransactionDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the description of the current transaction.

Get: TransactionDescription(self: IDesignerHost) -> str

"""


    Activated = None
    Deactivated = None
    LoadComplete = None
    TransactionClosed = None
    TransactionClosing = None
    TransactionOpened = None
    TransactionOpening = None


class IDesignerHostTransactionState:
    """ Specifies methods for the designer host to report on the state of transactions. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsClosingTransaction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the designer host is closing a transaction.

Get: IsClosingTransaction(self: IDesignerHostTransactionState) -> bool

"""



class IDictionaryService:
    """ Provides a basic, component site-specific, key-value pair dictionary through a service that a designer can use to store user-defined data. """
    def GetKey(self, value):
        """
        GetKey(self: IDictionaryService, value: object) -> object
        
            Gets the key corresponding to the specified value.
        
            value: The value to look up in the dictionary.
            Returns: The associated key, or null if no key exists.
        """
        pass

    def GetValue(self, key):
        """
        GetValue(self: IDictionaryService, key: object) -> object
        
            Gets the value corresponding to the specified key.
        
            key: The key to look up the value for.
            Returns: The associated value, or null if no value exists.
        """
        pass

    def SetValue(self, key, value):
        """
        SetValue(self: IDictionaryService, key: object, value: object)
            Sets the specified key-value pair.
        
            key: An object to use as the key to associate the value with.
            value: The value to store.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IEventBindingService:
    """ Provides a service for registering event handlers for component events. """
    def CreateUniqueMethodName(self, component, e):
        """
        CreateUniqueMethodName(self: IEventBindingService, component: IComponent, e: EventDescriptor) -> str
        
            Creates a unique name for an event-handler method for the specified component and event.
        
            component: The component instance the event is connected to.
            e: The event to create a name for.
            Returns: The recommended name for the event-handler method for this event.
        """
        pass

    def GetCompatibleMethods(self, e):
        """
        GetCompatibleMethods(self: IEventBindingService, e: EventDescriptor) -> ICollection
        
            Gets a collection of event-handler methods that have a method signature compatible with the 
             specified event.
        
        
            e: The event to get the compatible event-handler methods for.
            Returns: A collection of strings.
        """
        pass

    def GetEvent(self, property):
        """
        GetEvent(self: IEventBindingService, property: PropertyDescriptor) -> EventDescriptor
        
            Gets an System.ComponentModel.EventDescriptor for the event that the specified property 
             descriptor represents, if it represents an event.
        
        
            property: The property that represents an event.
            Returns: An System.ComponentModel.EventDescriptor for the event that the property represents, or null if 
             the property does not represent an event.
        """
        pass

    def GetEventProperties(self, events):
        """
        GetEventProperties(self: IEventBindingService, events: EventDescriptorCollection) -> PropertyDescriptorCollection
        
            Converts a set of event descriptors to a set of property descriptors.
        
            events: The events to convert to properties.
            Returns: An array of System.ComponentModel.PropertyDescriptor objects that describe the event set.
        """
        pass

    def GetEventProperty(self, e):
        """
        GetEventProperty(self: IEventBindingService, e: EventDescriptor) -> PropertyDescriptor
        
            Converts a single event descriptor to a property descriptor.
        
            e: The event to convert.
            Returns: A System.ComponentModel.PropertyDescriptor that describes the event.
        """
        pass

    def ShowCode(self, *__args):
        """
        ShowCode(self: IEventBindingService, component: IComponent, e: EventDescriptor) -> bool
        
            Displays the user code for the specified event.
        
            component: The component that the event is connected to.
            e: The event to display.
            Returns: true if the code is displayed; otherwise, false.
        ShowCode(self: IEventBindingService, lineNumber: int) -> bool
        
            Displays the user code for the designer at the specified line.
        
            lineNumber: The line number to place the caret on.
            Returns: true if the code is displayed; otherwise, false.
        ShowCode(self: IEventBindingService) -> bool
        
            Displays the user code for the designer.
            Returns: true if the code is displayed; otherwise, false.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IExtenderListService:
    """ Provides an interface that can list extender providers. """
    def GetExtenderProviders(self):
        """
        GetExtenderProviders(self: IExtenderListService) -> Array[IExtenderProvider]
        
            Gets the set of extender providers for the component.
            Returns: An array of type System.ComponentModel.IExtenderProvider that lists the active extender 
             providers. If there are no providers, an empty array is returned.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IExtenderProviderService:
    """ Provides an interface for adding and removing extender providers at design time. """
    def AddExtenderProvider(self, provider):
        """
        AddExtenderProvider(self: IExtenderProviderService, provider: IExtenderProvider)
            Adds the specified extender provider.
        
            provider: The extender provider to add.
        """
        pass

    def RemoveExtenderProvider(self, provider):
        """
        RemoveExtenderProvider(self: IExtenderProviderService, provider: IExtenderProvider)
            Removes the specified extender provider.
        
            provider: The extender provider to remove.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IHelpService:
    """ Provides methods for showing Help topics and adding and removing Help keywords at design time. """
    def AddContextAttribute(self, name, value, keywordType):
        """
        AddContextAttribute(self: IHelpService, name: str, value: str, keywordType: HelpKeywordType)
            Adds a context attribute to the document.
        
            name: The name of the attribute to add.
            value: The value of the attribute.
            keywordType: The type of the keyword, from the enumeration System.ComponentModel.Design.HelpKeywordType.
        """
        pass

    def ClearContextAttributes(self):
        """
        ClearContextAttributes(self: IHelpService)
            Removes all existing context attributes from the document.
        """
        pass

    def CreateLocalContext(self, contextType):
        """
        CreateLocalContext(self: IHelpService, contextType: HelpContextType) -> IHelpService
        
            Creates a local System.ComponentModel.Design.IHelpService to manage subcontexts.
        
            contextType: The priority type of the subcontext to add.
            Returns: The newly created System.ComponentModel.Design.IHelpService.
        """
        pass

    def RemoveContextAttribute(self, name, value):
        """
        RemoveContextAttribute(self: IHelpService, name: str, value: str)
            Removes a previously added context attribute.
        
            name: The name of the attribute to remove.
            value: The value of the attribute to remove.
        """
        pass

    def RemoveLocalContext(self, localContext):
        """
        RemoveLocalContext(self: IHelpService, localContext: IHelpService)
            Removes a context created with 
             System.ComponentModel.Design.IHelpService.CreateLocalContext(System.ComponentModel.Design.HelpCon
             textType).
        
        
            localContext: The local context System.ComponentModel.Design.IHelpService to remove.
        """
        pass

    def ShowHelpFromKeyword(self, helpKeyword):
        """
        ShowHelpFromKeyword(self: IHelpService, helpKeyword: str)
            Shows the Help topic that corresponds to the specified keyword.
        
            helpKeyword: The keyword of the Help topic to display.
        """
        pass

    def ShowHelpFromUrl(self, helpUrl):
        """
        ShowHelpFromUrl(self: IHelpService, helpUrl: str)
            Shows the Help topic that corresponds to the specified URL.
        
            helpUrl: The URL of the Help topic to display.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IInheritanceService:
    """ Provides methods for identifying the components of a component. """
    def AddInheritedComponents(self, component, container):
        """
        AddInheritedComponents(self: IInheritanceService, component: IComponent, container: IContainer)
            Searches the specified component for fields that implement the System.ComponentModel.IComponent 
             interface and adds each to the specified container, storing the inheritance level of each which 
             can be retrieved using the 
             System.ComponentModel.Design.IInheritanceService.GetInheritanceAttribute(System.ComponentModel.IC
             omponent) method.
        
        
            component: The System.ComponentModel.IComponent to search. Searching begins with this component.
            container: The System.ComponentModel.IContainer to add components to.
        """
        pass

    def GetInheritanceAttribute(self, component):
        """
        GetInheritanceAttribute(self: IInheritanceService, component: IComponent) -> InheritanceAttribute
        
            Gets the inheritance attribute for the specified component.
        
            component: The System.ComponentModel.IComponent for which to retrieve the inheritance attribute.
            Returns: An instance of System.ComponentModel.InheritanceAttribute that describes the level of 
             inheritance of the specified component.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IMenuCommandService:
    """ Provides methods to manage the global designer verbs and menu commands available in design mode, and to show some types of shortcut menus. """
    def AddCommand(self, command):
        """
        AddCommand(self: IMenuCommandService, command: MenuCommand)
            Adds the specified standard menu command to the menu.
        
            command: The System.ComponentModel.Design.MenuCommand to add.
        """
        pass

    def AddVerb(self, verb):
        """
        AddVerb(self: IMenuCommandService, verb: DesignerVerb)
            Adds the specified designer verb to the set of global designer verbs.
        
            verb: The System.ComponentModel.Design.DesignerVerb to add.
        """
        pass

    def FindCommand(self, commandID):
        """
        FindCommand(self: IMenuCommandService, commandID: CommandID) -> MenuCommand
        
            Searches for the specified command ID and returns the menu command associated with it.
        
            commandID: The System.ComponentModel.Design.CommandID to search for.
            Returns: The System.ComponentModel.Design.MenuCommand associated with the command ID, or null if no 
             command is found.
        """
        pass

    def GlobalInvoke(self, commandID):
        """
        GlobalInvoke(self: IMenuCommandService, commandID: CommandID) -> bool
        
            Invokes a menu or designer verb command matching the specified command ID.
        
            commandID: The System.ComponentModel.Design.CommandID of the command to search for and execute.
            Returns: true if the command was found and invoked successfully; otherwise, false.
        """
        pass

    def RemoveCommand(self, command):
        """
        RemoveCommand(self: IMenuCommandService, command: MenuCommand)
            Removes the specified standard menu command from the menu.
        
            command: The System.ComponentModel.Design.MenuCommand to remove.
        """
        pass

    def RemoveVerb(self, verb):
        """
        RemoveVerb(self: IMenuCommandService, verb: DesignerVerb)
            Removes the specified designer verb from the collection of global designer verbs.
        
            verb: The System.ComponentModel.Design.DesignerVerb to remove.
        """
        pass

    def ShowContextMenu(self, menuID, x, y):
        """
        ShowContextMenu(self: IMenuCommandService, menuID: CommandID, x: int, y: int)
            Shows the specified shortcut menu at the specified location.
        
            menuID: The System.ComponentModel.Design.CommandID for the shortcut menu to show.
            x: The x-coordinate at which to display the menu, in screen coordinates.
            y: The y-coordinate at which to display the menu, in screen coordinates.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Verbs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of the designer verbs that are currently available.

Get: Verbs(self: IMenuCommandService) -> DesignerVerbCollection

"""



class IReferenceService:
    """ Provides an interface for obtaining references to objects within a project by name or type, obtaining the name of a specified object, and for locating the parent of a specified object within a designer project. """
    def GetComponent(self, reference):
        """
        GetComponent(self: IReferenceService, reference: object) -> IComponent
        
            Gets the component that contains the specified component.
        
            reference: The object to retrieve the parent component for.
            Returns: The base System.ComponentModel.IComponent that contains the specified object, or null if no 
             parent component exists.
        """
        pass

    def GetName(self, reference):
        """
        GetName(self: IReferenceService, reference: object) -> str
        
            Gets the name of the specified component.
        
            reference: The object to return the name of.
            Returns: The name of the object referenced, or null if the object reference is not valid.
        """
        pass

    def GetReference(self, name):
        """
        GetReference(self: IReferenceService, name: str) -> object
        
            Gets a reference to the component whose name matches the specified name.
        
            name: The name of the component to return a reference to.
            Returns: An object the specified name refers to, or null if no reference is found.
        """
        pass

    def GetReferences(self, baseType=None):
        """
        GetReferences(self: IReferenceService, baseType: Type) -> Array[object]
        
            Gets all available references to components of the specified type.
        
            baseType: The type of object to return references to instances of.
            Returns: An array of all available objects of the specified type.
        GetReferences(self: IReferenceService) -> Array[object]
        
            Gets all available references to project components.
            Returns: An array of all objects with references available to the 
             System.ComponentModel.Design.IReferenceService.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IResourceService:
    """ Provides an interface for designers to access resource readers and writers for specific System.Globalization.CultureInfo resource types. """
    def GetResourceReader(self, info):
        """
        GetResourceReader(self: IResourceService, info: CultureInfo) -> IResourceReader
        
            Locates the resource reader for the specified culture and returns it.
        
            info: The System.Globalization.CultureInfo of the resource for which to retrieve a resource reader.
            Returns: An System.Resources.IResourceReader interface that contains the resources for the culture, or 
             null if no resources for the culture exist.
        """
        pass

    def GetResourceWriter(self, info):
        """
        GetResourceWriter(self: IResourceService, info: CultureInfo) -> IResourceWriter
        
            Locates the resource writer for the specified culture and returns it.
        
            info: The System.Globalization.CultureInfo of the resource for which to create a resource writer.
            Returns: An System.Resources.IResourceWriter interface for the specified culture.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IRootDesigner(IDesigner, IDisposable):
    """ Provides support for root-level designer view technologies. """
    def GetView(self, technology):
        """
        GetView(self: IRootDesigner, technology: ViewTechnology) -> object
        
            Gets a view object for the specified view technology.
        
            technology: A System.ComponentModel.Design.ViewTechnology that indicates a particular view technology.
            Returns: An object that represents the view for this designer.
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
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    SupportedTechnologies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the set of technologies that this designer can support for its display.

Get: SupportedTechnologies(self: IRootDesigner) -> Array[ViewTechnology]

"""



class ISelectionService:
    """ Provides an interface for a designer to select components. """
    def GetComponentSelected(self, component):
        """
        GetComponentSelected(self: ISelectionService, component: object) -> bool
        
            Gets a value indicating whether the specified component is currently selected.
        
            component: The component to test.
            Returns: true if the component is part of the user's current selection; otherwise, false.
        """
        pass

    def GetSelectedComponents(self):
        """
        GetSelectedComponents(self: ISelectionService) -> ICollection
        
            Gets a collection of components that are currently selected.
            Returns: A collection that represents the current set of components that are selected.
        """
        pass

    def SetSelectedComponents(self, components, selectionType=None):
        """
        SetSelectedComponents(self: ISelectionService, components: ICollection, selectionType: SelectionTypes)
            Selects the components from within the specified collection of components that match the 
             specified selection type.
        
        
            components: The collection of components to select.
            selectionType: A value from the System.ComponentModel.Design.SelectionTypes enumeration. The default is 
             System.ComponentModel.Design.SelectionTypes.Normal.
        
        SetSelectedComponents(self: ISelectionService, components: ICollection)
            Selects the specified collection of components.
        
            components: The collection of components to select.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    PrimarySelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the object that is currently the primary selected object.

Get: PrimarySelection(self: ISelectionService) -> object

"""

    SelectionCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the count of selected objects.

Get: SelectionCount(self: ISelectionService) -> int

"""


    SelectionChanged = None
    SelectionChanging = None


class ITreeDesigner(IDesigner, IDisposable):
    """ Provides support for building a set of related custom designers. """
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
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of child designers.

Get: Children(self: ITreeDesigner) -> ICollection

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent designer.

Get: Parent(self: ITreeDesigner) -> IDesigner

"""



class ITypeDescriptorFilterService:
    """ Provides an interface to modify the set of member descriptors for a component in design mode. """
    def FilterAttributes(self, component, attributes):
        """
        FilterAttributes(self: ITypeDescriptorFilterService, component: IComponent, attributes: IDictionary) -> bool
        
            Filters the attributes that a component exposes through a System.ComponentModel.TypeDescriptor.
        
            component: The component to filter the attributes of.
            attributes: A dictionary of attributes that can be modified.
            Returns: true if the set of filtered attributes is to be cached; false if the filter service must query 
             again.
        """
        pass

    def FilterEvents(self, component, events):
        """
        FilterEvents(self: ITypeDescriptorFilterService, component: IComponent, events: IDictionary) -> bool
        
            Filters the events that a component exposes through a System.ComponentModel.TypeDescriptor.
        
            component: The component to filter events for.
            events: A dictionary of events that can be modified.
            Returns: true if the set of filtered events is to be cached; false if the filter service must query again.
        """
        pass

    def FilterProperties(self, component, properties):
        """
        FilterProperties(self: ITypeDescriptorFilterService, component: IComponent, properties: IDictionary) -> bool
        
            Filters the properties that a component exposes through a System.ComponentModel.TypeDescriptor.
        
            component: The component to filter properties for.
            properties: A dictionary of properties that can be modified.
            Returns: true if the set of filtered properties is to be cached; false if the filter service must query 
             again.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ITypeDiscoveryService:
    """ Discovers available types at design time. """
    def GetTypes(self, baseType, excludeGlobalTypes):
        """
        GetTypes(self: ITypeDiscoveryService, baseType: Type, excludeGlobalTypes: bool) -> ICollection
        
            Retrieves the list of available types.
        
            baseType: The base type to match. Can be null.
            excludeGlobalTypes: Indicates whether types from all referenced assemblies should be checked.
            Returns: A collection of types that match the criteria specified by baseType and excludeGlobalTypes.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ITypeResolutionService:
    """ Provides an interface to retrieve an assembly or type by name. """
    def GetAssembly(self, name, throwOnError=None):
        """
        GetAssembly(self: ITypeResolutionService, name: AssemblyName, throwOnError: bool) -> Assembly
        
            Gets the requested assembly.
        
            name: The name of the assembly to retrieve.
            throwOnError: true if this method should throw an exception if the assembly cannot be located; otherwise, 
             false, and this method returns null if the assembly cannot be located.
        
            Returns: An instance of the requested assembly, or null if no assembly can be located.
        GetAssembly(self: ITypeResolutionService, name: AssemblyName) -> Assembly
        
            Gets the requested assembly.
        
            name: The name of the assembly to retrieve.
            Returns: An instance of the requested assembly, or null if no assembly can be located.
        """
        pass

    def GetPathOfAssembly(self, name):
        """
        GetPathOfAssembly(self: ITypeResolutionService, name: AssemblyName) -> str
        
            Gets the path to the file from which the assembly was loaded.
        
            name: The name of the assembly.
            Returns: The path to the file from which the assembly was loaded.
        """
        pass

    def GetType(self, name, throwOnError=None, ignoreCase=None):
        """
        GetType(self: ITypeResolutionService, name: str, throwOnError: bool, ignoreCase: bool) -> Type
        
            Loads a type with the specified name.
        
            name: The name of the type. If the type name is not a fully qualified name that indicates an assembly, 
             this service will search its internal set of referenced assemblies.
        
            throwOnError: true if this method should throw an exception if the assembly cannot be located; otherwise, 
             false, and this method returns null if the assembly cannot be located.
        
            ignoreCase: true to ignore case when searching for types; otherwise, false.
            Returns: An instance of System.Type that corresponds to the specified name, or null if no type can be 
             found.
        
        GetType(self: ITypeResolutionService, name: str, throwOnError: bool) -> Type
        
            Loads a type with the specified name.
        
            name: The name of the type. If the type name is not a fully qualified name that indicates an assembly, 
             this service will search its internal set of referenced assemblies.
        
            throwOnError: true if this method should throw an exception if the assembly cannot be located; otherwise, 
             false, and this method returns null if the assembly cannot be located.
        
            Returns: An instance of System.Type that corresponds to the specified name, or null if no type can be 
             found.
        
        GetType(self: ITypeResolutionService, name: str) -> Type
        
            Loads a type with the specified name.
        
            name: The name of the type. If the type name is not a fully qualified name that indicates an assembly, 
             this service will search its internal set of referenced assemblies.
        
            Returns: An instance of System.Type that corresponds to the specified name, or null if no type can be 
             found.
        """
        pass

    def ReferenceAssembly(self, name):
        """
        ReferenceAssembly(self: ITypeResolutionService, name: AssemblyName)
            Adds a reference to the specified assembly.
        
            name: An System.Reflection.AssemblyName that indicates the assembly to reference.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class SelectionTypes(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines identifiers that indicate the type of a selection.
    
    enum (flags) SelectionTypes, values: Add (64), Auto (1), Click (16), MouseDown (4), MouseUp (8), Normal (1), Primary (16), Remove (128), Replace (2), Toggle (32), Valid (31)
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

    Add = None
    Auto = None
    Click = None
    MouseDown = None
    MouseUp = None
    Normal = None
    Primary = None
    Remove = None
    Replace = None
    Toggle = None
    Valid = None
    value__ = None


class ServiceContainer(object, IServiceContainer, IServiceProvider, IDisposable):
    """
    Provides a simple implementation of the System.ComponentModel.Design.IServiceContainer interface. This class cannot be inherited.
    
    ServiceContainer()
    ServiceContainer(parentProvider: IServiceProvider)
    """
    def AddService(self, serviceType, *__args):
        """
        AddService(self: ServiceContainer, serviceType: Type, callback: ServiceCreatorCallback)
            Adds the specified service to the service container.
        
            serviceType: The type of service to add.
            callback: A callback object that can create the service. This allows a service to be declared as 
             available, but delays creation of the object until the service is requested.
        
        AddService(self: ServiceContainer, serviceType: Type, callback: ServiceCreatorCallback, promote: bool)
            Adds the specified service to the service container.
        
            serviceType: The type of service to add.
            callback: A callback object that can create the service. This allows a service to be declared as 
             available, but delays creation of the object until the service is requested.
        
            promote: true if this service should be added to any parent service containers; otherwise, false.
        AddService(self: ServiceContainer, serviceType: Type, serviceInstance: object)
            Adds the specified service to the service container.
        
            serviceType: The type of service to add.
            serviceInstance: An instance of the service to add. This object must implement or inherit from the type indicated 
             by the serviceType parameter.
        
        AddService(self: ServiceContainer, serviceType: Type, serviceInstance: object, promote: bool)
            Adds the specified service to the service container.
        
            serviceType: The type of service to add.
            serviceInstance: An instance of the service type to add. This object must implement or inherit from the type 
             indicated by the serviceType parameter.
        
            promote: true if this service should be added to any parent service containers; otherwise, false.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: ServiceContainer)
            Disposes this service container.
        """
        pass

    def GetService(self, serviceType):
        """
        GetService(self: ServiceContainer, serviceType: Type) -> object
        
            Gets the requested service.
        
            serviceType: The type of service to retrieve.
            Returns: An instance of the service if it could be found, or null if it could not be found.
        """
        pass

    def RemoveService(self, serviceType, promote=None):
        """
        RemoveService(self: ServiceContainer, serviceType: Type, promote: bool)
            Removes the specified service type from the service container.
        
            serviceType: The type of service to remove.
            promote: true if this service should be removed from any parent service containers; otherwise, false.
        RemoveService(self: ServiceContainer, serviceType: Type)
            Removes the specified service type from the service container.
        
            serviceType: The type of service to remove.
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
    def __new__(self, parentProvider=None):
        """
        __new__(cls: type)
        __new__(cls: type, parentProvider: IServiceProvider)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    DefaultServices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the default services implemented directly by System.ComponentModel.Design.ServiceContainer.

"""



class ServiceCreatorCallback(MulticastDelegate, ICloneable, ISerializable):
    """
    Provides a callback mechanism that can create an instance of a service on demand.
    
    ServiceCreatorCallback(object: object, method: IntPtr)
    """
    def BeginInvoke(self, container, serviceType, callback, object):
        """ BeginInvoke(self: ServiceCreatorCallback, container: IServiceContainer, serviceType: Type, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: ServiceCreatorCallback, result: IAsyncResult) -> object """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, container, serviceType):
        """ Invoke(self: ServiceCreatorCallback, container: IServiceContainer, serviceType: Type) -> object """
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


class StandardCommands(object):
    """
    Defines identifiers for the standard set of commands that are available to most applications.
    
    StandardCommands()
    """
    AlignBottom = None
    AlignHorizontalCenters = None
    AlignLeft = None
    AlignRight = None
    AlignToGrid = None
    AlignTop = None
    AlignVerticalCenters = None
    ArrangeBottom = None
    ArrangeIcons = None
    ArrangeRight = None
    BringForward = None
    BringToFront = None
    CenterHorizontally = None
    CenterVertically = None
    Copy = None
    Cut = None
    Delete = None
    DocumentOutline = None
    F1Help = None
    Group = None
    HorizSpaceConcatenate = None
    HorizSpaceDecrease = None
    HorizSpaceIncrease = None
    HorizSpaceMakeEqual = None
    LineupIcons = None
    LockControls = None
    MultiLevelRedo = None
    MultiLevelUndo = None
    Paste = None
    Properties = None
    PropertiesWindow = None
    Redo = None
    Replace = None
    SelectAll = None
    SendBackward = None
    SendToBack = None
    ShowGrid = None
    ShowLargeIcons = None
    SizeToControl = None
    SizeToControlHeight = None
    SizeToControlWidth = None
    SizeToFit = None
    SizeToGrid = None
    SnapToGrid = None
    TabOrder = None
    Undo = None
    Ungroup = None
    VerbFirst = None
    VerbLast = None
    VertSpaceConcatenate = None
    VertSpaceDecrease = None
    VertSpaceIncrease = None
    VertSpaceMakeEqual = None
    ViewCode = None
    ViewGrid = None


class StandardToolWindows(object):
    """
    Defines GUID identifiers that correspond to the standard set of tool windows that are available in the design environment.
    
    StandardToolWindows()
    """
    ObjectBrowser = None
    OutputWindow = None
    ProjectExplorer = None
    PropertyBrowser = None
    RelatedLinks = None
    ServerExplorer = None
    TaskList = None
    Toolbox = None


class TypeDescriptionProviderService(object):
    """ Provides a type description provider for a specified type. """
    def GetProvider(self, *__args):
        """
        GetProvider(self: TypeDescriptionProviderService, type: Type) -> TypeDescriptionProvider
        
            Gets a type description provider for the specified type.
        
            type: The type to get a type description provider for.
            Returns: A System.ComponentModel.TypeDescriptionProvider that corresponds with type.
        GetProvider(self: TypeDescriptionProviderService, instance: object) -> TypeDescriptionProvider
        
            Gets a type description provider for the specified object.
        
            instance: The object to get a type description provider for.
            Returns: A System.ComponentModel.TypeDescriptionProvider that corresponds with instance.
        """
        pass


class ViewTechnology(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines identifiers for a set of technologies that designer hosts support.
    
    enum ViewTechnology, values: Default (2), Passthrough (0), WindowsForms (1)
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

    Default = None
    Passthrough = None
    value__ = None
    WindowsForms = None


# variables with complex values

