
def test_index(client):
    """Test the index route."""
    response = client.get('/')
    assert response.status_code == 200


def test_about(client):
    """Test the about route."""
    response = client.get('/about')
    assert response.status_code == 200