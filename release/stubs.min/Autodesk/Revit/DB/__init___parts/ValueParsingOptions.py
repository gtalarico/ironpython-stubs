class ValueParsingOptions(object,IDisposable):
 """
 Options for parsing strings into numbers with units.

 

 ValueParsingOptions()
 """
 def Dispose(self):
  """ Dispose(self: ValueParsingOptions) """
  pass
 def GetFormatOptions(self):
  """
  GetFormatOptions(self: ValueParsingOptions) -> FormatOptions

  

   Gets the FormatOptions to optionally override the default settings in the Units 

    class.

  

   Returns: A copy of the FormatOptions.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ValueParsingOptions,disposing: bool) """
  pass
 def SetFormatOptions(self,formatOptions):
  """
  SetFormatOptions(self: ValueParsingOptions,formatOptions: FormatOptions)

   Sets the FormatOptions to optionally override the default settings in the Units 

    class.

  

  

   formatOptions: The FormatOptions.
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
 AllowedValues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The allowable range of values to be parsed.



Get: AllowedValues(self: ValueParsingOptions) -> AllowedValues



Set: AllowedValues(self: ValueParsingOptions)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: ValueParsingOptions) -> bool



"""


