import asyncio
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
    def __init__(self):
        self.queue = asyncio.Queue()

    async def generate_requests(self):
        while True:
            req = Request()
            await self.queue.put(req)
            print(f"Generated: {req}")
            # Interval between requests generation
            await asyncio.sleep(0.5)

    async def process_requests(self):
        while True:
            req = await self.queue.get()
            print(f"Processing: {req}")
            # Imitation of a request's processing
            await asyncio.sleep(2)
            print(f"Completed: {req}")
            self.queue.task_done()

    async def run(self):
        producer = asyncio.create_task(self.generate_requests())
        consumer = asyncio.create_task(self.process_requests())

        try:
            await asyncio.gather(producer, consumer)
        except asyncio.CancelledError:
            pass

    def shutdown(self):
        for task in asyncio.all_tasks():
            task.cancel()

def main():
    sc = ServiceCenter()
    try:
        asyncio.run(sc.run())
    except KeyboardInterrupt:
        print("\nShutting down Service Center ...")
        sc.shutdown()
        print("\nService Center has been shut down.")

if __name__ == '__main__':
    main()