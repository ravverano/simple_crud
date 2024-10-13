from sqlalchemy.orm import Session
from models import SampleData
from library import common
from fastapi.encoders import jsonable_encoder
from schemas.response import StandardResponse, GetResponse

class Crud():
    def get_data(
        self,
        db: Session,
        query_json: dict
    ):
        
        # INSTANTIATE VARIABLES
        query_json = query_json.dict(by_alias=True)
        data_id = query_json.get("data_id")
        data_description = query_json.get("data_description")
        data_name = query_json.get("data.name")

        # FETCH DATA
        data = (
            db.query(SampleData)
            .filter(SampleData.deleted_at == None)
        )

        if data_id:
            data = data.filter(
                SampleData.data_id == data_id
            )

        if data_description:
            data = data.filter(
                SampleData.data_description == data_description
            )

        if data_name:
            data = data.filter(
                SampleData.data_name == data_name
            )

        data = data.all()
        total_item = len(list(map(jsonable_encoder, data)))

        return GetResponse (
            status="ok",
            data=data,
            total_rows=total_item
        )

    def create_data(
        self,
        db: Session,
        query_json: dict
    ):
        # INSTANTIATE VARIABLES
        if type(query_json) != dict:
            query_json = query_json.dict(by_alias=True)

        print("query_json: ",query_json)

        # GENERATE ID
        query_json["data_id"] = common.uuid_generator()

        # GENERATE CREATION TIME
        query_json["created_at"] = common.get_timestamp(1)

        # INSERT DATA
        data = SampleData(**query_json)
        db.add(data)
        db.commit()

        return StandardResponse (
            status="ok",
            message="Data successfully created!"
        )
    
    def update_data(
        self,
        db: Session,
        query_json: dict    
    ):
        
        # INSTANTIATE VARIABLE
        if type(query_json) != dict:
            query_json = query_json.dict(by_alias=True)

            # REMOVE NULL VALUES
            query_json = {
                key: value for key, value in query_json.items() if value
            }

        data_id = query_json.get("data_id")

        # SETUP UPDATE JSON
        query_json["updated_at"] = common.get_timestamp(1)
        data = (
            db.query(SampleData)
            .filter(SampleData.data_id == data_id)
        )
        
        data.update(query_json)
        db.commit()

        return StandardResponse (
            status="ok",
            message="Data successfully updated!"
        )

    def delete_data(
        self,
        db: Session,
        item_id: str    
    ):
        # DELETE DATA BY ID
        data = (
            db.query(SampleData)
            .filter(SampleData.data_id == item_id)
        )

        query_json = {"deleted_at": common.get_timestamp(1)}
        data.update(query_json)
        db.commit()

        return StandardResponse (
            status="ok",
            message="Data successfully Deleted!"
        )
        
crud = Crud()

        