#!/usr/bin/env python3
import re
import json
import hashlib

# Fill in the function below using regular expressions.
def parse(s):
    args = []
    pattern = re.compile(r'''
        \s*                             # Skip leading whitespace
        (                              # Capture group for:
          "(                           #   Start quoted argument
            (?:                        #   Content inside quotes:
              \\[nt"\\]                #     valid escape sequences
              |                        #     or non-escape characters
              [^"\\]
            )*
          )"                           #   End of quoted argument
          |                            # OR
          (\S+)                        # Unquoted argument (non-whitespace)
        )
    ''', re.VERBOSE)

    pos = 0
    while pos < len(s):
        m = pattern.match(s, pos)
        if not m:
            return False

        quoted = m.group(2)
        unquoted = m.group(3)

        if quoted is not None:
            result = []
            i = 0
            while i < len(quoted):
                if quoted[i] == '\\':
                    if i + 1 >= len(quoted):
                        return False
                    esc = quoted[i + 1]
                    if esc == 'n':
                        result.append('\n')
                    elif esc == 't':
                        result.append('\t')
                    elif esc == '"':
                        result.append('"')
                    elif esc == '\\':
                        result.append('\\')
                    else:
                        return False
                    i += 2
                else:
                    result.append(quoted[i])
                    i += 1
            args.append(''.join(result))
        else:
            args.append(unquoted)

        pos = m.end()

    return args


# -----------------------------------------------------------------------------
# Testing code.

func = parse
final_results = []
for args, expected_result in [
  (('Very Simple Test',),                ['Very', 'Simple', 'Test']),
  (('"Hello, world!"',),                 ['Hello, world!']),
  (('"Hello, \\"world\\"!"',),           ['Hello, "world"!']),
  (('Arg1 "This is argument two" Arg3',),['Arg1', 'This is argument two', 'Arg3']),
  (('   Arg1     Arg2          Arg3    ',), ['Arg1', 'Arg2', 'Arg3']),
  ((r'"\n\t\"\\"',),                     ['\n\t"\\']),  # Escaped quotes.
  (('"Ending too soon',),               False),
  (('"Ending too soon\\',),             False),
  ((r'-c -v "--comment=Report generator\nVersion: 1.17" --output=report.odt',), None),
  ((r'"--error-handling=return-false',), None),
  ((r'-AkvV  "seek:17:write:10:A" "--input=file template.bin" "--output=file rendered.bin"',), None),
]:
    actual_result = func(*args)
    final_results.append(actual_result)
    if expected_result is not None:
        print(f"Testing {args}: ", end="")
        if actual_result == expected_result:
            print("GOOD!")
        else:
            print(f"Wrong! Expected result: {expected_result}, Actual result: {actual_result}")
    else:
        print(f"Running main test {args}...")

# Flag decoding logic
tmp = json.dumps(final_results)
hash = hashlib.sha512(tmp.encode()).digest()

GOOD_HASH = "84f4244827ef3a381bfe30c83b56b3dbce30c07a"
ENC_FLAG = (
    "cb552bedaa6992501fc81425ae0de62ef612e0207265"
    "5604863d297aefec8aa70c6bd3aaf9b908777f6b96b5"
)

if hash[:20].hex() == GOOD_HASH:
    print("Congrats! Here's the flag:")
    flag = bytes([f ^ h for f, h in zip(bytes.fromhex(ENC_FLAG), hash[20:])])
    print(flag.decode().strip())
else:
    print("One or more results were wrong!")
