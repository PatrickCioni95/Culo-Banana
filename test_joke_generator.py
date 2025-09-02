import joke_generator as jg

def test_joke_contains_keywords():
    words = ["pizza", "gatto", "banca"]
    joke = jg.generate_joke(words)
    for w in words:
        assert w in joke

def test_code_joke_format():
    words = ["pizza", "gatto", "banca"]
    code = jg.generate_code_joke(words)
    for w in words:
        assert w in code
    assert "if" in code and "print" in code
