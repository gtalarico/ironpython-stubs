class PanelScheduleTemplate(Element,IDisposable):
 """
 The PanelScheduleTemplate class represents an instance of panel schedule template
    element. An instance object could be a branch panel,a switchboard or a data panel template.
 """
 def CopyFrom(self,OtherADoc,otherElem):
  """
  CopyFrom(self: PanelScheduleTemplate,OtherADoc: Document,otherElem: PanelScheduleTemplate)
   Copies all values from other element to this object.
  
   OtherADoc: The Document for the otherElem
   otherElem: The element being copied from.
  """
  pass
 @staticmethod
 def Create(document,type,config,strName):
  """
  Create(document: Document,type: PanelScheduleType,config: PanelConfiguration,strName: str) -> PanelScheduleTemplate
  
   Creates a new instance of a panel schedule template.
  
   document: The document where the element will be created and added.
   type: The panel schedule type.
   config: The panel configuration type.
   strName: The name of the panel schedule template to be created.
   Returns: The newly created panel schedule template element.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetPanelScheduleType(self):
  """
  GetPanelScheduleType(self: PanelScheduleTemplate) -> PanelScheduleType
  
   Returns the panel schedule type.
  """
  pass
 def GetSectionData(self,sectionType):
  """
  GetSectionData(self: PanelScheduleTemplate,sectionType: SectionType) -> TableSectionData
  
   Gets the writable section data object.
   Returns: The table section data object.
  """
  pass
 def GetTableData(self):
  """
  GetTableData(self: PanelScheduleTemplate) -> PanelScheduleData
  
   Gets the writable table data object.
   Returns: The panel schedule data object.
  """
  pass
 def HasSameType(self,otherTemplate):
  """
  HasSameType(self: PanelScheduleTemplate,otherTemplate: PanelScheduleTemplate) -> bool
  
   Checks if given template has the same panel schedule type with this template.
  
   otherTemplate: The given template to check.
   Returns: True if the given template has the same panel schedule type with this template,
    false otherwise.
  """
  pass
 @staticmethod
 def IsValidPanelConfiguration(scheduleType,configuration):
  """
  IsValidPanelConfiguration(scheduleType: PanelScheduleType,configuration: PanelConfiguration) -> bool
  
   Checks if given panel configuration is valid for given panel schedule type.
  
   scheduleType: The panel schedule type.
   configuration: The given configuration to check.
   Returns: True if panel schedule template can have a valid configuration assigned,false 
    otherwise.
  """
  pass
 @staticmethod
 def IsValidType(*__args):
  """
  IsValidType(panelScheduleType: PanelScheduleType) -> bool
  
   Checks if given type is valid for this panel schedule template element.
  
   panelScheduleType: The given type to check.
   Returns: True if panel schedule template can have a type assigned and this type is valid 
    for this element,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetTableData(self,Data):
  """
  SetTableData(self: PanelScheduleTemplate,Data: PanelScheduleData)
   Assigns table data to this template
  
   Data: The panel schedule data
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
 IsBranchPanelSchedule=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Checks to see if this object is branch panel schedule template element.

Get: IsBranchPanelSchedule(self: PanelScheduleTemplate) -> bool

"""

 IsDataPanelSchedule=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Checks to see if this object is data panel schedule template element.

Get: IsDataPanelSchedule(self: PanelScheduleTemplate) -> bool

"""

 IsDefault=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Checks to see if this is default template for the given panel schedule type.

Get: IsDefault(self: PanelScheduleTemplate) -> bool

"""

 IsSwitchboardSchedule=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Checks to see if this object is switchboard schedule template element.

Get: IsSwitchboardSchedule(self: PanelScheduleTemplate) -> bool

"""


