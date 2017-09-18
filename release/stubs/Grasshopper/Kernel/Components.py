# encoding: utf-8
# module Grasshopper.Kernel.Components calls itself Components
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GH_CleanComponentUpgrader(object, IGH_UpgradeObject):
    """ GH_CleanComponentUpgrader() """
    def Upgrade(self, target, document):
        """ Upgrade(self: GH_CleanComponentUpgrader, target: IGH_DocumentObject, document: GH_Document) -> IGH_DocumentObject """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    UpgradeFrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpgradeFrom(self: GH_CleanComponentUpgrader) -> Guid

"""

    UpgradeTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpgradeTo(self: GH_CleanComponentUpgrader) -> Guid

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Version(self: GH_CleanComponentUpgrader) -> DateTime

"""



class GH_CleanTreeComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject, IGH_VariableParameterComponent):
    """ GH_CleanTreeComponent() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def CanInsertParameter(self, side, index):
        """ CanInsertParameter(self: GH_CleanTreeComponent, side: GH_ParameterSide, index: int) -> bool """
        pass

    def CanRemoveParameter(self, side, index):
        """ CanRemoveParameter(self: GH_CleanTreeComponent, side: GH_ParameterSide, index: int) -> bool """
        pass

    def CreateParameter(self, side, index):
        """ CreateParameter(self: GH_CleanTreeComponent, side: GH_ParameterSide, index: int) -> IGH_Param """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def DestroyParameter(self, side, index):
        """ DestroyParameter(self: GH_CleanTreeComponent, side: GH_ParameterSide, index: int) -> bool """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_CleanTreeComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_CleanTreeComponent, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_CleanTreeComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def VariableParameterMaintenance(self):
        """ VariableParameterMaintenance(self: GH_CleanTreeComponent) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_CleanTreeComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_CleanTreeComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_CleanTreeComponent_OBSOLETE(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_CleanTreeComponent_OBSOLETE() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_CleanTreeComponent_OBSOLETE, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_CleanTreeComponent_OBSOLETE, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_CleanTreeComponent_OBSOLETE, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_CleanTreeComponent_OBSOLETE) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_CleanTreeComponent_OBSOLETE) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_CleanTreeComponent_OSBOLETE_AS_WELL(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_CleanTreeComponent_OSBOLETE_AS_WELL() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_CleanTreeComponent_OSBOLETE_AS_WELL, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_CleanTreeComponent_OSBOLETE_AS_WELL, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_CleanTreeComponent_OSBOLETE_AS_WELL, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_CleanTreeComponent_OSBOLETE_AS_WELL) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_CleanTreeComponent_OSBOLETE_AS_WELL) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_CurvatureGraphComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_CurvatureGraphComponent() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def ClearData(self):
        """ ClearData(self: GH_CurvatureGraphComponent) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def DrawViewportWires(self, args):
        """ DrawViewportWires(self: GH_CurvatureGraphComponent, args: IGH_PreviewArgs) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_CurvatureGraphComponent) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_CurvatureGraphComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_CurvatureGraphComponent, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_CurvatureGraphComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_CurvatureGraphComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_CurvatureGraphComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_CustomPreviewComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_CustomPreviewComponent() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_CustomPreviewComponent, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def ClearData(self):
        """ ClearData(self: GH_CustomPreviewComponent) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def DrawViewportMeshes(self, args):
        """ DrawViewportMeshes(self: GH_CustomPreviewComponent, args: IGH_PreviewArgs) """
        pass

    def DrawViewportWires(self, args):
        """ DrawViewportWires(self: GH_CustomPreviewComponent, args: IGH_PreviewArgs) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def Read(self, reader):
        """ Read(self: GH_CustomPreviewComponent, reader: GH_IReader) -> bool """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_CustomPreviewComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_CustomPreviewComponent, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_CustomPreviewComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def Write(self, writer):
        """ Write(self: GH_CustomPreviewComponent, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ClippingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClippingBox(self: GH_CustomPreviewComponent) -> BoundingBox

"""

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_CustomPreviewComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_CustomPreviewComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ViewportFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewportFilter(self: GH_CustomPreviewComponent) -> str

