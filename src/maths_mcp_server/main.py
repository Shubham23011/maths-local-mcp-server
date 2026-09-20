from fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("MathServer")


# ============================================================
# MATH TOOLS
# ============================================================

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


@mcp.tool()
def modulus(a: float, b: float) -> float:
    """Return the remainder when a is divided by b."""
    if b == 0:
        raise ValueError("Cannot perform modulus with zero.")
    return a % b


# ============================================================
# START SERVER
# ============================================================

if __name__ == "__main__":
    mcp.run()