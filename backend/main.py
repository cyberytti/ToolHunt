from .semantic_search import search
import sqlite3
from sentence_transformers import SentenceTransformer


# Download from the 🤗 Hub
model = SentenceTransformer("sentence-transformers/all-MiniLM-L12-v2")



def rank_results(all_matched_tools_data,query):
    temp_descriptions=[]
    final_output_list=[]
    ranked_results={}
    for d in all_matched_tools_data:
        text=f"name:{d[0]} description:{d[1]}"
        # print (text.lower())
        temp_descriptions.append(text.lower())
    # print (temp_descriptions)
    query_embeddings = model.encode_query(query)
    document_embeddings = model.encode_document(temp_descriptions)
    similarities = model.similarity(query_embeddings, document_embeddings)
    for r in range(len(similarities[0])):
        # print (f"{temp_descriptions[r]} {similarities[0][r]:.4f}")
        # print (f"{all_matched_tools_data[r]} {similarities[0][r]:.4f}")
        ranked_results[all_matched_tools_data[r]]=similarities[0][r].item()
        # print("\n\n")
    # Optional: sort by similarity score (highest first)
    sorted_results = sorted(ranked_results.items(), key=lambda x: x[1], reverse=True)

    for (name, description, url), score in sorted_results:
        final_output_list.append(((name, description, url)))
    return (final_output_list)


def find_indices(primary_list, query_list):
    """
    Find the indices of elements from query_list in primary_list.

    Args:
        primary_list (list): The list to search in
        query_list (list): The list of elements to search for

    Returns:
        list: A list of indices where query elements are found in primary list
    """
    indices = []
    for query_item in query_list:
        try:
            index = primary_list.index(query_item)
            indices.append(index)
        except ValueError:
            pass 
    return indices



conn = sqlite3.connect('backend/database/tools.db')
cursor = conn.cursor()

# # Create table
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS tools (
#         name TEXT,
#         description TEXT,
#         url TEXT
#     )
# ''')


# # Insert values:
#     cursor.execute('''
#         INSERT INTO tools (name, description, url)
#         VALUES (?, ?, ?)
#     ''', (name,tool's description, url))


descriptions=[]
final_outputs_list=[]

cursor.execute("SELECT * FROM tools")
tools=cursor.fetchall()
for row in tools:
    text=f"{row[0]} {row[1]}"
    descriptions.append(text.lower())

# Commit changes and close connection
conn.commit()
conn.close()



def search_tool(query):
    """
    Searches for tools based on a query and returns the matching tool data.

    Args:
        query (str): The search query string.

    Returns:
        list: A list of lists, where each inner list represents a matching tool's data.
    """
    # Find matching tool descriptions based on the query
    matching_descriptions = search(descriptions, query.lower())

    # Find the indices of these matching descriptions in the main descriptions list
    matching_indices = find_indices(descriptions, matching_descriptions)

    # Collect the full tool data for each matching index
    matching_tools_data = []
    for index in matching_indices:
        matching_tools_data.append(tools[index])

    return rank_results(matching_tools_data,query)




