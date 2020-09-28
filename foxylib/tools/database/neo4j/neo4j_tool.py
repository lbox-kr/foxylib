import os
from functools import lru_cache

from neo4j import GraphDatabase


class Neo4jTool:
    @classmethod
    def env2host(cls, ):
        return os.environ.get("NEO4J_HOST")

    @classmethod
    def env2username(cls, ):
        return os.environ.get("NEO4J_USERNAME")

    @classmethod
    def env2password(cls, ):
        return os.environ.get("NEO4J_PASSWORD")

    @classmethod
    @lru_cache(maxsize=2)
    def env2driver(cls, ):
        host = cls.env2host()
        username = cls.env2username()
        password = cls.env2password()

        return GraphDatabase.driver(host, auth=(username, password), encrypted=False)

    @classmethod
    def execute_query(cls, driver, query, **kargs):
        with driver.session() as session:
            session.run(query, kargs)
        return None

