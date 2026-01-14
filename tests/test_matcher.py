import pytest
from main import ResumeMatcher

# Fixture: Setup the model once before tests run (saves time)
@pytest.fixture(scope="module")
def matcher():
    return ResumeMatcher()

def test_perfect_match(matcher):
    """Scenario 1: Identical text should have 100% match"""
    job = "Python Developer with AI skills"
    resume = {"Me": "Python Developer with AI skills"}
    
    results = matcher.match(job, resume)
    
    # Check if top score is very close to 100
    # (Floating point math can be 99.999, so we use approx)
    score = results[0][1]
    assert score > 99.0

def test_irrelevant_match(matcher):
    """Scenario 2: Completely different text should have low score"""
    job = "Python Developer with AI skills"
    resume = {"Chef": "I cook italian food and bake cakes."}
    
    results = matcher.match(job, resume)
    score = results[0][1]
    
    # Score should definitely be low (e.g., less than 20%)
    assert score < 30.0

def test_ranking_order(matcher):
    """Scenario 3: Good candidate should be ranked higher than bad one"""
    job = "Data Scientist"
    resumes = {
        "Good": "I am a Data Scientist with Python experience.",
        "Bad": "I am a HR Manager with management skills."
    }
    
    results = matcher.match(job, resumes)
    
    # The first result (index 0) should be 'Good'
    top_candidate = results[0][0]
    assert top_candidate == "Good"