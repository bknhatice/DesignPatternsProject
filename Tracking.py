class TrackingPublisher:
    def __init__(self):
        self.subscribers = []
        self.tracking_num = None

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify_subscribers(self, status):
        for subscriber in self.subscribers:
            subscriber.update(status)

    def set_tracking_num(self, tracking_num):
        self.tracking_num = tracking_num
        self.notify_subscribers(f"Your tracking number is: {self.tracking_num}")


class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, status):
        print(f"{self.name} received a notification: {status}")

'''
# Kullanım örneği
tracking_publisher = TrackingPublisher()

subscriber1 = Subscriber("John")
subscriber2 = Subscriber("Alice")
subscriber3 = Subscriber("Bob")

tracking_publisher.add_subscriber(subscriber1)
tracking_publisher.add_subscriber(subscriber2)
tracking_publisher.add_subscriber(subscriber3)

tracking_num = 123456789
tracking_publisher.set_tracking_num(tracking_num)

tracking_publisher.remove_subscriber(subscriber2)

new_tracking_num = 987654321
tracking_publisher.set_tracking_num(new_tracking_num)
'''