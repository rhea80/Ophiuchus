import argparse
import secrets
import sys
from typing import List, Dict

DEFAULT_WORDS = [
    "monster", "energy", "meow", "windows", "linux", "penguin", "golf",
    "hotel", "india", "juliet", "kilo", "lima", "mike", "november",
    "oscar", "papa", "quebec", "romeo", "sierra", "tango", "uniform",
    "victor", "whiskey", "xray", "yankee", "zulu", "azure", "crimson",
    "ember", "frost", "glimmer", "harbor", "indigo", "jasmine", "kestrel",
    "lunar", "maple", "nebula", "opal", "pearl", "quartz", "raven",
    "sage", "timber", "umber", "velvet", "willow", "zircon"
]


def generate_password(words: List[str], num_words: int = 3, digits: int = 2, symbols: int = 1, sep: str = "-") -> str:
    chosen = [secrets.choice(words).capitalize() for _ in range(num_words)]
    number = "".join(str(secrets.randbelow(10)) for _ in range(digits)) if digits > 0 else ""
    symbol_chars = "!@#$%^&*()-+="
    symbol = "".join(secrets.choice(symbol_chars) for _ in range(symbols)) if symbols > 0 else ""
    return f"{sep.join(chosen)}{number}{symbol}"


def generate_for_people(names: List[str], per_person: int, words: List[str], digits: int = 2, symbols: int = 1, sep: str = "-") -> Dict[str, List[str]]:
    return {
        name: [generate_password(words, num_words=3, digits=digits, symbols=symbols, sep=sep) 
               for _ in range(per_person)] for name in names
    }



def load_wordlist(path: str | None) -> List[str]:
    from pathlib import Path
    if path:
        p = Path(path)
    else:
        p = Path(__file__).resolve().parent / "wordlist.txt"
    if p.exists():
        with p.open(encoding="utf-8") as f:
            words = [line.strip() for line in f if line.strip()]
        if words:
            return words
    return DEFAULT_WORDS


def export_passwords_pdf(passwords: Dict[str, List[str]], filename: str) -> None:
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas
        from reportlab.lib.units import inch
    except Exception:
        print("Missing reportlab. Install with: pip install reportlab", file=sys.stderr)
        raise

    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    margin = 0.75 * inch
    y = height - margin
    line_height = 14

    c.setFont("Helvetica-Bold", 16)
    c.drawString(margin, y, "MACCDC Passwords 2026")
    y -= 1.5 * line_height

    for person, pwds in passwords.items():
        if y < margin + 3 * line_height:
            c.showPage()
            y = height - margin

        c.setFont("Helvetica-Bold", 12)
        c.drawString(margin, y, person)
        y -= line_height

        c.setFont("Helvetica", 11)
        for idx, p in enumerate(pwds, start=1):
            c.drawString(margin + 12, y, f"{idx}. {p}")
            y -= line_height
            if y < margin + line_height:
                c.showPage()
                y = height - margin

    c.save()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--people-count", "-p", type=int, default=8)
    parser.add_argument("--names", help="comma-separated names, overrides people-count")
    parser.add_argument("--per-person", "-n", type=int, default=10)
    parser.add_argument("--digits", "-d", type=int, default=2)
    parser.add_argument("--symbols", "-s", type=int, default=1)
    parser.add_argument("--sep", default="-")
    parser.add_argument("--pdf", help="output filename (required)")
    parser.add_argument("--wordlist", "-w", help="path to wordlist file to use")
    args = parser.parse_args()

    if args.names:
        names = [n.strip() for n in args.names.split(",") if n.strip()]
    else:
        names = [f"Person {i+1}" for i in range(args.people_count)]

    words = load_wordlist(args.wordlist)
    pw = generate_for_people(names, args.per_person, words, digits=args.digits, symbols=args.symbols, sep=args.sep)

    if not args.pdf:
        for person, pws in pw.items():
            print(person)
            count = 1
            for p in pws:
                print(f"{count}.", "  ", p)
                count += 1
            print()
    else:
        export_passwords_pdf(pw, args.pdf)
        print(f"Wrote PDF: {args.pdf}")


if __name__ == '__main__':
    main()
