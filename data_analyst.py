import json
import streamlit as st
import os
from phi.llm.google import Gemini
from phi.assistant.duckdb import DuckDbAssistant

# Set your Gemini API key
os.environ['GOOGLE_API_KEY'] = "AIzaSyDCe2Dw7a6Eb-WXSS_SPx_5_oeCNepLIyg"

data_analyst = DuckDbAssistant(
    llm=Gemini(model="gemini-2.0-flash-exp"),
    semantic_model=json.dumps(
        {
            "tables": [
                {
                    "name": "movies",
                    "description": "Contains information about movies from IMDB.",
                    "path": "imdb-top-1000.csv",
                }
            ]
        }
    ),
)

data_analyst.print_response("Highest rated movie in 2022? Show me the SQL.", markdown=True)
data_analyst.print_response("Different category of movies", markdown=True)