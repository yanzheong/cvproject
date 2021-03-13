from sys import platform

def isWindows():
    if platform == "win32":
        # print("Window")
        return 1
    elif platform == "darwin":
        # print("Mac")
        return 0
    return 0
    