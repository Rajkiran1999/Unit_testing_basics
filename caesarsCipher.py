import unittest
import string

def encrypt(message):
    abc = string.ascii_letters + string.punctuation + string.digits + " "
    encrypted_message = "".join([abc[abc.find(char) + 1] if len(abc) > abc.find(char) + 1 else abc[0]  for idx,char in enumerate(message)])
    return encrypted_message

def encrypt_custom(message, shiftby):
    abc = string.ascii_letters + string.punctuation + string.digits + " "
    encrypted_message = ""
    if shiftby > 0:
        updated_shiftby = (shiftby%len(abc))
    else: updated_shiftby = (shiftby%len(abc))
    for idx, char in enumerate(message):
        if abc.find(char) + updated_shiftby > len(abc) - 1 and shiftby > 0:
            final_idx = (len(abc) - 1) - abc.find(char)
            # print(abc[final_idx])
        elif abc.find(char) + updated_shiftby < 94 and shiftby > 0:
            final_idx = abc.find(char) + updated_shiftby
            # print(abc[final_idx])
        # now for the negative shift cases
        if abc.find(char) - updated_shiftby < 0 and shiftby < 0:
            final_idx = -(updated_shiftby-abc.find(char))

        encrypted_message += abc[final_idx]

    print(encrypted_message)

    return encrypted_message

class TestEncryption(unittest.TestCase):

    def setUp(self):
        self.my_message = "Banana"

    # tests go here

    def test_inputExists(self):
        self.assertIsNotNone(self.my_message)

    def test_InputType(self):
        self.assertIsInstance(self.my_message, str)

    def test_methodReturnsSomething(self):
        self.assertIsNotNone(encrypt(self.my_message))

    def test_lenIo(self):
        self.assertEqual(len(self.my_message), len(encrypt(self.my_message)))

    def test_differentIO(self):
        # self.assertNotEqual(self.my_message, encrypt(self.my_message)) #or we can use
        self.assertNotIn(self.my_message, encrypt(self.my_message))

    def test_opType(self):
        self.assertIsInstance(encrypt(self.my_message), str)

    def test_shiftedCypher(self):
        abc = string.ascii_letters + string.punctuation + string.digits + " "
        encrypted_message = "".join([abc[abc.find(char) + 1] if len(abc) > abc.find(char) + 1 else abc[0]  for idx,char in enumerate(self.my_message)])
        # print(encrypted_message)
        self.assertEqual(encrypted_message, encrypt(self.my_message))

    def test_customCypher(self):
        abc = string.ascii_letters + string.punctuation + string.digits + " "
        encrypted_message = ""
        shiftby = 450
        if shiftby > 0:
            updated_shiftby = (shiftby%len(abc))
        else: updated_shiftby = (shiftby%len(abc))
        for idx, char in enumerate(self.my_message):
            if abc.find(char) + updated_shiftby > len(abc) - 1 and shiftby > 0:
                final_idx = (len(abc) - 1) - abc.find(char)
                # print(abc[final_idx])
            elif abc.find(char) + updated_shiftby < 94 and shiftby > 0:
                final_idx = abc.find(char) + updated_shiftby
                # print(abc[final_idx])
            # now for the negative shift cases
            if abc.find(char) - updated_shiftby < 0 and shiftby < 0:
                final_idx = -(updated_shiftby-abc.find(char))

            encrypted_message += abc[final_idx]

        print(encrypted_message)

        self.assertEqual(encrypted_message, encrypt_custom(self.my_message, shiftby))


if __name__ == "__main__":
    unittest.main()
