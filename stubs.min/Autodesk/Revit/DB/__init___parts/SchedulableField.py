class SchedulableField(object,IDisposable):
 """
 A non-calculated field eligible to be included in a schedule.
 
 SchedulableField(fieldType: ScheduleFieldType,parameterId: ElementId)
 SchedulableField(fieldType: ScheduleFieldType)
 SchedulableField()
 """
 def Dispose(self):
  """ Dispose(self: SchedulableField) """
  pass
 def Equals(self,obj):
  """
  Equals(self: SchedulableField,obj: object) -> bool
  
   Determines whether the specified System.Object is equal to the current 
    System.Object.
  
  
   obj: The other object to evaluate.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: SchedulableField) -> int
  
   Gets the integer value of the SchedulableField as hash code
  """
  pass
 def GetName(self,document):
  """
  GetName(self: SchedulableField,document: Document) -> str
  
   Gets the name of the field.
  
   document: The document in which the field will be used.
   Returns: The name of the field.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: SchedulableField,disposing: bool) """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,fieldType=None,parameterId=None):
  """
  __new__(cls: type,fieldType: ScheduleFieldType,parameterId: ElementId)
  __new__(cls: type,fieldType: ScheduleFieldType)
  __new__(cls: type)
  """
  pass
 def __ne__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 FieldType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The type of data displayed by the field.

Get: FieldType(self: SchedulableField) -> ScheduleFieldType

Set: FieldType(self: SchedulableField)=value
"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: SchedulableField) -> bool

"""

 ParameterId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The ID of the parameter displayed by the field.

Get: ParameterId(self: SchedulableField) -> ElementId

Set: ParameterId(self: SchedulableField)=value
"""


