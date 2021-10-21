import json

from models.application import ApplicationApps
from service import data_pb2_grpc, data_pb2


class DataCenter(data_pb2_grpc.DataCenterServicer):

    def GetApplication(self, request, context):
        # 查询数据
        identifier = request.identifier
        app = ApplicationApps.select().where(ApplicationApps.identifier==identifier).dicts().get()
        print(app)
        return data_pb2.GetApplicationResponse(message=json.dumps(app))