import random
class OTP:

    def __init__(self, alphabet):
        self.message = ""
        self.key = ""
        self.cipher = ""
        self.partition = 0
        self.encoding = {}
        self.decrypted = ""
        self.decoded = ""
        for letter in alphabet.keys():
            self.encoding[letter] = {}
            self.encoding[letter]["code"] = alphabet[letter]
            self.encoding[letter]["binary"] = bin(alphabet[letter])[2:]
        for letter in alphabet.keys():
            if len(self.encoding[letter]["binary"]) > int(self.partition):
                self.partition = len(self.encoding[letter]["binary"])

    @staticmethod
    def formatString(string, encoder, fill):
        word = ""
        for letter in string:
            word += encoder[letter]["binary"].zfill(fill) + " "
        return word
    def encodeMessage(self, string):
        self.message = self.formatString(string, self.encoding, self.partition)
    def generateKey(self):
        for i in range(len(self.message.split())):
            for _ in range(self.partition):
                self.key += random.choice(["0", "1"])
            self.key += " "
    @staticmethod
    def XOR(bitstring1, bitstring2):
        bitstringlist1 = bitstring1.split()
        bitstringlist2 = bitstring2.split()
        flow = zip(bitstringlist1, bitstringlist2)
        result = []
        for group1, group2 in flow:

            xor_group = "".join(str((int(bit1) + int(bit2)) % 2) for bit1, bit2 in zip(group1, group2))
            result.append(xor_group)
        return " ".join(result)
    def encrypt(self):
        self.cipher = self.XOR(self.message, self.key)
    def decrypt(self):
        self.decrypted = self.XOR(self.cipher, self.key)

    def decode(self):
        decodedMessage = ""
        for item in self.decrypted.split():
            for letter, code in self.encoding.items():
                if item == code["binary"].zfill(self.partition):
                    decodedMessage += letter
                else: pass
        self.decoded = decodedMessage

    def __str__(self):
        return (f"message: {self.message}\n"
                f"key generated: {self.key}\n"
                f"cipher: {self.cipher}\n"
                f"decrypted: {self.decrypted}"
                f"\ndecoded: {self.decoded}")


alphabet = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8,
            'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16,
            'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
            'Z': 25, '.': 26, '!': 27, '?': 28, '(': 29, ')': 30, '-': 31}
def randomMessageGenerator(alphabet, length):
    result = ""
    for _ in range(length):
        result += random.choice(list(alphabet.keys()))
    return result

otp = OTP(alphabet)
message = randomMessageGenerator(alphabet, 190)
otp.encodeMessage(message)
otp.generateKey()
otp.encrypt()
otp.decrypt()
otp.decode()
print(message)
print(otp)