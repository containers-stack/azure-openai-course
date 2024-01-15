import openai
from faker import Faker

# set the openai configuration
openai.api_key = ""
openai.api_base = ""
openai.api_type = "azure"
openai.api_version = "2023-07-01-preview"
deployment_name = "gpt-35-turbo"


messages = []

# get user_data.csv file content
with open('user_data.csv', 'r') as f:
    user_data = f.readlines()

    # convert list to string
    user_data = ''.join(user_data)

messages.append(
    {
        "role": "system",
        "content": "you are AI Assistent to awnser users question about user_data.csv file, here the file content: " + user_data
    })

while True:
    # get input from user
    user_input = input("You: ")

    messages.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        engine=deployment_name,
        messages=messages
    )

    messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})
    print(response["choices"][0]["message"]["content"])
