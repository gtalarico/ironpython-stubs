class IExportContext:
 """ An interface that is used in custom export to process a Revit model. """
 def Finish(self):
  """
  Finish(self: IExportContext)

   This method is called at the very end of the export process,

     after all 

    entities were processed (or after the process was cancelled).
  """
  pass
 def IsCanceled(self):
  """
  IsCanceled(self: IExportContext) -> bool

  

   This method is queried at the beginning of every element.

   Returns: Return True if you wish to cancel the exporting process,or False otherwise.
  """
  pass
 def OnElementBegin(self,elementId):
  """
  OnElementBegin(self: IExportContext,elementId: ElementId) -> RenderNodeAction

  

   This method marks the beginning of an element to be exported

  

   elementId: The Id of the element that is about to be processed

   Returns: Return RenderNodeAction.Skip if you wish to skip exporting this element,

     or 

    return RenderNodeAction.Proceed otherwise.
  """
  pass
 def OnElementEnd(self,elementId):
  """
  OnElementEnd(self: IExportContext,elementId: ElementId)

   This method marks the end of an element being exported

  

   elementId: The Id of the element that has just been processed
  """
  pass
 def OnFaceBegin(self,node):
  """
  OnFaceBegin(self: IExportContext,node: FaceNode) -> RenderNodeAction

  

   This method marks the beginning of a Face to be exported

  

   node: An output node that represents a Face.

   Returns: Return RenderNodeAction. Proceed if you wish to receive geometry (polymesh)

     

    for this face,or return RenderNodeAction.Skip otherwise.
  """
  pass
 def OnFaceEnd(self,node):
  """
  OnFaceEnd(self: IExportContext,node: FaceNode)

   This method marks the end of the current face being exported.

  

   node: An output node that represents a Face.
  """
  pass
 def OnInstanceBegin(self,node):
  """
  OnInstanceBegin(self: IExportContext,node: InstanceNode) -> RenderNodeAction

  

   This method marks the beginning of a family instance to be exported

   Returns: Return RenderNodeAction.Skip if you wish to skip processing this family 

    instance,

     or return RenderNodeAction.Proceed otherwise.
  """
  pass
 def OnInstanceEnd(self,node):
  """
  OnInstanceEnd(self: IExportContext,node: InstanceNode)

   This method marks the end of a family instance being exported

  

   node: An output node that represents a family instance.
  """
  pass
 def OnLight(self,node):
  """
  OnLight(self: IExportContext,node: LightNode)

   This method marks the beginning of export of a light object.

  

   node: A node describing the light object.
  """
  pass
 def OnLinkBegin(self,node):
  """
  OnLinkBegin(self: IExportContext,node: LinkNode) -> RenderNodeAction

  

   This method marks the beginning of a link instance to be exported.

   Returns: Return RenderNodeAction.Skip if you wish to skip processing this link instance,


    
     or return RenderNodeAction.Proceed otherwise.
  """
  pass
 def OnLinkEnd(self,node):
  """
  OnLinkEnd(self: IExportContext,node: LinkNode)

   This method marks the end of a link instance being exported.

  

   node: An output node that represents a Revit link.
  """
  pass
 def OnMaterial(self,node):
  """
  OnMaterial(self: IExportContext,node: MaterialNode)

   This method marks a change of the material.

  

   node: A node describing the current material.
  """
  pass
 def OnPolymesh(self,node):
  """
  OnPolymesh(self: IExportContext,node: PolymeshTopology)

   This method is called when a tessellated polymesh of a 3d face is being output.

  

   node: A node representing topology of the polymesh
  """
  pass
 def OnRPC(self,node):
  """
  OnRPC(self: IExportContext,node: RPCNode)

   This method marks the beginning of export of an RPC object.

  

   node: A node with asset information about the RPC object.
  """
  pass
 def OnViewBegin(self,node):
  """
  OnViewBegin(self: IExportContext,node: ViewNode) -> RenderNodeAction

  

   This method marks the beginning of a 3D view to be exported

  

   node: Geometry node associated with the view

   Returns: Return RenderNodeAction.Skip if you wish to skip exporting this view,

     or 

    return RenderNodeAction.Proceed otherwise.
  """
  pass
 def OnViewEnd(self,elementId):
  """
  OnViewEnd(self: IExportContext,elementId: ElementId)

   This method marks the end of a 3D view being exported

  

   elementId: The Id of the 3D view that has just been processed
  """
  pass
 def Start(self):
  """
  Start(self: IExportContext) -> bool

  

   This method is called at the very start of the export process,

     still before 

    the first entity of the model was send out.

  

   Returns: Return True if you are ready to proceed with processing the export.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
