from enum import Enum

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status code is not equal to expected"
    WROND_ELEMENT_COUNT = "Number of items is not equal to expected"