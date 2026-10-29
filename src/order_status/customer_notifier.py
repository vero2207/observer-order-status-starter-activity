from .observer import Observer


class CustomerNotifier(Observer):
    def __init__(self):
        self.messages = []

    def update(self, order_id, status):
        self.messages.append(f"{order_id}:{status}")