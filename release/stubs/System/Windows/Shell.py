# encoding: utf-8
# module System.Windows.Shell calls itself Shell
# from PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class JumpItem(object):
    """ Represents the base class for the System.Windows.Shell.JumpPath and System.Windows.Shell.JumpTask classes. """
    CustomCategory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the category the System.Windows.Shell.JumpItem is grouped with in the Windows 7�taskbar Jump List.

Get: CustomCategory(self: JumpItem) -> str

Set: CustomCategory(self: JumpItem) = value
"""



class JumpItemRejectionReason(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes why a System.Windows.Shell.JumpItem could not be added to the Jump List by the Windows shell.
    
    enum JumpItemRejectionReason, values: InvalidItem (1), None (0), NoRegisteredHandler (2), RemovedByUser (3)
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

    InvalidItem = None
    None = None
    NoRegisteredHandler = None
    RemovedByUser = None
    value__ = None


class JumpItemsRejectedEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Shell.JumpList.JumpItemsRejected event.
    
    JumpItemsRejectedEventArgs()
    JumpItemsRejectedEventArgs(rejectedItems: IList[JumpItem], reasons: IList[JumpItemRejectionReason])
    """
    @staticmethod # known case of __new__
    def __new__(self, rejectedItems=None, reasons=None):
        """
        __new__(cls: type)
        __new__(cls: type, rejectedItems: IList[JumpItem], reasons: IList[JumpItemRejectionReason])
        """
        pass

    RejectedItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of Jump List items that could not be added to the Jump List by the Windows shell.

Get: RejectedItems(self: JumpItemsRejectedEventArgs) -> IList[JumpItem]

"""

    RejectionReasons = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of reasons why the rejected Jump List items could not be added to the Jump List.

Get: RejectionReasons(self: JumpItemsRejectedEventArgs) -> IList[JumpItemRejectionReason]

"""



class JumpItemsRemovedEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Shell.JumpList.JumpItemsRemovedByUser event.
    
    JumpItemsRemovedEventArgs()
    JumpItemsRemovedEventArgs(removedItems: IList[JumpItem])
    """
    @staticmethod # known case of __new__
    def __new__(self, removedItems=None):
        """
        __new__(cls: type)
        __new__(cls: type, removedItems: IList[JumpItem])
        """
        pass

    RemovedItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of Jump List items that have been removed by the user since the System.Windows.Shell.JumpList.Apply method was last called.

Get: RemovedItems(self: JumpItemsRemovedEventArgs) -> IList[JumpItem]

"""



class JumpList(object, ISupportInitialize):
    """
    Represents a list of items and tasks displayed as a menu on a Windows 7 taskbar button.
    
    JumpList()
    JumpList(items: IEnumerable[JumpItem], showFrequent: bool, showRecent: bool)
    """
    @staticmethod
    def AddToRecentCategory(*__args):
        """
        AddToRecentCategory(jumpTask: JumpTask)
            Adds the specified jump task to the Recent category of the Jump List.
        
            jumpTask: The System.Windows.Shell.JumpTask to add to the Jump List.
        AddToRecentCategory(jumpPath: JumpPath)
            Adds the specified jump path to the Recent category of the Jump List.
        
            jumpPath: The System.Windows.Shell.JumpPath to add to the Jump List.
        AddToRecentCategory(itemPath: str)
            Adds the specified item path to the Recent category of the Jump List.
        
            itemPath: The path to add to the Jump List.
        """
        pass

    def Apply(self):
        """
        Apply(self: JumpList)
            Sends the System.Windows.Shell.JumpList to the Windows shell in its current state.
        """
        pass

    def BeginInit(self):
        """
        BeginInit(self: JumpList)
            Signals the start of the System.Windows.Shell.JumpList initialization.
        """
        pass

    def EndInit(self):
        """
        EndInit(self: JumpList)
            Signals the end of the System.Windows.Shell.JumpList initialization.
        """
        pass

    @staticmethod
    def GetJumpList(application):
        """
        GetJumpList(application: Application) -> JumpList
        
            Returns the System.Windows.Shell.JumpList object associated with an application.
        
            application: The application associated with the System.Windows.Shell.JumpList.
            Returns: The System.Windows.Shell.JumpList object associated with the specified application.
        """
        pass

    @staticmethod
    def SetJumpList(application, value):
        """
        SetJumpList(application: Application, value: JumpList)
            Sets the System.Windows.Shell.JumpList object associated with an application.
        
            application: The application associated with the System.Windows.Shell.JumpList.
            value: The System.Windows.Shell.JumpList to associate with the application.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, items=None, showFrequent=None, showRecent=None):
        """
        __new__(cls: type)
        __new__(cls: type, items: IEnumerable[JumpItem], showFrequent: bool, showRecent: bool)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    JumpItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of System.Windows.Shell.JumpItem objects that are displayed in the Jump List.

