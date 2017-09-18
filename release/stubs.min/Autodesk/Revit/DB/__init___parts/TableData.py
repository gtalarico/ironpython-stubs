class TableData(object,IDisposable):
 """
 The TableData class is implemented to hold most of the data that describe

    the style of the rows,columns,and cells in a table.
 """
 def Dispose(self):
  """ Dispose(self: TableData) """
  pass
 def GetSectionData(self,*__args):
  """
  GetSectionData(self: TableData,sectionType: SectionType) -> TableSectionData

  

   Returns the pointer to the section data array element at the specified section 

    type.

  

  

   sectionType: The section type of section data array. If the integral value of the section 

    type is out of the boundary of section data array,

     null is returned.

  

  GetSectionData(self: TableData,nIndex: int) -> TableSectionData

  

   Returns the section data array element at the specified index.

  

   nIndex: The index of section data array. If the index is out of the boundary of section 

    data array,

     ll is returned.
  """
  pass
 def IsEqual(self,OtherElem):
  """
  IsEqual(self: TableData,OtherElem: TableData) -> bool

  

   Checks if this element is equal in value to the other element.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: TableData,disposing: bool) """
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
 FreezeColumnsAndRows=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """set to true if the columns and rows should be unmovable by the slider grips



Get: FreezeColumnsAndRows(self: TableData) -> bool



Set: FreezeColumnsAndRows(self: TableData)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: TableData) -> bool



"""

 NumberOfSections=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of items in section data array.



Get: NumberOfSections(self: TableData) -> int



"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the table width in feet



Get: Width(self: TableData) -> float



Set: Width(self: TableData)=value

"""

 WidthInPixels=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the width of the panel schedule in pixels



Get: WidthInPixels(self: TableData) -> int



"""


