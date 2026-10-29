from .observer import Observer


class AnalyticsObserver(Observer):
    def __init__(self):
        self.status_counts = {}

    def update(self, order_id, status):
        if status not in self.status_counts:
            self.status_counts[status] = 0

        self.status_counts[status] += 1