Get: JumpItems(self: JumpList) -> List[JumpItem]

"""

    ShowFrequentCategory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether frequently used items are displayed in the Jump List.

Get: ShowFrequentCategory(self: JumpList) -> bool

Set: ShowFrequentCategory(self: JumpList) = value
"""

    ShowRecentCategory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether recently used items are displayed in the Jump List.

Get: ShowRecentCategory(self: JumpList) -> bool

Set: ShowRecentCategory(self: JumpList) = value
"""


    JumpItemsRejected = None
    JumpItemsRemovedByUser = None


class JumpPath(JumpItem):
    """
    Represents a link to a file that is displayed in a Windows 7 taskbar Jump List.
    
    JumpPath()
    """
    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the path to the file to be included in the Jump List.

Get: Path(self: JumpPath) -> str

Set: Path(self: JumpPath) = value
"""



class JumpTask(JumpItem):
    """
    Represents a shortcut to an application in the Windows 7 taskbar Jump List.
    
    JumpTask()
    """
    ApplicationPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the path to the application.

Get: ApplicationPath(self: JumpTask) -> str

Set: ApplicationPath(self: JumpTask) = value
"""

    Arguments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the arguments passed to the application on startup.

Get: Arguments(self: JumpTask) -> str

Set: Arguments(self: JumpTask) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the text displayed in the tooltip for the task in the Jump List.

Get: Description(self: JumpTask) -> str

Set: Description(self: JumpTask) = value
"""

    IconResourceIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the zero-based index of an icon embedded in a resource.

Get: IconResourceIndex(self: JumpTask) -> int

Set: IconResourceIndex(self: JumpTask) = value
"""

    IconResourcePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the path to a resource that contains the icon to display in the Jump List.

Get: IconResourcePath(self: JumpTask) -> str

Set: IconResourcePath(self: JumpTask) = value
"""

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the text displayed for the task in the Jump List.

Get: Title(self: JumpTask) -> str

Set: Title(self: JumpTask) = value
"""

    WorkingDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the working directory of the application on startup.

Get: WorkingDirectory(self: JumpTask) -> str

Set: WorkingDirectory(self: JumpTask) = value
"""



class NonClientFrameEdges(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) NonClientFrameEdges, values: Bottom (8), Left (1), None (0), Right (4), Top (2) """
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

    Bottom = None
    Left = None
    None = None
    Right = None
    Top = None
    value__ = None


class ResizeGripDirection(Enum, IComparable, IFormattable, IConvertible):
    """ enum ResizeGripDirection, values: Bottom (6), BottomLeft (7), BottomRight (5), Left (8), None (0), Right (4), Top (2), TopLeft (1), TopRight (3) """
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

    Bottom = None
    BottomLeft = None
    BottomRight = None
    Left = None
    None = None
    Right = None
    Top = None
    TopLeft = None
    TopRight = None
    value__ = None


class TaskbarItemInfo(Freezable, ISealable):
    """
    Represents information about how the taskbar thumbnail is displayed.
    
    TaskbarItemInfo()
    """
    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a clone (deep copy) of the specified System.Windows.Freezable using base 
             (non-animated) property values.
        
        
            sourceFreezable: The object to clone.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a modifiable clone (deep copy) of the specified System.Windows.Freezable 
             using current property values.
        
        
            sourceFreezable: The System.Windows.Freezable to be cloned.
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
        """ CreateInstanceCore(self: TaskbarItemInfo) -> Freezable """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: Freezable, isChecking: bool) -> bool
        
            Makes the System.Windows.Freezable object unmodifiable or tests whether it can be made 
             unmodifiable.
        
        
            isChecking: true to return an indication of whether the object can be frozen (without actually freezing it); 
             false to actually freeze the object.
        
            Returns: If isChecking is true, this method returns true if the System.Windows.Freezable can be made 
             unmodifiable, or false if it cannot be made unmodifiable. If isChecking is false, this method 
             returns true if the if the specified System.Windows.Freezable is now unmodifiable, or false if 
             it cannot be made unmodifiable.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a frozen clone of the specified System.Windows.Freezable using base 
             (non-animated) property values.
        
        
            sourceFreezable: The instance to copy.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the current instance a frozen clone of the specified System.Windows.Freezable. If the 
             object has animated dependency properties, their current animated values are copied.
        
        
            sourceFreezable: The System.Windows.Freezable to copy and freeze.
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
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the text for the taskbar item tooltip.

Get: Description(self: TaskbarItemInfo) -> str

Set: Description(self: TaskbarItemInfo) = value
"""

    Overlay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the image that is displayed over the program icon in the taskbar button.

