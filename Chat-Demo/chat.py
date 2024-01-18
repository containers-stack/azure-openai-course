import os
import openai

# set the openai configuration
openai.api_type = "azure"
openai.api_key = ""
openai.api_version = "2023-07-01-preview"
openai.api_base = ""
LLM_DEPLOYMENT_NAME = "gpt-35-turbo"
EMBEDDINGS_MODEL_NAME = "text-embedding-ada-002"
    
# chat function
def chat():
    messages = []
        
    messages.append(
        {
            "role": "system",
            "content": "you are AI Assistent to awnser users question:",
        })

    while True:
        # get input from user
        user_input = input("You: ")

        messages.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(
            engine=LLM_DEPLOYMENT_NAME,
            messages=messages)

        messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})
        print(response["choices"][0]["message"]["content"])

# embedding function
def embedding():
    
    # read user data from file
    with open("./chat-demo/user_data.csv", "r") as f:
        file_conent = f.readlines()
        user_data = ''.join(file_conent)
    
    # create embedding
    embedding_data = openai.Embedding.create(
        engine=EMBEDDINGS_MODEL_NAME,
        input=user_data)

    # write embedding to file
    with open("./chat-demo/embedding_data.csv", "w") as f:
        f.write(str(embedding_data))

embedding()