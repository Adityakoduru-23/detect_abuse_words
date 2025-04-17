abusive_words = {'damn', 'hell', 'bastard', 'idiot', 'stupid', 'fool', 'jerk', 'moron', 'crap', 'ass', 'bitch'}
violation_count = 0
MAX_VIOLATIONS = 3

print("Abusive Language Monitor Active")

while True:
    try:
        text = input("\nEnter your message(or 'quit): ")
        if text.lower() == 'quit':
            print("Goodbye!")
            break

        words = text.split()
        filtered = []
        violations = 0

        for word in words:
            cleaned = ''.join(c for c in word if c.isalpha()).lower()
            if cleaned in abusive_words:
                violations += 1
                filtered.append(word.replace(cleaned, '*' * len(cleaned)))
            else:
                filtered.append(word)

        violation_count += violations
        filtered_text = ' '.join(filtered)

        if violation_count >= MAX_VIOLATIONS:
            print("You are banned due to repeated use of abusive language. Message not sent.")
        elif violation_count == MAX_VIOLATIONS - 1:
            print("Warning: Abusive language detected. One more violation will result in a ban.")
            print("Message sent:", filtered_text)
        else:
            print("Message sent:", filtered_text)

    except (EOFError, KeyboardInterrupt):
        print("\nSession ended.")
        break