Get: Overlay(self: TaskbarItemInfo) -> ImageSource

Set: Overlay(self: TaskbarItemInfo) = value
"""

    ProgressState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates how the progress indicator is displayed in the taskbar button.

Get: ProgressState(self: TaskbarItemInfo) -> TaskbarItemProgressState

Set: ProgressState(self: TaskbarItemInfo) = value
"""

    ProgressValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates the fullness of the progress indicator in the taskbar button.

Get: ProgressValue(self: TaskbarItemInfo) -> float

Set: ProgressValue(self: TaskbarItemInfo) = value
"""

    ThumbButtonInfos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the collection of System.Windows.Shell.ThumbButtonInfo objects that are associated with the System.Windows.Window.

Get: ThumbButtonInfos(self: TaskbarItemInfo) -> ThumbButtonInfoCollection

Set: ThumbButtonInfos(self: TaskbarItemInfo) = value
"""

    ThumbnailClipMargin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that specifies the part of the application window's client area that is displayed in the taskbar thumbnail.

Get: ThumbnailClipMargin(self: TaskbarItemInfo) -> Thickness

Set: ThumbnailClipMargin(self: TaskbarItemInfo) = value
"""


    DescriptionProperty = None
    OverlayProperty = None
    ProgressStateProperty = None
    ProgressValueProperty = None
    ThumbButtonInfosProperty = None
    ThumbnailClipMarginProperty = None


class TaskbarItemProgressState(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the state of the progress indicator in the Windows taskbar.
    
    enum TaskbarItemProgressState, values: Error (3), Indeterminate (1), None (0), Normal (2), Paused (4)
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

    Error = None
    Indeterminate = None
    None = None
    Normal = None
    Paused = None
    value__ = None


class ThumbButtonInfo(Freezable, ISealable, ICommandSource):
    """
    Represents information about how to display a button in the Windows 7�taskbar thumbnail.
    
    ThumbButtonInfo()
    """
    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a clone (deep copy) of the specified System.Windows.Freezable using base 
             (non-animated) property values.
        
        
            sourceFreezable: The object to clone.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a modifiable clone (deep copy) of the specified System.Windows.Freezable 
             using current property values.
        
        
            sourceFreezable: The System.Windows.Freezable to be cloned.
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
        """ CreateInstanceCore(self: ThumbButtonInfo) -> Freezable """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: Freezable, isChecking: bool) -> bool
        
            Makes the System.Windows.Freezable object unmodifiable or tests whether it can be made 
             unmodifiable.
        
        
            isChecking: true to return an indication of whether the object can be frozen (without actually freezing it); 
             false to actually freeze the object.
        
            Returns: If isChecking is true, this method returns true if the System.Windows.Freezable can be made 
             unmodifiable, or false if it cannot be made unmodifiable. If isChecking is false, this method 
             returns true if the if the specified System.Windows.Freezable is now unmodifiable, or false if 
             it cannot be made unmodifiable.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a frozen clone of the specified System.Windows.Freezable using base 
             (non-animated) property values.
        
        
            sourceFreezable: The instance to copy.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the current instance a frozen clone of the specified System.Windows.Freezable. If the 
             object has animated dependency properties, their current animated values are copied.
        
        
            sourceFreezable: The System.Windows.Freezable to copy and freeze.
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
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Command = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the command to invoke when this thumbnail button is clicked.

Get: Command(self: ThumbButtonInfo) -> ICommand

Set: Command(self: ThumbButtonInfo) = value
"""

    CommandParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the parameter to pass to the System.Windows.Shell.ThumbButtonInfo.Command property.