Set: ViewportFilter(self: GH_CustomPreviewComponent) = value
"""


    m_attributes = None


class GH_DataDamAttributes(GH_ComponentAttributes, IGH_Attributes, GH_ISerializable, IGH_ResponsiveObject, IGH_TooltipAwareObject):
    """ GH_DataDamAttributes(owner: GH_DataDamComponent) """
    def Layout(self, *args): #cannot find CLR method
        """ Layout(self: GH_DataDamAttributes) """
        pass

    def PrepareForRender(self, *args): #cannot find CLR method
        """ PrepareForRender(self: GH_Attributes[IGH_Component], canvas: GH_Canvas) """
        pass

    def Render(self, *args): #cannot find CLR method
        """ Render(self: GH_DataDamAttributes, canvas: GH_Canvas, graphics: Graphics, channel: GH_CanvasChannel) """
        pass

    def RenderComponentCapsule(self, *args): #cannot find CLR method
        """ RenderComponentCapsule(self: GH_ComponentAttributes, canvas: GH_Canvas, graphics: Graphics, drawComponentBaseBox: bool, drawComponentNameBox: bool, drawJaggedEdges: bool, drawParameterGrips: bool, drawParameterNames: bool, drawZuiElements: bool)RenderComponentCapsule(self: GH_ComponentAttributes, canvas: GH_Canvas, graphics: Graphics) """
        pass

    def RenderIncomingWires(self, *args): #cannot find CLR method
        """ RenderIncomingWires(self: GH_Attributes[IGH_Component], painter: GH_Painter, sources: IEnumerable[IGH_Param], styles: IEnumerable[Pen])RenderIncomingWires(self: GH_Attributes[IGH_Component], painter: GH_Painter, sources: IEnumerable[IGH_Param], style: GH_ParamWireDisplay) """
        pass

    def RenderVariableParameterUI(self, *args): #cannot find CLR method
        """ RenderVariableParameterUI(self: GH_ComponentAttributes, canvas: GH_Canvas, graphics: Graphics) """
        pass

    def RespondToMouseMove(self, sender, e):
        """ RespondToMouseMove(self: GH_DataDamAttributes, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseUp(self, sender, e):
        """ RespondToMouseUp(self: GH_DataDamAttributes, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def SetupTooltip(self, canvasPoint, e):
        """ SetupTooltip(self: GH_DataDamAttributes, canvasPoint: PointF, e: GH_TooltipDisplayEventArgs) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, owner):
        """ __new__(cls: type, owner: GH_DataDamComponent) """
        pass

    m_innerBounds = None


class GH_DataDamComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject, IGH_VariableParameterComponent):
    """ GH_DataDamComponent() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AppendMenuItems(self, menu):
        """ AppendMenuItems(self: GH_DataDamComponent, menu: ToolStripDropDown) -> bool """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def CanInsertParameter(self, side, index):
        """ CanInsertParameter(self: GH_DataDamComponent, side: GH_ParameterSide, index: int) -> bool """
        pass

    def CanRemoveParameter(self, side, index):
        """ CanRemoveParameter(self: GH_DataDamComponent, side: GH_ParameterSide, index: int) -> bool """
        pass

    def CreateAttributes(self):
        """ CreateAttributes(self: GH_DataDamComponent) """
        pass

    def CreateParameter(self, side, index):
        """ CreateParameter(self: GH_DataDamComponent, side: GH_ParameterSide, index: int) -> IGH_Param """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def DestroyParameter(self, side, index):
        """ DestroyParameter(self: GH_DataDamComponent, side: GH_ParameterSide, index: int) -> bool """
        pass

    def DocumentContextChanged(self, document, context):
        """ DocumentContextChanged(self: GH_DataDamComponent, document: GH_Document, context: GH_DocumentContext) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def ExpireSolution(self, recompute):
        """ ExpireSolution(self: GH_DataDamComponent, recompute: bool) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def Read(self, reader):
        """ Read(self: GH_DataDamComponent, reader: GH_IReader) -> bool """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_DataDamComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_DataDamComponent, pManager: GH_OutputParamManager) """
        pass

    def RemovedFromDocument(self, document):
        """ RemovedFromDocument(self: GH_DataDamComponent, document: GH_Document) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_DataDamComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def VariableParameterMaintenance(self):
        """ VariableParameterMaintenance(self: GH_DataDamComponent) """
        pass

    def Write(self, writer):
        """ Write(self: GH_DataDamComponent, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_DataDamComponent) -> Guid

"""

    Delay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Delay(self: GH_DataDamComponent) -> TimeSpan

Set: Delay(self: GH_DataDamComponent) = value
"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_DataDamComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Mode(self: GH_DataDamComponent) -> BufferMode

Set: Mode(self: GH_DataDamComponent) = value
"""

    TransferPossible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransferPossible(self: GH_DataDamComponent) -> bool

"""


    BufferMode = None
    m_attributes = None


class GH_DocExampleComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_DocExampleComponent() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_DocExampleComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_DocExampleComponent, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_DocExampleComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_DocExampleComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_DocExampleComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_ExplodeTreeComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject, IGH_VariableParameterComponent):
    """ GH_ExplodeTreeComponent() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_ExplodeTreeComponent, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def CanInsertParameter(self, side, index):
        """ CanInsertParameter(self: GH_ExplodeTreeComponent, side: GH_ParameterSide, index: int) -> bool """
        pass

    def CanRemoveParameter(self, side, index):
        """ CanRemoveParameter(self: GH_ExplodeTreeComponent, side: GH_ParameterSide, index: int) -> bool """
        pass

    def CreateParameter(self, side, index):
        """ CreateParameter(self: GH_ExplodeTreeComponent, side: GH_ParameterSide, index: int) -> IGH_Param """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def DestroyParameter(self, side, index):
        """ DestroyParameter(self: GH_ExplodeTreeComponent, side: GH_ParameterSide, index: int) -> bool """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_ExplodeTreeComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_ExplodeTreeComponent, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_ExplodeTreeComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def VariableParameterMaintenance(self):
        """ VariableParameterMaintenance(self: GH_ExplodeTreeComponent) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_ExplodeTreeComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_ExplodeTreeComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_ExplodeTreeComponent_OBSOLETE(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject, IGH_VarParamComponent):
    """ GH_ExplodeTreeComponent_OBSOLETE() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def ConstructVariable(self, e):
        """ ConstructVariable(self: GH_ExplodeTreeComponent_OBSOLETE, e: GH_VarParamEventArgs) -> IGH_Param """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def IsVariableParam(self, e):
        """ IsVariableParam(self: GH_ExplodeTreeComponent_OBSOLETE, e: GH_VarParamEventArgs) -> bool """
        pass

    def ManagerConstructed(self, side, manager):
        """ ManagerConstructed(self: GH_ExplodeTreeComponent_OBSOLETE, side: GH_VarParamSide, manager: GH_VariableParameterManager) """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def ParametersModified(self, side):
        """ ParametersModified(self: GH_ExplodeTreeComponent_OBSOLETE, side: GH_VarParamSide) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_ExplodeTreeComponent_OBSOLETE, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_ExplodeTreeComponent_OBSOLETE, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_ExplodeTreeComponent_OBSOLETE, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_ExplodeTreeComponent_OBSOLETE) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_ExplodeTreeComponent_OBSOLETE) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsInputVariable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInputVariable(self: GH_ExplodeTreeComponent_OBSOLETE) -> bool

"""

    IsOutputVariable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOutputVariable(self: GH_ExplodeTreeComponent_OBSOLETE) -> bool

