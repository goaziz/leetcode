class ListNode:
    def __init__(self, val, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        self.current = self.head

    def visit(self, url: str) -> None:
        new_node = ListNode(url)
        self.current.next = new_node
        new_node.prev = self.current
        self.current = new_node

    def back(self, steps: int) -> str:
        while steps and self.current.prev:
            self.current = self.current.prev
            steps -= 1

        return self.current.val

    def forward(self, steps: int) -> str:
        while steps and self.current.next:
            self.current = self.current.next
            steps -= 1
        return self.current.val


class BrowserHistory2:

    def __init__(self, homepage: str):
        self.current_page = homepage
        self.back_stack = []
        self.forward_stack = []

    def visit(self, url: str) -> None:
        self.back_stack.append(self.current_page)
        self.forward_stack.clear()
        self.current_page = url

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.back_stack:
                self.forward_stack.append(self.current_page)
                self.current_page = self.back_stack.pop()
            else:
                return self.current_page

        return self.current_page

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.forward_stack:
                self.back_stack.append(self.current_page)
                self.current_page = self.forward_stack.pop()
            else:
                return self.current_page

        return self.current_page


class BrowserHistory3:

    def __init__(self, homepage: str):
        self.history = {0: homepage}
        self.current = 0

    def visit(self, url: str) -> None:
        self.history[self.current + 1] = url
        self.current += 1

        for i in range(self.current + 1, len(self.history)):
            self.history.pop(i)

    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]


obj = BrowserHistory2('leetcode.com')
obj.visit('google.com')
obj.visit('facebook.com')
obj.visit('youtube.com')
print(obj.back(1))
print(obj.back(1))
obj.visit('linkedin.com')
