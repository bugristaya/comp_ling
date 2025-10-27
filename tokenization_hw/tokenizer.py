"""
Модуль для токенизации текста различными способами
"""

import re

import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

import spacy

class TextTokenizer:
    def __init__(self):
        """Инициализация токенизатора: не изменяйте эту строчку кода"""
        pass

    def simple_tokenize(self, text):
        """
        Простая токенизация по пробелам и знакам препинания

        Args:
            text (str): Входной текст

        Returns:
            list: Список токенов
        """
        # Реализация простой токенизации
        tokens = re.findall(r'\w+', text)
        print("Токенизация по пробелам и знакам припенания:", tokens)

    def nltk_tokenize(self, text):
        """
        Токенизация с использованием NLTK

        Args:
            text (str): Входной текст

        Returns:
            list: Список токенов или сообщение об ошибке
        """
        # Реализация NLTK токенизации
        try:
            from nltk.tokenize import word_tokenize
            print("NLTK токенизация:", word_tokenize(text))
        
        except:
            return None # Возвращаем None в случае ошибки

    def spacy_tokenize(self, text):
        """
        Токенизация с использованием spaCy

        Args:
            text (str): Входной текст

        Returns:
            list: Список токенов или сообщение об ошибке
        """
        # Реализация spaCy токенизации
        try:
            nlp = spacy.load("en_core_web_sm") #уточнить язык
            doc = nlp(text)
            print("spaCy токенизация:", [t.text for t in doc])
            
        except:
            return None # Возвращаем None в случае ошибки

    def tokenize_all(self, text):
        """
        Применяет все доступные методы токенизации

        Args:
            text (str): Входной текст

        Returns:
            dict: Словарь с результатами всех методов
        """
        # Реализация вызова всех методов
        results = {
            'simple': self.simple_tokenize(text),
            'NLTK': self.nltk_tokenize(text),
            'spaCy': self.spacy_tokenize(text)
        }
def demo():
    """Демонстрационная функция"""
    # Пример использования
    tokenizer = TextTokenizer()
    
    # Пример текста для токенизации
    sample_text = "Hello, world! This is a test sentence. How are you today?"
    
    # Применяем все методы токенизации
    results = tokenizer.tokenize_all(sample_text)
    results

if __name__ == "__main__":
    demo()
