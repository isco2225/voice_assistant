import socket

def has_internet_connection(host="8.8.8.8", port=53, timeout=2):
    """
    İnternet bağlantısı olup olmadığını kontrol eder.
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        print('internet Var.')
        return True
    except OSError:
        print('internet Yok.')
        return False
    
