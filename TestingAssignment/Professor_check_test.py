import pytest
import System

#this test will check whether a professor can add a student to a class they dont teach. if so test fails

def test_professor_check(grading_system):
    grading_system.login('goggins','augurrox')
    grading_system.usr.add_student('akend3','cloud_computing')
    if grading_system.users['akend3']['courses']['cloud_computing'] is not None:
        assert False
    assert True

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem