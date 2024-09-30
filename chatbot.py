from openai import OpenAI


client = OpenAI(api_key="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")

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["quit", "exit", "bye", "sair", "tchau"]:
            break
        
        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)
