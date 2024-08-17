import string
from typing import List
from trends.models import Trend
from tweets.models import Tweet
from django.db.models import F
from nltk.util import ngrams
from nltk.corpus import stopwords


def extract_tokens(text: str):
    tokens = text.split()
    cleaned_tokens = [token.rstrip(string.punctuation) for token in tokens]
    return cleaned_tokens


def extract_unigrams(tokens: List[str]):
    filtered_tokens = [
        token.title() for token in tokens if not token in stopwords.words("english")
    ]
    return filtered_tokens


def extract_bigrams(tokens: List[str]):
    bigram_tuples = ngrams(tokens, 2)
    bigrams = [" ".join(bigram_tuple).title() for bigram_tuple in bigram_tuples]
    return bigrams


def extract_trigrams(tokens: List[str]):
    trigram_tuples = ngrams(tokens, 3)
    trigrams = [" ".join(trigram_tuple).title() for trigram_tuple in trigram_tuples]
    return trigrams


def create_or_update_unigram_trends(tweet, tokens):
    for token in tokens:
        trend, _ = Trend.objects.get_or_create(phrase=token)
        trend.hits = F("hits") + 1
        trend.save()
        trend.tweets.add(tweet)


def create_or_update_bigram_trends(tweet, bigram_tokens):
    for token in bigram_tokens:
        trend, _ = Trend.objects.get_or_create(phrase=token)
        trend.hits = F("hits") + 1
        trend.save()
        trend.tweets.add(tweet)


def create_or_update_trigram_trends(tweet, trigram_tokens):
    for token in trigram_tokens:
        trend, _ = Trend.objects.get_or_create(phrase=token)
        trend.hits = F("hits") + 1
        trend.save()
        trend.tweets.add(tweet)


def analyse_tweet_trends(tweet: Tweet):
    content = tweet.content
    tokens = extract_tokens(content.lower())

    unigrams = extract_unigrams(tokens)
    bigrams = extract_bigrams(tokens)
    trigrams = extract_trigrams(tokens)

    create_or_update_unigram_trends(tweet, unigrams)
    create_or_update_bigram_trends(tweet, bigrams)
    create_or_update_trigram_trends(tweet, trigrams)
