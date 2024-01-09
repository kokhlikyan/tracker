import threading
import time

from PySide6.QtCore import QTime


class Timer(threading.Thread):
    def __init__(self, app):
        super(Timer, self).__init__()

        self.app = app
        self.second = 0
        self.formatted_time = '00:00:00'
        self.stop_flag = threading.Event()
        self.elapsed_time = QTime(0, 0)

    def run(self):
        self.stop_flag.clear()
        thr = threading.Thread(target=self.run_timer, daemon=True)
        thr.start()

    def run_timer(self):
        while not self.stop_flag.is_set():
            self.second += 1
            hours, remainder = divmod(self.second, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.formatted_time = "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))
            time.sleep(1)
            self.update_time()

    def update_time(self):
        self.formatted_time = self.elapsed_time.toString("hh:mm:ss")
        self.app.timer_window.setText(self.formatted_time)
        self.elapsed_time = self.elapsed_time.addSecs(1)

    def stop(self):
        self.stop_flag.set()
