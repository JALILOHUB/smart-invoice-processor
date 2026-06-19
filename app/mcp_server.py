from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# Initialize the MCP Server
server = Server("invoice-knowledge-base")

# In-memory database for demonstration
# In a real scenario, this would connect to a persistent database like SQLite
INVOICE_DB = [
    {"id": "INV-001", "vendor": "TechCorp", "amount": 1500.00, "status": "paid"},
    {"id": "INV-002", "vendor": "OfficeSupplies", "amount": 250.50, "status": "pending"},
    {"id": "INV-003", "vendor": "CloudServices", "amount": 89.99, "status": "paid"},
]

@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools for the agent to discover."""
    return [
        Tool(
            name="search_invoices",
            description="Search for invoices by vendor name",
            inputSchema={
                "type": "object",
                "properties": {
                    "vendor": {
                        "type": "string", 
                        "description": "Vendor name to search for"
                    }
                },
                "required": ["vendor"]
            },
        ),
        Tool(
            name="get_invoice_stats",
            description="Get total amount and count of all invoices",
            inputSchema={
                "type": "object",
                "properties": {},
            },
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Execute the requested tool and return the result."""
    if name == "search_invoices":
        vendor = arguments.get("vendor", "").lower()
        results = [inv for inv in INVOICE_DB if vendor in inv["vendor"].lower()]
        return [TextContent(type="text", text=str(results))]
    
    elif name == "get_invoice_stats":
        total = sum(inv["amount"] for inv in INVOICE_DB)
        count = len(INVOICE_DB)
        return [TextContent(type="text", text=f"Total invoices: {count}, Total amount: ${total}")]
    
    return [TextContent(type="text", text="Unknown tool")]

async def main():
    """Run the MCP server using stdio transport."""
    async with stdio_server() as (read, write):
        await server.run(read, write, server.create_initialization_options())

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())