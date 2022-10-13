import pytest
import System

def test_check_ontime(grading_system):
    grading_system.login('hdjsr7','pass1234')
    # Testing if databases assignment 2 is on time. should be true
    check = grading_system.usr.check_ontime('2/5/20','2/6/20')
    if check == False:
        assert False
    grading_system.login('yted91','imoutofpasswordnames')
    #testing if cloud_computing assignment 1 is on time, should be late
    check2 = grading_system.usr.check_ontime('1/7/20','1/3/20')
    if check2 == True:
        assert False
    assert True

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
