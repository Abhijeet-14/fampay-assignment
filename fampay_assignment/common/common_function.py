import logging

def custom_logger(name):
    return logging.getLogger(name)

def get_func_name(current_frame):
    return f"{current_frame.f_code.co_name}()"