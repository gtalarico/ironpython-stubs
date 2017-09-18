class ViewDisplayModel(object,IDisposable):
 """
 Represents the settings for displaying model graphics.

    version 2: m_showHiddenLines type changed bool -> ShowHiddenLinesValues::Enum
 """
 def Dispose(self):
  """ Dispose(self: ViewDisplayModel) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ViewDisplayModel,disposing: bool) """
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 EnableSilhouettes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True to show silhouettes edges. False to disable showing them.



Get: EnableSilhouettes(self: ViewDisplayModel) -> bool



Set: EnableSilhouettes(self: ViewDisplayModel)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: ViewDisplayModel) -> bool



"""

 ShowHiddenLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True to enable hidden lines. False to disable showing them.



Get: ShowHiddenLines(self: ViewDisplayModel) -> ShowHiddenLinesValues



Set: ShowHiddenLines(self: ViewDisplayModel)=value

"""

 SilhouetteEdgesGStyleId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Style ID for silhouette edges



Get: SilhouetteEdgesGStyleId(self: ViewDisplayModel) -> ElementId



Set: SilhouetteEdgesGStyleId(self: ViewDisplayModel)=value

"""

 SmoothEdges=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True to enable "smooth edge" (anti-aliasing) effect. False to disable it.



Get: SmoothEdges(self: ViewDisplayModel) -> bool



Set: SmoothEdges(self: ViewDisplayModel)=value

"""

 Transparency=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The percentage (0..100) of surface transparency

   0 means the surfaces are opaque,100 means they are fully transparent



Get: Transparency(self: ViewDisplayModel) -> int



Set: Transparency(self: ViewDisplayModel)=value

"""


