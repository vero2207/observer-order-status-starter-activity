from .observer import Observer


class OrderStatus:
    def __init__(self, order_id):
        self.order_id = order_id
        self.status = "NEW"
        self.observers = []

    def subscribe(self, observer: Observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def unsubscribe(self, observer: Observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def set_status(self, status):
        self.status = status

        for observer in self.observers:
            observer.update(self.order_id, status)