import openai
import configparser

# Read API key from configuration file
config = configparser.ConfigParser()
config.read('config.ini')
api_key = config.get('API_KEYS', 'OPENAI_API_KEY')

# Set the API key
openai.api_key = api_key


# Define the chat function
def chat(prompt):
    model = "davinci"
    model2= "text-davinci-003"
    response = openai.Completion.create(
        engine=model2,
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()


# Start the conversation
print("Welcome to the ChatGPT demo. Let's chat!")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("ChatGPT: Goodbye!")
        break

    prompt = f"You: {user_input}\nChatGPT:"
    response = chat(prompt)
    print(response)
