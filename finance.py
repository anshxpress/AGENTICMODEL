from phi.assistant import Assistant
from phi.llm.google import Gemini
from phi.tools.yfinance import YFinanceTools
import os

# Set your Gemini API key
os.environ['GOOGLE_API_KEY'] = "AIzaSyDCe2Dw7a6Eb-WXSS_SPx_5_oeCNepLIyg"

assistant = Assistant(
    llm=Gemini(model="gemini-2.0-flash-exp"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    show_tool_calls=True,
    markdown=True,
)
assistant.print_response("What is the stock price of NVDA")
assistant.print_response("Write a comparison between NVDA and AMD, use all tools available.")