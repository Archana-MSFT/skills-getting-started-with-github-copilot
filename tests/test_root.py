def test_root_redirects_to_static_index(client):
    # Arrange
    path = "/"

    # Act
    response = client.get(path, follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_root_serves_html_when_redirect_is_followed(client):
    # Arrange
    path = "/"

    # Act
    response = client.get(path, follow_redirects=True)

    # Assert
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
