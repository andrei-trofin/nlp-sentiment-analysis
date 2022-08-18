"""
Preprocessing file that contains method to use for preprocessing text.
This is different from stage 1 of preprocessing because it is based on the training data.
This function removes all the least frequent words and the most frequent words that are not relevant.
However, the least frequent and most frequent tags are only relevant to the training set. Hence I wanted to make it
a clear point that these are 2 separate preprocessing steps.
"""
import json
from pickle import load
import pandas as pd
import spacy

with open("../../../data/lf_words.json", "rb") as file:
    lf_words = json.load(file)
    file.close()

with open("../../../data/mf_words.json", "rb") as file:
    mf_words = json.load(file)
    file.close()

with open("../../../data/m_feats_scaler.pkl", "rb") as file:
    scaler = load(file)
    file.close()

with open("../../../data/tf_vectorizer.pkl", "rb") as file:
    tf_vectorizer = load(file)
    file.close()

with open("../../../data/tfidf_vectorizer.pkl", "rb") as file:
    tfidf_vectorizer = load(file)
    file.close()

nlp = spacy.load('en_core_web_lg', disable=['tagger', 'parser', 'senter', 'attribute_ruler', 'lemmatizer', 'ner'])


def preprocess_text(text):
    """
    Function that removes smost frequent and least frequent words as established by previous preprocessing.
    :param text: The text to modify.
    :return: The text without most frequent and least frequent words.
    """
    return " ".join([word for word in text.split() if word not in lf_words and word not in mf_words])


def scale_manual_features(m_feats_df):
    """
    Function that scales a dataframe of an already established type (, 12)
    :param m_feats_df: The dataframe representing the raw extracted features.
    :return: Dataframe containing scaled values of the features.
    """
    return pd.DataFrame(scaler.transform(m_feats_df), index=m_feats_df.index, columns=m_feats_df.columns)


def get_tf_from_text(text_df):
    """
    Function that transforms a pandas.Series entries into term frequency encoding.
    :param text_df: The dataframe representing the preprocessed text.
    :return: Sparse matrix containing the tf representation of the given dataframe/series.
    """
    return tf_vectorizer.transform(text_df)


def get_tfidf_from_text(text_df):
    """
    Function that transforms a pandas.Series entries into term frequency - inverse document frequency encoding.
    :param text_df: The dataframe representing the preprocessed text.
    :return: Sparse matrix containing the tf-idf representation of the given dataframe/series.
    """
    return tfidf_vectorizer.transform(text_df)


def get_word2vec_from_text(text_df):
    """
    Function that gets a text dataframe or series.
    :param text_df: The dataframe representing the preprocessed text.
    :return: Sparse matrix containing the tf-idf representation of the given dataframe/series.
    """
    all_embeddings = []
    for doc in nlp.pipe(text_df, batch_size=200):
        all_embeddings.append(doc.vector)
    return pd.Series(all_embeddings, index=text_df.index.values)

