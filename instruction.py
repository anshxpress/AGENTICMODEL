from phi.assistant import Assistant
from phi.llm.google import Gemini
import os

# Set your Gemini API key
os.environ['GOOGLE_API_KEY'] = "AIzaSyDCe2Dw7a6Eb-WXSS_SPx_5_oeCNepLIyg"

assistant = Assistant(
    llm=Gemini(model="gemini-2.0-flash-exp"),
    description="You are a famous short story writer asked to write for a magazine",
    instructions=["You are a pilot on a plane flying from Hawaii to Japan."],
    markdown=True,
    debug_mode=True,
)
assistant.print_response("Tell me a 2 sentence horror story.")