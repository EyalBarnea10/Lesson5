from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("get_user_info")

address="https://jsonplaceholder.typicode.com/users/[id]"

print("Server is running...")

@mcp.tool()
def get_user_info(id: str):
    res=requests.get(address.replace("[id]", id))
    return res.json()
mcp.run(transport="stdio")

@mcp.tool()
def get_user(id:str):
    res = requests.get(address.replace("[id]", id))
    return res.json()["name"]