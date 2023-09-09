# 日志配置
import re
import os
import logging
from logging.handlers import TimedRotatingFileHandler


class FileLogger:
    def __init__(self):
        self.app = None

    def init_app(self, app):
        self.app = app
        log_file = app.config['LOG_FILE'] or os.path.join(
            app.root_path, 'logs/app.log')
        if not os.path.exists(os.path.dirname(log_file)):
            os.makedirs(os.path.dirname(log_file))
        formatter = logging.Formatter(app.config['LOG_FORMAT'])
        file_handler = TimedRotatingFileHandler(
            log_file, when="D", interval=1, backupCount=10)
        file_handler.setFormatter(formatter)
        app.logger.setLevel(app.config['LOG_LEVEL'])
        app.logger.addHandler(file_handler)


file_logger = FileLogger()
