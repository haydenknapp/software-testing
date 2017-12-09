# Hayden Knapp
#
# Implement behavioral driven development using python3 and
# the behave modual to test the calc module

@given('we have imported calc')
def step_impl(context):
    pass

@when('we send the single digit parser "{target}"')
def step_impl(context, target):
    result = evaluate_single_digits(target)

@then('it will return its integer value, "{target}"')
def step_impl(contex, target):
    assert int(result) == target
