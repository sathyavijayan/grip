import socket
import webbrowser
import time


def is_server_running(host, port):
    """
    Checks whether a server is currently listening on the specified
    host and port.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    rc = sock.connect_ex((host, port))
    return rc == 0


def wait_for_server(host, port):
    """
    Blocks until a local server is listening on the specified
    host and port.

    This is intended to be used in conjunction with running
    the Flask server.
    """
    while not is_server_running(host, port):
        time.sleep(0.1)


def start_browser(url):
    """
    Opens the specified URL in a new browser window.
    """
    try:
        webbrowser.open(url)
    except Exception:
        pass


def wait_and_start_browser(host, port):
    wait_for_server(host, port)
    start_browser('http://{0}:{1}/'.format(
        'localhost' if host == '0.0.0.0' else host, port))
