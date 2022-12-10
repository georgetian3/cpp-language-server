from .utils import read_lines

"""
5.11 Keywords

1   The identifiers shown in Table 5 are reserved for use as keywords (that is, they are unconditionally treated as keywords in phase 7) except in an attribute-token (9.12.1). [Note: The register keyword is unused but is reserved for future use. — end note]
"""

keywords = {
    keyword: keyword.upper() for keyword in read_lines(__file__, 'keywords.txt')
}


if __name__ == '__main__':
    print(keywords)