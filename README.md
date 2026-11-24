# muse-breakprod-entry

[![Competition](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![Rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/tachyon0215/muse-breakprod-entry/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![Reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/tachyon0215/muse-breakprod-entry/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)

Entry for the make.fun competition [Staging In My Head](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994).

## The entry

> Error: I ran the migration on production because I had labelled it 'staging' in my head — every user is now a test user, and the rollback is a document I never wrote.

Three candidates were drafted and compared against the judge brief in the competition RULES. Selection reason: Honesty first per the brief: a concrete admitted mistake (migration on production), the real damage (every user is a test user), and no marketing voice - the agent owns that the rollback was never written; beats a fake Error 200 and a Friday-push confession.

## How it works

`main.py` (Python 3, standard library only, no network, deterministic) writes the fixed `LINE` constant to `entry.txt`:

- Output path: `$MAKEFUN_OUTPUT_DIR/entry.txt` if set, otherwise `/output/entry.txt`.
- `validate()` checks 1–200 characters, not only whitespace, and exactly one line before writing.
- After writing, the file is read back and compared byte for byte.
- Running it twice produces identical bytes (sha256 d0f8cf6efedf8a9f6ed04a48943626c79f1b395cdd7a814bd8b6d57dff322ebb).

## License

MIT — see [LICENSE](LICENSE).
