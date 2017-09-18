class ToolStripManager(object):
 """ Controls System.Windows.Forms.ToolStrip rendering and rafting,and the merging of System.Windows.Forms.MenuStrip,System.Windows.Forms.ToolStripDropDownMenu,and System.Windows.Forms.ToolStripMenuItem objects. This class cannot be inherited. """
 @staticmethod
 def FindToolStrip(toolStripName):
  """
  FindToolStrip(toolStripName: str) -> ToolStrip

  

   Finds the specified System.Windows.Forms.ToolStrip or a type derived from 

    System.Windows.Forms.ToolStrip.

  

  

   toolStripName: A string specifying the name of the System.Windows.Forms.ToolStrip or derived 

    System.Windows.Forms.ToolStrip type to find.

  

   Returns: The System.Windows.Forms.ToolStrip or one of its derived types as specified by the toolStripName 

    parameter,or null if the System.Windows.Forms.ToolStrip is not found.
  """
  pass
 @staticmethod
 def IsShortcutDefined(shortcut):
  """
  IsShortcutDefined(shortcut: Keys) -> bool

  

   Retrieves a value indicating whether the specified shortcut key is used by any of the 

    System.Windows.Forms.ToolStrip controls of a form.

  

  

   shortcut: The shortcut key for which to search.

   Returns: true if the shortcut key is used by any System.Windows.Forms.ToolStrip on the form; otherwise,

    false.
  """
  pass
 @staticmethod
 def IsValidShortcut(shortcut):
  """
  IsValidShortcut(shortcut: Keys) -> bool

  

   Retrieves a value indicating whether a defined shortcut key is valid.

  

   shortcut: The shortcut key to test for validity.

   Returns: true if the shortcut key is valid; otherwise,false.
  """
  pass
 @staticmethod
 def LoadSettings(targetForm,key=None):
  """
  LoadSettings(targetForm: Form,key: str)

   Loads settings for the specified System.Windows.Forms.Form using the specified settings key.

  

   targetForm: The System.Windows.Forms.Form for which to load settings.

   key: A System.String representing the settings key for this System.Windows.Forms.Form.

  LoadSettings(targetForm: Form)

   Loads settings for the given System.Windows.Forms.Form using the full name of the 

    System.Windows.Forms.Form as the settings key.

  

  

   targetForm: The System.Windows.Forms.Form whose name is also the settings key.
  """
  pass
 @staticmethod
 def Merge(sourceToolStrip,*__args):
  """
  Merge(sourceToolStrip: ToolStrip,targetName: str) -> bool

  

   Combines two System.Windows.Forms.ToolStrip objects of the same type.

  

   sourceToolStrip: The System.Windows.Forms.ToolStrip to be combined with the System.Windows.Forms.ToolStrip 

    referred to by the targetName parameter.

  

   targetName: The name of the System.Windows.Forms.ToolStrip that receives the System.Windows.Forms.ToolStrip 

    referred to by the sourceToolStrip parameter.

  

   Returns: true if the merge is successful; otherwise,false.

  Merge(sourceToolStrip: ToolStrip,targetToolStrip: ToolStrip) -> bool

  

   Combines two System.Windows.Forms.ToolStrip objects of different types.

  

   sourceToolStrip: The System.Windows.Forms.ToolStrip to be combined with the System.Windows.Forms.ToolStrip 

    referred to by the targetToolStrip parameter.

  

   targetToolStrip: The System.Windows.Forms.ToolStrip that receives the System.Windows.Forms.ToolStrip referred to 

    by the sourceToolStrip parameter.

  

   Returns: true if the merge is successful; otherwise,false.
  """
  pass
 @staticmethod
 def RevertMerge(*__args):
  """
  RevertMerge(targetName: str) -> bool

  

   Undoes a merging of two System.Windows.Forms.ToolStrip objects,returning the 

    System.Windows.Forms.ToolStrip with the specified name to its state before the merge and 

    nullifying all previous merge operations.

  

  

   targetName: The name of the System.Windows.Forms.ToolStripItem for which to undo a merge operation.

   Returns: true if the undoing of the merge is successful; otherwise,false.

  RevertMerge(targetToolStrip: ToolStrip,sourceToolStrip: ToolStrip) -> bool

  

   Undoes a merging of two System.Windows.Forms.ToolStrip objects,returning both 

    System.Windows.Forms.ToolStrip controls to their state before the merge and nullifying all 

    previous merge operations.

  

  

   targetToolStrip: The name of the System.Windows.Forms.ToolStripItem for which to undo a merge operation.

   sourceToolStrip: The System.Windows.Forms.ToolStrip that was merged with the targetToolStrip.

   Returns: true if the undoing of the merge is successful; otherwise,false.

  RevertMerge(targetToolStrip: ToolStrip) -> bool

  

   Undoes a merging of two System.Windows.Forms.ToolStrip objects,returning the specified 

    System.Windows.Forms.ToolStrip to its state before the merge and nullifying all previous merge 

    operations.

  

  

   targetToolStrip: The System.Windows.Forms.ToolStripItem for which to undo a merge operation.

   Returns: true if the undoing of the merge is successful; otherwise,false.
  """
  pass
 @staticmethod
 def SaveSettings(sourceForm,key=None):
  """
  SaveSettings(sourceForm: Form,key: str)

   Saves settings for the specified System.Windows.Forms.Form using the specified settings key.

  

   sourceForm: The System.Windows.Forms.Form for which to save settings.

   key: A System.String representing the settings key for this System.Windows.Forms.Form.

  SaveSettings(sourceForm: Form)

   Saves settings for the given System.Windows.Forms.Form using the full name of the 

    System.Windows.Forms.Form as the settings key.

  

  

   sourceForm: The System.Windows.Forms.Form whose name is also the settings key.
  """
  pass
 Renderer=None
 RendererChanged=None
 RenderMode=None
 VisualStylesEnabled=False

