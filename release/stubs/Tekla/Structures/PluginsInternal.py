# encoding: utf-8
# module Tekla.Structures.PluginsInternal calls itself PluginsInternal
# from Tekla.Structures.Plugins, Version=2017.0.0.0, Culture=neutral, PublicKeyToken=2f04dbe497b71114
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ICDelegate:
    # no doc
    def DrawingExportAddPlugin(self, pPluginDefinition):
        """ DrawingExportAddPlugin(self: ICDelegate, pPluginDefinition: dotPluginDefinition_t) -> (int, dotPluginDefinition_t) """
        pass

    def DrawingExportCurrentDefineInputClientId(self, pInput):
        """ DrawingExportCurrentDefineInputClientId(self: ICDelegate, pInput: dotPluginClient_t) -> (int, dotPluginClient_t) """
        pass

    def DrawingExportDefineInputCompleted(self, pInput):
        """ DrawingExportDefineInputCompleted(self: ICDelegate, pInput: dotPluginClient_t) -> (int, dotPluginClient_t) """
        pass

    def DrawingExportGetPluginInput(self, pInput):
        """ DrawingExportGetPluginInput(self: ICDelegate, pInput: dotPluginInput_t) -> (int, dotPluginInput_t) """
        pass

    def DrawingExportPluginRunCompleted(self, pInput):
        """ DrawingExportPluginRunCompleted(self: ICDelegate, pInput: dotPluginClient_t) -> (int, dotPluginClient_t) """
        pass

    def DrawingExportSetPluginInput(self, pInput):
        """ DrawingExportSetPluginInput(self: ICDelegate, pInput: dotPluginInput_t) -> (int, dotPluginInput_t) """
        pass

    def ExportAddPlugin(self, pPluginDefinition, pConnectionType):
        """ ExportAddPlugin(self: ICDelegate, pPluginDefinition: dotPluginDefinition_t, pConnectionType: dotConnectionType_t) -> (int, dotPluginDefinition_t, dotConnectionType_t) """
        pass

    def ExportExecutePluginResult(self, ExecuteResult):
        """ ExportExecutePluginResult(self: ICDelegate, ExecuteResult: int) -> int """
        pass

    def ExportGetConnectionCode(self, ConnectionCode):
        """ ExportGetConnectionCode(self: ICDelegate, ConnectionCode: dotConnectionCode_t) -> (int, dotConnectionCode_t) """
        pass

    def ExportGetInput(self, pInput):
        """ ExportGetInput(self: ICDelegate, pInput: dotPluginInput_t) -> (int, dotPluginInput_t) """
        pass

    def ExportGetPluginBaseDirectory(self, pPluginBaseDirectory):
        """ ExportGetPluginBaseDirectory(self: ICDelegate, pPluginBaseDirectory: dotPluginBaseDirectory_t) -> (int, dotPluginBaseDirectory_t) """
        pass

    def ExportGetPluginDoubleAttributes(self, pInput):
        """ ExportGetPluginDoubleAttributes(self: ICDelegate, pInput: dotPluginAttributesDouble_t) -> (int, dotPluginAttributesDouble_t) """
        pass

    def ExportGetPluginId(self):
        """ ExportGetPluginId(self: ICDelegate) -> int """
        pass

    def ExportGetPluginIntAttributes(self, pInput):
        """ ExportGetPluginIntAttributes(self: ICDelegate, pInput: dotPluginAttributesInt_t) -> (int, dotPluginAttributesInt_t) """
        pass

    def ExportGetPluginName(self, pPluginName):
        """ ExportGetPluginName(self: ICDelegate, pPluginName: dotPluginName_t) -> (int, dotPluginName_t) """
        pass

    def ExportGetPluginStringAttributes(self, pInput):
        """ ExportGetPluginStringAttributes(self: ICDelegate, pInput: dotPluginAttributesString_t) -> (int, dotPluginAttributesString_t) """
        pass

    def ExportSetConnectionCode(self, ConnectionCode):
        """ ExportSetConnectionCode(self: ICDelegate, ConnectionCode: dotConnectionCode_t) -> (int, dotConnectionCode_t) """
        pass

    def ExportSetInput(self, pInput):
        """ ExportSetInput(self: ICDelegate, pInput: dotPluginInput_t) -> (int, dotPluginInput_t) """
        pass

    def ExportSetPluginResult(self, Result):
        """ ExportSetPluginResult(self: ICDelegate, Result: int) -> int """
        pass

    def ExportSignalInputEnded(self):
        """ ExportSignalInputEnded(self: ICDelegate) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class Remoter(object):
    """ Remoter() """
    @staticmethod
    def GetConnectionStatus():
        """ GetConnectionStatus() -> bool """
        pass

    @staticmethod
    def InitializeSandBox():
        """ InitializeSandBox() -> bool """
        pass


