class ScheduleField(object,IDisposable):
 """ A field in a schedule. """
 def CanDisplayMinMax(self):
  """
  CanDisplayMinMax(self: ScheduleField) -> bool
  
   Indicates if this field can display minimum and maximum values.
   Returns: True if this field can display minimum and maximum values,false otherwise.
  """
  pass
 def CanTotal(self):
  """
  CanTotal(self: ScheduleField) -> bool
  
   Indicates if totals can be enabled for this field.
   Returns: True if this field can be totaled,false otherwise.
  """
  pass
 def CanTotalByAssemblyType(self):
  """
  CanTotalByAssemblyType(self: ScheduleField) -> bool
  
   Indicates if totals by assembly type can be enabled for this field.
   Returns: True if this field can be totaled by assembly type,false otherwise.
  """
  pass
 def CreatesCircularReferences(self,fieldId):
  """
  CreatesCircularReferences(self: ScheduleField,fieldId: ScheduleFieldId) -> bool
  
   Checks whether a field ID would create a circular chain of references
     when 
    used by the PercentageOf property of this field.
  
  
   fieldId: The field ID to check.
   Returns: True if the field ID would create a circular chain of references,
     false 
    otherwise.
  """
  pass
 def Dispose(self):
  """ Dispose(self: ScheduleField) """
  pass
 def GetCombinedParameters(self):
  """
  GetCombinedParameters(self: ScheduleField) -> IList[TableCellCombinedParameterData]
  
   Gets this field's combine parameter array if applicable
   Returns: Gets array of TableCellCombinedParameterData with the combined parameters data
  """
  pass
 def GetFormatOptions(self):
  """
  GetFormatOptions(self: ScheduleField) -> FormatOptions
  
   Gets the FormatOptions to optionally override the default settings in the Units 
    class.
  
   Returns: A copy of the FormatOptions.
  """
  pass
 def GetName(self):
  """
  GetName(self: ScheduleField) -> str
  
   Gets the name of the field.
   Returns: The name of the field.
  """
  pass
 def GetSchedulableField(self):
  """
  GetSchedulableField(self: ScheduleField) -> SchedulableField
  
   Gets a SchedulableField object representing this field.
   Returns: The SchedulableField object.
  """
  pass
 def GetStyle(self):
  """
  GetStyle(self: ScheduleField) -> TableCellStyle
  
   Gets the style of this field.
  """
  pass
 def IsValidCombinedParameters(self,data):
  """ IsValidCombinedParameters(self: ScheduleField,data: IList[TableCellCombinedParameterData]) -> bool """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ScheduleField,disposing: bool) """
  pass
 def ResetOverride(self):
  """
  ResetOverride(self: ScheduleField)
   Resets the override of this field.
  """
  pass
 def SetCombinedParameters(self,data):
  """ SetCombinedParameters(self: ScheduleField,data: IList[TableCellCombinedParameterData]) """
  pass
 def SetFormatOptions(self,formatOptions):
  """
  SetFormatOptions(self: ScheduleField,formatOptions: FormatOptions)
   Sets the FormatOptions to optionally override the default settings in the Units 
    class.
  
  
   formatOptions: The FormatOptions.
  """
  pass
 def SetStyle(self,style):
  """
  SetStyle(self: ScheduleField,style: TableCellStyle)
   Sets the style of this field.
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 ColumnHeading=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The column heading text.

Get: ColumnHeading(self: ScheduleField) -> str

Set: ColumnHeading(self: ScheduleField)=value
"""

 Definition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The ScheduleDefinition that this field belongs to.

Get: Definition(self: ScheduleField) -> ScheduleDefinition

"""

 DisplayType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates the chosen display type for the field.

Get: DisplayType(self: ScheduleField) -> ScheduleFieldDisplayType

Set: DisplayType(self: ScheduleField)=value
"""

 FieldId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The ID of the field in the containing ScheduleDefinition.

Get: FieldId(self: ScheduleField) -> ScheduleFieldId

"""

 FieldIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The index of the field in the containing ScheduleDefinition.

Get: FieldIndex(self: ScheduleField) -> int

"""

 FieldType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The type of data displayed by the field.

Get: FieldType(self: ScheduleField) -> ScheduleFieldType

"""

 GridColumnWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The width of the column in the editable grid view,measured in feet.

Get: GridColumnWidth(self: ScheduleField) -> float

Set: GridColumnWidth(self: ScheduleField)=value
"""

 HasSchedulableField=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if this ScheduleField object has access to a SchedulableField.
   Calculated and combined parameter fields will not have the access.

Get: HasSchedulableField(self: ScheduleField) -> bool

"""

 HasTotals=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the field displays totals.

Get: HasTotals(self: ScheduleField) -> bool

Set: HasTotals(self: ScheduleField)=value
"""

 HeadingOrientation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The orientation of the column heading text.

Get: HeadingOrientation(self: ScheduleField) -> ScheduleHeadingOrientation

Set: HeadingOrientation(self: ScheduleField)=value
"""

 HorizontalAlignment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The horizontal alignment of text in the column.

Get: HorizontalAlignment(self: ScheduleField) -> ScheduleHorizontalAlignment

Set: HorizontalAlignment(self: ScheduleField)=value
"""

 IsCalculatedField=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the field is a calculated field (Formula or Percentage).

Get: IsCalculatedField(self: ScheduleField) -> bool

"""

 IsCombinedParameterField=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the field is a combined parameter field.

Get: IsCombinedParameterField(self: ScheduleField) -> bool

"""

 IsHidden=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the field is hidden in the schedule.

Get: IsHidden(self: ScheduleField) -> bool

Set: IsHidden(self: ScheduleField)=value
"""

 IsOverridden=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the field is overridden or not.

Get: IsOverridden(self: ScheduleField) -> bool

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ScheduleField) -> bool

"""

 ParameterId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The ID of the parameter displayed by the field.

Get: ParameterId(self: ScheduleField) -> ElementId

"""

 PercentageBy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The ID of the grouped schedule field used to calculate percentage totals.

Get: PercentageBy(self: ScheduleField) -> ScheduleFieldId

Set: PercentageBy(self: ScheduleField)=value
"""

 PercentageOf=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The ID of the field to calculate percentages of.

Get: PercentageOf(self: ScheduleField) -> ScheduleFieldId

Set: PercentageOf(self: ScheduleField)=value
"""

 Schedule=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The schedule that this field belongs to.

Get: Schedule(self: ScheduleField) -> ViewSchedule

"""

 SheetColumnWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The width of the column on a sheet,measured in feet.

Get: SheetColumnWidth(self: ScheduleField) -> float

Set: SheetColumnWidth(self: ScheduleField)=value
"""

 TotalByAssemblyType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """In an assembly schedule view,indicates if totals are calculated for all
   assembly instances of the same type or only for a single instance.

Get: TotalByAssemblyType(self: ScheduleField) -> bool

Set: TotalByAssemblyType(self: ScheduleField)=value
"""

 UnitType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The unit type of this field,if applicable.

Get: UnitType(self: ScheduleField) -> UnitType

"""


