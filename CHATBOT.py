print("Hello! I am your chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()  # Take user input and make it lowercase

    if user_input == "hi" or user_input == "hello":
        print("Chatbot: Hello! How can I help you?")
    elif user_input == "how are you":
        print("Chatbot: I am fine, thank you! How are you?")
    elif user_input == "i am fine":
        print("Chatbot: That's great to hear!")
    elif user_input == "what is your name":
        print("Chatbot: I am a simple chatbot made in Python.")
    elif user_input == "bye":
        print("Chatbot: Goodbye! Have a nice day!")
        break
    else:
        print("Chatbot: Sorry, I don't understand that.")
