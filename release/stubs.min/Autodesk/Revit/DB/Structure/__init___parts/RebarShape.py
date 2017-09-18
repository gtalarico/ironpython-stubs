class RebarShape(ElementType,IDisposable):
 """ RebarShape specifies the shape type for a Rebar instance. """
 @staticmethod
 def Create(doc,definition,multiplanarDefinition,style,attachmentType,startHookAngle,startHookOrientation,endHookAngle,endHookOrientation,higherEnd):
  """
  Create(doc: Document,definition: RebarShapeDefinition,multiplanarDefinition: RebarShapeMultiplanarDefinition,style: RebarStyle,attachmentType: StirrupTieAttachmentType,startHookAngle: int,startHookOrientation: RebarHookOrientation,endHookAngle: int,endHookOrientation: RebarHookOrientation,higherEnd: int) -> RebarShape

  

   Create a new instance of a Rebar Shape,which defines the shape of a rebar.

  

   doc: A document to contain the RebarShape.

   definition: The definition of the rebar shape,as a set of curves in a plane

     driven by 

    parameters.

  

   multiplanarDefinition: If not null,the created RebarShape will be a 3D shape. The shape

     is built 

    out of the planar RebarShapeDefinition,with additional

     out-of-plane 

    segments defined by the RebarShapeMultiplanarDefinition

     object. Not 

    supported in conjunction with RebarShapeDefinitionByArc

     of type Spiral or 

    LappedCircle.

  

   style: Whether the shape is to be used as a standard bar or a stirrup/tie.

   attachmentType: When the style is stirrup/tie,specify whether it will attach to the

     

    interior of cover (cover is measured to the stirrups),or to the

     exterior 

    of cover (cover is measured to the standard bars).

     Ignored when the style 

    is Standard.

  

   startHookAngle: The start hook angle,expressed as an integral number of degrees.

     If 0,the 

    shape will have no start hook. Common values are 0,90,135,and 180.

  

   startHookOrientation: The orientation of the start hook.

     Ignored when startHookAngle is 0.

   endHookAngle: The end hook angle,expressed as an integral number of degrees.

     If 0,the 

    shape will have no end hook. Common values are 0,90,135,and 180.

  

   endHookOrientation: The orientation of the end hook.

     Ignored when endHookAngle is 0.

   higherEnd: When the rebar crosses itself,one end will be "lifted" to avoid 

    self-intersection.

     Specify which end should be lifted: 0 for start,1 for 

    end.

  

   Returns: A new RebarShape instance.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def GetAllowed(self,barType):
  """
  GetAllowed(self: RebarShape,barType: RebarBarType) -> bool

  

   Check whether a bar type can be used with this RebarShape. Bar types are 

    allowed by default.

  

  

   barType: A bar type in the same document as this shape.

   Returns: True if this shape may be combined with this barType.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetCurvesForBrowser(self):
  """
  GetCurvesForBrowser(self: RebarShape) -> IList[Curve]

  

   Generate curves for the shape,as used in the shape browser.

   Returns: An array of curves representing the shape with its default parameters.
  """
  pass
 def GetDefaultHookAngle(self,index):
  """
  GetDefaultHookAngle(self: RebarShape,index: int) -> int

  

   Get the hook angle,expressed as an integral number of degrees (common values 

    are 0,90,135,and 180).

  

  

   index: 0 for the starting hook,1 for the ending hook.
  """
  pass
 def GetDefaultHookOrientation(self,index):
  """
  GetDefaultHookOrientation(self: RebarShape,index: int) -> RebarHookOrientation

  

   Get the hook orientation.

  

   index: 0 for the starting hook,1 for the ending hook.
  """
  pass
 def GetEndTreatmentTypeId(self,iEnd):
  """
  GetEndTreatmentTypeId(self: RebarShape,iEnd: int) -> ElementId

  

   get the id of the end treatment for the designated shape end
  """
  pass
 def GetMultiplanarDefinition(self):
  """
  GetMultiplanarDefinition(self: RebarShape) -> RebarShapeMultiplanarDefinition

  

   The optional 3D structure of the shape.

   Returns: A copy of the multiplanar definition. Changes will not affect the RebarShape.
  """
  pass
 def GetRebarShapeDefinition(self):
  """
  GetRebarShapeDefinition(self: RebarShape) -> RebarShapeDefinition

  

   Return the definition of the RebarShape.

   Returns: A copy of the definition. Changes will not affect the RebarShape.
  """
  pass
 def HasEndTreatment(self):
  """
  HasEndTreatment(self: RebarShape) -> bool

  

   returns true if the shape has end treatment for at least one end.
  """
  pass
 def IsSameShapeIgnoringHooks(self,otherShape):
  """
  IsSameShapeIgnoringHooks(self: RebarShape,otherShape: RebarShape) -> bool

  

   Test whether two shapes have equivalent definitions by comparing

     the 

    RebarShapeDefinition and MultiplanarDefinition properties.

  

  

   otherShape: Another shape to be compared to this one.

   Returns: True if the shape definitions match,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def SetAllowed(self,barType,allowed):
  """
  SetAllowed(self: RebarShape,barType: RebarBarType,allowed: bool)

   Specify which bar types can be used with this RebarShape. Bar types are allowed 

    by default.

  

  

   barType: A bar type in the same document as this shape.

   allowed: Whether this shape may be combined with barType.
  """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetEndTreatmentTypeId(self,treatmenetId,iEnd):
  """
  SetEndTreatmentTypeId(self: RebarShape,treatmenetId: ElementId,iEnd: int)

   set the end treatment type id for the designated shape end
  """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 HigherEnd=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Defines the higher end of rebar shape.



Get: HigherEnd(self: RebarShape) -> int



"""

 RebarStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether the shape represents a standard bar or a stirrup.



Get: RebarStyle(self: RebarShape) -> RebarStyle



"""

 ShapeFamilyId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get and return the rebar shape family id.



Get: ShapeFamilyId(self: RebarShape) -> ElementId



"""

 SimpleArc=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Check whether this shape consists of a single arc,possibly with hooks.



Get: SimpleArc(self: RebarShape) -> bool



"""

 SimpleLine=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Check whether this shape consists of a single straight segment,possibly with hooks.



Get: SimpleLine(self: RebarShape) -> bool



"""

 StirrupTieAttachment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The attachment type of stirrup ties and rebars.



Get: StirrupTieAttachment(self: RebarShape) -> StirrupTieAttachmentType



"""


