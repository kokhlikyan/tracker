import json
import logging
from PySide6 import QtSql
from core.config import APP_LOCAL_FOLDER


class Database:
    def __init__(self):
        self.db = QtSql.QSqlDatabase.database()


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
        self.create_session_table()
        self.create_timer_table()
        self.create_mouse_events_table()
        self.create_keyboard_events_table()
    def get_query(self):
        return self.query
    def create_session_table(self):
        try:
            self.query.exec(
                """ CREATE TABLE IF NOT EXISTS `sessions` (
                    `id` INTEGER PRIMARY KEY AUTOINCREMENT, 
                    `datetime` DATETIME NOT NULL,
                    `last_screenshot_path` VARCHAR DEFAULT NULL,
                    `is_closed` INTEGER DEFAULT 0 
                    )
                """)
        except Exception as e:
            logging.error(str(e))

    def create_timer_table(self):
        try:
            self.query.exec(
                """ CREATE TABLE IF NOT EXISTS `tracks` (
                    `id` INTEGER PRIMARY KEY AUTOINCREMENT, 
                    `time` UNSIGNED BIG INT NOT NULL, 
                    `session_id` INTEGER NOT NULL,
                    FOREIGN KEY (`session_id`) REFERENCES `sessions`(`id`))
                """)
        except Exception as e:
            logging.error(str(e))

    def create_mouse_events_table(self):
        try:

            self.query.exec(
                """ CREATE TABLE IF NOT EXISTS `mouse_events` (
                            `id` INTEGER PRIMARY KEY AUTOINCREMENT, 
                            `left`  INTEGER DEFAULT 0,
                            `right`  INTEGER DEFAULT 0,
                            `session_id` INTEGER NOT NULL,
                            FOREIGN KEY (`session_id`) REFERENCES `sessions`(`id`))
                        """
            )
        except Exception as e:
            logging.error(str(e))

    def create_keyboard_events_table(self):
        try:
            self.query.exec(
                """ CREATE TABLE IF NOT EXISTS `keyboard_events` (
                            `id` INTEGER PRIMARY KEY AUTOINCREMENT, 
                            `click` INT NOT NULL,
                            `session_id` INTEGER NOT NULL,
                            FOREIGN KEY (`session_id`) REFERENCES `sessions`(`id`))
                        """
            )
        except Exception as e:
            logging.error(str(e))

    def add_mouse_event(self, data):
        pass
        # self.query.prepare("INSERT INTO `mouse_events` (`data`) VALUES (?)")
        # self.query.addBindValue(json.dumps(data))
        # self.query.exec()
