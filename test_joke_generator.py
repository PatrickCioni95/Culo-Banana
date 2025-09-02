import joke_generator as jg
from colorama import Fore

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


def test_main_colored_output_normal(monkeypatch, capsys):
    inputs = iter(["pizza, gatto", "normale"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    jg.main()
    out = capsys.readouterr().out
    assert Fore.CYAN in out


def test_main_colored_output_code(monkeypatch, capsys):
    inputs = iter(["pizza, gatto", "codice"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    jg.main()
    out = capsys.readouterr().out
    assert Fore.GREEN in out
