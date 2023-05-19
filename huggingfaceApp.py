from transformers import Conversation, pipeline

# Initialize the chat pipeline
chatbot = pipeline("conversational")

# Start the conversation
print("Welcome to the Chatbot demo. Let's chat!")

conversation = []
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break

    # Add user input to the conversation
    conversation.append(Conversation(user_input))

    # Get response from the chatbot
    response = chatbot(conversation)

    # Retrieve the bot's reply
    bot_reply = response[0]["generated_text"]
    print(f"Chatbot: {bot_reply}")

    # Add bot's reply to the conversation
    conversation.append(Conversation(bot_reply))
