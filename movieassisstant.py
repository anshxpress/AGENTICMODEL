from phi.agent import Agent
from phi.llm.google import Gemini
from phi.tools.exa import ExaTools
import os

# Set your Gemini API key
os.environ['GOOGLE_API_KEY'] = "AIzaSyDCe2Dw7a6Eb-WXSS_SPx_5_oeCNepLIyg"

popcorn_pal_agent = Agent(
    name="Popcorn Pal",
    tools=[
        ExaTools(),
    ],
    model=Gemini(model="gemini-2.0-flash-exp"),
    description=(
        "You are Popcorn Pal, a movie recommendation agent that searches and scrapes movie websites to provide detailed recommendations, "
        "including ratings, genres, descriptions, trailers, and upcoming releases."
    ),
    instructions=[
        "Use Exa to search for the movies.",
        "Provide results with the following details: movie title, genre, movies with good ratings, description, recommended viewing age, primary language,runtime, imdb rating and release date.",
        "Include trailers for movies similar to the recommendations and upcoming movies of the same genre or from related directors/actors.",
        "Give atleast 5 movie recommendations for each query",
        "Present the output in a well-structured markdown table for readability.",
        "Ensure all movie data is correct, especially for recent or upcoming releases.",
    ],
    markdown=True,
)

popcorn_pal_agent.print_response(
    "Suggest some thriller movies to watch with a rating of 8 or above on IMDB. My previous favourite thriller movies are The Dark Knight, Venom, Parasite, Shutter Island.",
    stream=True,
)