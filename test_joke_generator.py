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


def test_main_invalid_keywords(monkeypatch, capsys):
    inputs = iter(["pizza", "pizza,gatto", "normale"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    jg.main()
    captured = capsys.readouterr().out
    assert "Per favore inserisci almeno due parole chiave." in captured
    assert "pizza" in captured and "gatto" in captured


def test_main_invalid_mode(monkeypatch, capsys):
    inputs = iter(["pizza,gatto", "pippo", "codice"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    jg.main()
    captured = capsys.readouterr().out
    assert "Modalità non valida" in captured
    assert "if" in captured