"""


    m_attributes = None


class GH_FlattenComponentUpgrader(object, IGH_UpgradeObject):
    """ GH_FlattenComponentUpgrader() """
    def Upgrade(self, target, document):
        """ Upgrade(self: GH_FlattenComponentUpgrader, target: IGH_DocumentObject, document: GH_Document) -> IGH_DocumentObject """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    UpgradeFrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpgradeFrom(self: GH_FlattenComponentUpgrader) -> Guid

"""

    UpgradeTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpgradeTo(self: GH_FlattenComponentUpgrader) -> Guid

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Version(self: GH_FlattenComponentUpgrader) -> DateTime

"""



class GH_FlattenTreeComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_FlattenTreeComponent() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_FlattenTreeComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_FlattenTreeComponent, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_FlattenTreeComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_FlattenTreeComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_FlattenTreeComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_FlattenTreeComponent_OBSOLETE(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_FlattenTreeComponent_OBSOLETE() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_FlattenTreeComponent_OBSOLETE, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_FlattenTreeComponent_OBSOLETE, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_FlattenTreeComponent_OBSOLETE, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_FlattenTreeComponent_OBSOLETE) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_FlattenTreeComponent_OBSOLETE) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_FlipDataMatrixComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_FlipDataMatrixComponent() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_FlipDataMatrixComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_FlipDataMatrixComponent, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_FlipDataMatrixComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_FlipDataMatrixComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_FlipDataMatrixComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_GraftTreeComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_GraftTreeComponent() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_GraftTreeComponent, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def Read(self, reader):
        """ Read(self: GH_GraftTreeComponent, reader: GH_IReader) -> bool """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_GraftTreeComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_GraftTreeComponent, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_GraftTreeComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def Write(self, writer):
        """ Write(self: GH_GraftTreeComponent, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_GraftTreeComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_GraftTreeComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_GraftTreeComponent_OBSOLETE(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_GraftTreeComponent_OBSOLETE() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_GraftTreeComponent_OBSOLETE, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_GraftTreeComponent_OBSOLETE, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_GraftTreeComponent_OBSOLETE, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_GraftTreeComponent_OBSOLETE) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_GraftTreeComponent_OBSOLETE) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_GrasshopperLibraryInfo(GH_AssemblyInfo):
    """ GH_GrasshopperLibraryInfo() """
    AuthorContact = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AuthorContact(self: GH_GrasshopperLibraryInfo) -> str

"""

    AuthorName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AuthorName(self: GH_GrasshopperLibraryInfo) -> str

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: GH_GrasshopperLibraryInfo) -> str

"""

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon(self: GH_GrasshopperLibraryInfo) -> Bitmap

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: GH_GrasshopperLibraryInfo) -> Guid

"""

    License = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: License(self: GH_GrasshopperLibraryInfo) -> GH_LibraryLicense

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: GH_GrasshopperLibraryInfo) -> str

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Version(self: GH_GrasshopperLibraryInfo) -> str

"""



