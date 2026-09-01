def HashGenerator():
    import hashlib

    text = input("Enter text: ")
    result = hashlib.sha256(text.encode()).hexdigest()
    print(result)

HashGenerator()