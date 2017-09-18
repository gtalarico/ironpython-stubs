class GH_MetaBallComponent(GH_Component,IGH_InstanceDescription,GH_ISerializable,IGH_DocumentObject,IGH_ActiveObject,IGH_Component,IGH_PreviewObject,IGH_BakeAwareObject):
 """ GH_MetaBallComponent() """
 def AfterSolveInstance(self,*args):
  """ AfterSolveInstance(self: GH_Component) """
  pass
 def AppendAdditionalComponentMenuItems(self,*args):
  """ AppendAdditionalComponentMenuItems(self: GH_Component,menu: ToolStripDropDown) """
  pass
 def AssignInitCodeToInputParameter(self,*args):
  """ AssignInitCodeToInputParameter(self: GH_Component,paramIndex: int,code: str) -> bool """
  pass
 def BeforeSolveInstance(self,*args):
  """ BeforeSolveInstance(self: GH_Component) """
  pass
 def DestroyIconCache(self,*args):
  """ DestroyIconCache(self: GH_DocumentObject) """
  pass
 def ExpireDownStreamObjects(self,*args):
  """ ExpireDownStreamObjects(self: GH_Component) """
  pass
 def GenerateDefaultHTML(self,*args):
  """ GenerateDefaultHTML(self: GH_Component) -> GH_HtmlFormatter """
  pass
 def GenerateParameterHelp(self,*args):
  """
  GenerateParameterHelp(self: GH_Component,param: IGH_Param) -> str

  GenerateParameterHelp(self: GH_Component) -> str
  """
  pass
 def GetValue(self,*args):
  """
  GetValue(self: GH_DocumentObject,name: str,default: str) -> str

  GetValue(self: GH_DocumentObject,name: str,default: Color) -> Color

  GetValue(self: GH_DocumentObject,name: str,default: float) -> float

  GetValue(self: GH_DocumentObject,name: str,default: bool) -> bool

  GetValue(self: GH_DocumentObject,name: str,default: int) -> int
  """
  pass
 def HtmlHelp_Source(self,*args):
  """ HtmlHelp_Source(self: GH_Component) -> str """
  pass
 def Menu_AppendBakeItem(self,*args):
  """ Menu_AppendBakeItem(self: GH_ActiveObject,menu: ToolStripDropDown) """
  pass
 def Menu_AppendEnableItem(self,*args):
  """ Menu_AppendEnableItem(self: GH_ActiveObject,menu: ToolStripDropDown) """
  pass
 def Menu_AppendObjectHelp(self,*args):
  """ Menu_AppendObjectHelp(self: GH_DocumentObject,menu: ToolStripDropDown) """
  pass
 def Menu_AppendObjectName(self,*args):
  """ Menu_AppendObjectName(self: GH_DocumentObject,menu: ToolStripDropDown) """
  pass
 def Menu_AppendObjectNameEx(self,*args):
  """ Menu_AppendObjectNameEx(self: GH_DocumentObject,menu: ToolStripDropDown) """
  pass
 def Menu_AppendPreviewItem(self,*args):
  """ Menu_AppendPreviewItem(self: GH_ActiveObject,menu: ToolStripDropDown) """
  pass
 def Menu_AppendPublish(self,*args):
  """ Menu_AppendPublish(self: GH_DocumentObject,menu: ToolStripDropDown) """
  pass
 def Menu_AppendRuntimeMessages(self,*args):
  """ Menu_AppendRuntimeMessages(self: GH_ActiveObject,menu: ToolStripDropDown) """
  pass
 def Menu_AppendWarningsAndErrors(self,*args):
  """ Menu_AppendWarningsAndErrors(self: GH_ActiveObject,menu: ToolStripDropDown) """
  pass
 def PostConstructor(self,*args):
  """ PostConstructor(self: GH_Component) """
  pass
 def RegisterInputParams(self,*args):
  """ RegisterInputParams(self: GH_MetaBallComponent,pManager: GH_InputParamManager) """
  pass
 def RegisterOutputParams(self,*args):
  """ RegisterOutputParams(self: GH_MetaBallComponent,pManager: GH_OutputParamManager) """
  pass
 def SetValue(self,*args):
  """ SetValue(self: GH_DocumentObject,name: str,value: str)SetValue(self: GH_DocumentObject,name: str,value: Color)SetValue(self: GH_DocumentObject,name: str,value: float)SetValue(self: GH_DocumentObject,name: str,value: bool)SetValue(self: GH_DocumentObject,name: str,value: int) """
  pass
 def SolveInstance(self,*args):
  """ SolveInstance(self: GH_MetaBallComponent,DA: IGH_DataAccess) """
  pass
 @staticmethod
 def SolveMetaBall(component,DA,context,plane,threshold):
  """ SolveMetaBall(component: GH_Component,DA: IGH_DataAccess,context: GH_Context,plane: Plane,threshold: float) """
  pass
 def ValuesChanged(self,*args):
  """ ValuesChanged(self: GH_DocumentObject) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 ComponentGuid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ComponentGuid(self: GH_MetaBallComponent) -> Guid



"""

 Exposure=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Exposure(self: GH_MetaBallComponent) -> GH_Exposure



"""

 HelpDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)

 Icon=property(lambda self: object(),lambda self,v: None,lambda self: None)

 Internal_Icon_24x24=property(lambda self: object(),lambda self,v: None,lambda self: None)


 m_attributes=None

