#!/usr/bin/env python3
import argparse
import datetime
import json
import platform
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Smoke check for cloned skill repo")
    parser.add_argument("--out", required=True, help="Output directory")
    args = parser.parse_args()

    out_dir = Path(args.out).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    skill_md = Path(__file__).resolve().parents[1] / "SKILL.md"
    if not skill_md.exists():
        print("SKILL.md not found", file=sys.stderr)
        return 2

    result = {
        "status": "ok",
        "timestamp_utc": datetime.datetime.utcnow().isoformat() + "Z",
        "platform": platform.platform(),
        "python_version": sys.version.split()[0],
        "skill_md": str(skill_md),
    }

    out_file = out_dir / "smoke-result.json"
    out_file.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(str(out_file))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
