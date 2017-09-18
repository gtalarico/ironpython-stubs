# encoding: utf-8
# module DSOffice
# from DSOffice, Version=1.2.1.3083, Culture=neutral, PublicKeyToken=null
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class Excel(object):
    # no doc
    @staticmethod
    def AddExcelWorksheetToWorkbook(workbook, name):
        """ AddExcelWorksheetToWorkbook(workbook: WorkBook, name: str) -> WorkSheet """
        pass

    @staticmethod
    def GetDataFromExcelWorksheet(worksheet):
        """ GetDataFromExcelWorksheet(worksheet: WorkSheet) -> Array[Array[object]] """
        pass

    @staticmethod
    def GetExcelWorksheetByName(workbook, name):
        """ GetExcelWorksheetByName(workbook: WorkBook, name: str) -> WorkSheet """
        pass

    @staticmethod
    def GetWorksheetsFromExcelWorkbook(workbook):
        """ GetWorksheetsFromExcelWorkbook(workbook: WorkBook) -> Array[WorkSheet] """
        pass

    @staticmethod
    def NewExcelWorkbook():
        """ NewExcelWorkbook() -> WorkBook """
        pass

    @staticmethod
    def Read(filePath, sheetName):
        """ Read(filePath: str, sheetName: str) -> Array[Array[object]] """
        pass

    @staticmethod
    def ReadExcelFile(file):
        """
        ReadExcelFile(file: str) -> WorkBook
        ReadExcelFile(file: FileInfo) -> WorkBook
        """
        pass

    @staticmethod
    def ReadFromFile(file, sheetName, readAsStrings):
        """
        ReadFromFile(file: FileInfo, sheetName: str, readAsStrings: bool) -> Array[Array[object]]
        
            Read data from a Microsoft Excel spreadsheet. Data is read by row and
                        returned 
             in a series of lists by row. Rows and columns are zero-indexed;
                        for example, 
             the value in cell A1 will appear in the data list at [0,0].
                        This node requires 
             Microsoft Excel to be installed.
        
        
            file: File representing the Microsoft Excel spreadsheet.
            sheetName: Name of the worksheet containing the data.
            readAsStrings: toggle to switch between reading Excel file as strings only or not
            Returns: Rows of data from the Excel worksheet.
        """
        pass

    @staticmethod
    def SaveAsExcelWorkbook(workbook, filename):
        """ SaveAsExcelWorkbook(workbook: WorkBook, filename: str) -> WorkBook """
        pass

    @staticmethod
    def WriteDataToExcelWorksheet(worksheet, startRow, startColumn, data):
        """ WriteDataToExcelWorksheet(worksheet: WorkSheet, startRow: int, startColumn: int, data: Array[Array[object]]) -> WorkSheet """
        pass

    @staticmethod
    def WriteToFile(filePath, sheetName, startRow, startCol, data, overWrite):
        """
        WriteToFile(filePath: str, sheetName: str, startRow: int, startCol: int, data: Array[Array[object]], overWrite: bool) -> Array[Array[object]]
        
            Write data to a Microsoft Excel spreadsheet. Data is written by row
                        with 
             sublists to be written in successive rows. Rows and columns are
                        zero-indexed; 
             for example, the value in the data list at [0,0] will
                        be written to cell A1. 
             Null values and empty lists are written to Excel 
                        as empty cells. This node 
             requires Microsoft Excel to be installed.
        
        
            filePath: File path to the Microsoft Excel spreadsheet.
            sheetName: Name of the workseet to write data to.
            startRow: Start row for writing data. Enter 0 for A, 1 for B, etc.
            startCol: Start column for writing data. Enter 0 for col 1, 1 for column 2, ect.
            data: Data to write to the spreadsheet.
            Returns: Data written to the spreadsheet.
        """
        pass

    __all__ = [
        'AddExcelWorksheetToWorkbook',
        'GetDataFromExcelWorksheet',
        'GetExcelWorksheetByName',
        'GetWorksheetsFromExcelWorkbook',
        'NewExcelWorkbook',
        'Read',
        'ReadExcelFile',
        'ReadFromFile',
        'SaveAsExcelWorkbook',
        'WriteDataToExcelWorksheet',
        'WriteToFile',
    ]


class WorkBook(object):
    # no doc

class WorkSheet(object):
    # no doc

