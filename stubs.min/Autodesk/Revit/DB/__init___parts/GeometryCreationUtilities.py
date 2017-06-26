class GeometryCreationUtilities(object):
 """ A utility that allows construction of basic solid shapes. """
 @staticmethod
 def CreateBlendGeometry(firstLoop,secondLoop,vertexPairs,solidOptions=None):
  """
  CreateBlendGeometry(firstLoop: CurveLoop,secondLoop: CurveLoop,vertexPairs: ICollection[VertexPair]) -> Solid
  CreateBlendGeometry(firstLoop: CurveLoop,secondLoop: CurveLoop,vertexPairs: ICollection[VertexPair],solidOptions: SolidOptions) -> Solid
  """
  pass
 @staticmethod
 def CreateExtrusionGeometry(profileLoops,extrusionDir,extrusionDist,solidOptions=None):
  """
  CreateExtrusionGeometry(profileLoops: IList[CurveLoop],extrusionDir: XYZ,extrusionDist: float) -> Solid
  CreateExtrusionGeometry(profileLoops: IList[CurveLoop],extrusionDir: XYZ,extrusionDist: float,solidOptions: SolidOptions) -> Solid
  """
  pass
 @staticmethod
 def CreateFixedReferenceSweptGeometry(sweepPath,pathAttachmentCrvIdx,pathAttachmentParam,profileLoops,fixedReferenceDirection,solidOptions=None):
  """
  CreateFixedReferenceSweptGeometry(sweepPath: CurveLoop,pathAttachmentCrvIdx: int,pathAttachmentParam: float,profileLoops: IList[CurveLoop],fixedReferenceDirection: XYZ) -> Solid
  CreateFixedReferenceSweptGeometry(sweepPath: CurveLoop,pathAttachmentCrvIdx: int,pathAttachmentParam: float,profileLoops: IList[CurveLoop],fixedReferenceDirection: XYZ,solidOptions: SolidOptions) -> Solid
  """
  pass
 @staticmethod
 def CreateLoftGeometry(profileLoops,solidOptions):
  """ CreateLoftGeometry(profileLoops: IList[CurveLoop],solidOptions: SolidOptions) -> Solid """
  pass
 @staticmethod
 def CreateRevolvedGeometry(coordinateFrame,profileLoops,startAngle,endAngle,solidOptions=None):
  """
  CreateRevolvedGeometry(coordinateFrame: Frame,profileLoops: IList[CurveLoop],startAngle: float,endAngle: float) -> Solid
  CreateRevolvedGeometry(coordinateFrame: Frame,profileLoops: IList[CurveLoop],startAngle: float,endAngle: float,solidOptions: SolidOptions) -> Solid
  """
  pass
 @staticmethod
 def CreateSweptBlendGeometry(pathCurve,pathParams,profileLoops,vertexPairs,solidOptions=None):
  """
  CreateSweptBlendGeometry(pathCurve: Curve,pathParams: IList[float],profileLoops: IList[CurveLoop],vertexPairs: IList[ICollection[VertexPair]]) -> Solid
  CreateSweptBlendGeometry(pathCurve: Curve,pathParams: IList[float],profileLoops: IList[CurveLoop],vertexPairs: IList[ICollection[VertexPair]],solidOptions: SolidOptions) -> Solid
  """
  pass
 @staticmethod
 def CreateSweptGeometry(sweepPath,pathAttachmentCrvIdx,pathAttachmentParam,profileLoops,solidOptions=None):
  """
  CreateSweptGeometry(sweepPath: CurveLoop,pathAttachmentCrvIdx: int,pathAttachmentParam: float,profileLoops: IList[CurveLoop]) -> Solid
  CreateSweptGeometry(sweepPath: CurveLoop,pathAttachmentCrvIdx: int,pathAttachmentParam: float,profileLoops: IList[CurveLoop],solidOptions: SolidOptions) -> Solid
  """
  pass
 __all__=[
  'CreateBlendGeometry',
  'CreateExtrusionGeometry',
  'CreateFixedReferenceSweptGeometry',
  'CreateLoftGeometry',
  'CreateRevolvedGeometry',
  'CreateSweptBlendGeometry',
  'CreateSweptGeometry',
 ]

