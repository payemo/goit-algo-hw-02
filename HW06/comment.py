class Comment:
    def __init__(self, text: str, author: str):
        self.text = text
        self.author = author
        self.is_deleted = False
        self.replies = []

    def add_reply(self, reply_comment: str):
        self.replies.append(reply_comment)

    def remove_reply(self):
        self.text = "That comment has been deleted."
        self.is_deleted = True

    def display(self, indent = 0):
        indent_str = '  ' * indent
        if self.is_deleted:
            print(f"{indent_str}{self.text}")
        else:
            print(f"{indent_str}{self.author}: {self.text}")
        for reply in self.replies:
            reply.display(indent + 1)


root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()