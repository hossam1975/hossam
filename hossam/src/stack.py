class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def get_stack_siz(self):
        return len(self.items)
    def get_peek_element(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    def pop(self):
        ppoped_item = self.get_peek_element()
        self.items.remove(ppoped_item)
        return ppoped_item
    def get_all_items(self):
        return self.items   