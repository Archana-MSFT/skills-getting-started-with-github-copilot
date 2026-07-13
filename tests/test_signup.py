def test_signup_registers_new_student(client):
    # Arrange
    activity_name = "Chess Club"
    email = "new.student@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for {activity_name}"

    activities_response = client.get("/activities")
    assert email in activities_response.json()[activity_name]["participants"]


def test_signup_rejects_duplicate_student(client):
    # Arrange
    activity_name = "Chess Club"
    existing_email = "michael@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup", params={"email": existing_email}
    )

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"


def test_signup_rejects_unknown_activity(client):
    # Arrange
    activity_name = "Unknown Club"
    email = "test@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_rejects_when_activity_is_full(client):
    # Arrange
    activity_name = "Chess Club"
    filler_emails = [
        "filler1@mergington.edu",
        "filler2@mergington.edu",
        "filler3@mergington.edu",
        "filler4@mergington.edu",
        "filler5@mergington.edu",
        "filler6@mergington.edu",
        "filler7@mergington.edu",
        "filler8@mergington.edu",
        "filler9@mergington.edu",
        "filler10@mergington.edu",
    ]
    overflow_email = "overflow@mergington.edu"

    for email in filler_emails:
        prefill_response = client.post(
            f"/activities/{activity_name}/signup", params={"email": email}
        )
        assert prefill_response.status_code == 200

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup", params={"email": overflow_email}
    )

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Activity is full"
