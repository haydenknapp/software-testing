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

@then('it will return its single integer value, "{target}"')
def step_impl(contex, target):
    global result
    assert int(result) == int(target)

@when('we send the multi digit parser "{target}"')
def step_impl(context, target):
    global result
    result = calc.evaluate_positive_number(target)

@then('it will return its multiple integer value, "{target}"')
def step_impl(contex, target):
    global result
    assert int(result) == int(target)

@when('we send the float parser "{target}"')
def step_impl(context, target):
    global result
    result = calc.evaluate_floating_point_number(target)

@then('it will return its float value, "{target}"')
def step_impl(contex, target):
    global result
    assert float(result) == float(target)

@when('we send the single hex parser "{target}"')
def step_impl(context, target):
    global result
    result = calc.evaluate_single_hexadecimal_digit(target)

@then('it will return its hex value, "{target}"')
def step_impl(contex, target):
    global result
    assert int(result) == int(target)

@when('we send the full hex parser "{target}"')
def step_impl(context, target):
    global result
    result = calc.evaluate_hexadecimal(target)

@then('it will return its multi hex value, "{target}"')
def step_impl(contex, target):
    global result
    assert int(result) == int(target)


