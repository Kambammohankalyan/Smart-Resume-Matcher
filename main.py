import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class ResumeMatcher:
    def __init__(self):
        # Load the BERT model
        # We use a cache_folder to prevent re-downloading if possible, 
        # but standard load is fine for now.
        print("⏳ Loading AI Model...")
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def get_embedding(self, text):
        """Converts text into a vector."""
        return self.model.encode(text)

    def match(self, job_description, resumes):
        """
        Compares JD vector against Resume vectors.
        Returns a list of tuples: [('Name', Score), ...]
        """
        print("🧠 Processing Semantic Matching...")
        
        # 1. Vectorize Job Description
        jd_vector = self.get_embedding(job_description).reshape(1, -1)
        
        results = []
        
        # 2. Vectorize Candidate Resumes
        for filename, text in resumes.items():
            resume_vector = self.get_embedding(text).reshape(1, -1)
            
            # Calculate Cosine Similarity
            similarity = cosine_similarity(jd_vector, resume_vector)[0][0]
            percentage = round(similarity * 100, 2)
            
            results.append((filename, percentage))
            
        # 3. Sort by highest score
        results.sort(key=lambda x: x[1], reverse=True)
        return results