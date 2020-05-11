import os
import json
import logging
from pythonjsonlogger import jsonlogger
from datetime import datetime


class JsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(JsonFormatter, self).add_fields(log_record, record, message_dict)

        if not log_record.get('timestamp'):
            # this doesn't use record.created, so it is slightly off
            now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]
            log_record['time'] = "{}Z".format(now)

        if log_record.get('level'):
            log_record['level'] = log_record['level'].lower()
        else:
            log_record['level'] = record.levelname.lower()

        error = {}
        if log_record.get("exc_info"):
            error.update({"exception": log_record.get("exc_info")})
            log_record.pop("exc_info", None)
        elif log_record.get("exception"):
            error.update({"exception": log_record.get("exception")})
            log_record.pop("exception", None)

        if error:
            log_record["error"] = error

        extra = {}
        for key, value in log_record.copy().items():
            if key not in ["message", "level", "time", "correlation_id", "extra", "error"]:
                extra.update({ key: value })
                log_record.pop(key, None)

        if extra:
            log_record["extra"] = extra


class Logger:
    logger = None

    def __init__(self):
        self.logger = logging.getLogger("seatfrog-push-notification-service")
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = JsonFormatter()
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def info(self, message, correlation_id=None, data=None):
        extra = {
            "correlation_id": correlation_id,
        }

        if data:
            extra = {**extra, **data}

        self.logger.info(message, extra=extra)

    def error(self, message, correlation_id=None, data=None, exception=None):
        extra = {
            "correlation_id": correlation_id,
            "level": "error",
        }

        if data:
            extra = {**extra, **data}

        self.logger.critical(message,
                             exc_info=exception,
                             extra=extra)

    def warn(self, message, correlation_id=None, data=None):
        extra = {
            "correlation_id": correlation_id,
            "level": "warn",
        }

        if data:
            extra = {**extra, **data}

        self.logger.warning(message, extra=extra)