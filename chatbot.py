print("AI Chatbot Assistant")
print("Type 'exit' to stop the chat")

while True:
    user = input("You: ")

    if user.lower() == "hello":
        print("Bot: Hello! How can I help you?")
    elif user.lower() == "how are you":
        print("Bot: I am fine. Thanks for asking.")
    elif user.lower() == "what is your name":
        print("Bot: I am a simple AI chatbot.")
    elif user.lower() == "exit":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I don't understand that.")
