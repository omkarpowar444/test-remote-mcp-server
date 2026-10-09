from fastmcp import FastMCP
import random
import json

mcp=FastMCP(name="Simple Calculator Server")



@mcp.tool
def add(a:float,b:float)->float:
    "add two numbers"

    return a+b



@mcp.tool
def random_number(min_val:int, max_val:int)->int:

    "returns the random number from given range"

    return random.randint(min_val, max_val)




@mcp.resource("info://server")
def server_info()->str:
    "Get information about these server"

    info={
        "name":"Simple Calculator server",
        "version":"1.0.0",
        "description":"A basic mcp server with math tools",
        "tools":["add","random_number"],
        "author":"Omkar"
    }

    return json.dumps(info,indent=2)



if __name__=="__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)