import pytest
import System

username = 'cmhbf5'
password = 'bestTA'

def test_createAssignment(grading_system):
    grading_system.login(username,password)
    grading_system.usr.create_assignment('assignment3','11/01/20','software_engineering')
    grading_system.reload_data()
    
    if grading_system.courses['software_engineering']['assignments']['assignment3']['due_date'] == '11/01/20':
        assert True
    else:
        assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem