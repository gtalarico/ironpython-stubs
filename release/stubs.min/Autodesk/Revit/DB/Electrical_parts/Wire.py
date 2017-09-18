class Wire(MEPCurve,IDisposable):
 """ Electrical wire element. """
 def AppendVertex(self,vertexPoint):
  """
  AppendVertex(self: Wire,vertexPoint: XYZ)

   Appends one vertex to the end of the wire.

  

   vertexPoint: The vertex to be appended.
  """
  pass
 @staticmethod
 def AreVertexPointsValid(vertexPoints,startConnector,endConnector):
  """ AreVertexPointsValid(vertexPoints: IList[XYZ],startConnector: Connector,endConnector: Connector) -> bool """
  pass
 def ConnectTo(self,startConnectorTo,endConnectorTo):
  """
  ConnectTo(self: Wire,startConnectorTo: Connector,endConnectorTo: Connector)

   Connects the wire to other elements.

  

   startConnectorTo: The connector that the start connector of the wire connects to.

   endConnectorTo: The connector that the end connector of the wire connects to.
  """
  pass
 @staticmethod
 def Create(document,wireTypeId,viewId,wiringType,vertexPoints,startConnectorTo,endConnectorTo):
  """ Create(document: Document,wireTypeId: ElementId,viewId: ElementId,wiringType: WiringType,vertexPoints: IList[XYZ],startConnectorTo: Connector,endConnectorTo: Connector) -> Wire """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetMEPSystems(self):
  """
  GetMEPSystems(self: Wire) -> IList[ElementId]

  

   Gets the systems to which the wire belongs.

   Returns: The systems to which the wire belongs.
  """
  pass
 def GetVertex(self,index):
  """
  GetVertex(self: Wire,index: int) -> XYZ

  

   Gets the position of an existing vertex.

  

   index: The index of the existing vertex. Should be between 0 and 

    Autodesk.Revit.DB.Electrical.Wire.NumberOfVertices.

  

   Returns: The position of the vertex.
  """
  pass
 def InsertVertex(self,index,vertexPoint):
  """
  InsertVertex(self: Wire,index: int,vertexPoint: XYZ)

   Inserts a new vertex before the specified index.

  

   index: The index of the vertex to come after this new vertex. Should be between 0 and 

    Autodesk.Revit.DB.Electrical.Wire.NumberOfVertices.

  

   vertexPoint: The point of the new vertex.
  """
  pass
 def IsVertexPointValid(self,vertexPoint):
  """
  IsVertexPointValid(self: Wire,vertexPoint: XYZ) -> bool

  

   Checks if the given vertex point can be added to this wire.

  

   vertexPoint: The vertex point.

   Returns: True if the vertex point can be added,false if the point cannot be added 

    because there is already a vertex at this position on the view plane (within 

    tolerance).
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def RemoveVertex(self,index):
  """
  RemoveVertex(self: Wire,index: int)

   Removes the vertex corresponding to the specified index.

     Can not remove the 

    start or end vertex if it already connects to other element.

  

  

   index: The index which should be in [0,NumberOfVertices).
  """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetVertex(self,index,vertexPoint):
  """
  SetVertex(self: Wire,index: int,vertexPoint: XYZ)

   Sets the position of a given vertex.

     If the vertex is start or end point,

    and the wire connects to electrical device,the wire end offset will be set 

    according to the given vertex.

     If the vertex is start or end point,and the 

    wire connects to other wire,user can't set the vertex and exception will be 

    thrown.

     If the vertex is start or end point,and the wire connects to 

    nothing,the vertex will be set as the given vertex.

  

  

   index: The index of the existing vertex. Should be between 0 and 

    Autodesk.Revit.DB.Electrical.Wire.NumberOfVertices.

  

   vertexPoint: The new position for the vertex.
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
 GroundConductorNum=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The ground conductor number. Its default value is zero after created.



Get: GroundConductorNum(self: Wire) -> int



Set: GroundConductorNum(self: Wire)=value

"""

 HotConductorNum=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The hot conductor number. Its default value is zero after created.



Get: HotConductorNum(self: Wire) -> int



Set: HotConductorNum(self: Wire)=value

"""

 NeutralConductorNum=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The neutral conductor number. Its default value is zero after created.



Get: NeutralConductorNum(self: Wire) -> int



Set: NeutralConductorNum(self: Wire)=value

"""

 NumberOfVertices=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number of vertices of the wire,including the start and end point.



Get: NumberOfVertices(self: Wire) -> int



"""

 WiringType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The wiring type(arc or chamfer) for the wire.



Get: WiringType(self: Wire) -> WiringType



Set: WiringType(self: Wire)=value

"""


