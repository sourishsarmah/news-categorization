import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer


def removeDuplicateLabels(labels):
    """
    Remove duplicate labels
    """
    labels.replace(["ARTS", "CULTURE & ARTS"], "ARTS & CULTURE", inplace=True)
    labels.replace("STYLE", "STYLE & BEAUTY", inplace=True)
    labels.replace(["WELLNESS", "HEALTHY LIVING"],
                   "HOME & LIVING", inplace=True)
    labels.replace("PARENTS", "PARENTING", inplace=True)
    labels.replace("WORLDPOST", "WORLD NEWS", inplace=True)
    labels.replace("COLLEGE", "EDUCATION", inplace=True)
    labels.replace("TASTE", "FOOD & DRINK", inplace=True)
    labels.replace("GREEN", "ENVIRONMENT", inplace=True)
    # labels.replace("MONEY", "BUSINESS", inplace=True)
    labels.replace("COMEDY", "ENTERTAINMENT", inplace=True)
    # labels.replace("IMPACT", "GOOD NEWS", inplace=True)
    # labels.replace(["BLACK VOICES", "LATINO VOICES", "QUEER VOICES"], "VOICES", inplace=True)

    return labels


def cleanText(data):
    """
    Clean Text
    - Keep only letters
    - Remove stopwords
    - Stem words
    """
    lemmatizer = WordNetLemmatizer()
    text = re.sub('[^a-zA-Z]', ' ', data)
    words = nltk.word_tokenize(text.lower())
    stops = set(stopwords.words('english'))
    lem_words = [lemmatizer.lemmatize(w) for w in words if w not in stops]
    return ' '.join(lem_words)
