from typing import List

from project_document_management.category import Category
from project_document_management.document import Document
from project_document_management.topic import Topic


class Storage:

    categories: List[Category] = []
    topics: List[Topic] = []
    documents: List[Document] = []

    @classmethod
    def add_category(cls, category: Category):
        if category not in cls.categories:
            cls.categories.append(category)

    @classmethod
    def add_topic(cls, topic: Topic):
        if topic not in cls.topics:
            cls.topics.append(topic)

    @classmethod
    def add_document(cls, document: Document):
        if document not in cls.documents:
            cls.documents.append(document)

    @classmethod
    def edit_category(cls, category_id: int, new_name: str):
        category = [x for x in cls.categories if x.id == category_id][0]
        category.name = new_name

    @classmethod
    def edit_topic(cls, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = [x for x in cls.topics if x.id == topic_id][0]
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    @classmethod
    def edit_document(cls, document_id: int, new_file_name: str):
        document = [x for x in cls.documents if x.id == document_id][0]
        document.file_name = new_file_name

    @classmethod
    def delete_category(cls, category_id):
        category = [x for x in cls.categories if x.id == category_id][0]
        cls.categories.remove(category)

    @classmethod
    def delete_document(cls, document_id):
        document = [x for x in cls.documents if x.id == document_id][0]
        cls.documents.remove(document)

    @classmethod
    def delete_topic(cls, topic_id):
        topic = [x for x in cls.topics if x.id == topic_id][0]
        cls.topics.remove(topic)

    @classmethod
    def get_document(cls, document_id: int):
        document = ''.join(str(x) for x in cls.documents if x.id == document_id)
        return document

    def __repr__(self):
        return '\n'.join(str(x) for x in self.documents)





















