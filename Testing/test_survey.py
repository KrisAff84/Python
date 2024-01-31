import pytest
from survey import AnonymousSurvey

# A fixture is used to create a test object to be used in multiple tests.
@pytest.fixture  
def language_survey():
    """Set up a survey instance for use in all tests."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)    
    return language_survey

def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    """Test that three individual responses are stored properly."""
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
