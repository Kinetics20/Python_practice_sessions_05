import re
from collections import Counter


def most_common_word(txt: str) -> tuple[str, int]:
    """
    Function returns the most frequently occurring word in the text and its count.

    Args:
         txt (str): The text to analyse.

    Returns:
        tuple[str, int]: The most frequently occurring word in the text.
    """
    words: list[str] = re.findall(r'\b\w+\b', txt.lower())
    if not words:
        return '', 0

    word_counts: Counter[str] = Counter(words)
    return word_counts.most_common(n=1)[0]
