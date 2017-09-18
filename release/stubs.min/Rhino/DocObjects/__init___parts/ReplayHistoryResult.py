class ReplayHistoryResult(object):
 # no doc
 def UpdateToAngularDimension(self,dimension,attributes):
  """ UpdateToAngularDimension(self: ReplayHistoryResult,dimension: AngularDimension,attributes: ObjectAttributes) -> bool """
  pass
 def UpdateToArc(self,arc,attributes):
  """ UpdateToArc(self: ReplayHistoryResult,arc: Arc,attributes: ObjectAttributes) -> bool """
  pass
 def UpdateToBrep(self,brep,attributes):
  """ UpdateToBrep(self: ReplayHistoryResult,brep: Brep,attributes: ObjectAttributes) -> bool """
  pass
 def UpdateToCircle(self,circle,attributes):
  """ UpdateToCircle(self: ReplayHistoryResult,circle: Circle,attributes: ObjectAttributes) -> bool """
  pass
 def UpdateToClippingPlane(self,plane,uMagnitude,vMagnitude,*__args):
  """
  UpdateToClippingPlane(self: ReplayHistoryResult,plane: Plane,uMagnitude: float,vMagnitude: float,clippedViewportIds: IEnumerable[Guid],attributes: ObjectAttributes) -> bool

  UpdateToClippingPlane(self: ReplayHistoryResult,plane: Plane,uMagnitude: float,vMagnitude: float,clippedViewportId: Guid,attributes: ObjectAttributes) -> bool
  """
  pass
 def UpdateToCurve(self,curve,attributes):
  """ UpdateToCurve(self: ReplayHistoryResult,curve: Curve,attributes: ObjectAttributes) -> bool """
  pass
 def UpdateToEllipse(self,ellipse,attributes):
  """ UpdateToEllipse(self: ReplayHistoryResult,ellipse: Ellipse,attributes: ObjectAttributes) -> bool """
  pass
 def UpdateToExtrusion(self,extrusion,attributes):
  """ UpdateToExtrusion(self: ReplayHistoryResult,extrusion: Extrusion,attributes: ObjectAttributes) -> bool """
  pass
 def UpdateToHatch(self,hatch,attributes):
  """ UpdateToHatch(self: ReplayHistoryResult,hatch: Hatch,attributes: ObjectAttributes) -> bool """
  pass
 def UpdateToLeader(self,leader,attributes):
  """ UpdateToLeader(self: ReplayHistoryResult,leader: Leader,attributes: ObjectAttributes) -> bool """
  pass
 def UpdateToLine(self,from,to,attributes):
  """ UpdateToLine(self: ReplayHistoryResult,from: Point3d,to: Point3d,attributes: ObjectAttributes) -> bool """
  pass
 def UpdateToLinearDimension(self,dimension,attributes):
  """ UpdateToLinearDimension(self: ReplayHistoryResult,dimension: LinearDimension,attributes: ObjectAttributes) -> bool """
  pass
 def UpdateToMesh(self,mesh,attributes):
  """ UpdateToMesh(self: ReplayHistoryResult,mesh: Mesh,attributes: ObjectAttributes) -> bool """
  pass
 def UpdateToPoint(self,point,attributes):
  """ UpdateToPoint(self: ReplayHistoryResult,point: Point3d,attributes: ObjectAttributes) -> bool """
  pass
 def UpdateToPointCloud(self,*__args):
  """
  UpdateToPointCloud(self: ReplayHistoryResult,points: IEnumerable[Point3d],attributes: ObjectAttributes) -> bool

  UpdateToPointCloud(self: ReplayHistoryResult,cloud: PointCloud,attributes: ObjectAttributes) -> bool
  """
  pass
 def UpdateToPolyline(self,points,attributes):
  """ UpdateToPolyline(self: ReplayHistoryResult,points: IEnumerable[Point3d],attributes: ObjectAttributes) -> bool """
  pass
 def UpdateToRadialDimension(self,dimension,attributes):
  """ UpdateToRadialDimension(self: ReplayHistoryResult,dimension: RadialDimension,attributes: ObjectAttributes) -> bool """
  pass
 def UpdateToSphere(self,sphere,attributes):
  """ UpdateToSphere(self: ReplayHistoryResult,sphere: Sphere,attributes: ObjectAttributes) -> bool """
  pass
 def UpdateToSurface(self,surface,attributes):
  """ UpdateToSurface(self: ReplayHistoryResult,surface: Surface,attributes: ObjectAttributes) -> bool """
  pass
 def UpdateToText(self,text,*__args):
  """
  UpdateToText(self: ReplayHistoryResult,text: TextEntity,attributes: ObjectAttributes) -> bool

  UpdateToText(self: ReplayHistoryResult,text: str,plane: Plane,height: float,fontName: str,bold: bool,italic: bool,justification: TextJustification,attributes: ObjectAttributes) -> bool
  """
  pass
 def UpdateToTextDot(self,dot,attributes):
  """ UpdateToTextDot(self: ReplayHistoryResult,dot: TextDot,attributes: ObjectAttributes) -> bool """
  pass
 ExistingObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExistingObject(self: ReplayHistoryResult) -> RhinoObject



"""


