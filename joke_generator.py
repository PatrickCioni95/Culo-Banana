import argparse
import random

def generate_joke(keywords):
    """Generate a simple joke using given keywords."""
    words = (keywords + ["..."])[:3]
    w1, w2, w3 = words
    templates = [
        f"Un {w1} e un {w2} entrarono in una {w3}. Il barista chiese: 'È una barzelletta o un esperimento?'",
        f"C'era una volta un {w1} che voleva una {w3}. Gli dissero di chiedere al {w2}, ma lui rispose: 'Preferisco una pizza!'",
        f"Perché il {w1} portò un {w2} nella {w3}? Perché sperava di trovare l'ingrediente segreto!",
    ]
    return random.choice(templates)

def generate_code_joke(keywords):
    """Generate a pseudo-programming joke using keywords."""
    words = (keywords + ["..."])[:3]
    w1, w2, w3 = words
    return (
        f"if {w1} == '{w2}':\n"
        f"    print('Miagola in {w3}!')\n"
        f"else:\n"
        f"    print('Meglio una {w1} che un {w2}!')"
    )


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Generatore di barzellette")
    parser.add_argument("--keywords", nargs="+", help="Parole chiave per la barzelletta")
    parser.add_argument("--mode", choices=["normale", "codice"], help="Modalità della barzelletta")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    keywords = args.keywords
    if not keywords:
        raw = input("Inserisci 2-3 parole chiave separate da virgola: ")
        keywords = [w.strip() for w in raw.split(',') if w.strip()]
    mode = args.mode
    if not mode:
        mode = input("Modalità (normale/codice): ").strip().lower()
    else:
        mode = mode.lower()
    if mode.startswith('c'):
        print(generate_code_joke(keywords))
    else:
        print(generate_joke(keywords))


if __name__ == "__main__":
    main()
