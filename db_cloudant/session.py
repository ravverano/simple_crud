from modulefinder import packagePathMap
from ibmcloudant.cloudant_v1 import (
    BulkDocs,
    CloudantV1,
    Document,
)
from ibmcloudant import CouchDbSessionAuthenticator, ApiException
from config import settings
from typing import List
import requests

class DBCloudant:
    def __init__(self, username, password, url):
        self.authenticator = CouchDbSessionAuthenticator(username, password)
        self.service = CloudantV1(authenticator=self.authenticator)
        self.service.set_service_url(url)
        self.service.set_disable_ssl_verification(True)
        # set timeout to 600 seconds
        self.service.set_http_config({"timeout": 600})
        # set retry to 5 retry and 1 sec retry interval
        self.service.enable_retries(max_retries=5, retry_interval=1.0)


    def created_or_update_doc(self, db_name: str, doc: dict):
        doc = Document(**doc)
        res = self.service.post_document(db=db_name, document=doc).get_result()
        return res

    def get_document(self, db_name: str, doc_id: str):
        try:
            res = self.service.get_document(
                db=db_name, doc_id=doc_id
            ).get_result()
            return res
        except Exception as e:
            print("e: ", e)
            return None
    
    def query_docs_by_selector(
        self,
        db_name: str,
        selector: dict,
        fields: list = None,
        sort: list = None,
        skip: int = 0,
        limit: int = 0,
        use_index: list = None,
    ):

        res = self.service.post_find(
            db=db_name,
            selector=selector,
            fields=fields,
            sort=sort,
            skip=skip,
            limit=limit,
            use_index=use_index,
        ).get_result()

        return res

CloudantSessionLocal = DBCloudant(
    settings.CLOUDANT_USERNAME,
    settings.CLOUDANT_PASSWORD,
    settings.CLOUDANT_URL,
)