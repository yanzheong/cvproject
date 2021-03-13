from sys import platform

def isWindows():
    if platform == "win32":
        # print("Window")
        return True
    elif platform == "darwin":
        # print("Mac")
        return False
    return 0
    