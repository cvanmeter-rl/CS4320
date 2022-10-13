import pytest
import System
import json

username = 'akend3'
password = '123454321'

username2 = 'cmhbf5'
password2 = 'bestTA'

username3 = 'saab'
password3 = 'boomr345'
def test_login(grading_system):
    grading_system.login(username2,password2)
    role = grading_system.users[username2]['role']
    grading_system.login(username,password)
    role2 = grading_system.users[username]['role'] 
    grading_system.login(username,password)
    role3 = grading_system.users[username3]['role']
    if role == 'ta' and role2 == 'student' and role3 == 'professor':
        assert True
    else:
        assert False


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
