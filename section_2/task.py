out_container = []


def is_question_sentense(input_str):

    if input_str.startswith(("who", "how", "where", "why")):
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

print(" ".join(out_container))
