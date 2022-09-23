user_output = ''


def is_question(input_str):
    interrogatives = ('who', 'what', 'where', 'when', 'why', 'how')
    input_is_question = False
    if input_str.lower().startswith(interrogatives):
        input_is_question = True

    return input_is_question


def remove_trailing_space(input_str):
    if input_str.endswith(' '):
        mod_input = input_str.rsplit(' ', 1)
        mod_input.pop()
        input_str = mod_input[0]

    return input_str


def add_period(input_str, should_have_question_mark):
    if input_str.endswith('?') and not should_have_question_mark:
        input_str = input_str.replace('?', '. ')
    elif not input_str.endswith('.') and not should_have_question_mark:
        input_str = f'{input_str}. '
    elif input_str.endswith('.') and should_have_question_mark:
        input_str.replace('.', '? ')

    return input_str


def add_question_mark(input_str, should_have_question_mark):
    if not input_str.endswith('?') and should_have_question_mark:
        input_str = f'{input_str}? '

    return input_str


def format_input(input_str):
    input_str = input_str.capitalize()
    input_str = remove_trailing_space(input_str)
    should_add_question_mark = is_question(input_str)
    input_str = add_period(input_str, should_add_question_mark)
    input_str = add_question_mark(input_str, should_add_question_mark)

    return input_str


while True:
    user_input = input('Say something: ')
    if '/end' in user_input:
        break
    formatted_input = format_input(user_input)
    user_output = f'{user_output}{formatted_input}'

print(user_output)

