from textblob import TextBlob

text = input('Enter a sentence: ')

analysis = TextBlob(text)

if analysis.sentiment.polarity > 0:
    print('Sentiment : Positive response')
elif analysis.sentiment.polarity < 0:
    print('Sentiment : Negative response')
else:
    print('Sentiment : neutral response')
    
