# encoding: utf-8
# module System.Drawing.Design calls itself Design
# from System.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class CategoryNameCollection(ReadOnlyCollectionBase, ICollection, IEnumerable):
    """
    Represents a collection of category name strings.
    
    CategoryNameCollection(value: CategoryNameCollection)
    CategoryNameCollection(value: Array[str])
    """
    def Contains(self, value):
        """
        Contains(self: CategoryNameCollection, value: str) -> bool
        
            Indicates whether the specified category is contained in the collection.
        
            value: The string to check for in the collection.
            Returns: true if the specified category is contained in the collection; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: CategoryNameCollection, array: Array[str], index: int)
            Copies the collection elements to the specified array at the specified index.
        
            array: The array to copy to.
            index: The index of the destination array at which to begin copying.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: CategoryNameCollection, value: str) -> int
        
            Gets the index of the specified value.
        
            value: The category name to retrieve the index of in the collection.
            Returns: The index in the collection, or null if the string does not exist in the collection.
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

    @staticmethod # known case of __new__
    def __new__(self, value):
        """
        __new__(cls: type, value: CategoryNameCollection)
        __new__(cls: type, value: Array[str])
        """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of elements contained in the System.Collections.ReadOnlyCollectionBase instance.

"""



class IPropertyValueUIService:
    """ Provides an interface to manage the images, ToolTips, and event handlers for the properties of a component displayed in a property browser. """
    def AddPropertyValueUIHandler(self, newHandler):
        """
        AddPropertyValueUIHandler(self: IPropertyValueUIService, newHandler: PropertyValueUIHandler)
            Adds the specified System.Drawing.Design.PropertyValueUIHandler to this service.
        
            newHandler: The property value UI handler to add.
        """
        pass

    def GetPropertyUIValueItems(self, context, propDesc):
        """
        GetPropertyUIValueItems(self: IPropertyValueUIService, context: ITypeDescriptorContext, propDesc: PropertyDescriptor) -> Array[PropertyValueUIItem]
        
            Gets the System.Drawing.Design.PropertyValueUIItem objects that match the specified context and 
             property descriptor characteristics.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that can be used to gain additional context 
             information.
        
            propDesc: A System.ComponentModel.PropertyDescriptor that indicates the property to match with the 
             properties to return.
        
            Returns: An array of System.Drawing.Design.PropertyValueUIItem objects that match the specified 
             parameters.
        """
        pass

    def NotifyPropertyValueUIItemsChanged(self):
        """
        NotifyPropertyValueUIItemsChanged(self: IPropertyValueUIService)
            Notifies the System.Drawing.Design.IPropertyValueUIService implementation that the global list 
             of System.Drawing.Design.PropertyValueUIItem objects has been modified.
        """
        pass

    def RemovePropertyValueUIHandler(self, newHandler):
        """
        RemovePropertyValueUIHandler(self: IPropertyValueUIService, newHandler: PropertyValueUIHandler)
            Removes the specified System.Drawing.Design.PropertyValueUIHandler from the property value UI 
             service.
        
        
            newHandler: The handler to remove.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    PropertyUIValueItemsChanged = None


class IToolboxItemProvider:
    """ Exposes a collection of toolbox items. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of System.Drawing.Design.ToolboxItem objects.

Get: Items(self: IToolboxItemProvider) -> ToolboxItemCollection

