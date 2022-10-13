import pytest
import System

#This test will check whether or not a TA can make an assignment for a class that they aren't a TA for. if they are
#able to create a assignment for a class they are not a part of the test will fail

def test_TA_assignment_creation(grading_system):
    grading_system.login('cmhbf5','bestTA')
    grading_system.usr.create_assignment('assignment3','10/15/22','databases')
    if grading_system.courses['databases']['assignments']['assignment3']['due_date'] == '10/15/22':
        assert False
    assert True
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem