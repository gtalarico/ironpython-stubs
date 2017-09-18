class GH_ReadFileComponent(GH_Component,IGH_InstanceDescription,GH_ISerializable,IGH_DocumentObject,IGH_ActiveObject,IGH_Component,IGH_PreviewObject,IGH_BakeAwareObject):
 """
 GH_ReadFileComponent()

 GH_ReadFileComponent(file: str)
 """
 def AfterSolveInstance(self,*args):
  """ AfterSolveInstance(self: GH_Component) """
  pass
 def AppendAdditionalComponentMenuItems(self,*args):
  """ AppendAdditionalComponentMenuItems(self: GH_ReadFileComponent,menu: ToolStripDropDown) """
  pass
 def AssignInitCodeToInputParameter(self,*args):
  """ AssignInitCodeToInputParameter(self: GH_Component,paramIndex: int,code: str) -> bool """
  pass
 def BeforeSolveInstance(self,*args):
  """ BeforeSolveInstance(self: GH_ReadFileComponent) """
  pass
 def CreateAttributes(self):
  """ CreateAttributes(self: GH_ReadFileComponent) """
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
 @staticmethod
 def IsAcceptableFileFormat(filename):
  """ IsAcceptableFileFormat(filename: str) -> bool """
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
 def Menu_ParserClicked(self,sender,e):
  """ Menu_ParserClicked(self: GH_ReadFileComponent,sender: object,e: EventArgs) """
  pass
 def Menu_PerLineClicked(self,sender,e):
  """ Menu_PerLineClicked(self: GH_ReadFileComponent,sender: object,e: EventArgs) """
  pass
 def PostConstructor(self,*args):
  """ PostConstructor(self: GH_Component) """
  pass
 def Read(self,reader):
  """ Read(self: GH_ReadFileComponent,reader: GH_IReader) -> bool """
  pass
 def RegisterInputParams(self,*args):
  """ RegisterInputParams(self: GH_ReadFileComponent,pManager: GH_InputParamManager) """
  pass
 def RegisterOutputParams(self,*args):
  """ RegisterOutputParams(self: GH_ReadFileComponent,pManager: GH_OutputParamManager) """
  pass
 def SetValue(self,*args):
  """ SetValue(self: GH_DocumentObject,name: str,value: str)SetValue(self: GH_DocumentObject,name: str,value: Color)SetValue(self: GH_DocumentObject,name: str,value: float)SetValue(self: GH_DocumentObject,name: str,value: bool)SetValue(self: GH_DocumentObject,name: str,value: int) """
  pass
 def SolveInstance(self,*args):
  """ SolveInstance(self: GH_ReadFileComponent,DA: IGH_DataAccess) """
  pass
 def ValuesChanged(self,*args):
  """ ValuesChanged(self: GH_DocumentObject) """
  pass
 def Write(self,writer):
  """ Write(self: GH_ReadFileComponent,writer: GH_IWriter) -> bool """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,file=None):
  """
  __new__(cls: type)

  __new__(cls: type,file: str)
  """
  pass
 ComponentGuid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ComponentGuid(self: GH_ReadFileComponent) -> Guid



"""

 Exposure=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Exposure(self: GH_ReadFileComponent) -> GH_Exposure



"""

 HelpDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)

 Icon=property(lambda self: object(),lambda self,v: None,lambda self: None)

 Internal_Icon_24x24=property(lambda self: object(),lambda self,v: None,lambda self: None)

 Parser=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Parser(self: GH_ReadFileComponent) -> GH_LineParser



Set: Parser(self: GH_ReadFileComponent)=value

"""

 PerLineParse=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PerLineParse(self: GH_ReadFileComponent) -> bool



Set: PerLineParse(self: GH_ReadFileComponent)=value

"""


 m_attributes=None

