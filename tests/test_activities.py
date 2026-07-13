def test_get_activities_returns_activity_map(client):
    # Arrange
    path = "/activities"

    # Act
    response = client.get(path)

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert "Chess Club" in payload
    assert "Programming Class" in payload


def test_get_activities_returns_expected_activity_fields(client):
    # Arrange
    path = "/activities"
    expected_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get(path)

    # Assert
    assert response.status_code == 200
    payload = response.json()
    first_activity = next(iter(payload.values()))
    assert expected_fields.issubset(first_activity.keys())
    assert isinstance(first_activity["participants"], list)
