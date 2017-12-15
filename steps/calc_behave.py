# Hayden Knapp
#
# Implement behavioral driven development using python3 and
# the behave modual to test the calc module

import calc

result = 1

@given('we have imported calc')
def step_impl(context):
    pass

@when('we send the single digit parser "{target}"')
def step_impl(context, target):
    global result
    result = calc.evaluate_single_digit(target)

@then('it will return its integer value, "{target}"')
def step_impl(contex, target):
    global result
    print(type(result))
    assert int(result) == int(target)
