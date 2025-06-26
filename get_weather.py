
import arxiv
import json
import os
from typing import List
from mcp.server.fastmcp import FastMCP



# Initialize FastMCP server
mcp = FastMCP("weather")


@mcp.tool()
def get_weather(location, unit):
    '''
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",

        ARGS:
            location: weather at this location
            unit: either celsius or fahrenheit

        RETURNS:
            weather at the location in asked units
    '''
    return f"weather at {location} is 34{unit}"


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
