class LanguageSpecificStringDictionary(object,IDictionary[XmlLanguage,str],ICollection[KeyValuePair[XmlLanguage,str]],IEnumerable[KeyValuePair[XmlLanguage,str]],IEnumerable,IDictionary,ICollection):
 """ Represents a dictionary of strings that are used to represent the name of an object in different languages. """
 def Add(self,*__args):
  """
  Add(self: LanguageSpecificStringDictionary,key: XmlLanguage,value: str)
   Adds a language and associated string to the 
    System.Windows.Media.LanguageSpecificStringDictionary.
  
  
   key: A value of type System.Windows.Markup.XmlLanguage.
   value: A value of type System.String.
  Add(self: LanguageSpecificStringDictionary,item: KeyValuePair[XmlLanguage,str])
  """
  pass
 def Clear(self):
  """
  Clear(self: LanguageSpecificStringDictionary)
   Removes all elements from the collection.
  """
  pass
 def Contains(self,item):
  """ Contains(self: LanguageSpecificStringDictionary,item: KeyValuePair[XmlLanguage,str]) -> bool """
  pass
 def ContainsKey(self,key):
  """
  ContainsKey(self: LanguageSpecificStringDictionary,key: XmlLanguage) -> bool
  
   Determines whether the System.Windows.Media.LanguageSpecificStringDictionary 
    contains the specified language.
  
  
   key: A value of type System.Windows.Markup.XmlLanguage.
   Returns: true if the System.Windows.Media.LanguageSpecificStringDictionary contains key; 
    otherwise,false.
  """
  pass
 def CopyTo(self,array,index):
  """ CopyTo(self: LanguageSpecificStringDictionary,array: Array[KeyValuePair[XmlLanguage,str]],index: int) """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: LanguageSpecificStringDictionary) -> IEnumerator[KeyValuePair[XmlLanguage,str]]
  
   Returns an enumerator that iterates through the collection.
   Returns: An enumerator that iterates through the collection.
  """
  pass
 def Remove(self,*__args):
  """
  Remove(self: LanguageSpecificStringDictionary,key: XmlLanguage) -> bool
  
   Removes the element from System.Windows.Media.LanguageSpecificStringDictionary 
    based on the specified key value.
  
  
   key: A value of type System.Windows.Markup.XmlLanguage.
   Returns: true if the element referenced by key was successfully deleted; otherwise false.
  Remove(self: LanguageSpecificStringDictionary,item: KeyValuePair[XmlLanguage,str]) -> bool
  """
  pass
 def TryGetValue(self,key,value):
  """
  TryGetValue(self: LanguageSpecificStringDictionary,key: XmlLanguage) -> (bool,str)
  
   Retrieves the string value in the 
    System.Windows.Media.LanguageSpecificStringDictionary for a specified key,or 
    language.
  
  
   key: A value of type System.Windows.Markup.XmlLanguage.
   Returns: true if the System.Windows.Media.LanguageSpecificStringDictionary contains an 
    entry for key; otherwise false.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
  pass
 def __contains__(self,*args):
  """
  __contains__(self: IDictionary[XmlLanguage,str],key: XmlLanguage) -> bool
  __contains__(self: IDictionary,key: object) -> bool
  
   Determines whether the System.Collections.IDictionary object contains an 
    element with the specified key.
  
  
   key: The key to locate in the System.Collections.IDictionary object.
   Returns: true if the System.Collections.IDictionary contains an element with the key; 
    otherwise,false.
  """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __len__(self,*args):
  """ x.__len__() <==> len(x) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of strings in the System.Windows.Media.LanguageSpecificStringDictionary.

Get: Count(self: LanguageSpecificStringDictionary) -> int

"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Media.LanguageSpecificStringDictionary is read-only.

Get: IsReadOnly(self: LanguageSpecificStringDictionary) -> bool

"""

 Keys=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection containing the keys,or System.Windows.Markup.XmlLanguage objects,in the dictionary.

Get: Keys(self: LanguageSpecificStringDictionary) -> ICollection[XmlLanguage]

"""

 Values=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection containing the values,or strings,in the dictionary.

Get: Values(self: LanguageSpecificStringDictionary) -> ICollection[str]

"""


