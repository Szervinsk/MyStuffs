import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import sys
import os

class ChangeHandler(FileSystemEventHandler):
    def __init__(self, server_process):
        self.server_process = server_process

    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            print(f"Mudança detectada em {event.src_path}. Reiniciando o servidor...")
            self.server_process.terminate()
            self.server_process = start_server()

def start_server():
    return subprocess.Popen([sys.executable, 'route.py'])

if __name__ == "__main__":
    server_process = start_server()
    
    event_handler = ChangeHandler(server_process)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()

    print("Watchdog está monitorando alterações. Pressione Ctrl+C para sair.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Encerrando o Watchdog e o servidor...")
        observer.stop()
        server_process.terminate()
    observer.join()
