# -*- coding: utf-8 -*-
import pymongo
from pymongo.errors import DuplicateKeyError
from sina.items import RelationshipsItem, InformationItem
from sina.settings import LOCAL_MONGO_HOST, LOCAL_MONGO_PORT, DB_NAME
from py2neo import Graph, Node, Relationship, NodeMatcher


class MongoDBPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(LOCAL_MONGO_HOST, LOCAL_MONGO_PORT)
        db = client[DB_NAME]
        self.Information = db["Information"]
        self.Relationships = db["Relationships"]

    def process_item(self, item, spider):
        """ 判断item的类型，并作相应的处理，再入数据库 """
        if isinstance(item, RelationshipsItem):
            self.insert_item(self.Relationships, item)
            self.insert_relation(self,item)
            print("relation inserted")
        elif isinstance(item, InformationItem):
            self.insert_item(self.Information, item)
            print("information inserted")
        return item

    @staticmethod
    def insert_item(collection, item):
        try:
            collection.insert(dict(item))
        except DuplicateKeyError:
            """
            说明有重复数据
            """
            pass

    @staticmethod
    def insert_relation(graph, item):
        graph = Graph('http://localhost:7474', username='neo4j', password='11210113')
        tx = graph.begin()
        matcher = NodeMatcher(graph)
        try:
            a = Node("Person", uid=item['fan_id'])
            tx.merge(a, primary_label="Person", primary_key="uid")
            b = Node("Person", uid=item['followed_id'])
            tx.merge(b, primary_label="Person", primary_key="uid")
            ab = Relationship(a, 'follow', b)
            if matcher.match(uid=item['followed_id']):
                print("--------------same follow-----------")
            tx.merge(ab)
            tx.commit()
        except KeyError:
            pass
