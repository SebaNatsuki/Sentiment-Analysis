from textblob import TextBlob

text = input('Enter a sentence: ')

analysis = TextBlob(text)

if analysis.sentiment.polarity > 0:
    print('Positive response')
elif analysis.sentiment.polarity < 0:
    print('Negative response')
else:
    print('neutral response')
    