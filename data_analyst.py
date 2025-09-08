import duckdb
import pandas as pd
import os
from phi.llm.google import Gemini
from phi.assistant import Assistant

# Set your Gemini API key
os.environ['GOOGLE_API_KEY'] = "AIzaSyDCe2Dw7a6Eb-WXSS_SPx_5_oeCNepLIyg"

def analyze_movies():
    # Load data with DuckDB
    conn = duckdb.connect()
    
    try:
        # Load CSV into DuckDB
        conn.execute("CREATE TABLE movies AS SELECT * FROM read_csv_auto('imdb-top-1000.csv')")
        
        print("=== Data Loaded Successfully ===\n")
        
        # Show table structure
        result = conn.execute("DESCRIBE movies").fetchall()
        print("Table Structure:")
        for row in result:
            print(f"  {row[0]}: {row[1]}")
        
        print("\n" + "="*50 + "\n")
        
        # Top 5 highest rated movies
        result = conn.execute("""
            SELECT Series_Title, Released_Year, IMDB_Rating, Director 
            FROM movies 
            ORDER BY IMDB_Rating DESC 
            LIMIT 5
        """).fetchall()
        
        print("Top 5 Highest Rated Movies:")
        for i, (title, year, rating, director) in enumerate(result, 1):
            print(f"{i}. {title} ({year}) - {rating}/10 - Dir: {director}")
        
        print("\n" + "="*50 + "\n")
        
        # Movies by decade
        result = conn.execute("""
            SELECT 
                (Released_Year / 10) * 10 as Decade,
                COUNT(*) as Movie_Count,
                ROUND(AVG(IMDB_Rating), 2) as Avg_Rating
            FROM movies 
            GROUP BY (Released_Year / 10) * 10
            ORDER BY Decade DESC
        """).fetchall()
        
        print("Movies by Decade:")
        for decade, count, avg_rating in result:
            print(f"{int(decade)}s: {count} movies, Avg Rating: {avg_rating}")
            
    except Exception as e:
        print(f"Database error: {e}")
    
    finally:
        conn.close()

# Create AI assistant for additional analysis
assistant = Assistant(
    llm=Gemini(model="gemini-2.0-flash-exp"),
    description="You are a movie data analyst who provides insights about IMDB movie data.",
)

if __name__ == "__main__":
    # Run manual analysis
    analyze_movies()
    
    print("\n" + "="*60 + "\n")
    
    # Ask AI for insights
    assistant.print_response(
        "Based on the IMDB top 1000 movies data, what trends do you notice about movie ratings across different decades?",
        markdown=True
    )