"""



class IToolboxService:
    """ Provides methods and properties to manage and query the toolbox in the development environment. """
    def AddCreator(self, creator, format, host=None):
        """
        AddCreator(self: IToolboxService, creator: ToolboxItemCreatorCallback, format: str, host: IDesignerHost)
            Adds a new toolbox item creator for a specified data format and designer host.
        
            creator: A System.Drawing.Design.ToolboxItemCreatorCallback that can create a component when the toolbox 
             item is invoked.
        
            format: The data format that the creator handles.
            host: The System.ComponentModel.Design.IDesignerHost that represents the designer host to associate 
             with the creator.
        
        AddCreator(self: IToolboxService, creator: ToolboxItemCreatorCallback, format: str)
            Adds a new toolbox item creator for a specified data format.
        
            creator: A System.Drawing.Design.ToolboxItemCreatorCallback that can create a component when the toolbox 
             item is invoked.
        
            format: The data format that the creator handles.
        """
        pass

    def AddLinkedToolboxItem(self, toolboxItem, *__args):
        """
        AddLinkedToolboxItem(self: IToolboxService, toolboxItem: ToolboxItem, category: str, host: IDesignerHost)
            Adds the specified project-linked toolbox item to the toolbox in the specified category.
        
            toolboxItem: The linked System.Drawing.Design.ToolboxItem to add to the toolbox.
            category: The toolbox item category to add the toolbox item to.
            host: The System.ComponentModel.Design.IDesignerHost for the current design document.
        AddLinkedToolboxItem(self: IToolboxService, toolboxItem: ToolboxItem, host: IDesignerHost)
            Adds the specified project-linked toolbox item to the toolbox.
        
            toolboxItem: The linked System.Drawing.Design.ToolboxItem to add to the toolbox.
            host: The System.ComponentModel.Design.IDesignerHost for the current design document.
        """
        pass

    def AddToolboxItem(self, toolboxItem, category=None):
        """
        AddToolboxItem(self: IToolboxService, toolboxItem: ToolboxItem, category: str)
            Adds the specified toolbox item to the toolbox in the specified category.
        
            toolboxItem: The System.Drawing.Design.ToolboxItem to add to the toolbox.
            category: The toolbox item category to add the System.Drawing.Design.ToolboxItem to.
        AddToolboxItem(self: IToolboxService, toolboxItem: ToolboxItem)
            Adds the specified toolbox item to the toolbox.
        
            toolboxItem: The System.Drawing.Design.ToolboxItem to add to the toolbox.
        """
        pass

    def DeserializeToolboxItem(self, serializedObject, host=None):
        """
        DeserializeToolboxItem(self: IToolboxService, serializedObject: object, host: IDesignerHost) -> ToolboxItem
        
            Gets a toolbox item from the specified object that represents a toolbox item in serialized form, 
             using the specified designer host.
        
        
            serializedObject: The object that contains the System.Drawing.Design.ToolboxItem to retrieve.
            host: The System.ComponentModel.Design.IDesignerHost to associate with this 
             System.Drawing.Design.ToolboxItem.
        
            Returns: The System.Drawing.Design.ToolboxItem created from deserialization.
        DeserializeToolboxItem(self: IToolboxService, serializedObject: object) -> ToolboxItem
        
            Gets a toolbox item from the specified object that represents a toolbox item in serialized form.
        
            serializedObject: The object that contains the System.Drawing.Design.ToolboxItem to retrieve.
            Returns: The System.Drawing.Design.ToolboxItem created from the serialized object.
        """
        pass

    def GetSelectedToolboxItem(self, host=None):
        """
        GetSelectedToolboxItem(self: IToolboxService, host: IDesignerHost) -> ToolboxItem
        
            Gets the currently selected toolbox item if it is available to all designers, or if it supports 
             the specified designer.
        
        
            host: The System.ComponentModel.Design.IDesignerHost that the selected tool must be associated with 
             for it to be returned.
        
            Returns: The System.Drawing.Design.ToolboxItem that is currently selected, or null if no toolbox item is 
             currently selected.
        
        GetSelectedToolboxItem(self: IToolboxService) -> ToolboxItem
        
            Gets the currently selected toolbox item.
            Returns: The System.Drawing.Design.ToolboxItem that is currently selected, or null if no toolbox item has 
             been selected.
        """
        pass

    def GetToolboxItems(self, *__args):
        """
        GetToolboxItems(self: IToolboxService, category: str) -> ToolboxItemCollection
        
            Gets a collection of toolbox items from the toolbox that match the specified category.
        
            category: The toolbox item category to retrieve all the toolbox items from.
            Returns: A System.Drawing.Design.ToolboxItemCollection that contains the current toolbox items that are 
             associated with the specified category.
        
        GetToolboxItems(self: IToolboxService, category: str, host: IDesignerHost) -> ToolboxItemCollection
        
            Gets the collection of toolbox items that are associated with the specified designer host and 
             category from the toolbox.
        
        
            category: The toolbox item category to retrieve the toolbox items from.
            host: The System.ComponentModel.Design.IDesignerHost that is associated with the toolbox items to 
             retrieve.
        
            Returns: A System.Drawing.Design.ToolboxItemCollection that contains the current toolbox items that are 
             associated with the specified category and designer host.
        
        GetToolboxItems(self: IToolboxService) -> ToolboxItemCollection
        
            Gets the entire collection of toolbox items from the toolbox.
            Returns: A System.Drawing.Design.ToolboxItemCollection that contains the current toolbox items.
        GetToolboxItems(self: IToolboxService, host: IDesignerHost) -> ToolboxItemCollection
        
            Gets the collection of toolbox items that are associated with the specified designer host from 
             the toolbox.
        
        
            host: The System.ComponentModel.Design.IDesignerHost that is associated with the toolbox items to 
             retrieve.
        
            Returns: A System.Drawing.Design.ToolboxItemCollection that contains the current toolbox items that are 
             associated with the specified designer host.
        """
        pass

    def IsSupported(self, serializedObject, *__args):
        """
        IsSupported(self: IToolboxService, serializedObject: object, filterAttributes: ICollection) -> bool
        
            Gets a value indicating whether the specified object which represents a serialized toolbox item 
             matches the specified attributes.
        
        
            serializedObject: The object that contains the System.Drawing.Design.ToolboxItem to retrieve.
            filterAttributes: An System.Collections.ICollection that contains the attributes to test the serialized object for.
            Returns: true if the object matches the specified attributes; otherwise, false.
        IsSupported(self: IToolboxService, serializedObject: object, host: IDesignerHost) -> bool
        
            Gets a value indicating whether the specified object which represents a serialized toolbox item 
             can be used by the specified designer host.
        
        
            serializedObject: The object that contains the System.Drawing.Design.ToolboxItem to retrieve.
            host: The System.ComponentModel.Design.IDesignerHost to test for support for the 
             System.Drawing.Design.ToolboxItem.
        
            Returns: true if the specified object is compatible with the specified designer host; otherwise, false.
        """
        pass

    def IsToolboxItem(self, serializedObject, host=None):
        """
        IsToolboxItem(self: IToolboxService, serializedObject: object, host: IDesignerHost) -> bool
        
            Gets a value indicating whether the specified object is a serialized toolbox item, using the 
             specified designer host.
        
        
            serializedObject: The object to inspect.
            host: The System.ComponentModel.Design.IDesignerHost that is making this request.
            Returns: true if the object contains a toolbox item object; otherwise, false.
        IsToolboxItem(self: IToolboxService, serializedObject: object) -> bool
        
            Gets a value indicating whether the specified object is a serialized toolbox item.
        
            serializedObject: The object to inspect.
            Returns: true if the object contains a toolbox item object; otherwise, false.
        """
        pass

    def Refresh(self):
        """
        Refresh(self: IToolboxService)
            Refreshes the state of the toolbox items.
        """
        pass

    def RemoveCreator(self, format, host=None):
        """
        RemoveCreator(self: IToolboxService, format: str, host: IDesignerHost)
            Removes a previously added toolbox creator that is associated with the specified data format and 
             the specified designer host.
        
        
            format: The data format of the creator to remove.
            host: The System.ComponentModel.Design.IDesignerHost that is associated with the creator to remove.
        RemoveCreator(self: IToolboxService, format: str)
            Removes a previously added toolbox item creator of the specified data format.
        
            format: The data format of the creator to remove.
        """
        pass

    def RemoveToolboxItem(self, toolboxItem, category=None):
        """
        RemoveToolboxItem(self: IToolboxService, toolboxItem: ToolboxItem, category: str)
            Removes the specified toolbox item from the toolbox.
        
            toolboxItem: The System.Drawing.Design.ToolboxItem to remove from the toolbox.
            category: The toolbox item category to remove the System.Drawing.Design.ToolboxItem from.
        RemoveToolboxItem(self: IToolboxService, toolboxItem: ToolboxItem)
            Removes the specified toolbox item from the toolbox.
        
            toolboxItem: The System.Drawing.Design.ToolboxItem to remove from the toolbox.
        """
        pass

    def SelectedToolboxItemUsed(self):
        """
        SelectedToolboxItemUsed(self: IToolboxService)
            Notifies the toolbox service that the selected tool has been used.
        """
        pass

    def SerializeToolboxItem(self, toolboxItem):
        """
        SerializeToolboxItem(self: IToolboxService, toolboxItem: ToolboxItem) -> object
        
            Gets a serializable object that represents the specified toolbox item.
        
            toolboxItem: The System.Drawing.Design.ToolboxItem to serialize.
            Returns: An object that represents the specified System.Drawing.Design.ToolboxItem.
        """
        pass

    def SetCursor(self):
        """
        SetCursor(self: IToolboxService) -> bool
        
            Sets the current application's cursor to a cursor that represents the currently selected tool.
            Returns: true if the cursor is set by the currently selected tool, false if there is no tool selected and 
             the cursor is set to the standard windows cursor.
        """
        pass

    def SetSelectedToolboxItem(self, toolboxItem):
        """
        SetSelectedToolboxItem(self: IToolboxService, toolboxItem: ToolboxItem)
            Selects the specified toolbox item.
        
            toolboxItem: The System.Drawing.Design.ToolboxItem to select.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CategoryNames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the names of all the tool categories currently on the toolbox.

