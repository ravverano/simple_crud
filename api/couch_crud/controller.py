from sqlalchemy.orm import Session
from models import SampleData
from library import common
from fastapi.encoders import jsonable_encoder
from schemas.response import StandardResponse, GetResponse
from config import settings
from fastapi import HTTPException
import requests
CLOUDANT_DB = settings.CLOUDANT_DB

class Crud():
    def get_data(
        self,
        cdb: Session,
        query_json: dict
    ):
        
        # INSTANTIATE VARIABLES
        query_json = query_json.dict(by_alias=True)
        data_id = query_json.get("data_id")
        data_description = query_json.get("data_description")
        data_name = query_json.get("data_name")

        # USE SELECTOR TO QUERY DATA
        selector = {}
        if data_id:
            selector["_id"] = str(data_id)

        if data_name:
            selector["data_name"] = {
                "$regex": data_name
                }

        if data_description:
            selector["data_description"] = {
                "$regex": data_description
                }

        # FETCH DATA
        data = cdb.query_docs_by_selector(
            CLOUDANT_DB,
            selector=selector,
            limit=999999
        )

        data = data.get("docs", [])
        total_item = len(data)

        return GetResponse (
            status="ok",
            data=data,  
            total_rows=total_item
        )

    def create_data(
        self,
        cdb: Session,
        query_json: dict
    ):
        # INSTANTIATE VARIABLES
        if type(query_json) != dict:
            query_json = query_json.dict(by_alias=True)

        # GENERATE ID
        _id = common.uuid_generator()
        query_json["data_id"] = _id
        query_json["id"] = _id

        # GENERATE CREATION TIME
        query_json["created_at"] = common.get_timestamp(1)

        # INSERT TO DB
        cdb.created_or_update_doc(CLOUDANT_DB, query_json)
        
        return StandardResponse (
            status="ok",
            message="Data successfully created!"
        )
    
    def update_data(
        self,
        cdb: Session,
        query_json: dict    
    ):
        
        # INSTANTIATE VARIABLE
        if type(query_json) != dict:
            query_json = query_json.dict(by_alias=True)

        _id = query_json.get("data_id")

        # FETCH DATA REVISION
        data = cdb.get_document(CLOUDANT_DB, _id)

        if not data:
            raise HTTPException(status_code=404, detail="Data not found")
        
        data = common.clean_couch_doc(data)
        data["updated_at"] = common.get_timestamp(1)
        for x in query_json:
            data[x] = query_json[x]

        # UPDATE TO DB
        cdb.created_or_update_doc(CLOUDANT_DB, data)

        return StandardResponse (
            status="ok",
            message="Data successfully updated!"
        )

    def delete_data(
        self,
        cdb: Session,
        doc_id: str    
    ):
        # FETCH DATA REVISION
        data = cdb.get_document(CLOUDANT_DB, doc_id)

        if not data:
            raise HTTPException(status_code=404, detail="Data not found")
        
        # ADD DELETED ATTRIBUTE
        data = common.clean_couch_doc(data)
        data["deleted"] = True
        
        # UPDATE TO DB
        cdb.created_or_update_doc(CLOUDANT_DB, data)

        return StandardResponse (
            status="ok",
            message="Data successfully Deleted!"
        )
    
crud = Crud()

        