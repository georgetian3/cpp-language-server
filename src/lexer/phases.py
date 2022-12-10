

"""
5.2 Phases of translation

3   The source file is decomposed into preprocessing tokens (5.4) and sequences of white-space characters
(including comments). A source file shall not end in a partial preprocessing token or in a partial
comment.7 Each comment is replaced by one space character. New-line characters are retained.
Whether each nonempty sequence of white-space characters other than new-line is retained or replaced
by one space character is unspecified. The process of dividing a source file’s characters into preprocessing
tokens is context-dependent. [Example: See the handling of < within a #include preprocessing directive.
— end example]
"""