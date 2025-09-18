"""
Metrics calculation module for Style Transfer AI.
Handles readability metrics and statistical text analysis.
"""

import re
import math
from collections import Counter
from ..utils.text_processing import count_syllables


def calculate_readability_metrics(text):
    """Calculate various readability and complexity metrics."""
    # Input validation
    if not text or not text.strip():
        return {}
    
    # Basic text statistics
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    words = text.split()
    
    # Additional validation
    if not words or not sentences:
        return {}
    
    syllables = sum([count_syllables(word) for word in words])
    
    # Readability scores
    avg_sentence_length = len(words) / len(sentences)
    avg_syllables_per_word = syllables / len(words)
    
    # Flesch Reading Ease
    flesch_score = 206.835 - (1.015 * avg_sentence_length) - (84.6 * avg_syllables_per_word)
    
    # Flesch-Kincaid Grade Level
    fk_grade = (0.39 * avg_sentence_length) + (11.8 * avg_syllables_per_word) - 15.59
    
    # Coleman-Liau Index
    avg_letters_per_100_words = (sum(len(word) for word in words) / len(words)) * 100
    avg_sentences_per_100_words = (len(sentences) / len(words)) * 100
    coleman_liau = (0.0588 * avg_letters_per_100_words) - (0.296 * avg_sentences_per_100_words) - 15.8
    
    return {
        "flesch_reading_ease": round(flesch_score, 2),
        "flesch_kincaid_grade": round(fk_grade, 2),
        "coleman_liau_index": round(coleman_liau, 2),
        "avg_sentence_length": round(avg_sentence_length, 2),
        "avg_syllables_per_word": round(avg_syllables_per_word, 2)
    }


def analyze_text_statistics(text):
    """Perform detailed statistical analysis of text."""
    # Input validation
    if not text or not text.strip():
        return {
            'word_count': 0,
            'sentence_count': 0,
            'paragraph_count': 0,
            'character_count': 0,
            'avg_words_per_sentence': 0,
            'avg_sentences_per_paragraph': 0,
            'word_frequency': {},
            'punctuation_counts': {},
            'sentence_types': {},
            'unique_words': 0,
            'lexical_diversity': 0
        }
    
    words = text.split()
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    
    # Additional validation for empty results
    if not words:
        return {
            'word_count': 0,
            'sentence_count': len(sentences),
            'paragraph_count': len(paragraphs),
            'character_count': len(text),
            'avg_words_per_sentence': 0,
            'avg_sentences_per_paragraph': 0,
            'word_frequency': {},
            'punctuation_counts': {},
            'sentence_types': {},
            'unique_words': 0,
            'lexical_diversity': 0
        }
    
    # Word frequency analysis
    word_freq = Counter(word.lower().strip('.,!?";:()[]{}') for word in words)
    
    # Punctuation analysis
    punctuation_counts = {
        'commas': text.count(','),
        'periods': text.count('.'),
        'semicolons': text.count(';'),
        'colons': text.count(':'),
        'exclamations': text.count('!'),
        'questions': text.count('?'),
        'dashes': text.count('—') + text.count('--'),
        'parentheses': text.count('(')
    }
    
    # Sentence type analysis
    sentence_types = {
        'declarative': len([s for s in sentences if s.strip().endswith('.')]),
        'interrogative': len([s for s in sentences if s.strip().endswith('?')]),
        'exclamatory': len([s for s in sentences if s.strip().endswith('!')]),
        'imperative': 0  # Would need more sophisticated analysis
    }
    
    # Safe calculations with validation
    unique_words_count = len(set(word.lower() for word in words))
    
    return {
        'word_count': len(words),
        'sentence_count': len(sentences),
        'paragraph_count': len(paragraphs),
        'character_count': len(text),
        'avg_words_per_sentence': round(len(words) / len(sentences), 2) if sentences else 0,
        'avg_sentences_per_paragraph': round(len(sentences) / len(paragraphs), 2) if paragraphs else 0,
        'word_frequency': dict(word_freq.most_common(20)),
        'punctuation_counts': punctuation_counts,
        'sentence_types': sentence_types,
        'unique_words': unique_words_count,
        'lexical_diversity': round(unique_words_count / len(words), 3) if words else 0
    }