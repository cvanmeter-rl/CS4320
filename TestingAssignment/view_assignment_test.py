import pytest
import System

def test_view_assignment(grading_system):
    grading_system.login('hdjsr7','pass1234')
    assign = grading_system.usr.view_assignments('databases')
    if assign[0][1] != '1/6/20':
        assert False
    if assign[1][1] != '2/6/20':
        assert False
    assert True


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