Get: CategoryNames(self: IToolboxService) -> CategoryNameCollection

"""

    SelectedCategory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the currently selected tool category from the toolbox.

Get: SelectedCategory(self: IToolboxService) -> str

Set: SelectedCategory(self: IToolboxService) = value
"""



class IToolboxUser:
    """ Defines an interface for setting the currently selected toolbox item and indicating whether a designer supports a particular toolbox item. """
    def GetToolSupported(self, tool):
        """
        GetToolSupported(self: IToolboxUser, tool: ToolboxItem) -> bool
        
            Gets a value indicating whether the specified tool is supported by the current designer.
        
            tool: The System.Drawing.Design.ToolboxItem to be tested for toolbox support.
            Returns: true if the tool is supported by the toolbox and can be enabled; false if the document designer 
             does not know how to use the tool.
        """
        pass

    def ToolPicked(self, tool):
        """
        ToolPicked(self: IToolboxUser, tool: ToolboxItem)
            Selects the specified tool.
        
            tool: The System.Drawing.Design.ToolboxItem to select.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class PaintValueEventArgs(EventArgs):
    """
    Provides data for the System.Drawing.Design.UITypeEditor.PaintValue(System.Object,System.Drawing.Graphics,System.Drawing.Rectangle) method.
    
    PaintValueEventArgs(context: ITypeDescriptorContext, value: object, graphics: Graphics, bounds: Rectangle)
    """
    @staticmethod # known case of __new__
    def __new__(self, context, value, graphics, bounds):
        """ __new__(cls: type, context: ITypeDescriptorContext, value: object, graphics: Graphics, bounds: Rectangle) """
        pass

    Bounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the rectangle that indicates the area in which the painting should be done.

Get: Bounds(self: PaintValueEventArgs) -> Rectangle

"""

    Context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.ComponentModel.ITypeDescriptorContext interface to be used to gain additional information about the context this value appears in.

Get: Context(self: PaintValueEventArgs) -> ITypeDescriptorContext

"""

    Graphics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Drawing.Graphics object with which painting should be done.

Get: Graphics(self: PaintValueEventArgs) -> Graphics

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value to paint.

Get: Value(self: PaintValueEventArgs) -> object

"""



class PropertyValueUIHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that adds a delegate to an implementation of System.Drawing.Design.IPropertyValueUIService.
    
    PropertyValueUIHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, context, propDesc, valueUIItemList, callback, object):
        """ BeginInvoke(self: PropertyValueUIHandler, context: ITypeDescriptorContext, propDesc: PropertyDescriptor, valueUIItemList: ArrayList, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: PropertyValueUIHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, context, propDesc, valueUIItemList):
        """ Invoke(self: PropertyValueUIHandler, context: ITypeDescriptorContext, propDesc: PropertyDescriptor, valueUIItemList: ArrayList) """
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


class PropertyValueUIItem(object):
    """
    Provides information about a property displayed in the Properties window, including the associated event handler, pop-up information string, and the icon to display for the property.
    
    PropertyValueUIItem(uiItemImage: Image, handler: PropertyValueUIItemInvokeHandler, tooltip: str)
    """
    def Reset(self):
        """
        Reset(self: PropertyValueUIItem)
            Resets the user interface (UI) item.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, uiItemImage, handler, tooltip):
        """ __new__(cls: type, uiItemImage: Image, handler: PropertyValueUIItemInvokeHandler, tooltip: str) """
        pass

    Image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the 8 x 8 pixel image that will be drawn in the Properties window.

Get: Image(self: PropertyValueUIItem) -> Image

"""

    InvokeHandler = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the handler that is raised when a user double-clicks this item.

Get: InvokeHandler(self: PropertyValueUIItem) -> PropertyValueUIItemInvokeHandler

"""

    ToolTip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the information string to display for this item.

Get: ToolTip(self: PropertyValueUIItem) -> str

