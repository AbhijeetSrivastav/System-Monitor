"Exception for monitor package"


import os 
import sys


def error_message_detail(error, error_detail: sys):
    """
    Extract error causing script, error causing line, error 
    -------------------------------------------------------
    input:
    - `error`: from the MonitorException class
    - `error_detail`: from the MonitorException class      
    ------------------------------------------------------
    return: error_message
    """

    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Python script: [{0}] Line number: [{1}] Error message: [{3}]".format(file_name, exc_tb.tb_lineno, str(error))

    return error_message


class MonitorException(Exception):
    """
    Raise MonitorException 
    --------------------------------------------------------------
    `error`: from error_message_detail function
    `error_detail`: from error_message_detail function
    ---------------------------------------------------------------
    return: monitor exception error message
    """
    def __init__(self, error_message, error_detail: sys):
        self.error_message = error_message_detail(error=error_message, error_detail=error_detail)

    def __str__(self) -> str:
        return self.error_message