class GH_GroupGeometryComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_GroupGeometryComponent() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_GroupGeometryComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_GroupGeometryComponent, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_GroupGeometryComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_GroupGeometryComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_GroupGeometryComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_IsNullDataComponent_OBSOLETE(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_IsNullDataComponent_OBSOLETE() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_IsNullDataComponent_OBSOLETE, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_IsNullDataComponent_OBSOLETE, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_IsNullDataComponent_OBSOLETE, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_IsNullDataComponent_OBSOLETE) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_IsNullDataComponent_OBSOLETE) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_MatchTreeComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_MatchTreeComponent() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_MatchTreeComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_MatchTreeComponent, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_MatchTreeComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_MatchTreeComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_MatchTreeComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_MergeGroupComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_MergeGroupComponent() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_MergeGroupComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_MergeGroupComponent, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_MergeGroupComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_MergeGroupComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_MergeGroupComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_MetaBallComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_MetaBallComponent() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_MetaBallComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_MetaBallComponent, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_MetaBallComponent, DA: IGH_DataAccess) """
        pass

    @staticmethod
    def SolveMetaBall(component, DA, context, plane, threshold):
        """ SolveMetaBall(component: GH_Component, DA: IGH_DataAccess, context: GH_Context, plane: Plane, threshold: float) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_MetaBallComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_MetaBallComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_MetaBallComponentThreshold(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_MetaBallComponentThreshold() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_MetaBallComponentThreshold, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_MetaBallComponentThreshold, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_MetaBallComponentThreshold, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_MetaBallComponentThreshold) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_MetaBallComponentThreshold) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_MetaBallComponentThresholdEx(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_MetaBallComponentThresholdEx() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_MetaBallComponentThresholdEx, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_MetaBallComponentThresholdEx, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_MetaBallComponentThresholdEx, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_MetaBallComponentThresholdEx) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_MetaBallComponentThresholdEx) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_PathCompareComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_PathCompareComponent() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_PathCompareComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_PathCompareComponent, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_PathCompareComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_PathCompareComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_PathCompareComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_PointListComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_PointListComponent() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BakeGeometry(self, doc, *__args):
        """ BakeGeometry(self: GH_PointListComponent, doc: RhinoDoc, att: ObjectAttributes, obj_ids: List[Guid]) """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def DrawViewportWires(self, args):
        """ DrawViewportWires(self: GH_PointListComponent, args: IGH_PreviewArgs) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_PointListComponent) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_PointListComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_PointListComponent, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_PointListComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ClippingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClippingBox(self: GH_PointListComponent) -> BoundingBox

"""

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_PointListComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_PointListComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsPreviewCapable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPreviewCapable(self: GH_PointListComponent) -> bool

"""


    m_attributes = None


class GH_PruneTreeComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_PruneTreeComponent() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_PruneTreeComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_PruneTreeComponent, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_PruneTreeComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_PruneTreeComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_PruneTreeComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_ReadFileComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """
    GH_ReadFileComponent()
    GH_ReadFileComponent(file: str)
    """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_ReadFileComponent, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_ReadFileComponent) """
        pass

    def CreateAttributes(self):
        """ CreateAttributes(self: GH_ReadFileComponent) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    @staticmethod
    def IsAcceptableFileFormat(filename):
        """ IsAcceptableFileFormat(filename: str) -> bool """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_ParserClicked(self, sender, e):
        """ Menu_ParserClicked(self: GH_ReadFileComponent, sender: object, e: EventArgs) """
        pass

    def Menu_PerLineClicked(self, sender, e):
        """ Menu_PerLineClicked(self: GH_ReadFileComponent, sender: object, e: EventArgs) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def Read(self, reader):
        """ Read(self: GH_ReadFileComponent, reader: GH_IReader) -> bool """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_ReadFileComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_ReadFileComponent, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_ReadFileComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def Write(self, writer):
        """ Write(self: GH_ReadFileComponent, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, file=None):
        """
        __new__(cls: type)
        __new__(cls: type, file: str)
        """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_ReadFileComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_ReadFileComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Parser = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parser(self: GH_ReadFileComponent) -> GH_LineParser

Set: Parser(self: GH_ReadFileComponent) = value
"""

    PerLineParse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PerLineParse(self: GH_ReadFileComponent) -> bool

Set: PerLineParse(self: GH_ReadFileComponent) = value
"""


    m_attributes = None


class GH_ReadFileComponentAttributes(GH_ComponentAttributes, IGH_Attributes, GH_ISerializable, IGH_ResponsiveObject, IGH_TooltipAwareObject):
    """ GH_ReadFileComponentAttributes(owner: GH_ReadFileComponent) """
    def Layout(self, *args): #cannot find CLR method
        """ Layout(self: GH_ComponentAttributes) """
        pass

    def PrepareForRender(self, *args): #cannot find CLR method
        """ PrepareForRender(self: GH_Attributes[IGH_Component], canvas: GH_Canvas) """
        pass

    def Render(self, *args): #cannot find CLR method
        """ Render(self: GH_ComponentAttributes, canvas: GH_Canvas, graphics: Graphics, channel: GH_CanvasChannel) """
        pass

    def RenderComponentCapsule(self, *args): #cannot find CLR method
        """ RenderComponentCapsule(self: GH_ComponentAttributes, canvas: GH_Canvas, graphics: Graphics, drawComponentBaseBox: bool, drawComponentNameBox: bool, drawJaggedEdges: bool, drawParameterGrips: bool, drawParameterNames: bool, drawZuiElements: bool)RenderComponentCapsule(self: GH_ComponentAttributes, canvas: GH_Canvas, graphics: Graphics) """
        pass

    def RenderIncomingWires(self, *args): #cannot find CLR method
        """ RenderIncomingWires(self: GH_Attributes[IGH_Component], painter: GH_Painter, sources: IEnumerable[IGH_Param], styles: IEnumerable[Pen])RenderIncomingWires(self: GH_Attributes[IGH_Component], painter: GH_Painter, sources: IEnumerable[IGH_Param], style: GH_ParamWireDisplay) """
        pass

    def RenderVariableParameterUI(self, *args): #cannot find CLR method
        """ RenderVariableParameterUI(self: GH_ComponentAttributes, canvas: GH_Canvas, graphics: Graphics) """
        pass

    def RespondToMouseDoubleClick(self, sender, e):
        """ RespondToMouseDoubleClick(self: GH_ReadFileComponentAttributes, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, owner):
        """ __new__(cls: type, owner: GH_ReadFileComponent) """
        pass

    m_innerBounds = None