"""



class PropertyValueUIItemInvokeHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Drawing.Design.PropertyValueUIItem.InvokeHandler event of a System.Drawing.Design.PropertyValueUIItem.
    
    PropertyValueUIItemInvokeHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, context, descriptor, invokedItem, callback, object):
        """ BeginInvoke(self: PropertyValueUIItemInvokeHandler, context: ITypeDescriptorContext, descriptor: PropertyDescriptor, invokedItem: PropertyValueUIItem, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: PropertyValueUIItemInvokeHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, context, descriptor, invokedItem):
        """ Invoke(self: PropertyValueUIItemInvokeHandler, context: ITypeDescriptorContext, descriptor: PropertyDescriptor, invokedItem: PropertyValueUIItem) """
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


class ToolboxComponentsCreatedEventArgs(EventArgs):
    """
    Provides data for the System.Drawing.Design.ToolboxItem.ComponentsCreated event that occurs when components are added to the toolbox.
    
    ToolboxComponentsCreatedEventArgs(components: Array[IComponent])
    """
    @staticmethod # known case of __new__
    def __new__(self, components):
        """ __new__(cls: type, components: Array[IComponent]) """
        pass

    Components = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an array containing the components to add to the toolbox.

Get: Components(self: ToolboxComponentsCreatedEventArgs) -> Array[IComponent]

"""



class ToolboxComponentsCreatedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that handles the System.Drawing.Design.ToolboxItem.ComponentsCreated event.
    
    ToolboxComponentsCreatedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: ToolboxComponentsCreatedEventHandler, sender: object, e: ToolboxComponentsCreatedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: ToolboxComponentsCreatedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ToolboxComponentsCreatedEventHandler, sender: object, e: ToolboxComponentsCreatedEventArgs) """
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


class ToolboxComponentsCreatingEventArgs(EventArgs):
    """
    Provides data for the System.Drawing.Design.ToolboxItem.ComponentsCreating event that occurs when components are added to the toolbox.
    
    ToolboxComponentsCreatingEventArgs(host: IDesignerHost)
    """
    @staticmethod # known case of __new__
    def __new__(self, host):
        """ __new__(cls: type, host: IDesignerHost) """
        pass

    DesignerHost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an instance of the System.ComponentModel.Design.IDesignerHost that made the request to create toolbox components.

Get: DesignerHost(self: ToolboxComponentsCreatingEventArgs) -> IDesignerHost

"""



class ToolboxComponentsCreatingEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that handles the System.Drawing.Design.ToolboxItem.ComponentsCreating event.
    
    ToolboxComponentsCreatingEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: ToolboxComponentsCreatingEventHandler, sender: object, e: ToolboxComponentsCreatingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: ToolboxComponentsCreatingEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ToolboxComponentsCreatingEventHandler, sender: object, e: ToolboxComponentsCreatingEventArgs) """
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


