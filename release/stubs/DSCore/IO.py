# encoding: utf-8
# module DSCore.IO calls itself IO
# from DSCoreNodes, Version=1.2.1.3083, Culture=neutral, PublicKeyToken=null
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class CSV(object):
    """ Methods for working with CSV (comma-separated values) files. """
    @staticmethod
    def ReadFromFile(file):
        """
        ReadFromFile(file: FileInfo) -> Array[Array[object]]
        
            Reads a text file containing comma-separated values into a two dimensional list.
                    
             Outer list represents rows, inner lists represent columns.
        
        
            file: File object to read from.
            Returns: CSV contents of the given file.
        """
        pass

    @staticmethod
    def WriteToFile(filePath, data):
        """
        WriteToFile(filePath: str, data: Array[Array[object]])
            Write a list of lists into a file using a comma-separated values 
                        format. Outer 
             list represents rows, inner lists represent columns.
        
        
            filePath: Path to write to
            data: List of lists to write into CSV
            Returns: Contents of the text file.
        """
        pass

    __all__ = [
        'ReadFromFile',
        'WriteToFile',
    ]


class Directory(object):
    """ Methods for working with Directories. """
    @staticmethod
    def Contents(directory, searchString):
        """
        Contents(directory: DirectoryInfo, searchString: str) -> Dictionary[str, IList]
        
            Returns all of the contents of a given directory.
        
            directory: Directory to get contents of.
            searchString: Search string used to filter results. Defaults to "*.*" (displays all contents).
        """
        pass

    @staticmethod
    def Copy(directory, destinationPath, overwriteFiles):
        """
        Copy(directory: DirectoryInfo, destinationPath: str, overwriteFiles: bool)
            Copies a directory to a destination location.
        
            directory: Directory to copy.
            destinationPath: Destination of the copy operation on disk.
        """
        pass

    @staticmethod
    def Delete(path, recursive):
        """
        Delete(path: str, recursive: bool)
            Deletes a directory.
        
            path: Path to a directory on disk.
            recursive: Whether or not to delete all contents of the directory, defaults to false.
        """
        pass

    @staticmethod
    def Exists(path):
        """
        Exists(path: str) -> bool
        
            Determines if a directory exists at the given path.
        
            path: Path to a directory on disk.
        """
        pass

    @staticmethod
    def FromPath(path):
        """ FromPath(path: str) -> DirectoryInfo """
        pass

    @staticmethod
    def Move(path, newPath, overwriteFiles):
        """
        Move(path: str, newPath: str, overwriteFiles: bool)
            Moves a directory to a new location.
        """
        pass

    __all__ = [
        'Contents',
        'Copy',
        'Delete',
        'Exists',
        'FromPath',
        'Move',
    ]


class File(object):
    """ Methods for working with Files. """
    @staticmethod
    def AbsolutePath(path, hintPath):
        """ AbsolutePath(path: str, hintPath: str) -> str """
        pass

    @staticmethod
    def Copy(file, destinationPath, overwrite):
        """
        Copy(file: FileInfo, destinationPath: str, overwrite: bool)
            Copies a file.
        """
        pass

    @staticmethod
    def Delete(path):
        """
        Delete(path: str)
            Deletes the specified file.
        """
        pass

    @staticmethod
    def Exists(path):
        """
        Exists(path: str) -> bool
        
            Determines if a file exists at the given path.
        """
        pass

    @staticmethod
    def ExportToCSV(filePath, data):
        """ ExportToCSV(filePath: str, data: Array[Array[object]]) """
        pass

    @staticmethod
    def FromPath(path):
        """ FromPath(path: str) -> FileInfo """
        pass

    @staticmethod
    def LoadImageFromPath(path):
        """ LoadImageFromPath(path: str) -> Bitmap """
        pass

    @staticmethod
    def Move(path, newPath, overwrite):
        """
        Move(path: str, newPath: str, overwrite: bool)
            Moves a specified file to a new location
        """
        pass

    @staticmethod
    def ReadImage(path, xSamples, ySamples):
        """ ReadImage(path: str, xSamples: int, ySamples: int) -> Array[Color] """
        pass

    @staticmethod
    def ReadText(*__args):
        """
        ReadText(path: str) -> str
        ReadText(file: FileInfo) -> str
        
            Reads a text file and returns the contents as a string.
            Returns: Contents of the text file.
        """
        pass

    @staticmethod
    def WriteImage(filePath, fileName, image):
        """ WriteImage(filePath: str, fileName: str, image: Bitmap) -> bool """
        pass

    @staticmethod
    def WriteText(filePath, text):
        """
        WriteText(filePath: str, text: str)
            Write the text content to a file specified by the path
        
            filePath: Path to write to
            text: Text content
        """
        pass

    __all__ = [
        'AbsolutePath',
        'Copy',
        'Delete',
        'Exists',
        'ExportToCSV',
        'FromPath',
        'LoadImageFromPath',
        'Move',
        'ReadImage',
        'ReadText',
        'WriteImage',
        'WriteText',
    ]


