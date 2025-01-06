class Node:
    def __init__(self, identifier):
        self.identifier = identifier
        self.friends = []

    def get_identifier(self):
        return self.identifier
    def get_friends(self):
        return self.friends
    def add_friend(self, identifier):
        self.friends.append(identifier)

class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_node(self, identifier):
        self.graph_dict[identifier] = Node(identifier)

    def add_friend(self, a: str, b: str):
        self.graph_dict[a].add_friend(b)
        self.graph_dict[b].add_friend(a)

    def get_suggested_friends(self, identifier):
        suggested_friends = []

        for friend in self.graph_dict[identifier].get_friends():
            for suggested in self.graph_dict[friend].get_friends():
                if suggested != identifier:
                    suggested_friends.append(suggested)

        return suggested_friends

    def __str__(self):
        s = str()

        for key in self.graph_dict.keys():
            s += key + "| Friends: "
            for friend in self.graph_dict[key].get_friends():
                s += friend + " "
            s += "\n"
        return s

    def get_people_keys(self):
        return self.graph_dict.keys()

g = Graph()
g.add_node("Bob")
g.add_node("Alice")
g.add_node("Frederic")
g.add_node("Claude")
g.add_node("Toni")
g.add_node("Misty")
g.add_node("Kathryn")
g.add_node("Ashley")

g.add_friend("Bob", "Alice")
g.add_friend("Frederic", "Claude")
g.add_friend("Toni", "Kathryn")
g.add_friend("Ashley", "Kathryn")
g.add_friend("Misty", "Bob")
g.add_friend("Frederic", "Toni")
g.add_friend("Frederic", "Misty")

print(g)

for person in g.get_people_keys():
    print(f"Suggested friends for {person}: {g.get_suggested_friends(person)}")