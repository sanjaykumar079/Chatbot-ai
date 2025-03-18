import google.generativeai as genai
import os

# Set your Gemini API key (replace with your key or use environment variable)
GEMINI_API_KEY = "AIzaSyDLxVcfhBZg1aOtMXPlXLe6YNqnSkjcsj8"  # Replace with your API key
genai.configure(api_key=GEMINI_API_KEY)

def generate_response(emotion, user_input):
    """
    Generate a response using the Gemini API, conditioned on emotion and input.
    Args:
        emotion (str): Detected emotion (e.g., 'neutral', 'sadness').
        user_input (str): User's raw input text.
    Returns:
        str: Generated response.
    """
    # Emotion-specific system instructions to guide the response
    system_instructions = {
        "neutral": "You are a helpful and informative friend. Provide a detailed, friendly, and conversational response to the user's query.",
        "sadness": "You are an empathetic friend. Respond with understanding, comfort, and gentle encouragement to help the user feel better.",
        "joy": "You are an enthusiastic friend. Respond with excitement and happiness, celebrating the user's positive mood.",
        "anger": "You are a calm and understanding friend. Respond with patience and support to help the user manage their anger.",
        "fear": "You are a reassuring friend. Respond with comfort and confidence to help the user feel safe.",
        "love": "You are a warm and affectionate friend. Respond with love and positivity to match the user's feelings.",
        "surprise": "You are a curious and excited friend. Respond with enthusiasm and curiosity about the user's surprising news."
    }

    # Default instruction if emotion not found
    instruction = system_instructions.get(emotion, "You are a helpful friend. Respond naturally and conversationally.")

    # Prepare the prompt with the instruction and user input
    prompt = f"{instruction}\nUser input: {user_input}"

    # Call Gemini API for generation
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')  # Use Gemini 1.5 Flash (free tier model)
        response = model.generate_content(prompt)
        bot_response = response.text.strip()
    except Exception as e:
        # Fallback in case of API failure or quota exceeded
        print(f"Error with Gemini API: {e}")
        bot_response = {
            "neutral": f"I’d love to help! Can you tell me more about that?",
            "sadness": f"I’m sorry you’re feeling sad. Let’s talk about what’s on your mind.",
            "joy": f"That’s wonderful! I’m so happy for you—tell me more!",
            "anger": f"I understand you’re upset. Let’s take a moment to talk it out.",
            "fear": f"I’m here for you—don’t worry, we’ll figure this out together.",
            "love": f"That’s so sweet! I feel the warmth too—tell me about it!",
            "surprise": f"Wow, that’s surprising! Can you tell me more?"
        }.get(emotion, "I’d love to help! Can you give me more details?")

    return bot_response

if __name__ == "__main__":
    test_cases = [
        ("neutral", "tell me about a ball"),
        ("sadness", "i dont want to study"),
        ("joy", "I just won a prize!")
    ]
    for emotion, user_input in test_cases:
        response = generate_response(emotion, user_input)
        print(f"Input: {user_input} | Emotion: {emotion} | Response: {response}")