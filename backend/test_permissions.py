import requests

def test_assignments_unauthorized():
    # Simulate unauthorized role (Admin trying to access assignments)
    resp = requests.get("http://localhost:8000/assignments", headers={"X-User-Role": "Admin"})
    assert resp.status_code == 403, f"Expected 403, got {resp.status_code}"
    print("PASS: Unauthorized Admin access to /assignments is blocked.")

def test_analytics_unauthorized():
    # Simulate unauthorized role (Student trying to access analytics)
    resp = requests.get("http://localhost:8000/analytics", headers={"X-User-Role": "Student"})
    assert resp.status_code == 403, f"Expected 403, got {resp.status_code}"
    print("PASS: Unauthorized Student access to /analytics is blocked.")

if __name__ == "__main__":
    test_assignments_unauthorized()
    test_analytics_unauthorized()
