import pytest
import System

username = 'goggins'
password = 'augurrox'

def test_add_student(grading_system):
    grading_system.login(username,password)
    grading_system.usr.add_student('yted91','databases')
    grading_system.reload_data()

    c = grading_system.users['yted91']['courses']
    for key in c:
        if c == 'databases':
            assert True
    assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
