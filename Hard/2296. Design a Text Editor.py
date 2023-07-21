class Node:
    def __init__(self, val = None, prev = None, next = None):
        self.val = val
        self.prev= prev
        self.next = next

class TextEditor:

    def __init__(self):
        self.dummy = Node()
        self.cursor = self.dummy
        

    def addText(self, text: str) -> None:
        nxt = self.cursor.next
        for c in text:
            self.cursor.next = Node(c, self.cursor)
            self.cursor = self.cursor.next
        self.cursor.next = nxt
        if nxt:
            nxt.prev = self.cursor

    def deleteText(self, k: int) -> int:
        count = 0
        nxt = self.cursor.next
        while count < k and self.cursor.val:
            count += 1
            self.cursor = self.cursor.prev
        self.cursor.next = nxt
        if nxt:
            nxt.prev = self.cursor
        return count

    def cursorLeft(self, k: int) -> str:
        count = 0
        while count < k and self.cursor.prev:
            count += 1
            self.cursor = self.cursor.prev
        i = 0
        temp = self.cursor
        ans = []
        while i < 10 and temp.val:
            ans.append(temp.val)
            temp = temp.prev
            i += 1
        return ''.join(ans[::-1])


        

    def cursorRight(self, k: int) -> str:
        count = 0
        while count < k and self.cursor.next:
            count += 1
            self.cursor = self.cursor.next
        i = 0
        temp = self.cursor
        ans = []
        while i < 10 and temp.val:
            ans.append(temp.val)
            temp = temp.prev
            i += 1
        return ''.join(ans[::-1])


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
