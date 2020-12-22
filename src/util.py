def formatExceptionMessage(error: Exception):
    return error.__class__.__name__ + ": " + str(error)