from .observer import Observer


class AuditObserver(Observer):
    def __init__(self):
        self.entries = []

    def update(self, order_id, status):
        self.entries.append((order_id, status))