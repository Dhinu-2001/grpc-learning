import grpc
import sys
sys.path.append('../user_service')
import user_pb2
import user_pb2_grpc

async def get_user(user_id):
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = user_pb2_grpc.UserServiceStub(channel)
        response = await stub.GetUser(user_pb2.UserRequest(user_id=user_id))
    return response