from mcp.server.fastmcp import FastMCP
from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Read Gemini API Key
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Create Gemini Client
client = genai.Client(
    api_key=API_KEY
)

# Create MCP Server
mcp = FastMCP("Gemini MCP Server")


@mcp.tool()
def ask_gemini(question: str) -> str:
    """
    Ask a question to Gemini and return the response.
    """

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=question
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def explain_mcp() -> str:
    """
    Explain MCP.
    """

    return """
MCP stands for Model Context Protocol.

It is a standard protocol that allows AI models
to connect with external tools, APIs, databases,
and files through MCP servers.
"""


if __name__ == "__main__":
    print("Starting Gemini MCP Server...")
    mcp.run()