Get: CommandParameter(self: ThumbButtonInfo) -> object

Set: CommandParameter(self: ThumbButtonInfo) = value
"""

    CommandTarget = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element on which to raise the specified command.

Get: CommandTarget(self: ThumbButtonInfo) -> IInputElement

Set: CommandTarget(self: ThumbButtonInfo) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the text to display for the thumbnail button tooltip.

Get: Description(self: ThumbButtonInfo) -> str

Set: Description(self: ThumbButtonInfo) = value
"""

    DismissWhenClicked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the taskbar thumbnail closes when the thumbnail button is clicked.

Get: DismissWhenClicked(self: ThumbButtonInfo) -> bool

Set: DismissWhenClicked(self: ThumbButtonInfo) = value
"""

    ImageSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the image that is displayed on the thumbnail button.

Get: ImageSource(self: ThumbButtonInfo) -> ImageSource

Set: ImageSource(self: ThumbButtonInfo) = value
"""

    IsBackgroundVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether a border and highlight is displayed around the thumbnail button.

Get: IsBackgroundVisible(self: ThumbButtonInfo) -> bool

Set: IsBackgroundVisible(self: ThumbButtonInfo) = value
"""

    IsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the thumbnail button is enabled.

Get: IsEnabled(self: ThumbButtonInfo) -> bool

Set: IsEnabled(self: ThumbButtonInfo) = value
"""

    IsInteractive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the user can interact with the thumbnail button.

Get: IsInteractive(self: ThumbButtonInfo) -> bool

Set: IsInteractive(self: ThumbButtonInfo) = value
"""

    Visibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that specifies the display state of the thumbnail button.

Get: Visibility(self: ThumbButtonInfo) -> Visibility

Set: Visibility(self: ThumbButtonInfo) = value
"""


    Click = None
    CommandParameterProperty = None
    CommandProperty = None
    CommandTargetProperty = None
    DescriptionProperty = None
    DismissWhenClickedProperty = None
    ImageSourceProperty = None
    IsBackgroundVisibleProperty = None
    IsEnabledProperty = None
    IsInteractiveProperty = None
    VisibilityProperty = None


