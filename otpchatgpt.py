import random
class OTP:
    def __init__(self, alphabet):
        self.encoding = {}
        self.message = ""
        self.key = ""
        self.cipher = ""
        self.partition = 0

        # Build encoding dictionary and determine max binary length
        for letter in alphabet.keys():
            self.encoding[letter] = {
                "code": alphabet[letter],
                "binary": str(bin(alphabet[letter])[2:])
            }
        # Find the maximum binary length for padding (partition size)
        self.partition = max(len(data["binary"]) for data in self.encoding.values())

    @staticmethod
    def formatString(string, encoder, fill):
        word = ""
        for letter in string:
            word += encoder[letter]["binary"].zfill(fill) + " "
        return word.strip()

    def encodeMessage(self, string):
        self.message = self.formatString(string, self.encoding, self.partition)

    def generateKey(self):
        key_bits = [
            str(random.choice([0, 1])) for _ in range(len(self.message.replace(" ", "")))
        ]
        self.key = "".join(key_bits)

# Example usage
alphabet = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8,
            'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16,
            'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
            'Z': 25, '.': 26, '!': 27, '?': 28, '(': 29, ')': 30, '-': 31}

otp = OTP(alphabet)
otp.encodeMessage("ABCD")
otp.generateKey()

print(f"Formatted Message: {otp.message}")
print(f"Generated Key: {otp.key}")
