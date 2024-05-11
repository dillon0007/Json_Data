import json

def get_question_data():
    question_number = int(input("Enter question number: "))
    question_id = int(input("Enter question ID: "))
    question_text = input("Enter question text: ")
    option_number = int(input("Enter option number: "))
    option_text = input("Enter option text: ")
    is_correct = input("Is this option correct? (True/False): ").lower() == 'true'
    solution_text = input("Enter solution text: ")

    question_data = {
        "questionNumber": question_number,
        "questionId": question_id,
        "questionText": question_text,
        "options": [
            {
                "optionNumber": option_number,
                "optionText": option_text,
                "isCorrect": is_correct
            }
        ],
        "solutionText": solution_text
    }

    return question_data

def add_question_to_file(question_data):
    try:
        with open("output.json", "r") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = []

    data.append(question_data)

    with open("output.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

def generate_json_output(data):
    json_output = json.dumps(data, indent=4)
    print(json_output)

if __name__ == "__main__":
    while True:
        question_data = get_question_data()
        add_question_to_file(question_data)
        generate_json_output(question_data)
        cont = input("Do you want to add another question? (yes/no): ").lower()
        if cont != 'yes':
            break
