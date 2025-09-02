import csv
from pathlib import Path
from .semantic_search import search


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


csv_path = Path("backend/database/tool_list_database.csv")
with csv_path.open(newline='', encoding="utf-8") as f:
    tools = list(csv.reader(f))        # includes header
    header, *tools = tools             # split header / body if you want
print("Loaded", len(tools), "rows")


descriptions=[]
final_outputs_list=[]


for r in tools:
    text=f"{r[0]} {r[1]}"
    descriptions.append(text.lower())



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

    return matching_tools_data




