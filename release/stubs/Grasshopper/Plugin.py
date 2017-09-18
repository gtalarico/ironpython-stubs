# encoding: utf-8
# module Grasshopper.Plugin calls itself Plugin
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class Commands(object):
    # no doc
    @staticmethod
    def Run_Grasshopper():
        """ Run_Grasshopper() -> bool """
        pass

    @staticmethod
    def Run_GrasshopperBake():
        """ Run_GrasshopperBake() -> bool """
        pass

    @staticmethod
    def Run_GrasshopperDeveloperSettings():
        """ Run_GrasshopperDeveloperSettings() -> bool """
        pass

    @staticmethod
    def Run_GrasshopperExportHelp():
        """ Run_GrasshopperExportHelp() -> bool """
        pass

    @staticmethod
    def Run_GrasshopperFolders():
        """ Run_GrasshopperFolders() -> bool """
        pass

    @staticmethod
    def Run_GrasshopperGetSDKDocumentation():
        """ Run_GrasshopperGetSDKDocumentation() -> bool """
        pass

    @staticmethod
    def Run_GrasshopperScripted():
        """ Run_GrasshopperScripted() -> bool """
        pass

    @staticmethod
    def Run_GrasshopperUnloadPlugin():
        """ Run_GrasshopperUnloadPlugin() -> bool """
        pass

    BakeDocument = None
    BakeObject = None


class GH_LatestVersionInfo(object):
    # no doc
    IsUpToDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsUpToDate(self: GH_LatestVersionInfo) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_LatestVersionInfo) -> bool

"""


    CurrentVersion = None
    DataAge = None
    DownloadUrl = None
    InstallerUrl = None
    LatestVersion = None


class GH_PluginUtil(object):
    # no doc
    @staticmethod
    def BringRhinoToTop():
        """ BringRhinoToTop() """
        pass

    @staticmethod
    def BringWindowToTop(hWnd):
        """ BringWindowToTop(hWnd: IntPtr) -> bool """
        pass

    @staticmethod
    def FocusOnRhino():
        """ FocusOnRhino() """
        pass

    @staticmethod
    def LoadGrasshopper(pluginAssembly, message):
        """ LoadGrasshopper(pluginAssembly: Assembly, message: str) -> (bool, str) """
        pass

    @staticmethod
    def RegisterGrasshopperFileExtensions():
        """ RegisterGrasshopperFileExtensions() """
        pass

    @staticmethod
    def SaveSettings():
        """ SaveSettings() """
        pass

    @staticmethod
    def SendKeyCodeToRhino(key):
        """ SendKeyCodeToRhino(key: str)SendKeyCodeToRhino(key: Char)SendKeyCodeToRhino(key: int) """
        pass

    @staticmethod
    def SendMessage(hWnd, msg, wParam, lParam):
        """ SendMessage(hWnd: IntPtr, msg: int, wParam: int, lParam: IntPtr) -> IntPtr """
        pass

    @staticmethod
    def SetFocus(hWnd):
        """ SetFocus(hWnd: IntPtr) """
        pass

    @staticmethod
    def UnloadGrasshopper():
        """ UnloadGrasshopper() -> bool """
        pass


class GH_ResourceGate(object):
    # no doc
    BlackIcon = None
    Error_12x12 = None
    Error_16x16 = None
    Error_24x24 = None
    Error_40x40 = None
    Info_12x12 = None
    Info_16x16 = None
    Info_24x24 = None
    Info_40x40 = None
    OK_12x12 = None
    OK_16x16 = None
    OK_24x24 = None
    OK_40x40 = None
    Warning_12x12 = None
    Warning_16x16 = None
    Warning_24x24 = None
    Warning_40x40 = None
    WhiteIcon = None


class GH_RhinoScriptInterface(object):
    """ GH_RhinoScriptInterface() """
    def AssignDataToParameter(self, parameterID, data):
        """ AssignDataToParameter(self: GH_RhinoScriptInterface, parameterID: str, data: object) -> bool """
        pass

    def BakeDataInObject(self, objectID):
        """ BakeDataInObject(self: GH_RhinoScriptInterface, objectID: str) -> object """
        pass

    def CloseAllDocuments(self):
        """ CloseAllDocuments(self: GH_RhinoScriptInterface) -> bool """
        pass

    def CloseDocument(self):
        """ CloseDocument(self: GH_RhinoScriptInterface) -> bool """
        pass

    def DisableBanner(self):
        """ DisableBanner(self: GH_RhinoScriptInterface) """
        pass

    def DisableSolver(self):
        """ DisableSolver(self: GH_RhinoScriptInterface) """
        pass

    def EnableBanner(self):
        """ EnableBanner(self: GH_RhinoScriptInterface) """
        pass

    def EnableSolver(self):
        """ EnableSolver(self: GH_RhinoScriptInterface) """
        pass

    def HideEditor(self):
        """ HideEditor(self: GH_RhinoScriptInterface) """
        pass

    def IsEditorLoaded(self):
        """ IsEditorLoaded(self: GH_RhinoScriptInterface) -> bool """
        pass

    def IsEditorVisible(self):
        """ IsEditorVisible(self: GH_RhinoScriptInterface) -> bool """
        pass

    def IsSolverEnabled(self):
        """ IsSolverEnabled(self: GH_RhinoScriptInterface) -> bool """
        pass

    def LoadEditor(self):
        """ LoadEditor(self: GH_RhinoScriptInterface) """
        pass

    def OpenDocument(self, filename):
        """ OpenDocument(self: GH_RhinoScriptInterface, filename: str) -> bool """
        pass

    def RunSolver(self, expireAllObjects):
        """ RunSolver(self: GH_RhinoScriptInterface, expireAllObjects: bool) """
        pass

    def SaveDocument(self):
        """ SaveDocument(self: GH_RhinoScriptInterface) -> bool """
        pass

    def SaveDocumentAs(self, filename):
        """ SaveDocumentAs(self: GH_RhinoScriptInterface, filename: str) -> bool """
        pass

    def SetSliderRangeAndValue(self, sliderID, value, minimum, maximum):
        """ SetSliderRangeAndValue(self: GH_RhinoScriptInterface, sliderID: str, value: float, minimum: float, maximum: float) -> bool """
        pass

    def SetSliderValue(self, sliderID, value):
        """ SetSliderValue(self: GH_RhinoScriptInterface, sliderID: str, value: float) -> bool """
        pass

    def ShowEditor(self):
        """ ShowEditor(self: GH_RhinoScriptInterface) """
        pass


