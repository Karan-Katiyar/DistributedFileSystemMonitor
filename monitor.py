import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


def on_created(event):
    file1 = open("LogContainer1.txt","a")
    file1.write("\nCreated: " + event.src_path)
    file1.close()

def on_deleted(event):
    file1 = open("LogContainer1.txt","a")
    file1.write("\nDeleted: " + event.src_path)
    file1.close()

def on_modified(event):
    file1 = open("LogContainer1.txt","a")
    file1.write("\nModified: " + event.src_path)
    file1.close()

def on_moved(event):
    file1 = open("LogContainer1.txt","a")
    file1.write("\nMoved " + event.src_path +" to " + event.dest_path +"\n")
    file1.close()
    
if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    my_event_handler.on_created = on_created
    my_event_handler.on_deleted = on_deleted
    my_event_handler.on_modified = on_modified
    my_event_handler.on_moved = on_moved
    path = "/Users/karankatiyar/Documents/Fall19/CloudComputing/swiftmonitor"
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)

    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
