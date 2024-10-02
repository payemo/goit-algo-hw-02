import queue
import itertools
import time

class Request:
    # Unique number generator
    _id = itertools.count(1)

    def __init__(self):
        self._id = next(Request._id)
        self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def __str__(self) -> str:
        return f"Request ID: {self._id}, Time: {self.timestamp}"
    
class ServiceCenter:
    def __init__(self) -> None:
        self.queue = queue.Queue()

    def generate_request(self):
        request = Request()
        self.queue.put(request)
        print(f"Generated: {request}")

    def process_request(self):
        if not self.queue.empty():
            req = self.queue.get()
            print(f"Processing: {req}")
            # Imitating request processing.
            time.sleep(2)
            print(f"Completed: {req}")
        else:
            print("Queue is empty. No requests to process.")

    def run(self):
        try:
            while True:
                self.generate_request()
                self.process_request()
                # Imitating interval between requests generation.
                time.sleep(0.5)
        except KeyboardInterrupt:
            print("\nService Center shutting down.")

def main():
    sc = ServiceCenter()
    sc.run()

if __name__ == '__main__':
    main()