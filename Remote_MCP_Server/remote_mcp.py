from fastmcp import FastMCP
import random
import json

### Create the FastMcp server instance
mcp= FastMCP("Simple Calculator")

# Tool : Add 2 numbers
@mcp.tool
def add_numbers(a: int, b: int) -> int:
    """Add Two numbers
    
    Args:
        a: First Number
        b: Second Number
    
    Return:
    The sum of a and b
    """
    return a + b

# Generate a random number
@mcp.tool
def random_numbers(min_val: int =1, max_val: int=100) -> int:
    """Generate a random number within range.
    
    Args:
        min_val: Minimum Value
        max_val: Maximum Value
    
    Return:
    A random integer between min_val and max_val
    """
    return random.randint(min_val,max_val)

# Resource : Server info
@mcp.resource("info://server")
def server_infp() -> str :
    """Get information about the server."""

    info = {
        "name": "Simple Calculator Server",
        "version":"1.0.0",
        "description": "A basic MCP server with tools",
        "tools":['add_numbers','random_numbers'],
        "Author": "Ranjeet Kadam"
    }
    return json.dumps(info, indent=2)

# Start the Server
if __name__ == "__main__":
        mcp.run(transport="http",host = "0.0.0.0", port =8000)
