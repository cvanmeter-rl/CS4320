import pytest
import System

def test_submit_assignment(grading_system):
    grading_system.login('hdjsr7','pass1234')
    grading_system.usr.submit_assignment('software_engineering','assignment1','LETS GO','10/10/2022')
    grading_system.reload_data()

    submissionDate = grading_system.users['hdjsr7']['courses']['software_engineering']['assignment1']['submission_date']
    submission =  grading_system.users['hdjsr7']['courses']['software_engineering']['assignment1']['submission']
    if submission != 'LETS GO' or submissionDate != '10/10/2022':
        assert False   
    assert True
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem