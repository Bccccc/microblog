import requests

def test_assignment_1(student_id, url):
    response = requests.get(url + "/hello")
    assert response.status_code == 200
    assert "hello" in response.text.lower() 
    assert student_id in response.text 
    print("Passed test #1")

if __name__ == "__main__":
    name="bli14"
    url="http://bli14.pythonanywhere.com"
    test_assignment_1(name, url)