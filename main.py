import os
from openai import OpenAI
from dotenv import load_dotenv
from data_extractor import scrape_website


# Load API key from environment variables
load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# ChatGPT interaction
def get_chatgpt_response(prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            model="gpt-4o"
        )
        # Access the content correctly as an attribute
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error with ChatGPT API: {e}")
        return "Sorry, I couldn't process your request."


# Main chatbot function
def chatbot():
    url = input("Enter the website URL: ")
    print("Scraping website...")
    website_content = scrape_website(url)
    if not website_content:
        print("Failed to retrieve website content.")
        return
    print("Website content retrieved. You can now ask questions.")
    while True:
        user_query = input("You: ")
        if user_query.lower() in ["exit", "quit"]:
            print("Chatbot session ended.")
            break
        # Combine user query with website content
        prompt = f"The following content is from the website:\n\n{website_content}\n\nUser's query: {user_query}"
        response = get_chatgpt_response(prompt)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
