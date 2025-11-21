while True:
    msg=input("You: ").lower()
    if msg=="hello"or msg=="hi":
        print("Hi!")
    elif msg=="how are you:":
        print("I am fine.Thanks for asking.")
    elif msg== "bye":
        print("Goodbye!")
        break
    else:
        print("I don't understand.")
exit()
