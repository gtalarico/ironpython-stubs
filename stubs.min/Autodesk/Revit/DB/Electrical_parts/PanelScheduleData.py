class PanelScheduleData(TableData,IDisposable):
 """
 The PanelScheduleData class holds most of the data that describe
    the layout,appearance,and style of the rows,columns,and cells
    of a panel schedule
 """
 def AddLoadClassification(self,loadClassficationId):
  """
  AddLoadClassification(self: PanelScheduleData,loadClassficationId: ElementId) -> bool
  
   Add a Load Classification Id to the array of Load Classifications.
  
   loadClassficationId: The load classification to add
   Returns: True if success; false if the given Id has already existed.
  """
  pass
 def Dispose(self):
  """ Dispose(self: TableData,A_0: bool) """
  pass
 def GetLoadClassifications(self):
  """
  GetLoadClassifications(self: PanelScheduleData) -> IList[ElementId]
  
   Gets an array of the load classifications associated with this panel schedule
   Returns: The array of the load classifications
  """
  pass
 def GetNumberOfCircuitRows(self):
  """
  GetNumberOfCircuitRows(self: PanelScheduleData) -> int
  
   Gets the number of rows in the circuit table
   Returns: The number of rows
  """
  pass
 def IsSymmetric(self):
  """
  IsSymmetric(self: PanelScheduleData) -> bool
  
   Check if this panel schedule is symmetric
   Returns: True if this panel schedule is symmetric,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: TableData,disposing: bool) """
  pass
 def RemoveLoadClassification(self,nIndex):
  """
  RemoveLoadClassification(self: PanelScheduleData,nIndex: int)
   Remove a Load Classification Id from the array of Load Classifications
  
   nIndex: The index at which to remove the load classification
  """
  pass
 def SetBorderAroundSchedule(self,borderId):
  """
  SetBorderAroundSchedule(self: PanelScheduleData,borderId: ElementId)
   Adds a border around the schedule
  
   borderId: The border to set around the schedule
  """
  pass
 def SetBorderAroundSections(self,borderId):
  """
  SetBorderAroundSections(self: PanelScheduleData,borderId: ElementId)
   Adds a border around the sections
  
   borderId: The border to set around the sections
  """
  pass
 def SetLoadClassifications(self,loadClassificaions):
  """ SetLoadClassifications(self: PanelScheduleData,loadClassificaions: IList[ElementId]) """
  pass
 def UpdateCircuitTableForInstance(self,pPanel):
  """
  UpdateCircuitTableForInstance(self: PanelScheduleData,pPanel: FamilyInstance)
   Redraw the circuit table for the given panel with the given parameter updates
  
   pPanel: The panel that this circuit table is being drawn for
  """
  pass
 def UpdateCircuitTableForTemplate(self,newType,nNumSlots,bPhasesAsCurrents):
  """
  UpdateCircuitTableForTemplate(self: PanelScheduleData,newType: PanelSchedulePhaseLoadType,nNumSlots: int,bPhasesAsCurrents: bool)
   Redraw the circuit table for a template with the given parameter updates
  
   newType: The new phase load type of the circuit table
   nNumSlots: The number of circuit slots
   bPhasesAsCurrents: True if the phase columns should be currents,false if they should be loads
  """
  pass
 def UpdateIsSectionHidden(self,sectionType,bHide):
  """
  UpdateIsSectionHidden(self: PanelScheduleData,sectionType: SectionType,bHide: bool)
   Update if this section is hidden or not
  
   sectionType: The Section Type
   bHide: Whether to hide this section or not
  """
  pass
 def UpdateLoadSummary(self):
  """
  UpdateLoadSummary(self: PanelScheduleData)
   Update the load summary section
  """
  pass
 def UpdateVerticalHeadersInSection(self,sectionType,bVertical):
  """
  UpdateVerticalHeadersInSection(self: PanelScheduleData,sectionType: SectionType,bVertical: bool)
   Sets if this header should have vertical text
  
   sectionType: The section type
   bVertical: Whether headers are vertical or not
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
 BodyShowsVerticalHeaders=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Shows text in the Load Summary section's headers vertically instead of horizontally

Get: BodyShowsVerticalHeaders(self: PanelScheduleData) -> bool

"""

 BorderAroundSchedule=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Places a border (GraphicStyle element) around the entire schedule,visible only on the instance and sheet