class FilePath(object):
    """ Methods for operating on strings representing file paths. """
    @staticmethod
    def ChangeExtension(path, newExtension):
        """
        ChangeExtension(path: str, newExtension: str) -> str
        
            Changes the extension of a file path.
        
            path: Path to change extension of.
            newExtension: New extension.
        """
        pass

    @staticmethod
    def Combine(paths):
        """
        Combine(*paths: Array[str]) -> str
        
            Combines multiple strings into a single file path.
        
            paths: String to combine into a path.
        """
        pass

    @staticmethod
    def DirectoryName(path):
        """
        DirectoryName(path: str) -> str
        
            Returns the directory name of a file path.
        
            path: Path to get directory information of.
        """
        pass

    @staticmethod
    def Extension(path):
        """
        Extension(path: str) -> str
        
            Returns the extension from a file path.
        
            path: Path to get extension of.
        """
        pass

    @staticmethod
    def FileName(path, withExtension):
        """
        FileName(path: str, withExtension: bool) -> str
        
            Returns the file name of a file path.
        
            path: Path to get the file name of.
            withExtension: Determines whether or not the extension is included in the result, defaults to true.
        """
        pass

    @staticmethod
    def HasExtension(path):
        """
        HasExtension(path: str) -> bool
        
            Determines whether or not a file path contains an extension.
        
            path: Path to check for an extension.
        """
        pass

    __all__ = [
        'ChangeExtension',
        'Combine',
        'DirectoryName',
        'Extension',
        'FileName',
        'HasExtension',
    ]


class Image(object):
    """ Methods for operating on Image Bitmaps. """
    @staticmethod
    def Dimensions(image):
        """
        Dimensions(image: Bitmap) -> Dictionary[str, int]
        
            Returns the width and height of an image.
        
            image: Image to get dimensions of.
        """
        pass

    @staticmethod
    def FromPixels(colors, width=None, height=None):
        """
        FromPixels(colors: Array[Color], width: int, height: int) -> Bitmap
        
            Constructs an image from a flat list of pixels, a width, and a height.
        
            colors: List of colors representing the pixels.
            width: Width of the new image, in pixels.
            height: Height of the new image, in pixels.
            Returns: Image
        FromPixels(colors: Array[Array[Color]]) -> Bitmap
        
            Constructs an image from a 2d list of pixels.
        
            colors: 2d rectangular list of colors representing the pixels.
            Returns: Image
        """
        pass

    @staticmethod
    def Pixels(image, xSamples, ySamples):
        """ Pixels(image: Bitmap, xSamples: Nullable[int], ySamples: Nullable[int]) -> Array[Array[Color]] """
        pass

    @staticmethod
    def ReadFromFile(file):
        """
        ReadFromFile(file: FileInfo) -> Bitmap
        
            Loads the file as a bitmap.
        
            file: File object to load image from.
            Returns: Image
        """
        pass

    @staticmethod
    def WriteToFile(path, image):
        """
        WriteToFile(path: str, image: Bitmap)
            Write the image to a path, given the specified file name.
        
            image: The image to write
            Returns: It is successful or not.
        """
        pass

    __all__ = [
        'Dimensions',
        'FromPixels',
        'Pixels',
        'ReadFromFile',
        'WriteToFile',
    ]


