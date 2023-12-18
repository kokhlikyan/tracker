import json
import logging
from PySide6 import QtSql
from core.config import APP_LOCAL_FOLDER


class Storage:
    def __init__(self):
        self.query = None
        self.db = QtSql.QSqlDatabase.database()
        

    def connect(self):
        if not self.db.isValid():
            self.db = self.db.addDatabase('QSQLITE')
            if not self.db.isValid():
                logging.error("Cannot add database")

        filename = f'{APP_LOCAL_FOLDER}/storage.db'
        self.db.setDatabaseName(filename)
        if not self.db.open():
            logging.error("Cannot open database")
        logging.info("Database is opened")
        self.query = QtSql.QSqlQuery()
        self.create_mouse_events_table()

    def create_timer_table(self):
        self.query.exec(
            """ CREATE TABLE IF NOT EXISTS `timer` (
                `id` INTEGER PRIMARY KEY AUTOINCREMENT, 
                `timstemp` UNSIGNED BIG INT NOT NULL, 
                `start` VARCHAR(20) NOT NULL, 
                `end` VARCHAR(20) NOT NULL)
            """)

    def create_mouse_events_table(self):
        self.query.exec(
            """ CREATE TABLE IF NOT EXISTS `mouse_events` (
                        `id` INTEGER PRIMARY KEY AUTOINCREMENT, 
                        `data` JSON NOT NULL)
                    """
        )

    def add_mouse_event(self, data):
        self.query.prepare("INSERT INTO `mouse_events` (`data`) VALUES (?)")
        self.query.addBindValue(json.dumps(data))
        self.query.exec()
