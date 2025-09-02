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


def test_parse_args():
    args = jg.parse_args(["--keywords", "pizza", "gatto", "banca", "--mode", "codice"])
    assert args.keywords == ["pizza", "gatto", "banca"]
    assert args.mode == "codice"


def test_main_uses_args(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: (_ for _ in ()).throw(AssertionError("input should not be called")))
    jg.main(["--keywords", "pizza", "gatto", "banca", "--mode", "codice"])
    out = capsys.readouterr().out
    assert "if" in out and "pizza" in out


def test_main_fallback(monkeypatch, capsys):
    inputs = iter(["pizza, gatto, banca", "codice"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    jg.main([])
    out = capsys.readouterr().out
    assert "if" in out and "pizza" in out
