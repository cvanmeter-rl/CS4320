import pytest
import System

#This test will see if the system will handle if a student tries to check grades for a course they are not enrolled in
#the test will fail if the system doesn't handle if a course is entered that the student isn't enrolled in

def test_wrong_course_grade(grading_system):
    grading_system.login('akend3','123454321')
    grades = grading_system.usr.check_grades('software_engineering')
    if grades is None:
        assert True
    assert False
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
