I was bored and made an AST-transformer based deobfuscator for some malware
which is said to have been obfuscated with https://github.com/Blank-c/BlankOBF
Note that I haven't looked at all at BlankOBF, just played with this malware.

*Gynvael Coldwind (Dec'23)*

#### Example

This is `example.txt` before deobfuscation (which actually is obfuscated Python
source code; it was stage 2 in the malware I looked at):

```py
# Obfuscated code.
____ = "somebase64"
_____ = "morebase64"
______ = "yetagainbase64"
_______ = "yesitsbase64"
__import__(getattr(__import__(bytes([98, 97, 115, 101, 54, 52]).decode()), bytes([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(bytes([89, 110, 86, 112, 98, 72, 82, 112, 98, 110, 77, 61])).decode()).exec(__import__(getattr(__import__(bytes([98, 97, 115, 101, 54, 52]).decode()), bytes([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(bytes([98, 87, 70, 121, 99, 50, 104, 104, 98, 65, 61, 61])).decode()).loads(__import__(getattr(__import__(bytes([98, 97, 115, 101, 54, 52]).decode()), bytes([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(bytes([89, 109, 70, 122, 90, 84, 89, 48])).decode()).b64decode(__import__(getattr(__import__(bytes([98, 97, 115, 101, 54, 52]).decode()), bytes([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(bytes([89, 50, 57, 107, 90, 87, 78, 122])).decode()).decode(____, __import__(getattr(__import__(bytes([98, 97, 115, 101, 54, 52]).decode()), bytes([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(bytes([89, 109, 70, 122, 90, 84, 89, 48])).decode()).b64decode("cm90MTM=").decode())+_____+______[::-1]+_______)))
```

And this is the output of the partial deobfuscator:

```py
# Transformation iteration 1
# Transformation iteration 2
# Transformation iteration 3
# Transformation iteration 4
____ = 'somebase64'
_____ = 'morebase64'
______ = 'yetagainbase64'
_______ = 'yesitsbase64'
exec(marshal.loads(base64.b64decode(codecs.decode(____, 'rot13') + _____ + ______[::-1] + _______)))
```