class GH_ReplacePathComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_ReplacePathComponent() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetMasksAndPaths(self, *args): #cannot find CLR method
        """ GetMasksAndPaths(self: GH_ReplacePathComponent, DA: IGH_DataAccess) -> (bool, List[GH_TreeRules], List[GH_Path]) """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_ReplacePathComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_ReplacePathComponent, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_ReplacePathComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_ReplacePathComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_ReplacePathComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_ShiftDataPathComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_ShiftDataPathComponent() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_ShiftDataPathComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_ShiftDataPathComponent, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_ShiftDataPathComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_ShiftDataPathComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_ShiftDataPathComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_SimplifyComponentUpgrader(object, IGH_UpgradeObject):
    """ GH_SimplifyComponentUpgrader() """
    def Upgrade(self, target, document):
        """ Upgrade(self: GH_SimplifyComponentUpgrader, target: IGH_DocumentObject, document: GH_Document) -> IGH_DocumentObject """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    UpgradeFrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpgradeFrom(self: GH_SimplifyComponentUpgrader) -> Guid

"""

    UpgradeTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpgradeTo(self: GH_SimplifyComponentUpgrader) -> Guid

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Version(self: GH_SimplifyComponentUpgrader) -> DateTime

"""



class GH_SimplifyTreeComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_SimplifyTreeComponent() """
    def AddedToDocument(self, document):
        """ AddedToDocument(self: GH_SimplifyTreeComponent, document: GH_Document) """
        pass

    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def MovedBetweenDocuments(self, oldDocument, newDocument):
        """ MovedBetweenDocuments(self: GH_SimplifyTreeComponent, oldDocument: GH_Document, newDocument: GH_Document) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_SimplifyTreeComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_SimplifyTreeComponent, pManager: GH_OutputParamManager) """
        pass

    def RemovedFromDocument(self, document):
        """ RemovedFromDocument(self: GH_SimplifyTreeComponent, document: GH_Document) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_SimplifyTreeComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_SimplifyTreeComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_SimplifyTreeComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_SimplifyTreeComponent_OBSOLETE(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_SimplifyTreeComponent_OBSOLETE() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_SimplifyTreeComponent_OBSOLETE, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_SimplifyTreeComponent_OBSOLETE, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_SimplifyTreeComponent_OBSOLETE, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_SimplifyTreeComponent_OBSOLETE) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_SimplifyTreeComponent_OBSOLETE) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_SmoothNumbersComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_SmoothNumbersComponent() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_SmoothNumbersComponent, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def Read(self, reader):
        """ Read(self: GH_SmoothNumbersComponent, reader: GH_IReader) -> bool """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_SmoothNumbersComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_SmoothNumbersComponent, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_SmoothNumbersComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def Write(self, writer):
        """ Write(self: GH_SmoothNumbersComponent, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_SmoothNumbersComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_SmoothNumbersComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_SplitGroupComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_SplitGroupComponent() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_SplitGroupComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_SplitGroupComponent, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_SplitGroupComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_SplitGroupComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_SplitGroupComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_StreamFilterComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject, IGH_VariableParameterComponent):
    """ GH_StreamFilterComponent() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def CanInsertParameter(self, side, index):
        """ CanInsertParameter(self: GH_StreamFilterComponent, side: GH_ParameterSide, index: int) -> bool """
        pass

    def CanRemoveParameter(self, side, index):
        """ CanRemoveParameter(self: GH_StreamFilterComponent, side: GH_ParameterSide, index: int) -> bool """
        pass

    def CreateParameter(self, side, index):
        """ CreateParameter(self: GH_StreamFilterComponent, side: GH_ParameterSide, index: int) -> IGH_Param """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def DestroyParameter(self, side, index):
        """ DestroyParameter(self: GH_StreamFilterComponent, side: GH_ParameterSide, index: int) -> bool """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_StreamFilterComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_StreamFilterComponent, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_StreamFilterComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def VariableParameterMaintenance(self):
        """ VariableParameterMaintenance(self: GH_StreamFilterComponent) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_StreamFilterComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_StreamFilterComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_StreamFilterComponent_OBSOLETE(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject, IGH_VarParamComponent):
    """ GH_StreamFilterComponent_OBSOLETE() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def ConstructVariable(self, e):
        """ ConstructVariable(self: GH_StreamFilterComponent_OBSOLETE, e: GH_VarParamEventArgs) -> IGH_Param """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def IsVariableParam(self, e):
        """ IsVariableParam(self: GH_StreamFilterComponent_OBSOLETE, e: GH_VarParamEventArgs) -> bool """
        pass

    def ManagerConstructed(self, side, manager):
        """ ManagerConstructed(self: GH_StreamFilterComponent_OBSOLETE, side: GH_VarParamSide, manager: GH_VariableParameterManager) """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def ParametersModified(self, side):
        """ ParametersModified(self: GH_StreamFilterComponent_OBSOLETE, side: GH_VarParamSide) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_StreamFilterComponent_OBSOLETE, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_StreamFilterComponent_OBSOLETE, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_StreamFilterComponent_OBSOLETE, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_StreamFilterComponent_OBSOLETE) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_StreamFilterComponent_OBSOLETE) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsInputVariable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInputVariable(self: GH_StreamFilterComponent_OBSOLETE) -> bool

"""

    IsOutputVariable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOutputVariable(self: GH_StreamFilterComponent_OBSOLETE) -> bool

