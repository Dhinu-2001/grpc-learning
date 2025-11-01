import grpc
from concurrent import futures
import user_pb2
import user_pb2_grpc

class UserService(user_pb2_grpc.UserService):
    def GetUser(self, request, context):
        print("REACHED - user server")
        #Simulate user lookup
        user = {
            1: {"name": "Ashik", "email": "ashik@example.com"},
            2: {"name": "Rony", "email": "rony@example.com"}
        }
        user = user.get(request.user_id, {"name": "Unknown user", "email": ""})
        return user_pb2.UserResponse(
            user_id=request.user_id, name=user["name"], email=user["email"]
        )
        
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('localhost:50051')
    print("User service running on port 50051")
    server.start()
    server.wait_for_termination()
    

if __name__ == "__main__":
    serve()