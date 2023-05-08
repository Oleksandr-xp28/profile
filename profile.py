import csv

filename = "my_data.csv"
fields = ['question', 'answer']

def enter_information():
    responses = []
    print("Please answer the following questions:")
    print("=====================================")
    while True:
        response = {}
        response['question'] = input("What is your name? ")
        response['answer'] = input("What is your answer? ")
        responses.append(response)
        another = input("Do you want to add another question? (y/n) ")
        if another.lower() == "n":
            break
        response = {}
        response['question'] = input("What is your favorite book? ")
        response['answer'] = input("What is your answer? ")
        responses.append(response)
        response = {}
        response['question'] = input("What is your favorite movie? ")
        response['answer'] = input("What is your answer? ")
        responses.append(response)
    return responses

def save_csv(data):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(fields)
        for response in data:
            writer.writerow([response['question'], response['answer']])
        print(f"Data saved to {filename} successfully!")

def load_csv():
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['question']}: {row['answer']}")

def main():
    while True:
        print('1 - enter information: 2 - load information')
        action = input('action->')
        if action == '1':
            responses = enter_information()
            save_csv(responses)
        elif action == '2':
            load_csv()
        else:
            print('Invalid action. Please choose 1 or 2.')

if __name__ == '__main__':
    main()
