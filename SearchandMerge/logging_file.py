import logging as lg

class Logger:
    def __init__(self):
        lg.basicConfig(filename="task_class_object.log", level=lg.INFO, format="%(asctime)s:%(levelname)s:%(message)s")

    def log(self, typeof, message):
        if typeof == "info":
            lg.info(message)
        elif typeof == "error":
            lg.error(message)