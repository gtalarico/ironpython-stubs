class ProjectInfo(Element,IDisposable):
 """ An object that represents a Project Information within the Autodesk Revit project. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
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
 Address=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get or Set the Project Address of the Project Information.



Get: Address(self: ProjectInfo) -> str



Set: Address(self: ProjectInfo)=value

"""

 Author=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get or Set the Project Author of the Project Information.



Get: Author(self: ProjectInfo) -> str



Set: Author(self: ProjectInfo)=value

"""

 BuildingName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get or Set the Building Name of the Project Information.



Get: BuildingName(self: ProjectInfo) -> str



Set: BuildingName(self: ProjectInfo)=value

"""

 ClientName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get or Set the Client Name of the Project Information.



Get: ClientName(self: ProjectInfo) -> str



Set: ClientName(self: ProjectInfo)=value

"""

 IssueDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get or Set the Project Issue Date of the Project Information.



Get: IssueDate(self: ProjectInfo) -> str



Set: IssueDate(self: ProjectInfo)=value

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get or Set the Project Name of the Project Information.



Get: Name(self: ProjectInfo) -> str



Set: Name(self: ProjectInfo)=value

"""

 Number=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get or Set the Project Number of the Project Information.



Get: Number(self: ProjectInfo) -> str



Set: Number(self: ProjectInfo)=value

"""

 OrganizationDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get or Set the Organization Description of the Project Information.



Get: OrganizationDescription(self: ProjectInfo) -> str



Set: OrganizationDescription(self: ProjectInfo)=value

"""

 OrganizationName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get or Set the Organization Name of the Project Information.



Get: OrganizationName(self: ProjectInfo) -> str



Set: OrganizationName(self: ProjectInfo)=value

"""

 Status=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get or Set the Project Status of the Project Information.



Get: Status(self: ProjectInfo) -> str



Set: Status(self: ProjectInfo)=value

"""


