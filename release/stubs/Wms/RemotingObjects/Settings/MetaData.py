from System import *
# encoding: utf-8
# module Wms.RemotingObjects.Settings.MetaData calls itself MetaData
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class GetValidValues(MulticastDelegate):
    """ GetValidValues(object: object, method: IntPtr) """
    def BeginInvoke(self, callback, object):
        """ BeginInvoke(self: GetValidValues, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null, if the method represented by the current delegate does 
             not require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: GetValidValues, result: IAsyncResult) -> Hashtable """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self):
        """ Invoke(self: GetValidValues) -> Hashtable """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original 
             invocation list.
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

    Instance = GetValidValues()
    """hardcoded/returns an instance of the class"""

class ISystemSettingsAttribute:
    """ Defines base interface for creating attributes to enricht system settting properties. """
    def UpdateInfo(self, row):
        """ UpdateInfo(self: ISystemSettingsAttribute, row: SystemSettingsTableRow) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Instance = ISystemSettingsAttribute()
    """hardcoded/returns an instance of the class"""

class Group:
    """
    Specify the group, the setting is part of.
    
    Group(sortKey: str, name: str)
    """
    def UpdateInfo(self, row):
        """ UpdateInfo(self: Group, row: SystemSettingsTableRow) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, sortKey, name):
        """ __new__(cls: type, sortKey: str, name: str) """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Name(self: Group) -> str

Set: Name(self: Group) = value
"""

    SortKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SortKey(self: Group) -> str

Set: SortKey(self: Group) = value
"""


    Instance = Group()
    """hardcoded/returns an instance of the class"""

class Label:
    """
    Specify a descriptive name for the setting.
                 Shown in UI.
    
    Label(value: str)
    """
    def UpdateInfo(self, row):
        """ UpdateInfo(self: Label, row: SystemSettingsTableRow) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, value):
        """ __new__(cls: type, value: str) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Value(self: Label) -> str

Set: Value(self: Label) = value
"""


    Instance = Label()
    """hardcoded/returns an instance of the class"""

class MachineSetting:
    """
    Specify if setting is a machine based setting.
    
    MachineSetting()
    """
    def UpdateInfo(self, row):
        """ UpdateInfo(self: MachineSetting, row: SystemSettingsTableRow) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Instance = MachineSetting()
    """hardcoded/returns an instance of the class"""

class MaxLength:
    """
    Specifies maximum length of characters allowed for this property.
    
    MaxLength(value: int)
    """
    def UpdateInfo(self, row):
        """ UpdateInfo(self: MaxLength, row: SystemSettingsTableRow) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, value):
        """ __new__(cls: type, value: int) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Value(self: MaxLength) -> int

Set: Value(self: MaxLength) = value
"""


    Instance = MaxLength()
    """hardcoded/returns an instance of the class"""

class Renderer:
    """
    Specify type of ui editor for setting.
    
    Renderer(value: RenderingTypes)
    """
    def UpdateInfo(self, row):
        """ UpdateInfo(self: Renderer, row: SystemSettingsTableRow) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, value):
        """ __new__(cls: type, value: RenderingTypes) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Value(self: Renderer) -> RenderingTypes

Set: Value(self: Renderer) = value
"""


    Instance = Renderer()
    """hardcoded/returns an instance of the class"""

class RenderingTypes:
    """
    Types of editors that can be used for settings.
    
    enum RenderingTypes, values: Auto (0), PlainTextArea (2), RichTextArea (1), WarehouseCombo (3)
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
    PlainTextArea = None
    RichTextArea = None
    value__ = None
    WarehouseCombo = None

    Instance = RenderingTypes()
    """hardcoded/returns an instance of the class"""

class SettingAttributesHelper():
    """ SettingAttributesHelper() """
    @staticmethod
    def ConvertToTable(settings, topLevelOnly):
        """ ConvertToTable(settings: SystemSettings, topLevelOnly: bool) -> SystemSettingsTable """
        pass

    @staticmethod
    def GetMemberValue(settingsObject, member):
        """ GetMemberValue(settingsObject: object, member: MemberInfo) -> object """
        pass

    Instance = SettingAttributesHelper()
    """hardcoded/returns an instance of the class"""

class UserSetting:
    """
    Specify if setting is a user based setting
    
    UserSetting()
    """
    def UpdateInfo(self, row):
        """ UpdateInfo(self: UserSetting, row: SystemSettingsTableRow) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Instance = UserSetting()
    """hardcoded/returns an instance of the class"""

class ValidValuePattern:
    """
    Specifies a regex pattern for allowed new setting values.
    
    ValidValuePattern(regex: str)
    ValidValuePattern(regex: str, errorMessage: str)
    """
    def UpdateInfo(self, row):
        """ UpdateInfo(self: ValidValuePattern, row: SystemSettingsTableRow) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, regex, errorMessage=None):
        """
        __new__(cls: type, regex: str)
        __new__(cls: type, regex: str, errorMessage: str)
        """
        pass

    Instance = ValidValuePattern()
    """hardcoded/returns an instance of the class"""

class ValidValues:
    """
    Specify valid values for setting.
    
    ValidValues(delegateName: str)
    """
    def UpdateInfo(self, row):
        """ UpdateInfo(self: ValidValues, row: SystemSettingsTableRow) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, delegateName):
        """ __new__(cls: type, delegateName: str) """
        pass

    DelegateName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DelegateName(self: ValidValues) -> str

Set: DelegateName(self: ValidValues) = value
"""


    Instance = ValidValues()
    """hardcoded/returns an instance of the class"""

