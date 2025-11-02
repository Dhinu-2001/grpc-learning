# 🧩 Python gRPC Microservices (Sync + Async)

A learning project demonstrating how to build **microservices with gRPC in Python**, implemented in **both synchronous and asynchronous (asyncio)** styles.

This example uses two microservices:
- **User Service** — Provides user data  
- **Order Service** — Fetches user info via gRPC from the User Service

---

## 🚀 Overview

| Service | Description | Port |
|----------|--------------|------|
| **User Service** | Returns user details (id, name, email) | `50051` |
| **Order Service** | Returns order info and fetches user details via gRPC | `50052` |

You’ll find **two implementations** for both services:
- **Synchronous** (thread-based, `server.py` / `client.py`)
- **Asynchronous** (non-blocking, `async_server.py` / `async_*_client.py`)

---

## 🧱 Folder Structure
grpc-microservices/
│
├── order_service/
│ ├── protos/
│ │ └── order.proto
│ ├── order_pb2.py
│ ├── order_pb2_grpc.py
│ ├── server.py # Synchronous gRPC Server
│ ├── async_server.py # Async gRPC Server (grpc.aio)
│ ├── order_to_user.py # Sync client to UserService
│ ├── async_order_to_user.py # Async client to UserService
│ ├── test_client.py # Sync test client
│ └── async_test_client.py # Async test client
│
└── user_service/
├── protos/
│ └── user.proto
├── user_pb2.py
├── user_pb2_grpc.py
├── server.py # Synchronous gRPC Server
└── async_server.py # Async gRPC Server


---

## 🧰 Tech Stack

- **Python 3.10+**
- **gRPC** (`grpcio`, `grpcio-tools`)
- **AsyncIO** for non-blocking services
- **Protocol Buffers (protobuf)** for service definitions

---

## ⚙️ Setup

### 1️⃣ Install dependencies

```bash
pip install grpcio grpcio-tools
```

2️⃣ Generate gRPC Python files

Run this for both services:

# User Service
```bash
cd user_service
python -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/user.proto
```
# Order Service
```bash
cd ../order_service
python -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/order.proto
```
🚀 Run the Synchronous Version

Start User Service
```bash
cd user_service
python server.py
```

Start Order Service
```bash
cd order_service
python server.py
```

Test the setup
```bash
python test_client.py
```

⚡ Run the Asynchronous Version (grpc.aio)
Start Async User Service
```bash
cd user_service
python async_server.py
```

Start Async Order Service
```bash
cd order_service
python async_server.py
```

Run Async Test Client
```bash
python async_test_client.py
```

🧠 Sync vs Async gRPC Comparison
Feature	Synchronous	Asynchronous (grpc.aio)
Concurrency model	Thread-based	Event loop (asyncio)
Performance	Good for small-scale	Excellent for high concurrency
Implementation	grpc.server(...)	grpc.aio.server()
Use case	Simpler services	Scalable microservices / high load

🧱 Extending the Project

You can extend this project to:

Add databases (e.g., PostgreSQL, MongoDB)
Implement streaming RPCs
Use TLS for secure channels
Deploy both services using Docker Compose
Add a REST gateway (FastAPI or Django)

📚 References

gRPC Python Docs

Protocol Buffers Guide

AsyncIO Official Docs

✨ Author

Dhinu C Philip
📧 dhinucphilip1022001@gmail.com

💼 GitHub Profile
https://github.com/Dhinu-2001
