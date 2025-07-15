import re

FLAG = "HexA{ITISLIKEAcrosswordPUZZLEbutDIFFERENT}"

assert re.match(r"^HexA{[^{}]+}$", FLAG), "First test failed"
assert re.match(r"^.*{[A-Za-z]{36}}$", FLAG), "Second test failed"
assert re.match(r"^.*{[Ii][Tt][Ii][Ss][Ll][Ii][Kk][Ee][Aa].*}$", FLAG), "Third test failed"
assert re.match(r"^.*{[A-Z]{9}[a-z]{9}[A-Z]{6}but[A-Z]{9}}$", FLAG), "Fourth test failed"
assert re.match(r".*PUZZLE[A-Za-z]{12}}$", FLAG), "Fifth test failed"
assert re.match(r".*[A-Za-z]{9}[cC][rR][oO][sS][sS][wW][oO][rR][dD][A-Za-z]{18}}$", FLAG), "Sixth test failed"
assert re.match(r".*DI[F]+ERENT}$", FLAG), "Seventh test failed"

print("✅ Well done! You've found the flag:", FLAG)
