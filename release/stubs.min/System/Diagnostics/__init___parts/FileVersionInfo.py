class FileVersionInfo(object):
 """ Provides version information for a physical file on disk. """
 @staticmethod
 def GetVersionInfo(fileName):
  """
  GetVersionInfo(fileName: str) -> FileVersionInfo

  

   Returns a System.Diagnostics.FileVersionInfo representing the version information associated 

    with the specified file.

  

  

   fileName: The fully qualified path and name of the file to retrieve the version information for.

   Returns: A System.Diagnostics.FileVersionInfo containing information about the file. If the file did not 

    contain version information,the System.Diagnostics.FileVersionInfo contains only the name of 

    the file requested.
  """
  pass
 def ToString(self):
  """
  ToString(self: FileVersionInfo) -> str

  

   Returns a partial list of properties in the System.Diagnostics.FileVersionInfo and their values.

   Returns: A list of the following properties in this class and their values: 

    System.Diagnostics.FileVersionInfo.FileName,System.Diagnostics.FileVersionInfo.InternalName,

    System.Diagnostics.FileVersionInfo.OriginalFilename,

    System.Diagnostics.FileVersionInfo.FileVersion,

    System.Diagnostics.FileVersionInfo.FileDescription,

    System.Diagnostics.FileVersionInfo.ProductName,

    System.Diagnostics.FileVersionInfo.ProductVersion,System.Diagnostics.FileVersionInfo.IsDebug,

    System.Diagnostics.FileVersionInfo.IsPatched,System.Diagnostics.FileVersionInfo.IsPreRelease,

    System.Diagnostics.FileVersionInfo.IsPrivateBuild,

    System.Diagnostics.FileVersionInfo.IsSpecialBuild,System.Diagnostics.FileVersionInfo.Language.If 

    the file did not contain version information,this list will contain only the name of the 

    requested file. Boolean values will be false,and all other entries will be null.
  """
  pass
 Comments=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the comments associated with the file.



Get: Comments(self: FileVersionInfo) -> str



"""

 CompanyName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the company that produced the file.



Get: CompanyName(self: FileVersionInfo) -> str



"""

 FileBuildPart=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the build number of the file.



Get: FileBuildPart(self: FileVersionInfo) -> int



"""

 FileDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the description of the file.



Get: FileDescription(self: FileVersionInfo) -> str



"""

 FileMajorPart=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the major part of the version number.



Get: FileMajorPart(self: FileVersionInfo) -> int



"""

 FileMinorPart=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the minor part of the version number of the file.



Get: FileMinorPart(self: FileVersionInfo) -> int



"""

 FileName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the file that this instance of System.Diagnostics.FileVersionInfo describes.



Get: FileName(self: FileVersionInfo) -> str



"""

 FilePrivatePart=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the file private part number.



Get: FilePrivatePart(self: FileVersionInfo) -> int



"""

 FileVersion=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the file version number.



Get: FileVersion(self: FileVersionInfo) -> str



"""

 InternalName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the internal name of the file,if one exists.



Get: InternalName(self: FileVersionInfo) -> str



"""

 IsDebug=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that specifies whether the file contains debugging information or is compiled with debugging features enabled.



Get: IsDebug(self: FileVersionInfo) -> bool



"""

 IsPatched=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that specifies whether the file has been modified and is not identical to the original shipping file of the same version number.



Get: IsPatched(self: FileVersionInfo) -> bool



"""

 IsPreRelease=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that specifies whether the file is a development version,rather than a commercially released product.



Get: IsPreRelease(self: FileVersionInfo) -> bool



"""

 IsPrivateBuild=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that specifies whether the file was built using standard release procedures.



Get: IsPrivateBuild(self: FileVersionInfo) -> bool



"""

 IsSpecialBuild=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that specifies whether the file is a special build.



Get: IsSpecialBuild(self: FileVersionInfo) -> bool



"""

 Language=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the default language string for the version info block.



Get: Language(self: FileVersionInfo) -> str



"""

 LegalCopyright=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets all copyright notices that apply to the specified file.



Get: LegalCopyright(self: FileVersionInfo) -> str



"""

 LegalTrademarks=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the trademarks and registered trademarks that apply to the file.



Get: LegalTrademarks(self: FileVersionInfo) -> str



"""

 OriginalFilename=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name the file was created with.



Get: OriginalFilename(self: FileVersionInfo) -> str



"""

 PrivateBuild=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets information about a private version of the file.



Get: PrivateBuild(self: FileVersionInfo) -> str



"""

 ProductBuildPart=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the build number of the product this file is associated with.



Get: ProductBuildPart(self: FileVersionInfo) -> int



"""

 ProductMajorPart=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the major part of the version number for the product this file is associated with.



Get: ProductMajorPart(self: FileVersionInfo) -> int



"""

 ProductMinorPart=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the minor part of the version number for the product the file is associated with.



Get: ProductMinorPart(self: FileVersionInfo) -> int



"""

 ProductName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the product this file is distributed with.



Get: ProductName(self: FileVersionInfo) -> str



"""

 ProductPrivatePart=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the private part number of the product this file is associated with.



Get: ProductPrivatePart(self: FileVersionInfo) -> int



"""

 ProductVersion=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the version of the product this file is distributed with.



Get: ProductVersion(self: FileVersionInfo) -> str



"""

 SpecialBuild=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the special build information for the file.



Get: SpecialBuild(self: FileVersionInfo) -> str



"""


