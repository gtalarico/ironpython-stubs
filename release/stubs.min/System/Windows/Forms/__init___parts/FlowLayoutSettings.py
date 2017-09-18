class FlowLayoutSettings(LayoutSettings):
 """ Collects the characteristics associated with flow layouts. """
 def GetFlowBreak(self,child):
  """
  GetFlowBreak(self: FlowLayoutSettings,child: object) -> bool

  

   Returns a value that represents the flow break setting of the control.

  

   child: The child control.

   Returns: true if the flow break is set; otherwise,false.
  """
  pass
 def SetFlowBreak(self,child,value):
  """
  SetFlowBreak(self: FlowLayoutSettings,child: object,value: bool)

   Sets the value that represents the flow break setting of the control.

  

   child: The child control.

   value: The flow break value to set.
  """
  pass
 FlowDirection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating the flow direction of consecutive controls.



Get: FlowDirection(self: FlowLayoutSettings) -> FlowDirection



Set: FlowDirection(self: FlowLayoutSettings)=value

"""

 LayoutEngine=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current flow layout engine.



Get: LayoutEngine(self: FlowLayoutSettings) -> LayoutEngine



"""

 WrapContents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the contents should be wrapped or clipped when they exceed the original boundaries of their container.



Get: WrapContents(self: FlowLayoutSettings) -> bool



Set: WrapContents(self: FlowLayoutSettings)=value

"""


