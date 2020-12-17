out_container = []


def is_question_sentense(input_str):
    words_container = input_str.split(" ")
    if words_container[0].lower() == 'how' \
            or words_container[0].lower() == 'when' \
            or words_container[0].lower() == 'why' \
            or words_container[0].lower() == 'who':
        return True
    else:
        return False


while True:
    input_str = input("Say something: ")
    if input_str == '\\end':
        break
    if is_question_sentense(input_str):
        out_container.append(input_str.capitalize() + "?")
    else:
        out_container.append(input_str.capitalize() + ".")

for item in out_container:
    print(item)
