# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2
import json
from . import settings


class CrawlProductPipeline(object):
    def open_spider(self, spider):
        self.connection = psycopg2.connect(
            host=settings.DB_HOST,
            database=settings.DB_NAME,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
        )
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        try:
            self.cur.execute(
                "insert into products(name,brand,spec) values(%s,%s,%s)",
                (item["name"], item["brand"], json.dumps(item["spec"]),),
            )
            self.connection.commit()
        except psycopg2.DatabaseError as error:
            print(error)
        return item

