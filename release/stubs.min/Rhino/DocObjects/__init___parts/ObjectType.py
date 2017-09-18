class ObjectType(Enum,IComparable,IFormattable,IConvertible):
 """
 Defines binary mask values for each object type that can be found in a document.

 

 enum (flags) ObjectType,values: Annotation (512),AnyObject (4294967295),Brep (16),BrepLoop (524288),Cage (134217728),ClipPlane (536870912),Curve (4),Detail (32768),EdgeFilter (4194304),Extrusion (1073741824),Grip (16384),Hatch (65536),InstanceDefinition (2048),InstanceReference (4096),Light (256),Mesh (32),MeshEdge (33554432),MeshFace (67108864),MeshVertex (16777216),MorphControl (131072),None (0),Phantom (268435456),Point (1),PointSet (2),PolyedgeFilter (8388608),PolysrfFilter (2097152),Surface (8),TextDot (8192)
 """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Annotation=None
 AnyObject=None
 Brep=None
 BrepLoop=None
 Cage=None
 ClipPlane=None
 Curve=None
 Detail=None
 EdgeFilter=None
 Extrusion=None
 Grip=None
 Hatch=None
 InstanceDefinition=None
 InstanceReference=None
 Light=None
 Mesh=None
 MeshEdge=None
 MeshFace=None
 MeshVertex=None
 MorphControl=None
 None=None
 Phantom=None
 Point=None
 PointSet=None
 PolyedgeFilter=None
 PolysrfFilter=None
 Surface=None
 TextDot=None
 value__=None

