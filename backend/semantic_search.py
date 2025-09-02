from sentence_transformers import SentenceTransformer, util
import torch

# Load the model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L12-v2')

def search(descriptions,query):
    output=[]
    # Encode query and descriptions
    query_embedding = model.encode(query, convert_to_tensor=True)
    answer_embeddings = model.encode(descriptions, convert_to_tensor=True)

    # Compute cosine similarities
    cosine_scores = util.cos_sim(query_embedding, answer_embeddings)[0]  # Shape: [num_descriptions]

    # Set threshold
    threshold = 0.5

    # Filter scores above threshold AND sort by score (descending)
    filtered_scores = cosine_scores[cosine_scores > threshold]
    if len(filtered_scores) == 0:
        return []
    else:
        # Get indices of all scores above threshold, sorted by score (highest first)
        sorted_indices = torch.argsort(filtered_scores, descending=True)
        filtered_indices = torch.nonzero(cosine_scores > threshold).flatten()  # Original indices
        ranked_indices = filtered_indices[sorted_indices]  # Reorder by score

        for idx in ranked_indices:
            output.append(descriptions[idx])
        return output