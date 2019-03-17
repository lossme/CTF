import re


class Morse():
    BLANK_PATTERN = re.compile(r"\s")
    DECODE_MAP = {
        '.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..': 'D',
        '.': 'E',
        '..-.': 'F',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---': 'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z',
        '.----': '1',
        '..---': '2',
        '...--': '3',
        '....-': '4',
        '.....': '5',
        '-....': '6',
        '--...': '7',
        '---..': '8',
        '----.': '9',
        '-----': '0',
        '..--..': '?',
        '-..-.': '/',
        '-.--.-': '()',
        '-....-': '-',
        '.-.-.-': '.'
    }

    ENCODE_MAP = {v: k for k, v in DECODE_MAP.items()}

    @classmethod
    def decode(cls, message, sep=None):
        return "".join(
            map(
                lambda x: cls.DECODE_MAP.get(x, x), message.split(sep)
            )
        )

    @classmethod
    def encode(cls, message):
        s = message.upper()
        s = cls.BLANK_PATTERN.sub("", s)
        return " ".join(
            map(
                lambda x: cls.ENCODE_MAP.get(x, x), s
            )
        )


def test():
    message = "i love aylin"

    r = Morse.encode(message)
    print("密文: {}".format(r))

    r = Morse.decode(r)
    print("明文: {}".format(r))


if __name__ == '__main__':
    test()
