class FamilyElementVisibility(APIObject,IDisposable):
 """
 Provides access to the visibility parameters of family elements in family document.

 

 FamilyElementVisibility(visibilityType: FamilyElementVisibilityType)
 """
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: APIObject) """
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
 @staticmethod
 def __new__(self,visibilityType):
  """ __new__(cls: type,visibilityType: FamilyElementVisibilityType) """
  pass
 IsShownInCoarse=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the instance is display with Coarse detail level in the view 

of project document.



Get: IsShownInCoarse(self: FamilyElementVisibility) -> bool



Set: IsShownInCoarse(self: FamilyElementVisibility)=value

"""

 IsShownInFine=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the instance is display with Fine detail level in the view 

of project document.



Get: IsShownInFine(self: FamilyElementVisibility) -> bool



Set: IsShownInFine(self: FamilyElementVisibility)=value

"""

 IsShownInFrontBack=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the instance is display in Front/Back view of project document.



Get: IsShownInFrontBack(self: FamilyElementVisibility) -> bool



Set: IsShownInFrontBack(self: FamilyElementVisibility)=value

"""

 IsShownInLeftRight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the instance is display in Left/Right view of project document.



Get: IsShownInLeftRight(self: FamilyElementVisibility) -> bool



Set: IsShownInLeftRight(self: FamilyElementVisibility)=value

"""

 IsShownInMedium=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the instance is display with Medium detail level in the view 

of project document.



Get: IsShownInMedium(self: FamilyElementVisibility) -> bool



Set: IsShownInMedium(self: FamilyElementVisibility)=value

"""

 IsShownInPlanRCPCut=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the instance is displayed when cut in Plan/RCP (if the category permits).



Get: IsShownInPlanRCPCut(self: FamilyElementVisibility) -> bool



Set: IsShownInPlanRCPCut(self: FamilyElementVisibility)=value

"""

 IsShownInTopBottom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the instance is display in Plan/RCP view of project document.



Get: IsShownInTopBottom(self: FamilyElementVisibility) -> bool



Set: IsShownInTopBottom(self: FamilyElementVisibility)=value

"""

 IsShownOnlyWhenCut=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the instance is displayed only if it has been cut.



Get: IsShownOnlyWhenCut(self: FamilyElementVisibility) -> bool



Set: IsShownOnlyWhenCut(self: FamilyElementVisibility)=value

"""

 VisibilityType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the instance is Model or View specific.



Get: VisibilityType(self: FamilyElementVisibility) -> FamilyElementVisibilityType



"""


