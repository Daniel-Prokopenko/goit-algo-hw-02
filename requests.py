from queue import Queue


q = Queue()


def generate_request(queue: Queue, num: str) -> str:
    new_request = "Request №" + num
    queue.put(new_request)
    return "Request №" + num + " has been added."


def process_request(queue: Queue) -> str:
    if not queue.empty():
        return queue.get() + " has been processed."
    return "Queue is empty."


n = 1
print("Hello!")
while True:
    command = input("Enter a command ===>  ")
    if command == "generate":
        print(generate_request(q, str(n)))
        n += 1
    elif command == "process":
        print(process_request(q))
    elif command == "exit":
        print("Goodbye!")
        break
    else:
        print("Wrong command. Try generate/process/exit.")