class ToolboxItem(object, ISerializable):
    """
    Provides a base implementation of a toolbox item.
    
    ToolboxItem()
    ToolboxItem(toolType: Type)
    """
    def CheckUnlocked(self, *args): #cannot find CLR method
        """
        CheckUnlocked(self: ToolboxItem)
            Throws an exception if the toolbox item is currently locked.
        """
        pass

    def CreateComponents(self, host=None, defaultValues=None):
        """
        CreateComponents(self: ToolboxItem, host: IDesignerHost, defaultValues: IDictionary) -> Array[IComponent]
        
            Creates the components that the toolbox item is configured to create, using the specified 
             designer host and default values.
        
        
            host: The System.ComponentModel.Design.IDesignerHost to use when creating the components.
            defaultValues: A dictionary of property name/value pairs of default values with which to initialize the 
             component.
        
            Returns: An array of created System.ComponentModel.IComponent objects.
        CreateComponents(self: ToolboxItem, host: IDesignerHost) -> Array[IComponent]
        
            Creates the components that the toolbox item is configured to create, using the specified 
             designer host.
        
        
            host: The System.ComponentModel.Design.IDesignerHost to use when creating the components.
            Returns: An array of created System.ComponentModel.IComponent objects.
        CreateComponents(self: ToolboxItem) -> Array[IComponent]
        
            Creates the components that the toolbox item is configured to create.
            Returns: An array of created System.ComponentModel.IComponent objects.
        """
        pass

    def CreateComponentsCore(self, *args): #cannot find CLR method
        """
        CreateComponentsCore(self: ToolboxItem, host: IDesignerHost, defaultValues: IDictionary) -> Array[IComponent]
        
            Creates an array of components when the toolbox item is invoked.
        
            host: The designer host to use when creating components.
            defaultValues: A dictionary of property name/value pairs of default values with which to initialize the 
             component.
        
            Returns: An array of created System.ComponentModel.IComponent objects.
        CreateComponentsCore(self: ToolboxItem, host: IDesignerHost) -> Array[IComponent]
        
            Creates a component or an array of components when the toolbox item is invoked.
        
            host: The System.ComponentModel.Design.IDesignerHost to host the toolbox item.
            Returns: An array of created System.ComponentModel.IComponent objects.
        """
        pass

    def Deserialize(self, *args): #cannot find CLR method
        """
        Deserialize(self: ToolboxItem, info: SerializationInfo, context: StreamingContext)
            Loads the state of the toolbox item from the specified serialization information object.
        
            info: The System.Runtime.Serialization.SerializationInfo to load from.
            context: A System.Runtime.Serialization.StreamingContext that indicates the stream characteristics.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: ToolboxItem, obj: object) -> bool
        
            Determines whether two System.Drawing.Design.ToolboxItem instances are equal.
        
            obj: The System.Drawing.Design.ToolboxItem to compare with the current 
             System.Drawing.Design.ToolboxItem.
        
            Returns: true if the specified System.Drawing.Design.ToolboxItem is equal to the current 
             System.Drawing.Design.ToolboxItem; otherwise, false.
        """
        pass

    def FilterPropertyValue(self, *args): #cannot find CLR method
        """
        FilterPropertyValue(self: ToolboxItem, propertyName: str, value: object) -> object
        
            Filters a property value before returning it.
        
            propertyName: The name of the property to filter.
            value: The value against which to filter the property.
            Returns: A filtered property value.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ToolboxItem) -> int
        
            Returns the hash code for this instance.
            Returns: A hash code for the current System.Drawing.Design.ToolboxItem.
        """
        pass

    def GetType(self, host=None):
        """
        GetType(self: ToolboxItem, host: IDesignerHost) -> Type
        
            Enables access to the type associated with the toolbox item.
        
            host: The designer host to query for System.ComponentModel.Design.ITypeResolutionService.
            Returns: The type associated with the toolbox item.
        """
        pass

    def Initialize(self, type):
        """
        Initialize(self: ToolboxItem, type: Type)
            Initializes the current toolbox item with the specified type to create.
        
            type: The System.Type that the toolbox item creates.
        """
        pass

    def Lock(self):
        """
        Lock(self: ToolboxItem)
            Locks the toolbox item and prevents changes to its properties.
        """
        pass

    def OnComponentsCreated(self, *args): #cannot find CLR method
        """
        OnComponentsCreated(self: ToolboxItem, args: ToolboxComponentsCreatedEventArgs)
            Raises the System.Drawing.Design.ToolboxItem.ComponentsCreated event.
        
            args: A System.Drawing.Design.ToolboxComponentsCreatedEventArgs that provides data for the event.
        """
        pass

    def OnComponentsCreating(self, *args): #cannot find CLR method
        """
        OnComponentsCreating(self: ToolboxItem, args: ToolboxComponentsCreatingEventArgs)
            Raises the System.Drawing.Design.ToolboxItem.ComponentsCreating event.
        
            args: A System.Drawing.Design.ToolboxComponentsCreatingEventArgs that provides data for the event.
        """
        pass

    def Serialize(self, *args): #cannot find CLR method
        """
        Serialize(self: ToolboxItem, info: SerializationInfo, context: StreamingContext)
            Saves the state of the toolbox item to the specified serialization information object.
        
            info: The System.Runtime.Serialization.SerializationInfo to save to.
            context: A System.Runtime.Serialization.StreamingContext that indicates the stream characteristics.
        """
        pass

    def ToString(self):
        """
        ToString(self: ToolboxItem) -> str
        
            Returns a System.String that represents the current System.Drawing.Design.ToolboxItem.
            Returns: A System.String that represents the current System.Drawing.Design.ToolboxItem.
        """
        pass

    def ValidatePropertyType(self, *args): #cannot find CLR method
        """
        ValidatePropertyType(self: ToolboxItem, propertyName: str, value: object, expectedType: Type, allowNull: bool)
            Validates that an object is of a given type.
        
            propertyName: The name of the property to validate.
            value: Optional value against which to validate.
            expectedType: The expected type of the property.
            allowNull: true to allow null; otherwise, false.
        """
        pass

    def ValidatePropertyValue(self, *args): #cannot find CLR method
        """
        ValidatePropertyValue(self: ToolboxItem, propertyName: str, value: object) -> object
        
            Validates a property before it is assigned to the property dictionary.
        
            propertyName: The name of the property to validate.
            value: The value against which to validate.
            Returns: The value used to perform validation.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, toolType=None):
        """
        __new__(cls: type)
        __new__(cls: type, toolType: Type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AssemblyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the assembly that contains the type or types that the toolbox item creates.

Get: AssemblyName(self: ToolboxItem) -> AssemblyName

Set: AssemblyName(self: ToolboxItem) = value
"""

    Bitmap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a bitmap to represent the toolbox item in the toolbox.

Get: Bitmap(self: ToolboxItem) -> Bitmap

Set: Bitmap(self: ToolboxItem) = value
"""

    Company = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the company name for this System.Drawing.Design.ToolboxItem.

Get: Company(self: ToolboxItem) -> str

Set: Company(self: ToolboxItem) = value
"""

    ComponentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the component type for this System.Drawing.Design.ToolboxItem.

Get: ComponentType(self: ToolboxItem) -> str

"""

    DependentAssemblies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Reflection.AssemblyName for the toolbox item.

Get: DependentAssemblies(self: ToolboxItem) -> Array[AssemblyName]

Set: DependentAssemblies(self: ToolboxItem) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the description for this System.Drawing.Design.ToolboxItem.

Get: Description(self: ToolboxItem) -> str

Set: Description(self: ToolboxItem) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the display name for the toolbox item.

Get: DisplayName(self: ToolboxItem) -> str

Set: DisplayName(self: ToolboxItem) = value
"""

    Filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the filter that determines whether the toolbox item can be used on a destination component.

Get: Filter(self: ToolboxItem) -> ICollection

Set: Filter(self: ToolboxItem) = value
"""

    IsTransient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the toolbox item is transient.

Get: IsTransient(self: ToolboxItem) -> bool

Set: IsTransient(self: ToolboxItem) = value
"""

    Locked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the System.Drawing.Design.ToolboxItem is currently locked.

Get: Locked(self: ToolboxItem) -> bool

"""

    OriginalBitmap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OriginalBitmap(self: ToolboxItem) -> Bitmap

Set: OriginalBitmap(self: ToolboxItem) = value
"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a dictionary of properties.

Get: Properties(self: ToolboxItem) -> IDictionary

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the fully qualified name of the type of System.ComponentModel.IComponent that the toolbox item creates when invoked.

Get: TypeName(self: ToolboxItem) -> str

Set: TypeName(self: ToolboxItem) = value
"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the version for this System.Drawing.Design.ToolboxItem.

Get: Version(self: ToolboxItem) -> str

"""


    ComponentsCreated = None
    ComponentsCreating = None


class ToolboxItemCollection(ReadOnlyCollectionBase, ICollection, IEnumerable):
    """
    Represents a collection of toolbox items.
    
    ToolboxItemCollection(value: ToolboxItemCollection)
    ToolboxItemCollection(value: Array[ToolboxItem])
    """
    def Contains(self, value):
        """
        Contains(self: ToolboxItemCollection, value: ToolboxItem) -> bool
        
            Indicates whether the collection contains the specified System.Drawing.Design.ToolboxItem.
        
            value: A System.Drawing.Design.ToolboxItem to search the collection for.
            Returns: true if the collection contains the specified object; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: ToolboxItemCollection, array: Array[ToolboxItem], index: int)
            Copies the collection to the specified array beginning with the specified destination index.
        
            array: The array to copy to.
            index: The index to begin copying to.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: ToolboxItemCollection, value: ToolboxItem) -> int
        
            Gets the index of the specified System.Drawing.Design.ToolboxItem, if it exists in the 
             collection.
        
        
            value: A System.Drawing.Design.ToolboxItem to get the index of in the collection.
            Returns: The index of the specified System.Drawing.Design.ToolboxItem.
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

    @staticmethod # known case of __new__
    def __new__(self, value):
        """
        __new__(cls: type, value: ToolboxItemCollection)
        __new__(cls: type, value: Array[ToolboxItem])
        """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of elements contained in the System.Collections.ReadOnlyCollectionBase instance.

