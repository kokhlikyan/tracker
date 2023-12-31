import logging
from datetime import datetime, timedelta, time
from PySide6.QtSql import QSqlQuery


def add_new_session(query: QSqlQuery, project):
    local_datetime = datetime.now()
    date = local_datetime.strftime("%Y-%m-%d %H:%M:%S")
    query.prepare("INSERT INTO `sessions` (`datetime`, `project`) VALUES (?, ?)")
    query.addBindValue(date)
    query.addBindValue(project)
    query.exec()


def update_session(query: QSqlQuery, id):
    query.prepare("UPDATE `sessions` SET `is_closed` = 1 WHERE `id` = ?")
    query.addBindValue(id)
    query.exec()


def get_current_session(query: QSqlQuery, project):
    select_query = f"SELECT * FROM `sessions` WHERE `is_closed` = 0 AND `project` LIKE '%{project}%'"
    query.prepare(select_query)
    data = {}
    if query.exec(select_query) and query.next():
        column_count = query.record().count()
        for i in range(column_count):
            field_name = query.record().fieldName(i)
            field_value = query.value(i)
            data[field_name] = field_value
    return data


def session_start(query: QSqlQuery, project):
    data = get_current_session(query, project)
    if not data:
        add_new_session(query, project)
    else:
        given_datetime_str = data['datetime']
        given_datetime = datetime.strptime(given_datetime_str, "%Y-%m-%d %H:%M:%S")
        current_date = datetime.now().date()
        fixed_time = time(8, 0, 0)
        fixed_datetime = datetime.combine(current_date, fixed_time)
        time_difference = given_datetime - fixed_datetime
        if time_difference > timedelta(hours=24):
            add_new_session(query, project)
            update_session(query, data['id'])


def add_click_event(query: QSqlQuery, session_id: int):
    select_query = "SELECT * FROM `keyboard_events` WHERE `session_id` = :session_id"
    query.prepare(select_query)
    query.bindValue(':session_id', session_id)

    if query.exec() and query.next():
        select_query = "UPDATE `keyboard_events` SET `click` = `click` + 1 WHERE  `session_id` = :session_id"
        query.prepare(select_query)
        query.bindValue(':session_id', session_id)
        query.exec()
    else:
        query.prepare("INSERT INTO `keyboard_events` (`clicl`) VALUES (?)")
        query.addBindValue(1)
        query.exec()


def add_or_update_mouse_event(query: QSqlQuery, session_id: int, left: int, right: int):
    try:
        select_query = "SELECT * FROM `mouse_events` WHERE `session_id` = :session_id"
        query.prepare(select_query)
        query.bindValue(':session_id', session_id)
        if query.exec() and query.next():
            select_query = ("UPDATE `mouse_events` SET `left` = `left` + :left, `right` = `right` + :right WHERE  "
                            "`session_id` = :session_id")
            query.prepare(select_query)
            query.bindValue(':session_id', session_id)
            query.bindValue(':left', left)
            query.bindValue(':right', right)
            query.exec()
        else:
            query.prepare("INSERT INTO `mouse_events` (`session_id`,`left`, `right`) VALUES (?,?,?)")
            query.addBindValue(session_id)
            query.addBindValue(left)
            query.addBindValue(right)
            query.exec()
    except Exception as e:
        logging.error(str(e))


def save_tracked_time(query: QSqlQuery, session_id: int, time):
    try:
        select_query = "SELECT * FROM `tracks` WHERE `session_id` = :session_id"
        query.prepare(select_query)
        query.bindValue(':session_id', session_id)
        if query.exec() and query.next():
            select_query = ("UPDATE `tracks` SET `time` =  :time WHERE  "
                            "`session_id` = :session_id")
            query.prepare(select_query)
            query.bindValue(':session_id', session_id)
            query.bindValue(':time', time)
            query.exec()
        else:
            query.prepare("INSERT INTO `tracks` (`session_id`,`time`) VALUES (?,?)")
            query.addBindValue(session_id)
            query.addBindValue(time)
            query.exec()
    except Exception as e:
        logging.error(str(e))


def set_last_screenshot_path(query: QSqlQuery, session_id, path):
    query.prepare("UPDATE `sessions` SET `last_screenshot_path` = :path WHERE `id` = :session_id")
    query.bindValue(':session_id', session_id)
    query.bindValue(':path', path)
    query.exec()
