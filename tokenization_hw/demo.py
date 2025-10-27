from tokenizer import TextTokenizer

def main():
    tokenizer = TextTokenizer()

    # Пример текста для токенизации
    sample_text = "Hello, world! This is a test sentence. How are you today?"

    # Применяем все методы токенизации
    results = tokenizer.tokenize_all(sample_text)

    # Выводим результаты
    for method, tokens in results.items():
        print(f"{method}: {tokens}")

if __name__ == "__main__":
    main()
