class GeometryInstance(GeometryObject,IDisposable):
 """
 An instance of another element (symbol),specially positioned by this
 element.
 """
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 def GetInstanceGeometry(self,transform=None):
  """
  GetInstanceGeometry(self: GeometryInstance) -> GeometryElement
  
   Computes the geometric representation of the instance.
   Returns: An element which contains the computed geometry for the instance.
  GetInstanceGeometry(self: GeometryInstance,transform: Transform) -> GeometryElement
  
   Computes a transformation of the geometric representation of the instance.
  
   transform: The transformation to apply to the geometry.
   Returns: An element which contains the computed geometry for the transformed instance.
  """
  pass
 def GetSymbolGeometry(self,transform=None):
  """
  GetSymbolGeometry(self: GeometryInstance) -> GeometryElement
  
   Computes the geometric representation of the symbol which generates this 
    instance.
  
   Returns: An element which contains the computed geometry for the symbol.
  GetSymbolGeometry(self: GeometryInstance,transform: Transform) -> GeometryElement
  
   Computes a transformation of the geometric representation of the symbol 
  which 
    generates this instance.
  
  
   transform: The transformation to apply to the geometry.
   Returns: An element which contains the computed geometry for the transformed symbol.
  """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: GeometryObject) """
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
 Symbol=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The symbol element that this object is referring to.

Get: Symbol(self: GeometryInstance) -> Element

"""

 SymbolGeometry=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The geometric representation of the symbol which generates this instance.

Get: SymbolGeometry(self: GeometryInstance) -> GeometryElement

"""

 Transform=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The affine transformation from the local coordinate space of the symbol into the
coordinate space of the instance.

Get: Transform(self: GeometryInstance) -> Transform

"""


