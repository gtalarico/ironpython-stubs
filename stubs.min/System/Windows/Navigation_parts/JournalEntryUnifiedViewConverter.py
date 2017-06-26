class JournalEntryUnifiedViewConverter(object,IMultiValueConverter):
 """
 System.Windows.Navigation.JournalEntryUnifiedViewConverter merges navigation back history and navigation forward history (as exposed by System.Windows.Controls.Frame or System.Windows.Navigation.NavigationWindow) into a single,Windows Internet Explorer 7-style navigation menu.
 
 JournalEntryUnifiedViewConverter()
 """
 def Convert(self,values,targetType,parameter,culture):
  """
  Convert(self: JournalEntryUnifiedViewConverter,values: Array[object],targetType: Type,parameter: object,culture: CultureInfo) -> object
  
   Merges two navigation history stacks.
  
   values: An array of two navigation stacks.
   targetType: This parameter is not used.
   parameter: This parameter is not used.
   culture: This parameter is not used.
   Returns: An System.Collections.IEnumerable that can be used to enumerate the merged list 
    of navigation history stacks if neither passed navigation stack is null. null,
    otherwise.
  """
  pass
 def ConvertBack(self,value,targetTypes,parameter,culture):
  """
  ConvertBack(self: JournalEntryUnifiedViewConverter,value: object,targetTypes: Array[Type],parameter: object,culture: CultureInfo) -> Array[object]
  
   Not implemented.
  
   value: This parameter is not used.
   targetTypes: This parameter is not used.
   parameter: This parameter is not used.
   culture: This parameter is not used.
   Returns: Always returns System.Windows.Data.Binding.DoNothing.
  """
  pass
 @staticmethod
 def GetJournalEntryPosition(element):
  """
  GetJournalEntryPosition(element: DependencyObject) -> JournalEntryPosition
  
   Gets the 
    System.Windows.Navigation.JournalEntryUnifiedViewConverter.JournalEntryPosition�
    attached property for the specified element.
  
  
   element: The element from which to get the attached property value.
   Returns: The value of the 
    System.Windows.Navigation.JournalEntryUnifiedViewConverter.JournalEntryPosition�
    attached property of the journal entry for the specified element.
  """
  pass
 @staticmethod
 def SetJournalEntryPosition(element,position):
  """
  SetJournalEntryPosition(element: DependencyObject,position: JournalEntryPosition)
   Sets the 
    System.Windows.Navigation.JournalEntryUnifiedViewConverter.JournalEntryPositionP
    roperty�attached property of the specified element.
  
  
   element: The element on which to set the attached property value.
   position: Position of the System.Windows.Navigation.JournalEntryPosition object.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 JournalEntryPositionProperty=None