Get: BorderAroundSchedule(self: PanelScheduleData) -> ElementId

"""

 BorderAroundSections=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Places a border (GraphicStyle element) around each section,visible only on the instance and sheet

Get: BorderAroundSections(self: PanelScheduleData) -> ElementId

"""

 IsFooterSectionHidden=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True if the user wishes to hide the footer section; setting this value must go through the appropriate update function

Get: IsFooterSectionHidden(self: PanelScheduleData) -> bool

"""

 IsHeaderSectionHidden=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True if the user wishes to hide the header section; setting this value must go through the appropriate update function

Get: IsHeaderSectionHidden(self: PanelScheduleData) -> bool

"""

 IsPanelSinglePhase=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if the panel is single phase.

Get: IsPanelSinglePhase(self: PanelScheduleData) -> bool

Set: IsPanelSinglePhase(self: PanelScheduleData)=value
"""

 IsSummarySectionHidden=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True if the user wishes to hide the summary section; setting this value must go through the appropriate update function

Get: IsSummarySectionHidden(self: PanelScheduleData) -> bool

"""

 IsThirdPhaseHidden=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True if the user wishes to hide the 3rd phase column of a single phase panel

Get: IsThirdPhaseHidden(self: PanelScheduleData) -> bool

Set: IsThirdPhaseHidden(self: PanelScheduleData)=value
"""

 NumberOfSlots=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number of slots in the panel schedule; setting this value must go through the appropriate update function

Get: NumberOfSlots(self: PanelScheduleData) -> int

"""

 PanelConfiguration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The panel configuration of this panel schedule

Get: PanelConfiguration(self: PanelScheduleData) -> PanelConfiguration

"""

 PhaseLoadType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property determines the layout of the phase load columns; setting this value must go through the updateCircuitTable function

Get: PhaseLoadType(self: PanelScheduleData) -> PanelSchedulePhaseLoadType

"""

 PhasesAsCurrents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If true,the phase columns are currents (A),otherwise they are loads (VA); setting this value must go through the appropriate update function

Get: PhasesAsCurrents(self: PanelScheduleData) -> bool

"""

 ScheduleType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The panel schedule type of this panel schedule

Get: ScheduleType(self: PanelScheduleData) -> PanelScheduleType

"""

 ShowCircuitNumberOnOneRowForMultiphaseCircuits=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Shows the circuit number broken up on each row of the multiphase circuit rows if true,all on the first row otherwise

Get: ShowCircuitNumberOnOneRowForMultiphaseCircuits(self: PanelScheduleData) -> bool

Set: ShowCircuitNumberOnOneRowForMultiphaseCircuits(self: PanelScheduleData)=value
"""

 ShowMultipleRowsForMultiphaseCircuits=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """shows extra rows below multiphase circuits to indicate how many slots they take up if true,all on a single row otherwise

Get: ShowMultipleRowsForMultiphaseCircuits(self: PanelScheduleData) -> bool

Set: ShowMultipleRowsForMultiphaseCircuits(self: PanelScheduleData)=value
"""

 ShowSlotFromDeviceInsteadOfTemplate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When true,the number of rows in an instance will be the number of poles on the associated device,not a set number

Get: ShowSlotFromDeviceInsteadOfTemplate(self: PanelScheduleData) -> bool

Set: ShowSlotFromDeviceInsteadOfTemplate(self: PanelScheduleData)=value
"""

 SummaryShowsGroups=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Show groups of load classifications in the load summary section

Get: SummaryShowsGroups(self: PanelScheduleData) -> bool

Set: SummaryShowsGroups(self: PanelScheduleData)=value
"""

 SummaryShowsOnlyConnectedLoads=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Show only the connected load classifications in the summary section

Get: SummaryShowsOnlyConnectedLoads(self: PanelScheduleData) -> bool

Set: SummaryShowsOnlyConnectedLoads(self: PanelScheduleData)=value
"""

 SummaryShowsVerticalHeaders=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Shows text in the Load Summary section's headers vertically instead of horizontally

Get: SummaryShowsVerticalHeaders(self: PanelScheduleData) -> bool

"""


