from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def main() -> int:
    failures: list[str] = []
    checked = 0

    for document in sorted(ROOT.rglob("*.md")):
        text = document.read_text(encoding="utf-8")
        for raw_target in LINK.findall(text):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue

            relative_target = unquote(target.split("#", 1)[0])
            resolved = (document.parent / relative_target).resolve()
            checked += 1

            if not resolved.is_relative_to(ROOT):
                failures.append(
                    f"{document.relative_to(ROOT)}: link escapes repository: {target}"
                )
            elif not resolved.exists():
                failures.append(
                    f"{document.relative_to(ROOT)}: missing local target: {target}"
                )

    if failures:
        print("Documentation validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"Documentation validation passed: {checked} local links checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
