from .main import Maths_Test

math_test = Maths_Test('Testing')


def test_set_questions_1():
    math_test.set_questions([22, 26])
    assert (math_test.get_questions() == [22, 26])


# def test_days_until_launch_0():
#     assert (days_until_launch(253, 253) == 0)
#
#
# def test_days_until_launch_0_negative():
#     assert (days_until_launch(83, 64) == 0)
#
#
# def test_days_until_launch_1():
#     assert (days_until_launch(9, 10) == 1)
