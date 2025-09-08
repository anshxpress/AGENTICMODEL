from phi.assistant import Assistant
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.pgvector import PgVector2
from phi.llm.google import Gemini
import os

# Set your Gemini API key
os.environ['GOOGLE_API_KEY'] = "AIzaSyDCe2Dw7a6Eb-WXSS_SPx_5_oeCNepLIyg"

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector2(
        collection="recipes",
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
    ),
)

knowledge_base.load(recreate=False)

assistant = Assistant(
    llm=Gemini(model="gemini-2.0-flash-exp"),
    knowledge_base=knowledge_base,
    add_references_to_prompt=True,
)
assistant.print_response("What are the ingredients to make Massaman Gai?", markdown=True)