"""


    m_attributes = None


class GH_StreamGateComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject, IGH_VariableParameterComponent):
    """ GH_StreamGateComponent() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def CanInsertParameter(self, side, index):
        """ CanInsertParameter(self: GH_StreamGateComponent, side: GH_ParameterSide, index: int) -> bool """
        pass

    def CanRemoveParameter(self, side, index):
        """ CanRemoveParameter(self: GH_StreamGateComponent, side: GH_ParameterSide, index: int) -> bool """
        pass

    def CreateParameter(self, side, index):
        """ CreateParameter(self: GH_StreamGateComponent, side: GH_ParameterSide, index: int) -> IGH_Param """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def DestroyParameter(self, side, index):
        """ DestroyParameter(self: GH_StreamGateComponent, side: GH_ParameterSide, index: int) -> bool """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_StreamGateComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_StreamGateComponent, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_StreamGateComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def VariableParameterMaintenance(self):
        """ VariableParameterMaintenance(self: GH_StreamGateComponent) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_StreamGateComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_StreamGateComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_StreamGateComponent_OBSOLETE(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject, IGH_VarParamComponent):
    """ GH_StreamGateComponent_OBSOLETE() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def ConstructVariable(self, e):
        """ ConstructVariable(self: GH_StreamGateComponent_OBSOLETE, e: GH_VarParamEventArgs) -> IGH_Param """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def IsVariableParam(self, e):
        """ IsVariableParam(self: GH_StreamGateComponent_OBSOLETE, e: GH_VarParamEventArgs) -> bool """
        pass

    def ManagerConstructed(self, side, manager):
        """ ManagerConstructed(self: GH_StreamGateComponent_OBSOLETE, side: GH_VarParamSide, manager: GH_VariableParameterManager) """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def ParametersModified(self, side):
        """ ParametersModified(self: GH_StreamGateComponent_OBSOLETE, side: GH_VarParamSide) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_StreamGateComponent_OBSOLETE, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_StreamGateComponent_OBSOLETE, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_StreamGateComponent_OBSOLETE, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_StreamGateComponent_OBSOLETE) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_StreamGateComponent_OBSOLETE) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsInputVariable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInputVariable(self: GH_StreamGateComponent_OBSOLETE) -> bool

"""

    IsOutputVariable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOutputVariable(self: GH_StreamGateComponent_OBSOLETE) -> bool

"""


    m_attributes = None


class GH_TextTag3DComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_TextTag3DComponent() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BakeGeometry(self, doc, *__args):
        """ BakeGeometry(self: GH_TextTag3DComponent, doc: RhinoDoc, att: ObjectAttributes, obj_ids: List[Guid])BakeGeometry(self: GH_TextTag3DComponent, doc: RhinoDoc, obj_ids: List[Guid]) """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_TextTag3DComponent) """
        pass

    def ClearData(self):
        """ ClearData(self: GH_TextTag3DComponent) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def DrawViewportWires(self, args):
        """ DrawViewportWires(self: GH_TextTag3DComponent, args: IGH_PreviewArgs) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_TextTag3DComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_TextTag3DComponent, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_TextTag3DComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ClippingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClippingBox(self: GH_TextTag3DComponent) -> BoundingBox

"""

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_TextTag3DComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_TextTag3DComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsPreviewCapable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPreviewCapable(self: GH_TextTag3DComponent) -> bool

"""


    m_attributes = None


