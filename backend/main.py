import pandas as pd
from backend.semantic_search import SemanticSearch

# Initialize the search object
search_object = SemanticSearch()
df = search_object.df # Get the dataframe from the search object

def search_tool(query: str):
    """
    Searches for tools in the database based on a query.
    """
    # Get the descriptions from the search results
    descriptions = search_object.search(query)
    
    # Create the search key from the dataframe
    df_search_key = (df['name'] + ' ' + df['description'])
    
    # Retrieve the full tool information from the dataframe
    results = df[df_search_key.isin(descriptions)]
    
    # Convert the results to a list of lists
    return results.values.tolist()