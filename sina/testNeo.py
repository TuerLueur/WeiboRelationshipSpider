from py2neo import Graph, Node, Relationship, NodeMatcher
graph = Graph('http://localhost:7474', username='neo4j', password='11210113')

tx = graph.begin()

# a = Node("Cat", uid='001')
# tx.merge(a, primary_label="Cat", primary_key="uid")  # a:001
# b = Node("Cat", uid='002')
# tx.merge(b, primary_label="Cat", primary_key="uid")  # b:002
# c = Node("Cat", uid='003')
# tx.merge(c, primary_label="Cat", primary_key="uid")  # c:003
# d = Node("Cat", uid='004')
# tx.merge(d, primary_label="Cat", primary_key="uid")  # d:004
# ab = Relationship(a, 'feed', b)  # 001 feed 002
# ac = Relationship(a, 'feed', c)  # 001 feed 003
# ad = Relationship(a, 'feed', d)  # 001 feed 004
# tx.merge(ab)
# tx.merge(ac)
# tx.merge(ad)
# tx.commit()


a = Node("Cat", uid='002')
tx.merge(a, primary_label="Cat", primary_key="uid")  # a:002
b = Node("Cat", uid='001')
tx.merge(b, primary_label="Cat", primary_key="uid")  # b:001
c = Node("Cat", uid='003')
tx.merge(c, primary_label="Cat", primary_key="uid")  # c:003
d = Node("Cat", uid='005')
tx.merge(d, primary_label="Cat", primary_key="uid")  # d:005
ab = Relationship(a, 'feed', b)  # 001 feed 002
ac = Relationship(a, 'feed', c)  # 001 feed 003
ad = Relationship(a, 'feed', d)  # 001 feed 004
tx.merge(ab)
tx.merge(ac)
tx.merge(ad)
tx.commit()
