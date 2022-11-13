import pytest
from task2_input import Employee, Designer, Developer


@pytest.fixture
def developer_fixture():
    developer_name = 'Ilya'

    def init_developer(seniority):
        return Developer(developer_name, seniority=seniority)

    return init_developer


@pytest.mark.parametrize('enter,exception', [(1, 1), (5, 2), (8, 3), (13, 4)])
def test_developer_method(developer_fixture, enter, exception):
    dev_func_testing = developer_fixture(2)
    for i in range(enter):
        dev_func_testing.check_if_it_is_time_for_upgrade()
    assert dev_func_testing.grade == exception


@pytest.fixture
def designer_fixture():
    designer_name = 'Ilya'
    awards = 2

    def init_designer(seniority):
        return Designer(designer_name, seniority=seniority, awards=awards)

    return init_designer


@pytest.mark.parametrize('enter,exception', [(1, 1), (5, 2), (15, 3), (20, 4)])
def test_designer_metod(designer_fixture, enter, exception):
    design_func_testing = designer_fixture(2)
    for i in range(enter):
        design_func_testing.check_if_it_is_time_for_upgrade()
    assert design_func_testing.grade == exception
