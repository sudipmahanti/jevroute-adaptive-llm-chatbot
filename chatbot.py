import config
from providers import ask_gemini

def check_setup():
    """Return a helpful message if something is missing in .env, otherwise None."""
    if not config.GEMINI_API_KEY:
        return "GEMINI_API_KEY is missing.\nPlease add your Gemini API key to the .env file."
    if not config.JEV_API_KEY:
        return "JEV_API_KEY is missing.\nPlease add your Jev API key to the .env file."

def main():
    problem = check_setup()
    if problem:
        print(f"Error:{problem}")
        return

    print("Chatbot ready! Jev checks each prompt before Gemini answers.")
    print("Type exit or stop to quit.")

    while True:
        message = input("\nYou: ").strip()
        if message in ("exit","stop"):
            print("Goodbye!")
            break

        if not message:
            print("Pls enter a message!")
            continue

        try:
            print(f"\nAssistant: {ask_gemini(message)}")

        except Exception as e:
            print(f"Sorry the system got failed: {e}")

if __name__ == "__main__":
    main()


