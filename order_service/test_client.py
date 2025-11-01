import grpc
import order_pb2
import order_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50052') as channel:
        print("REACHED - calling order server")
        stub = order_pb2_grpc.OrderServiceStub(channel)
        response = stub.GetOrder(order_pb2.OrderRequest(
            order_id=3,
            user_id=2,
            quantity=4
        ))
    print(response)

if __name__ == "__main__":
    run()