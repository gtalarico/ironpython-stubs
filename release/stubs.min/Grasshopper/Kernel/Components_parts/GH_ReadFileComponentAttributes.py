class GH_ReadFileComponentAttributes(GH_ComponentAttributes,IGH_Attributes,GH_ISerializable,IGH_ResponsiveObject,IGH_TooltipAwareObject):
 """ GH_ReadFileComponentAttributes(owner: GH_ReadFileComponent) """
 def Layout(self,*args):
  """ Layout(self: GH_ComponentAttributes) """
  pass
 def PrepareForRender(self,*args):
  """ PrepareForRender(self: GH_Attributes[IGH_Component],canvas: GH_Canvas) """
  pass
 def Render(self,*args):
  """ Render(self: GH_ComponentAttributes,canvas: GH_Canvas,graphics: Graphics,channel: GH_CanvasChannel) """
  pass
 def RenderComponentCapsule(self,*args):
  """ RenderComponentCapsule(self: GH_ComponentAttributes,canvas: GH_Canvas,graphics: Graphics,drawComponentBaseBox: bool,drawComponentNameBox: bool,drawJaggedEdges: bool,drawParameterGrips: bool,drawParameterNames: bool,drawZuiElements: bool)RenderComponentCapsule(self: GH_ComponentAttributes,canvas: GH_Canvas,graphics: Graphics) """
  pass
 def RenderIncomingWires(self,*args):
  """ RenderIncomingWires(self: GH_Attributes[IGH_Component],painter: GH_Painter,sources: IEnumerable[IGH_Param],styles: IEnumerable[Pen])RenderIncomingWires(self: GH_Attributes[IGH_Component],painter: GH_Painter,sources: IEnumerable[IGH_Param],style: GH_ParamWireDisplay) """
  pass
 def RenderVariableParameterUI(self,*args):
  """ RenderVariableParameterUI(self: GH_ComponentAttributes,canvas: GH_Canvas,graphics: Graphics) """
  pass
 def RespondToMouseDoubleClick(self,sender,e):
  """ RespondToMouseDoubleClick(self: GH_ReadFileComponentAttributes,sender: GH_Canvas,e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,owner):
  """ __new__(cls: type,owner: GH_ReadFileComponent) """
  pass
 m_innerBounds=None

