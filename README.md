# Example bidirectional gRPC streaming service

This project implements a gRPC server and client using bidirectional streaming. The server receives messages from the client and logs them.

## Requirements

- gRPC dependencies listed in `Requirements.txt`

## Installation

1. **Clone the repository:**

    ```bash
    git clone <your-repository-url>
    cd <your-repository-directory>
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Generate gRPC Code from .proto:**

    ```bash
    python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. my_service.proto
    ```

## Running the server

To start the gRPC server, run:

```bash
python server.py
```

## Running the client

To start the gRPC server, run:

```bash
python client.py
```