class GH_TextTag3DComponent_OBSOLETE(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_TextTag3DComponent_OBSOLETE() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BakeGeometry(self, doc, *__args):
        """ BakeGeometry(self: GH_TextTag3DComponent_OBSOLETE, doc: RhinoDoc, obj_ids: List[Guid]) """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def ClearData(self):
        """ ClearData(self: GH_TextTag3DComponent_OBSOLETE) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def DrawViewportWires(self, args):
        """ DrawViewportWires(self: GH_TextTag3DComponent_OBSOLETE, args: IGH_PreviewArgs) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_TextTag3DComponent_OBSOLETE, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_TextTag3DComponent_OBSOLETE, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_TextTag3DComponent_OBSOLETE, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ClippingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClippingBox(self: GH_TextTag3DComponent_OBSOLETE) -> BoundingBox

"""

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_TextTag3DComponent_OBSOLETE) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_TextTag3DComponent_OBSOLETE) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsPreviewCapable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPreviewCapable(self: GH_TextTag3DComponent_OBSOLETE) -> bool

"""


    m_attributes = None


class GH_TextTag3DComponent_OBSOLETE_AS_WELL(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_TextTag3DComponent_OBSOLETE_AS_WELL() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BakeGeometry(self, doc, *__args):
        """ BakeGeometry(self: GH_TextTag3DComponent_OBSOLETE_AS_WELL, doc: RhinoDoc, att: ObjectAttributes, obj_ids: List[Guid])BakeGeometry(self: GH_TextTag3DComponent_OBSOLETE_AS_WELL, doc: RhinoDoc, obj_ids: List[Guid]) """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def ClearData(self):
        """ ClearData(self: GH_TextTag3DComponent_OBSOLETE_AS_WELL) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def DrawViewportWires(self, args):
        """ DrawViewportWires(self: GH_TextTag3DComponent_OBSOLETE_AS_WELL, args: IGH_PreviewArgs) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_TextTag3DComponent_OBSOLETE_AS_WELL, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_TextTag3DComponent_OBSOLETE_AS_WELL, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_TextTag3DComponent_OBSOLETE_AS_WELL, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ClippingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClippingBox(self: GH_TextTag3DComponent_OBSOLETE_AS_WELL) -> BoundingBox

"""

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_TextTag3DComponent_OBSOLETE_AS_WELL) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_TextTag3DComponent_OBSOLETE_AS_WELL) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsPreviewCapable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPreviewCapable(self: GH_TextTag3DComponent_OBSOLETE_AS_WELL) -> bool

"""


    m_attributes = None


class GH_TextTag3DUpgrader(object, IGH_UpgradeObject):
    """ GH_TextTag3DUpgrader() """
    def Upgrade(self, target, document):
        """ Upgrade(self: GH_TextTag3DUpgrader, target: IGH_DocumentObject, document: GH_Document) -> IGH_DocumentObject """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    UpgradeFrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpgradeFrom(self: GH_TextTag3DUpgrader) -> Guid

"""

    UpgradeTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpgradeTo(self: GH_TextTag3DUpgrader) -> Guid

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Version(self: GH_TextTag3DUpgrader) -> DateTime

"""



class GH_TextTagComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_TextTagComponent() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_TextTagComponent, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BakeGeometry(self, doc, *__args):
        """ BakeGeometry(self: GH_TextTagComponent, doc: RhinoDoc, att: ObjectAttributes, obj_ids: List[Guid])BakeGeometry(self: GH_TextTagComponent, doc: RhinoDoc, obj_ids: List[Guid]) """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def ClearData(self):
        """ ClearData(self: GH_TextTagComponent) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def DrawViewportWires(self, args):
        """ DrawViewportWires(self: GH_TextTagComponent, args: IGH_PreviewArgs) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_TextTagComponent) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def Read(self, reader):
        """ Read(self: GH_TextTagComponent, reader: GH_IReader) -> bool """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_TextTagComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_TextTagComponent, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_TextTagComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def Write(self, writer):
        """ Write(self: GH_TextTagComponent, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ClippingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClippingBox(self: GH_TextTagComponent) -> BoundingBox

"""

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_TextTagComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_TextTagComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsPreviewCapable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPreviewCapable(self: GH_TextTagComponent) -> bool

"""

    TagHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TagHeight(self: GH_TextTagComponent) -> int

Set: TagHeight(self: GH_TextTagComponent) = value
"""


    m_attributes = None


class GH_TextTagComponent_OBSOLETE(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_TextTagComponent_OBSOLETE() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_TextTagComponent_OBSOLETE, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BakeGeometry(self, doc, *__args):
        """ BakeGeometry(self: GH_TextTagComponent_OBSOLETE, doc: RhinoDoc, obj_ids: List[Guid]) """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def ClearData(self):
        """ ClearData(self: GH_TextTagComponent_OBSOLETE) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def DrawViewportWires(self, args):
        """ DrawViewportWires(self: GH_TextTagComponent_OBSOLETE, args: IGH_PreviewArgs) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_TextTagComponent_OBSOLETE) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def Read(self, reader):
        """ Read(self: GH_TextTagComponent_OBSOLETE, reader: GH_IReader) -> bool """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_TextTagComponent_OBSOLETE, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_TextTagComponent_OBSOLETE, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_TextTagComponent_OBSOLETE, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def Write(self, writer):
        """ Write(self: GH_TextTagComponent_OBSOLETE, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ClippingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClippingBox(self: GH_TextTagComponent_OBSOLETE) -> BoundingBox

"""

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_TextTagComponent_OBSOLETE) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_TextTagComponent_OBSOLETE) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsPreviewCapable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPreviewCapable(self: GH_TextTagComponent_OBSOLETE) -> bool

"""

    TagHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TagHeight(self: GH_TextTagComponent_OBSOLETE) -> int

Set: TagHeight(self: GH_TextTagComponent_OBSOLETE) = value
"""


    m_attributes = None


