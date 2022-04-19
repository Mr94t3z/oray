import pyae
from termcolor import colored

print(colored("\nKhoirul Ummam (1197050059)\nMuhammad Taopik (1197050081)", "blue"))

for isi in range(1, 5):

    original_msg = None
    original_msg = input("\nInputan dari user: ")
    print("\n[ Hasil inputan user ke -", isi, "]")

    frequency_table = {}

    for i in original_msg:
        if i in frequency_table:
            frequency_table[i] += 1
        else:
            frequency_table[i] = 1

    AE = pyae.ArithmeticEncoding(frequency_table=frequency_table,
                                 save_stages=True)

    print("Original Message: {msg}".format(msg=original_msg))

    encoded_msg, encoder, interval_min_value, interval_max_value = AE.encode(msg=original_msg,
                                                                             probability_table=AE.probability_table)
    print("Encoded Message: {msg}".format(msg=encoded_msg))

    binary_code, encoder_binary = AE.encode_binary(
        float_interval_min=interval_min_value, float_interval_max=interval_max_value)
    print("The binary code is: {binary_code}".format(binary_code=binary_code))

    decoded_msg, decoder = AE.decode(encoded_msg=encoded_msg,
                                     msg_length=len(original_msg),
                                     probability_table=AE.probability_table)
    print("Decoded Message: {msg}".format(msg=decoded_msg))

    decoded_msg = "".join(decoded_msg)
    print("Message Decoded Successfully? {result}".format(
        result=original_msg == decoded_msg))
isi+1
