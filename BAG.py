

class BAG:
    def __init__(self, contents, key_items, quest_items):
        self.contents = contents
        self.key_items = key_items
        self.quest_items = quest_items

    def add(self, item, is_quest_item=False, is_key_item=False, quantity=1):
        if item not in self.contents.keys():
            if is_key_item:
                self.key_items.append(item)
            if is_quest_item:
                self.quest_items.append(item)
            self.contents[item] = 0
        if len(self.contents) >= 20:
            return "BAG FULL"
        self.contents[item] += int(quantity)

    def remove(self, item, quantity=1):
        if item not in self.contents.keys() or item in self.key_items:
            return
        if int(self.contents[item]) <= int(quantity):
            del self.contents[item]
            return
        self.contents[item] -= int(quantity)

    def use_item(self, item):
        if item not in self.contents.keys():
            return
        if item in self.quest_items:
            print(f"Used the {item}.")
            return
        print(f"Used the {item}")