"""



class ToolboxItemCreatorCallback(MulticastDelegate, ICloneable, ISerializable):
    """
    Provides a callback mechanism that can create a System.Drawing.Design.ToolboxItem.
    
    ToolboxItemCreatorCallback(object: object, method: IntPtr)
    """
    def BeginInvoke(self, serializedObject, format, callback, object):
        """ BeginInvoke(self: ToolboxItemCreatorCallback, serializedObject: object, format: str, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: ToolboxItemCreatorCallback, result: IAsyncResult) -> ToolboxItem """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, serializedObject, format):
        """ Invoke(self: ToolboxItemCreatorCallback, serializedObject: object, format: str) -> ToolboxItem """
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


class UITypeEditor(object):
    """
    Provides a base class that can be used to design value editors that can provide a user interface (UI) for representing and editing the values of objects of the supported data types.
    
    UITypeEditor()
    """
    def EditValue(self, *__args):
        """
        EditValue(self: UITypeEditor, context: ITypeDescriptorContext, provider: IServiceProvider, value: object) -> object
        
            Edits the specified object's value using the editor style indicated by the 
             System.Drawing.Design.UITypeEditor.GetEditStyle method.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that can be used to gain additional context 
             information.
        
            provider: An System.IServiceProvider that this editor can use to obtain services.
            value: The object to edit.
            Returns: The new value of the object. If the value of the object has not changed, this should return the 
             same object it was passed.
        
        EditValue(self: UITypeEditor, provider: IServiceProvider, value: object) -> object
        
            Edits the value of the specified object using the editor style indicated by the 
             System.Drawing.Design.UITypeEditor.GetEditStyle method.
        
        
            provider: An System.IServiceProvider that this editor can use to obtain services.
            value: The object to edit.
            Returns: The new value of the object.
        """
        pass

    def GetEditStyle(self, context=None):
        """
        GetEditStyle(self: UITypeEditor, context: ITypeDescriptorContext) -> UITypeEditorEditStyle
        
            Gets the editor style used by the 
             System.Drawing.Design.UITypeEditor.EditValue(System.IServiceProvider,System.Object) method.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that can be used to gain additional context 
             information.
        
            Returns: A System.Drawing.Design.UITypeEditorEditStyle value that indicates the style of editor used by 
             the System.Drawing.Design.UITypeEditor.EditValue(System.IServiceProvider,System.Object) method. 
             If the System.Drawing.Design.UITypeEditor does not support this method, then 
             System.Drawing.Design.UITypeEditor.GetEditStyle will return 
             System.Drawing.Design.UITypeEditorEditStyle.None.
        
        GetEditStyle(self: UITypeEditor) -> UITypeEditorEditStyle
        
            Gets the editor style used by the 
             System.Drawing.Design.UITypeEditor.EditValue(System.IServiceProvider,System.Object) method.
        
            Returns: A System.Drawing.Design.UITypeEditorEditStyle enumeration value that indicates the style of 
             editor used by the current System.Drawing.Design.UITypeEditor. By default, this method will 
             return System.Drawing.Design.UITypeEditorEditStyle.None.
        """
        pass

    def GetPaintValueSupported(self, context=None):
        """
        GetPaintValueSupported(self: UITypeEditor, context: ITypeDescriptorContext) -> bool
        
            Indicates whether the specified context supports painting a representation of an object's value 
             within the specified context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that can be used to gain additional context 
             information.
        
            Returns: true if 
             System.Drawing.Design.UITypeEditor.PaintValue(System.Object,System.Drawing.Graphics,System.Drawin
             g.Rectangle) is implemented; otherwise, false.
        
        GetPaintValueSupported(self: UITypeEditor) -> bool
        
            Indicates whether this editor supports painting a representation of an object's value.
            Returns: true if 
             System.Drawing.Design.UITypeEditor.PaintValue(System.Object,System.Drawing.Graphics,System.Drawin
             g.Rectangle) is implemented; otherwise, false.
        """
        pass

    def PaintValue(self, *__args):
        """
        PaintValue(self: UITypeEditor, e: PaintValueEventArgs)
            Paints a representation of the value of an object using the specified 
             System.Drawing.Design.PaintValueEventArgs.
        
        
            e: A System.Drawing.Design.PaintValueEventArgs that indicates what to paint and where to paint it.
        PaintValue(self: UITypeEditor, value: object, canvas: Graphics, rectangle: Rectangle)
            Paints a representation of the value of the specified object to the specified canvas.
        
            value: The object whose value this type editor will display.
            canvas: A drawing canvas on which to paint the representation of the object's value.
            rectangle: A System.Drawing.Rectangle within whose boundaries to paint the value.
        """
        pass

    IsDropDownResizable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether drop-down editors should be resizable by the user.

Get: IsDropDownResizable(self: UITypeEditor) -> bool

"""



class UITypeEditorEditStyle(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies identifiers that indicate the value editing style of a System.Drawing.Design.UITypeEditor.
    
    enum UITypeEditorEditStyle, values: DropDown (3), Modal (2), None (1)
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

    DropDown = None
    Modal = None
    None = None
    value__ = None


