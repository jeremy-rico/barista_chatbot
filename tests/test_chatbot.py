import pytest

from barista import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_profanity_filter(client):
    # Send profane post request
    response = client.post('/chat', json={'message': 'fuck you'})
    
    # Check for 200 response
    assert response.status_code == 200
    
    # Check that profanity was detected
    data = response.get_json()
    profanity_message = (
        "Your message contains foul language. Please "
        "keep the conversation respectuful."
    )
    assert data['reply'] == profanity_message
