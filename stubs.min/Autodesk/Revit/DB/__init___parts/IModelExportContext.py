class IModelExportContext(IExportContext):
 """ An interface that is used in custom export to export 3D views of a Revit model. """
 def OnCurve(self,node):
  """
  OnCurve(self: IModelExportContext,node: CurveNode) -> RenderNodeAction
  
   This method is called when a 3D Curve is being output.
  
   node: An output node that represents a Curve.
   Returns: Return RenderNodeAction.Proceed if you wish to receive tessellated geometry
     
    (line or polyline segments) for this curve,or otherwise return 
    RenderNodeAction.Skip.
  """
  pass
 def OnLineSegment(self,segment):
  """
  OnLineSegment(self: IModelExportContext,segment: LineSegment)
   This method is called after unhandled 3D curve was tessellated to line segments 
    and sent to the output.
  
  
   segment: A structure describing the line segment.
  """
  pass
 def OnPoint(self,node):
  """
  OnPoint(self: IModelExportContext,node: PointNode) -> RenderNodeAction
  
   This method is called when a 3D Point is being output.
  
   node: An output node that represents a Point.
   Returns: Return RenderNodeAction.Proceed if you wish to receive low-level geometry
     
    (line segments) for this point,or otherwise return RenderNodeAction.Skip.
  """
  pass
 def OnPolyline(self,node):
  """
  OnPolyline(self: IModelExportContext,node: PolylineNode) -> RenderNodeAction
  
   This method is called when a 3D Polyline is being output.
  
   node: An output node that represents a Polyline.
   Returns: Return RenderNodeAction.Proceed if you wish to receive tessellated geometry
     
    (polyline segments) for this polyline,or otherwise return 
    RenderNodeAction.Skip.
  """
  pass
 def OnPolylineSegments(self,segments):
  """
  OnPolylineSegments(self: IModelExportContext,segments: PolylineSegments)
   This method is called after unhandled 3D curve was tessellated to polyline 
    segments and sent to the output.
  
  
   segments: A structure describing the polyline segments.
  """
  pass
 def OnText(self,node):
  """
  OnText(self: IModelExportContext,node: TextNode)
   This method is called when a text annoation object is being output.
  
   node: An output node that represents a text annotation.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
