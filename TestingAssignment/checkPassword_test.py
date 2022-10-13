import pytest
import System

username = 'goggins'
password = 'augurrox'
def test_check_password(grading_system):
    t = grading_system.check_password(username,password)
    t2 = grading_system.check_password(username,'augurrox')
    t3 = grading_system.check_password(username,'AUGURROX')
    if t == t3 or t2 == t3:
        assert False
    if t != t2:
        assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
