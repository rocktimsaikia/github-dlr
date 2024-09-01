import sys
import threading
import time


def loading_animation(msg):
    """Displays a loading animation with the given message."""
    sys.stdout.write(f"{msg}")
    sys.stdout.flush()
    while getattr(threading.currentThread(), "do_run", True):
        for char in "|/-\\":
            sys.stdout.write(f"\r{msg} {char}")
            sys.stdout.flush()
            time.sleep(0.1)


def start_loading_animation(msg):
    """Starts the loading animation in a separate thread."""
    loading_thread = threading.Thread(target=loading_animation, args=(msg,))
    loading_thread.start()
    return loading_thread


def stop_loading_animation(loading_thread):
    """Stops the loading animation."""
    loading_thread.do_run = False
    loading_thread.join()
