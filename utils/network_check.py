import socket
from utils.printer import Colors, customPrint

def has_internet_connection(host="8.8.8.8", port=53, timeout=2):
    """
    İnternet bağlantısı olup olmadığını kontrol eder.
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        #successPrint("İnternet var")
        return True
    except OSError:
        customPrint("İnternet bağlantısı yok",color=Colors.RED)
        return False
    
