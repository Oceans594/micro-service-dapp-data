import time
from concurrent import futures

import grpc

from service import data_pb2_grpc
from service.data import DataCenter

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

def start():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    data_pb2_grpc.add_DataCenterServicer_to_server(DataCenter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()  # start() 不会阻塞，如果运行时你的代码没有其它的事情可做，你可能需要循环等待。
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    start()