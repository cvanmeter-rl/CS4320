import pytest
import System
#This test will test whether or not a TA can change the grade for a student who isn't in their class
#this test will fail if the TA can successfully change a student's grade for a class that the TA doesn't associate with

def test_wrong_student_course_grade(grading_system):
    grading_system.login('cmhbf5','bestTA')
    grading_system.usr.change_grade('akend3','comp_sci','assignment1',15)
    grading_system.reload_data()
    
    grading_system.login('akend3','123454321')
    assert grading_system.users[grading_system.usr.name]['courses']['comp_sci']['assignment1']['grade'] == 99

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem