## Switches, Conventions, and Encodings

1. Computer store the data using bits: 0 or 1.
2. Byte contains a sequence of 8 bits.
3. Convert the bytes to the text by encoding, which is a kind of mapping from the number to the letters.
   And the most important one is ASCII.
4. But the ASCII has one problem is that it only encodes English.
5. Unicode: you can use the 32 bits number to encode a Unicode character.
6. But there are lots of white spaces wasted. So we use utf-8 and which make the character represented by the 8 bits and then escaped    out into 16 or 32 bits as needed.
7. utf-8:  Unicode Transformation Format 8 Bits.
8. b'' to tell Python this is ”bytes”.
9. In Python a string is a UTF-8 encoded sequence of characters for displaying or working with text.
10. Use .decode() to get the string from the raw bytes.
11. Use .encode() to get the bytes from the string.
12. "DBES": Decode Bytes Encode String
