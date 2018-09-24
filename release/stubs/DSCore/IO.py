# encoding: utf-8
# module DSCore.IO calls itself IO
# from DSCoreNodes, Version=2.0.1.5055, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class FileSystem(object):
    # no doc
    @staticmethod
    def AbsolutePath(path, hintPath):
        """ AbsolutePath(path: str, hintPath: str) -> str """
        pass

    @staticmethod
    def AppendText(filePath, text):
        """ AppendText(filePath: str, text: str) """
        pass

    @staticmethod
    def ChangePathExtension(path, newExtension):
        """ ChangePathExtension(path: str, newExtension: str) -> str """
        pass

    @staticmethod
    def CombinePath(paths):
        """ CombinePath(*paths: Array[str]) -> str """
        pass

    @staticmethod
    def CopyDirectory(directory, destinationPath, overwriteFiles):
        """ CopyDirectory(directory: DirectoryInfo, destinationPath: str, overwriteFiles: bool) """
        pass

    @staticmethod
    def CopyFile(file, destinationPath, overwrite):
        """ CopyFile(file: FileInfo, destinationPath: str, overwrite: bool) """
        pass

    @staticmethod
    def DeleteDirectory(path, recursive):
        """ DeleteDirectory(path: str, recursive: bool) """
        pass

    @staticmethod
    def DeleteFile(path):
        """ DeleteFile(path: str) """
        pass

    @staticmethod
    def DirectoryExists(path):
        """ DirectoryExists(path: str) -> bool """
        pass

    @staticmethod
    def DirectoryFromPath(path):
        """ DirectoryFromPath(path: str) -> DirectoryInfo """
        pass

    @staticmethod
    def DirectoryName(path):
        """ DirectoryName(path: str) -> str """
        pass

    @staticmethod
    def ExportToCSV(filePath, data):
        """ ExportToCSV(filePath: str, data: Array[Array[object]]) -> bool """
        pass

    @staticmethod
    def FileExists(path):
        """ FileExists(path: str) -> bool """
        pass

    @staticmethod
    def FileExtension(path):
        """ FileExtension(path: str) -> str """
        pass

    @staticmethod
    def FileFromPath(path):
        """ FileFromPath(path: str) -> FileInfo """
        pass

    @staticmethod
    def FileHasExtension(path):
        """ FileHasExtension(path: str) -> bool """
        pass

    @staticmethod
    def FileName(path, withExtension):
        """ FileName(path: str, withExtension: bool) -> str """
        pass

    @staticmethod
    def GetDirectoryContents(directory, searchString, includeSubdirectories):
        """ GetDirectoryContents(directory: DirectoryInfo, searchString: str, includeSubdirectories: bool) -> Dictionary[str, IList] """
        pass

    @staticmethod
    def LoadImageFromPath(path):
        """ LoadImageFromPath(path: str) -> Bitmap """
        pass

    @staticmethod
    def MoveDirectory(path, newPath, overwriteFiles):
        """ MoveDirectory(path: str, newPath: str, overwriteFiles: bool) """
        pass

    @staticmethod
    def MoveFile(path, newPath, overwrite):
        """ MoveFile(path: str, newPath: str, overwrite: bool) """
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
        """
        pass

    @staticmethod
    def WriteImage(filePath, fileName, image):
        """ WriteImage(filePath: str, fileName: str, image: Bitmap) -> bool """
        pass

    @staticmethod
    def WriteText(filePath, text):
        """ WriteText(filePath: str, text: str) """
        pass

    __all__ = [
        'AbsolutePath',
        'AppendText',
        'ChangePathExtension',
        'CombinePath',
        'CopyDirectory',
        'CopyFile',
        'DeleteDirectory',
        'DeleteFile',
        'DirectoryExists',
        'DirectoryFromPath',
        'DirectoryName',
        'ExportToCSV',
        'FileExists',
        'FileExtension',
        'FileFromPath',
        'FileHasExtension',
        'FileName',
        'GetDirectoryContents',
        'LoadImageFromPath',
        'MoveDirectory',
        'MoveFile',
        'ReadImage',
        'ReadText',
        'WriteImage',
        'WriteText',
    ]


class Image(object):
    # no doc
    @staticmethod
    def Dimensions(image):
        """ Dimensions(image: Bitmap) -> Dictionary[str, int] """
        pass

    @staticmethod
    def FromPixels(colors, width=None, height=None):
        """
        FromPixels(colors: Array[Color], width: int, height: int) -> Bitmap
        FromPixels(colors: Array[Array[Color]]) -> Bitmap
        """
        pass

    @staticmethod
    def Pixels(image, xSamples, ySamples):
        """ Pixels(image: Bitmap, xSamples: Nullable[int], ySamples: Nullable[int]) -> Array[Array[Color]] """
        pass

    @staticmethod
    def ReadFromFile(file):
        """ ReadFromFile(file: FileInfo) -> Bitmap """
        pass

    @staticmethod
    def WriteToFile(path, image):
        """ WriteToFile(path: str, image: Bitmap) """
        pass

    __all__ = [
        'Dimensions',
        'FromPixels',
        'Pixels',
        'ReadFromFile',
        'WriteToFile',
    ]


