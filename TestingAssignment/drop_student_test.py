import pytest
import System

def test_drop_student(grading_system):
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.drop_student('hdjsr7','databases')
    grading_system.reload_data()

    c = grading_system.users['hdjsr7']['courses']
    for key in c:
        if c == 'databases':
            assert False
    assert True


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