class GH_TreeSplitComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_TreeSplitComponent() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_TreeSplitComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_TreeSplitComponent, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_TreeSplitComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_TreeSplitComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_TreeSplitComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_TrimTreeComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_TrimTreeComponent() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_TrimTreeComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_TrimTreeComponent, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_TrimTreeComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_TrimTreeComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_TrimTreeComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_UnflattenTreeComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_UnflattenTreeComponent() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_UnflattenTreeComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_UnflattenTreeComponent, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_UnflattenTreeComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_UnflattenTreeComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_UnflattenTreeComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_UngroupGeometryComponent(GH_Component, IGH_InstanceDescription, GH_ISerializable, IGH_DocumentObject, IGH_ActiveObject, IGH_Component, IGH_PreviewObject, IGH_BakeAwareObject):
    """ GH_UngroupGeometryComponent() """
    def AfterSolveInstance(self, *args): #cannot find CLR method
        """ AfterSolveInstance(self: GH_Component) """
        pass

    def AppendAdditionalComponentMenuItems(self, *args): #cannot find CLR method
        """ AppendAdditionalComponentMenuItems(self: GH_Component, menu: ToolStripDropDown) """
        pass

    def AssignInitCodeToInputParameter(self, *args): #cannot find CLR method
        """ AssignInitCodeToInputParameter(self: GH_Component, paramIndex: int, code: str) -> bool """
        pass

    def BeforeSolveInstance(self, *args): #cannot find CLR method
        """ BeforeSolveInstance(self: GH_Component) """
        pass

    def DestroyIconCache(self, *args): #cannot find CLR method
        """ DestroyIconCache(self: GH_DocumentObject) """
        pass

    def ExpireDownStreamObjects(self, *args): #cannot find CLR method
        """ ExpireDownStreamObjects(self: GH_Component) """
        pass

    def GenerateDefaultHTML(self, *args): #cannot find CLR method
        """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
        pass

    def GenerateParameterHelp(self, *args): #cannot find CLR method
        """
        GenerateParameterHelp(self: GH_Component, param: IGH_Param) -> str
        GenerateParameterHelp(self: GH_Component) -> str
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: GH_DocumentObject, name: str, default: str) -> str
        GetValue(self: GH_DocumentObject, name: str, default: Color) -> Color
        GetValue(self: GH_DocumentObject, name: str, default: float) -> float
        GetValue(self: GH_DocumentObject, name: str, default: bool) -> bool
        GetValue(self: GH_DocumentObject, name: str, default: int) -> int
        """
        pass

    def HtmlHelp_Source(self, *args): #cannot find CLR method
        """ HtmlHelp_Source(self: GH_Component) -> str """
        pass

    def Menu_AppendBakeItem(self, *args): #cannot find CLR method
        """ Menu_AppendBakeItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendEnableItem(self, *args): #cannot find CLR method
        """ Menu_AppendEnableItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectHelp(self, *args): #cannot find CLR method
        """ Menu_AppendObjectHelp(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectName(self, *args): #cannot find CLR method
        """ Menu_AppendObjectName(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendObjectNameEx(self, *args): #cannot find CLR method
        """ Menu_AppendObjectNameEx(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPreviewItem(self, *args): #cannot find CLR method
        """ Menu_AppendPreviewItem(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendPublish(self, *args): #cannot find CLR method
        """ Menu_AppendPublish(self: GH_DocumentObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendRuntimeMessages(self, *args): #cannot find CLR method
        """ Menu_AppendRuntimeMessages(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def Menu_AppendWarningsAndErrors(self, *args): #cannot find CLR method
        """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject, menu: ToolStripDropDown) """
        pass

    def PostConstructor(self, *args): #cannot find CLR method
        """ PostConstructor(self: GH_Component) """
        pass

    def RegisterInputParams(self, *args): #cannot find CLR method
        """ RegisterInputParams(self: GH_UngroupGeometryComponent, pManager: GH_InputParamManager) """
        pass

    def RegisterOutputParams(self, *args): #cannot find CLR method
        """ RegisterOutputParams(self: GH_UngroupGeometryComponent, pManager: GH_OutputParamManager) """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: GH_DocumentObject, name: str, value: str)SetValue(self: GH_DocumentObject, name: str, value: Color)SetValue(self: GH_DocumentObject, name: str, value: float)SetValue(self: GH_DocumentObject, name: str, value: bool)SetValue(self: GH_DocumentObject, name: str, value: int) """
        pass

    def SolveInstance(self, *args): #cannot find CLR method
        """ SolveInstance(self: GH_UngroupGeometryComponent, DA: IGH_DataAccess) """
        pass

    def ValuesChanged(self, *args): #cannot find CLR method
        """ ValuesChanged(self: GH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ComponentGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentGuid(self: GH_UngroupGeometryComponent) -> Guid

"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: GH_UngroupGeometryComponent) -> GH_Exposure

"""

    HelpDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal_Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_attributes = None


class GH_UpgradeExplodeComponent(object, IGH_UpgradeObject):
    """ GH_UpgradeExplodeComponent() """
    def Upgrade(self, target, document):
        """ Upgrade(self: GH_UpgradeExplodeComponent, target: IGH_DocumentObject, document: GH_Document) -> IGH_DocumentObject """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    UpgradeFrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpgradeFrom(self: GH_UpgradeExplodeComponent) -> Guid

"""

    UpgradeTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpgradeTo(self: GH_UpgradeExplodeComponent) -> Guid

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Version(self: GH_UpgradeExplodeComponent) -> DateTime

"""



class Upgrade_StreamGateComponent(object, IGH_UpgradeObject):
    """ Upgrade_StreamGateComponent() """
    def Upgrade(self, target, document):
        """ Upgrade(self: Upgrade_StreamGateComponent, target: IGH_DocumentObject, document: GH_Document) -> IGH_DocumentObject """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    UpgradeFrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpgradeFrom(self: Upgrade_StreamGateComponent) -> Guid

"""

    UpgradeTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpgradeTo(self: Upgrade_StreamGateComponent) -> Guid

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Version(self: Upgrade_StreamGateComponent) -> DateTime

"""



