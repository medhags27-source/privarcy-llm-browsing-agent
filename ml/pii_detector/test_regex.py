from regex_detector import detect_pii


text = """
My name is Ananya.
My email is ananya@example.com.
My phone number is +919876543210.
My card number is 4111 1111 1111 1111.
My Aadhaar number is 1234 5678 9012.
"""


print("Input text:")
print(text)

print("\nDetected PII:")

results = detect_pii(text)

for result in results:
    print(result)