class ThumbButtonInfoCollection(FreezableCollection[ThumbButtonInfo], ISealable, IAnimatable, IResource, IList, ICollection, IEnumerable, IList[ThumbButtonInfo], ICollection[ThumbButtonInfo], IEnumerable[ThumbButtonInfo], INotifyCollectionChanged, INotifyPropertyChanged):
    """
    Represents a collection of System.Windows.Shell.ThumbButtonInfo objects that are associated with a System.Windows.Window.
    
    ThumbButtonInfoCollection()
    """
    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: FreezableCollection[ThumbButtonInfo], source: Freezable)
            Makes this instance a clone (deep copy) of the specified System.Windows.FreezableCollection 
             using base (non-animated) property values.
        
        
            source: The System.Windows.FreezableCollection to copy.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: FreezableCollection[ThumbButtonInfo], source: Freezable)
            Makes this instance a modifiable clone (deep copy) of the specified 
             System.Windows.FreezableCollection using current property values.
        
        
            source: The System.Windows.FreezableCollection to clone.
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
        CreateInstanceCore(self: ThumbButtonInfoCollection) -> Freezable
        
            Creates a new instance of the collection.
            Returns: The new instance of the collection.
        """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: FreezableCollection[ThumbButtonInfo], isChecking: bool) -> bool
        
            Makes this System.Windows.FreezableCollection object unmodifiable or determines whether it can 
             be made unmodifiable.
        
        
            isChecking: true if the System.Windows.FreezableCollection should simply return whether it can be frozen. 
             false if the System.Windows.FreezableCollection instance should actually freeze itself when this 
             method is called.
        
            Returns: If isChecking is true, this method returns true if this System.Windows.FreezableCollection can 
             be made unmodifiable, or false if it cannot be made unmodifiable. If isChecking is false, this 
             method returns true if the if the specified System.Windows.FreezableCollection is now 
             unmodifiable, or false if it cannot be made unmodifiable, with the side effect of having begun 
             to change the frozen status of this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: FreezableCollection[ThumbButtonInfo], source: Freezable)
            Makes this instance a frozen clone of the specified System.Windows.FreezableCollection using 
             base (non-animated) property values.
        
        
            source: The System.Windows.FreezableCollection to copy.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: FreezableCollection[ThumbButtonInfo], source: Freezable)
            Makes this instance a frozen clone of the specified System.Windows.Freezable. If this object has 
             animated dependency properties, their current animated values are copied.
        
        
            source: The System.Windows.FreezableCollection to copy.
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
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
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

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass


class WindowChrome(Freezable, ISealable):
    """ WindowChrome() """
    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a clone (deep copy) of the specified System.Windows.Freezable using base 
             (non-animated) property values.
        
        
            sourceFreezable: The object to clone.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a modifiable clone (deep copy) of the specified System.Windows.Freezable 
             using current property values.
        
        
            sourceFreezable: The System.Windows.Freezable to be cloned.
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
        """ CreateInstanceCore(self: WindowChrome) -> Freezable """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: Freezable, isChecking: bool) -> bool
        
            Makes the System.Windows.Freezable object unmodifiable or tests whether it can be made 
             unmodifiable.
        
        
            isChecking: true to return an indication of whether the object can be frozen (without actually freezing it); 
             false to actually freeze the object.
        
            Returns: If isChecking is true, this method returns true if the System.Windows.Freezable can be made 
             unmodifiable, or false if it cannot be made unmodifiable. If isChecking is false, this method 
             returns true if the if the specified System.Windows.Freezable is now unmodifiable, or false if 
             it cannot be made unmodifiable.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a frozen clone of the specified System.Windows.Freezable using base 
             (non-animated) property values.
        
        
            sourceFreezable: The instance to copy.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the current instance a frozen clone of the specified System.Windows.Freezable. If the 
             object has animated dependency properties, their current animated values are copied.
        
        
            sourceFreezable: The System.Windows.Freezable to copy and freeze.
        """
        pass

    @staticmethod
    def GetIsHitTestVisibleInChrome(inputElement):
        """ GetIsHitTestVisibleInChrome(inputElement: IInputElement) -> bool """
        pass

    @staticmethod
    def GetResizeGripDirection(inputElement):
        """ GetResizeGripDirection(inputElement: IInputElement) -> ResizeGripDirection """
        pass

    @staticmethod
    def GetWindowChrome(window):
        """ GetWindowChrome(window: Window) -> WindowChrome """
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
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    @staticmethod
    def SetIsHitTestVisibleInChrome(inputElement, hitTestVisible):
        """ SetIsHitTestVisibleInChrome(inputElement: IInputElement, hitTestVisible: bool) """
        pass

    @staticmethod
    def SetResizeGripDirection(inputElement, direction):
        """ SetResizeGripDirection(inputElement: IInputElement, direction: ResizeGripDirection) """
        pass

    @staticmethod
    def SetWindowChrome(window, chrome):
        """ SetWindowChrome(window: Window, chrome: WindowChrome) """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CaptionHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CaptionHeight(self: WindowChrome) -> float

Set: CaptionHeight(self: WindowChrome) = value
"""

    CornerRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CornerRadius(self: WindowChrome) -> CornerRadius

Set: CornerRadius(self: WindowChrome) = value
"""

    GlassFrameThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlassFrameThickness(self: WindowChrome) -> Thickness

Set: GlassFrameThickness(self: WindowChrome) = value
"""

    NonClientFrameEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NonClientFrameEdges(self: WindowChrome) -> NonClientFrameEdges

Set: NonClientFrameEdges(self: WindowChrome) = value
"""

    ResizeBorderThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResizeBorderThickness(self: WindowChrome) -> Thickness

Set: ResizeBorderThickness(self: WindowChrome) = value
"""

    UseAeroCaptionButtons = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseAeroCaptionButtons(self: WindowChrome) -> bool

Set: UseAeroCaptionButtons(self: WindowChrome) = value
"""


    CaptionHeightProperty = None
    CornerRadiusProperty = None
    GlassFrameCompleteThickness = None
    GlassFrameThicknessProperty = None
    IsHitTestVisibleInChromeProperty = None
    NonClientFrameEdgesProperty = None
    ResizeBorderThicknessProperty = None
    ResizeGripDirectionProperty = None
    UseAeroCaptionButtonsProperty = None
    WindowChromeProperty = None


