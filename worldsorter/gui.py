from PyQt5 import QtWidgets, uic
import sys, os
import sqlite3

TABLES = ('places', 'locations', 'people', 'people_connections')
TABLE_STRUCTURE = {TABLES[0] : ('id INTEGER', 'name TEXT', 'description TEXT'),
                   TABLES[1] : ('id INTEGER', 'name TEXT', 'description TEXT'),
                   TABLES[2] : ('id INTEGER', 'name TEXT', 'description TEXT'),
                   TABLES[3] : ('person INTEGER', 'connection INTEGER')}

def ensure_file_type(filePath: str, fileType: str) -> str:
    """Ensure that the given filePath ends with the desiredType."""
    if not isinstance(filePath, str):
        raise TypeError('filePath must be a string.')
    if not isinstance(fileType, str):
        raise TypeError('fileType must be a string.')

    filePathParts = filePath.split('/')
    fileNameParts = filePathParts[-1].split('.')
    if len(fileNameParts) == 1:
        return filePath + f'.{fileType}'
    
    if fileNameParts[-1] != fileType:
        filePath = '/'.join(filePathParts[:-1]) + fileNameParts[0] + f".{fileType}"
    return filePath

def create_table(cursor, name: str, headers: tuple):
    cursor.execute(f"CREATE TABLE {name} ({', '.join(headers)})")

class Main(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)

        self.testingMode = False

        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "main.ui"), self)
        # self.places 
        #
        self.newDatabase.triggered.connect(self.new_database)
        
    def new_database(self):
        """Creates a new database file in the selected location."""
        if not self.testingMode:
            # Select a location for the new database and the filename
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            filePath, _ = QtWidgets.QFileDialog.getSaveFileName(self,
                                                                "Create new database",
                                                                "",
                                                                "All Files (*);;Database Files (*.db)", 
                                                                options=options)
            if filePath == "":
                return
        else: 
            pass
        
        # The fileName is where the user decided to save the new database 
        # Check to ensure it ends with a .db 
        filePath = ensure_file_type(filePath, 'db')
        
        # Create the new db 
        connection = sqlite3.connect(filePath)
        
        # Add all tables 
        cursor = connection.cursor()
        for table in TABLE_STRUCTURE.keys():
            create_table(cursor, table, TABLE_STRUCTURE[table])        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
