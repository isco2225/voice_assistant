import socket
from utils.printer import successPrint, warningPrint

def has_internet_connection(host="8.8.8.8", port=53, timeout=2):
    """
    İnternet bağlantısı olup olmadığını kontrol eder.
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        successPrint("İnternet bağlantısı mevcut")
        return True
    except OSError:
        warningPrint("İnternet bağlantısı yok")
        return False
    
