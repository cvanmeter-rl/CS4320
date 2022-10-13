import pytest
import System

#This test will check whether the system handles the case where I try to remove a student from a course
#that they aren't enrolled in. if the system throws an error the test fails if the program handles this case
#then the test will pass

def test_remove_incorrect_student(grading_system):
    grading_system.login('goggins','augurrox')
    if grading_system.usr.drop_student('yted91','databases'):
        assert True
    assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem