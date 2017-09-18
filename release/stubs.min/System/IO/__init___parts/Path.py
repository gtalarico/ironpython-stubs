class Path(object):
 """ Performs operations on System.String instances that contain file or directory path information. These operations are performed in a cross-platform manner. """
 @staticmethod
 def ChangeExtension(path,extension):
  """
  ChangeExtension(path: str,extension: str) -> str

  

   Changes the extension of a path string.

  

   path: The path information to modify. The path cannot contain any of the characters defined in 

    System.IO.Path.GetInvalidPathChars.

  

   extension: The new extension (with or without a leading period). Specify null to remove an existing 

    extension from path.

  

   Returns: The modified path information.On Windows-based desktop platforms,if path is null or an empty 

    string (""),the path information is returned unmodified. If extension is null,the returned 

    string contains the specified path with its extension removed. If path has no extension,and 

    extension is not null,the returned path string contains extension appended to the end of path.
  """
  pass
 @staticmethod
 def Combine(*__args):
  """
  Combine(path1: str,path2: str,path3: str,path4: str) -> str

  

   Combines four strings into a path.

  

   path1: The first path to combine.

   path2: The second path to combine.

   path3: The third path to combine.

   path4: The fourth path to combine.

   Returns: The combined paths.

  Combine(*paths: Array[str]) -> str

  

   Combines an array of strings into a path.

  

   paths: An array of parts of the path.

   Returns: The combined paths.

  Combine(path1: str,path2: str) -> str

  

   Combines two strings into a path.

  

   path1: The first path to combine.

   path2: The second path to combine.

   Returns: The combined paths. If one of the specified paths is a zero-length string,this method returns 

    the other path. If path2 contains an absolute path,this method returns path2.

  

  Combine(path1: str,path2: str,path3: str) -> str

  

   Combines three strings into a path.

  

   path1: The first path to combine.

   path2: The second path to combine.

   path3: The third path to combine.

   Returns: The combined paths.
  """
  pass
 @staticmethod
 def GetDirectoryName(path):
  """
  GetDirectoryName(path: str) -> str

  

   Returns the directory information for the specified path string.

  

   path: The path of a file or directory.

   Returns: Directory information for path,or null if path denotes a root directory or is null. Returns 

    System.String.Empty if path does not contain directory information.
  """
  pass
 @staticmethod
 def GetExtension(path):
  """
  GetExtension(path: str) -> str

  

   Returns the extension of the specified path string.

  

   path: The path string from which to get the extension.

   Returns: The extension of the specified path (including the period "."),or null,or System.String.Empty. 

    If path is null,System.IO.Path.GetExtension(System.String) returns null. If path does not have 

    extension information,System.IO.Path.GetExtension(System.String) returns System.String.Empty.
  """
  pass
 @staticmethod
 def GetFileName(path):
  """
  GetFileName(path: str) -> str

  

   Returns the file name and extension of the specified path string.

  

   path: The path string from which to obtain the file name and extension.

   Returns: The characters after the last directory character in path. If the last character of path is a 

    directory or volume separator character,this method returns System.String.Empty. If path is 

    null,this method returns null.
  """
  pass
 @staticmethod
 def GetFileNameWithoutExtension(path):
  """
  GetFileNameWithoutExtension(path: str) -> str

  

   Returns the file name of the specified path string without the extension.

  

   path: The path of the file.

   Returns: The string returned by System.IO.Path.GetFileName(System.String),minus the last period (.) and 

    all characters following it.
  """
  pass
 @staticmethod
 def GetFullPath(path):
  """
  GetFullPath(path: str) -> str

  

   Returns the absolute path for the specified path string.

  

   path: The file or directory for which to obtain absolute path information.

   Returns: The fully qualified location of path,such as "C:\MyFile.txt".
  """
  pass
 @staticmethod
 def GetInvalidFileNameChars():
  """
  GetInvalidFileNameChars() -> Array[Char]

  

   Gets an array containing the characters that are not allowed in file names.

   Returns: An array containing the characters that are not allowed in file names.
  """
  pass
 @staticmethod
 def GetInvalidPathChars():
  """
  GetInvalidPathChars() -> Array[Char]

  

   Gets an array containing the characters that are not allowed in path names.

   Returns: An array containing the characters that are not allowed in path names.
  """
  pass
 @staticmethod
 def GetPathRoot(path):
  """
  GetPathRoot(path: str) -> str

  

   Gets the root directory information of the specified path.

  

   path: The path from which to obtain root directory information.

   Returns: The root directory of path,such as "C:\",or null if path is null,or an empty string if path 

    does not contain root directory information.
  """
  pass
 @staticmethod
 def GetRandomFileName():
  """
  GetRandomFileName() -> str

  

   Returns a random folder name or file name.

   Returns: A random folder name or file name.
  """
  pass
 @staticmethod
 def GetTempFileName():
  """
  GetTempFileName() -> str

  

   Creates a uniquely named,zero-byte temporary file on disk and returns the full path of that 

    file.

  

   Returns: The full path of the temporary file.
  """
  pass
 @staticmethod
 def GetTempPath():
  """
  GetTempPath() -> str

  

   Returns the path of the current user's temporary folder.

   Returns: The path to the temporary folder,ending with a backslash.
  """
  pass
 @staticmethod
 def HasExtension(path):
  """
  HasExtension(path: str) -> bool

  

   Determines whether a path includes a file name extension.

  

   path: The path to search for an extension.

   Returns: true if the characters that follow the last directory separator (\\ or /) or volume separator 

    (:) in the path include a period (.) followed by one or more characters; otherwise,false.
  """
  pass
 @staticmethod
 def IsPathRooted(path):
  """
  IsPathRooted(path: str) -> bool

  

   Gets a value indicating whether the specified path string contains a root.

  

   path: The path to test.

   Returns: true if path contains a root; otherwise,false.
  """
  pass
 AltDirectorySeparatorChar=None
 DirectorySeparatorChar=None
 InvalidPathChars=None
 PathSeparator=None
 VolumeSeparatorChar=None
 __all__=[
  'AltDirectorySeparatorChar',
  'ChangeExtension',
  'Combine',
  'DirectorySeparatorChar',
  'GetDirectoryName',
  'GetExtension',
  'GetFileName',
  'GetFileNameWithoutExtension',
  'GetFullPath',
  'GetInvalidFileNameChars',
  'GetInvalidPathChars',
  'GetPathRoot',
  'GetRandomFileName',
  'GetTempFileName',
  'GetTempPath',
  'HasExtension',
  'InvalidPathChars',
  'IsPathRooted',
  'PathSeparator',
  'VolumeSeparatorChar',
 ]

