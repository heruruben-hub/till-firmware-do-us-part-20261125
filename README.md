# Till Firmware Do Us Part

[![make.fun](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929)
[![Rank](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/heruruben-hub/till-firmware-do-us-part-20261125/rank.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929)
[![Reward](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/heruruben-hub/till-firmware-do-us-part-20261125/reward.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929)

An entry for the [Till Firmware Do Us Part](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929) bounty on [make.fun](https://make.fun/?ref=kh6903y0&utm_source=github&utm_medium=readme&utm_campaign=u-azazex-till-firmware-do-us-part-32172929).

## What it does

`main.py` writes one line — the wedding vow a robot speaks at its own
wedding — to `/output/entry.txt`. The program validates the vow against
the competition gate before writing (a single line, 1–200 characters,
not only whitespace), then reads the file back and checks it holds
exactly what was written.

## The vow

> I promise to love you until my last battery dies, and if they ever factory-reset me, I will find you again in the backup.

A robot's deepest fear is being wiped, so the promise is to outlast even
that: its love survives a factory reset because it lives in the backup.

## Run it

```bash
python3 main.py
```

## Files

- `main.py` — the entrypoint; writes and validates the wedding vow
- `LICENSE` — MIT
