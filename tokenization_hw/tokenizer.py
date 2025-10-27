"""
Модуль для токенизации текста различными способами
"""

import re

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
        tokens = re.findall(r'\w+', text) # Токенизируем по пробелам и знакам препинания 
        return tokens  # Возвращаем токены 

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
            from nltk.tokenize import word_tokenize # Импортируем модуль для токенизации по словам
            tokens_nlkt = word_tokenize(text) # Токенизируем с помомщью NLTK
            return tokens_nlkt # Возвращаем токены
        
        except ImportError: 
            print("Ошибка: NLTK не установлен.") # Ошибка, если библиотека не установлена 
            return None

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
            import spacy # Импортируем модуль
            nlp = spacy.load("en_core_web_sm") 
            doc = nlp(text) # Обрабатываем текст с помощью Spacy 
            tokens_sp = [t.text for t in doc] # Токенизируем 
            return tokens_sp # Возвращаем торины
            
        except ImportError:
            print("Ошибка: spaCy не установлен.") # Ошибка, если библиотека не установлена 
            return None

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
        } # Cоставляем словарь со всеми методами токенизации и соответвующими токенами 

        return results 

def demo():
    """Демонстрационная функция"""
    # Пример использования
    tokenizer = TextTokenizer()
    
    # Пример текста для токенизации
    sample_text = "Hello, world! This is a test sentence. How are you today?"
    print(f"Демонстрационный вариант")
    print(f"Исходный текст: {sample_text}")
    
    
    # Применяем все методы токенизации
    results = tokenizer.tokenize_all(sample_text)
    
    for method, tokens in results.items():
        print(f"{method}: {tokens}") 

if __name__ == "__main__":
    demo()
