# MCP Concept

This project demonstrates a simple client-server architecture using MCP (Multi-Component Protocol). The server exposes a multiplication tool, and the client connects to the server to use this tool.

## Files

- `server.py`: Implements an MCP server with a multiplication tool ([server.py](server.py)).
- `client.py`: Connects to the server and calls the multiplication tool ([client.py](client.py)).

## How to Run

1. **Start the server**  
   Open a terminal and run:
   ```sh
   python server.py
   ```

2. **Run the client**  
   In another terminal, run:
   ```sh
   python client.py
   ```

## Features

- The server provides a `mul(a, b)` tool to multiply two numbers.
- The client lists available tools and calls the multiplication tool.

## Requirements

- Python 3.11+
- `mcp` library
- `nest_asyncio` library

Install dependencies:
```sh
pip install mcp nest_asyncio
```
