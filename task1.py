# Simple Rule-Based Chatbot

def chatbot():
    print("🤖 ChatBot: Hello! I am your chatbot.")
    print("Type 'bye' to exit the chat.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("🤖 ChatBot: Hi! Nice to meet you.")

        elif user_input == "how are you":
            print("🤖 ChatBot: I'm fine, thanks! How about you?")

        elif user_input == "what is your name":
            print("🤖 ChatBot: My name is Python ChatBot.")

        elif user_input == "thank you":
            print("🤖 ChatBot: You're welcome!")

        elif user_input == "bye":
            print("🤖 ChatBot: Goodbye! Have a great day.")
            break

        else:
            print("🤖 ChatBot: Sorry, I don't understand that.")


chatbot()