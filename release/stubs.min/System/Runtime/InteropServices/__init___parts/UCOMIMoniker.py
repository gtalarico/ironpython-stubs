class UCOMIMoniker:
 """ Use System.Runtime.InteropServices.ComTypes.IMoniker instead. """
 def BindToObject(self,pbc,pmkToLeft,riidResult,ppvResult):
  """
  BindToObject(self: UCOMIMoniker,pbc: UCOMIBindCtx,pmkToLeft: UCOMIMoniker,riidResult: Guid) -> (Guid,object)

  

   Uses the moniker to bind to the object it identifies.

  

   pbc: A reference to the IBindCtx interface on the bind context object used in this binding operation.

   pmkToLeft: A reference to the moniker to the left of this moniker,if the moniker is part of a composite 

    moniker.

  

   riidResult: The interface identifier (IID) of the interface the client intends to use to communicate with 

    the object that the moniker identifies.
  """
  pass
 def BindToStorage(self,pbc,pmkToLeft,riid,ppvObj):
  """
  BindToStorage(self: UCOMIMoniker,pbc: UCOMIBindCtx,pmkToLeft: UCOMIMoniker,riid: Guid) -> (Guid,object)

  

   Retrieves an interface pointer to the storage that contains the object identified by the moniker.

  

   pbc: A reference to the IBindCtx interface on the bind context object used during this binding 

    operation.

  

   pmkToLeft: A reference to the moniker to the left of this moniker,if the moniker is part of a composite 

    moniker.

  

   riid: The interface identifier (IID) of the storage interface requested.
  """
  pass
 def CommonPrefixWith(self,pmkOther,ppmkPrefix):
  """
  CommonPrefixWith(self: UCOMIMoniker,pmkOther: UCOMIMoniker) -> UCOMIMoniker

  

   Creates a new moniker based on the common prefix that this moniker shares with another moniker.

  

   pmkOther: A reference to the IMoniker interface on another moniker to compare with this for a common 

    prefix.
  """
  pass
 def ComposeWith(self,pmkRight,fOnlyIfNotGeneric,ppmkComposite):
  """
  ComposeWith(self: UCOMIMoniker,pmkRight: UCOMIMoniker,fOnlyIfNotGeneric: bool) -> UCOMIMoniker

  

   Combines the current moniker with another moniker,creating a new composite moniker.

  

   pmkRight: A reference to the IMoniker interface on the moniker to compose onto the end of this moniker.

   fOnlyIfNotGeneric: If true,the caller requires a nongeneric composition,so the operation proceeds only if 

    pmkRight is a moniker class that this moniker can compose with in some way other than forming a 

    generic composite. If false,the method can create a generic composite if necessary.
  """
  pass
 def Enum(self,fForward,ppenumMoniker):
  """
  Enum(self: UCOMIMoniker,fForward: bool) -> UCOMIEnumMoniker

  

   Supplies a pointer to an enumerator that can enumerate the components of a composite moniker.

  

   fForward: If true,enumerates the monikers from left to right. If false,enumerates from right to left.
  """
  pass
 def GetClassID(self,pClassID):
  """
  GetClassID(self: UCOMIMoniker) -> Guid

  

   Retrieves the class identifier (CLSID) of an object.
  """
  pass
 def GetDisplayName(self,pbc,pmkToLeft,ppszDisplayName):
  """
  GetDisplayName(self: UCOMIMoniker,pbc: UCOMIBindCtx,pmkToLeft: UCOMIMoniker) -> str

  

   Gets the display name,which is a user-readable representation of this moniker.

  

   pbc: A reference to the bind context to use in this operation.

   pmkToLeft: A reference to the moniker to the left of this moniker,if the moniker is part of a composite 

    moniker.
  """
  pass
 def GetSizeMax(self,pcbSize):
  """
  GetSizeMax(self: UCOMIMoniker) -> Int64

  

   Returns the size in bytes of the stream needed to save the object.
  """
  pass
 def GetTimeOfLastChange(self,pbc,pmkToLeft,pFileTime):
  """
  GetTimeOfLastChange(self: UCOMIMoniker,pbc: UCOMIBindCtx,pmkToLeft: UCOMIMoniker) -> FILETIME

  

   Provides a number representing the time the object identified by this moniker was last changed.

  

   pbc: A reference to the bind context to be used in this binding operation.

   pmkToLeft: A reference to the moniker to the left of this moniker,if the moniker is part of a composite 

    moniker.
  """
  pass
 def Hash(self,pdwHash):
  """
  Hash(self: UCOMIMoniker) -> int

  

   Calculates a 32-bit integer using the internal state of the moniker.
  """
  pass
 def Inverse(self,ppmk):
  """
  Inverse(self: UCOMIMoniker) -> UCOMIMoniker

  

   Provides a moniker that,when composed to the right of this moniker or one of similar structure,

    composes to nothing.
  """
  pass
 def IsDirty(self):
  """
  IsDirty(self: UCOMIMoniker) -> int

  

   Checks the object for changes since it was last saved.

   Returns: An S_OKHRESULT value if the object has changed; otherwise,an S_FALSEHRESULT value.
  """
  pass
 def IsEqual(self,pmkOtherMoniker):
  """
  IsEqual(self: UCOMIMoniker,pmkOtherMoniker: UCOMIMoniker)

   Compares this moniker with a specified moniker and indicates whether they are identical.

  

   pmkOtherMoniker: A reference to the moniker to be used for comparison.
  """
  pass
 def IsRunning(self,pbc,pmkToLeft,pmkNewlyRunning):
  """
  IsRunning(self: UCOMIMoniker,pbc: UCOMIBindCtx,pmkToLeft: UCOMIMoniker,pmkNewlyRunning: UCOMIMoniker)

   Determines whether the object that is identified by this moniker is currently loaded and running.

  

   pbc: A reference to the bind context to be used in this binding operation.

   pmkToLeft: A reference to the moniker to the left of this moniker if this moniker is part of a composite.

   pmkNewlyRunning: A reference to the moniker most recently added to the Running Object Table.
  """
  pass
 def IsSystemMoniker(self,pdwMksys):
  """
  IsSystemMoniker(self: UCOMIMoniker) -> int

  

   Indicates whether this moniker is of one of the system-supplied moniker classes.
  """
  pass
 def Load(self,pStm):
  """
  Load(self: UCOMIMoniker,pStm: UCOMIStream)

   Initializes an object from the stream where it was previously saved.

  

   pStm: Stream from which the object is loaded.
  """
  pass
 def ParseDisplayName(self,pbc,pmkToLeft,pszDisplayName,pchEaten,ppmkOut):
  """
  ParseDisplayName(self: UCOMIMoniker,pbc: UCOMIBindCtx,pmkToLeft: UCOMIMoniker,pszDisplayName: str) -> (int,UCOMIMoniker)

  

   Reads as many characters of the specified display name as it understands and builds a moniker 

    corresponding to the portion read.

  

  

   pbc: A reference to the bind context to be used in this binding operation.

   pmkToLeft: A reference to the moniker that has been built out of the display name up to this point.

   pszDisplayName: A reference to the string containing the remaining display name to parse.
  """
  pass
 def Reduce(self,pbc,dwReduceHowFar,ppmkToLeft,ppmkReduced):
  """
  Reduce(self: UCOMIMoniker,pbc: UCOMIBindCtx,dwReduceHowFar: int,ppmkToLeft: UCOMIMoniker) -> (UCOMIMoniker,UCOMIMoniker)

  

   Returns a reduced moniker which is another moniker that refers to the same object as this 

    moniker but can be bound with equal or greater efficiency.

  

  

   pbc: A reference to the IBindCtx interface on the bind context to be used in this binding operation.

   dwReduceHowFar: Specifies how far this moniker should be reduced.

   ppmkToLeft: A reference to the moniker to the left of this moniker.
  """
  pass
 def RelativePathTo(self,pmkOther,ppmkRelPath):
  """
  RelativePathTo(self: UCOMIMoniker,pmkOther: UCOMIMoniker) -> UCOMIMoniker

  

   Supplies a moniker that,when appended to this moniker (or one with a similar structure),yields 

    the specified moniker.

  

  

   pmkOther: A reference to the moniker to which a relative path should be taken.
  """
  pass
 def Save(self,pStm,fClearDirty):
  """
  Save(self: UCOMIMoniker,pStm: UCOMIStream,fClearDirty: bool)

   Saves an object to the specified stream.

  

   pStm: The stream into which the object is saved.

   fClearDirty: Indicates whether to clear the modified flag after the save is complete.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
