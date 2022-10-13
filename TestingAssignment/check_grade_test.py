import pytest
import System

def test_check_grades(grading_system):
    grading_system.login('yted91','imoutofpasswordnames')
    grades = grading_system.usr.check_grades('cloud_computing')
    if grades['assignment1']['grade'] != 3:
        assert False
    if grades['assignment2']['grade'] != 5:
        assert False
    assert True
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem