from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP(
    name="MultCalculation",
)


# Multiply two numbers 
@mcp.tool()
def mul(a: int, b: int) -> int:
    """Multiply two numbers together"""
    return a * b


# Run the server
if __name__ == "__main__":
   mcp.run()