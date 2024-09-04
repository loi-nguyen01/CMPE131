from textblob import TextBlob

def get_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the sentiment polarity
    sentiment_polarity = blob.sentiment.polarity
    
    # Determine if the sentiment is positive, negative, or neutral
    if sentiment_polarity > 0:
        return "Positive"
    elif sentiment_polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def main():
    while True:
        # Get user input
        text = input("Enter a sentence for sentiment analysis (or type 'exit' to quit): ")
        
        # Exit condition
        if text.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        
        # Analyze the sentiment
        sentiment = get_sentiment(text)
        
        # Print the result
        print(f"The sentiment of the sentence is: {sentiment}")

if __name__ == "__main__":
    main()
