import openai 

openai.api_key = "sk-proj-zVJs3TDHoe0s0KxH9y3XT3BlbkFJsJxpKCgvwxbEZRUzNN8L"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].messages.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit","exit","bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ",response)
