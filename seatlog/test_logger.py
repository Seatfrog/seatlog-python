import unittest
from .logger import Logger
from datetime import date

class TestLogger(unittest.TestCase):

    # This is just for eyeballing the structure since hooking stdout is a bit tricky
    def test_all(self):
        log = Logger()
        log.debug("i'm debug", "1234", {"some": "data"})
        log.info("i'm info", "1234", {"some": "data"})
        log.warn("i'm warn", "1234", {"some": "data"})
        log.error("i'm error", "1234", {"some": "data"}, NameError("whatever"))

    def test_normal_extra_data(self):
        log = Logger()
        try:
            data = {"hi": "there"}
            log.info("i'm a test message with some normal extra data", data=data)
            self.assertTrue(True, "Passing normal data to the logger works fine")
        except:
            self.assertTrue(False, "Passing normal data to the logger broke it")

    def test_invalid_extra_data(self):
        log = Logger()
        try:
            d = date.today()
            log.info("i'm a test message with some normal extra data", data=d)
            self.assertTrue(True, "Passing a date is handled gracefully")
        except:
            self.assertTrue(False, "Passing a date to the extra data bit causes an exception")

    def test_exception(self):
        log = Logger()
        log.error("broken", "1234", {"hi": "there"}, "I'm not really an exception")
        log.error("broken", "1234", {"hi": "there"}, NameError("I AM an exception"))
        log.error("broken", "1234", {"hi": "there"}, None)
        self.assertTrue(True, "No problems with dodgy exception data")

if __name__ == '__main__':
    unittest.main()