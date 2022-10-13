import pytest
import System
import json

username = 'cmhbf5'
password = 'bestTA'

def test_change_grade(grading_system):
    grading_system.login(username,password)
    grading_system.usr.change_grade('hdjsr7','software_engineering','assignment1',50)
    grading_system.reload_data()
    
    grading_system.login('hdjsr7','pass1234')
    assert grading_system.users[grading_system.usr.name]['courses']['software_engineering']['assignment1']['grade'] == 50

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem