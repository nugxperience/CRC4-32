"""
CRC4-32

CRC-32 is slow: "... most of our CPU time (~10%) was spent ... in a function called crc32() ..."
https://fastmail.blog/2015/12/03/the-search-for-a-faster-crc32/

RC4 is fast: "... remarkable for its simplicity and speed ..."
https://en.wikipedia.org/wiki/RC4
"""
from Crypto.Cipher import ARC4
import struct

CRC432 =  b'zmQaNTV3z8yA7BSpqZiOIQCxtSiBI0ZghJzEsV3wuV1G8NwSyz6PIF18zqQnGr9B'
CRC432 += b'lYjDonKivBhH69JKhPrLHnO8ld3pavCUVPSXctHmVfax4mHDuqjT80m7uq9Gnhem'
CRC432 += b'tAbsHj5vz3noZevFu4WyqPEKzpitvuakzuNLMSDvzxTZ5mh6z8fitMZuzmFNMOZd'
CRC432 += b't0Fdobissl1D2NIPvOI0ywX1yn495TGHwHA50WmasVrbWy0xsAr1vbxiqZgzlrBA'
CRC432 += b'zqbZNtuKs6K1YNzdzRLxQVwEsUX9YSwpvIHaGJrRlu2oQx5CsJcRSigmvByUHnzR'
CRC432 += b't6w1jl5PsRZ6fDvkz340LZOqvYUHuVJlzTPw4gdun1HwBkmGtEZ6K2viuBCWASUP'
CRC432 += b'sRKpCuH9zWksAUwdzZmyrBYswAZGNdSJtTyXFMnvubOtlR0Uuj4EzQrvzqQkng92'
CRC432 += b'zyOg3lpKtIRCM1VHhfAZg3oBodZF3VWPifyxevHDvOjTE3WlzpiNXjSOuCOMdvsD'
CRC432 += b'zqQAPr5dzqfxP7BVsgOF2j7mfPXkjDS3vCEwg25MzfeL5362tGqACdjsuCvIWxZm'
CRC432 += b'vypFn2G4wuIQ8dcbyu4mUgEvpfY1HoS6vNCUmGcsRDQMyOVKo0tPw2KCwKhqczla'
CRC432 += b'uCq9WocUysVxKnUbzd2PMOhYzqeLsGPjuYt4ALwDzmQfw9SKsJ8qLuOxwogeENzB'
CRC432 += b'suC5otJvzqEmknbKziOb3oHuuVZCtQ0Dz8nYIwvuzyJwb5lKl4eTavJDu3SRmAbh'
CRC432 += b'zcLNRw52z8LsTIpKtOjY9cPenvhASc0JpB4fPz8yhrjqdOiEuZGWgwxFtuhEcvon'
CRC432 += b'zsnNFAbptAvoPBGZs6Z3yLxJweREXY0VuvZBKAnbzqbmVIAGoZqSeVFTZuVRDN6r'
CRC432 += b'zqLTZmSsuNzH09iTwoHGNxP7oNUS724RytodRUg7uBbt4Rd7yYSc9mUTs6FyI2db'
CRC432 += b'z1xtSO6azqEWfFAShqcgrBbiutTl0LvJyzliqXBHz0aknCA7tIwzgOoYw9gDU5Sk'
CRC432 += b'wUGyXrSBzWfim8vIuVbEhLIcvuFgzGrlf1Fgphu5yoSlq5a1kx5CgmnFtRlZMrfN'
CRC432 += b'tKbqx05Ju1WXAkmvyzNS9L2Ftd1l950KhEm8IPdvvBiuFzGPzfsU36vuceZjmlx9'
CRC432 += b'njsLtQBWmHxiB37ezLeBvwYUvUFLaksrw9uyidqWsE2rQ95WsMw2LNHxzQekM49j'
CRC432 += b'w6eHGfkFubFM8RmHsVjeopb0mAGBbkvuz0FAHBSKzoclSsU4z90g8IAEp4tqKxeV'
CRC432 += b'z3GEYOCpzfdTghuAzLTMrIakukHw1Xqsvd8yUFa7sfzdbGxmtQCTbxP8yzOjinbM'
CRC432 += b'lsLi1kaEzq1MmtunuEWt5YxpspvMnHIYbU8i3qpPu6qzEgm2oQZYUza9zcQkJRgb'
CRC432 += b'tQZuzFNLzsof6maCsrQJ9uIxzqp0cysut4f3l0q2yVAmPQ2FtER7IlkroOiDNI0k'
CRC432 += b'yuxc04QDvOTEHcJWldL543xEvh0HuqtlvDIhUnzlzEfesTlvmyj5bJZqoOjDhf41'
CRC432 += b'pkXJKxMFzfRg9lSpvUua2tGAuZOKWQNDtARz1m5qqLyJU43SuMGLTS8bzE1eRr4j'
CRC432 += b'uq3OGiInniPb6tEal5ZAevYGqcFtIV3pqmyESUPazCNXrOKapNPX9nOxzfT5iytG'
CRC432 += b'tT62Ym3ZzWqfbTS8prqwOGcVs8VDW2nJvEHupF65sty5gLzWuy1qjQIst4ywlNkW'
CRC432 += b'twujYlNou2aM9dwruJU4RAb1zXQeiG4KtADFmYckvDp673tGzLx20S8AzZXBuIEK'
CRC432 += b'zmcWLGJbu7DfCAnjviQh6e2KqHi64FJ7zdQCgjwUlFLXC1zdqZmy6STKh5T2vxiN'
CRC432 += b'u2FKTWhru3ZWUi5mzWLFCJAxsYNrUkM1zekYr452zXWnZwBKzqPciMOGzWpoZvUu'
CRC432 += b's6ZFhKoatGJpKda8q8JOZodptm6KnojNsj9QVHAKuVjGE5NwuNzx6woZpLwOSi7C'
CRC432 += b'tVEfhxcKsTfw2lW3spGWLA2Jplkbox7ysRgDzNbmmhpWGNorsf5yWKv6t67uNcCZ'

def rc4(key, data):
    """
    RC4 encrypt data.
    """
    return ARC4.new(b'CRC432:' + key).encrypt(data)

def crc432(data):
    """
    Compute CRC-32 using RC4 for speed.
    """
    checksum = rc4(b'82hlUyXE', b'\x00'*4)
    for byte in data:
        offset = (checksum[0] ^ byte) * 8
        key = CRC432[offset:offset+8]
        checksum = rc4(key, checksum[1:] + b'\x00')
    checksum =  rc4(b'Bu9NnHI6', checksum)
    return struct.unpack('<I', checksum)[0]

if __name__ == '__main__':
    print(hex(crc432(b'123456789')))
