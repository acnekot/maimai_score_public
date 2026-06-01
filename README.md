# maimai_score

Retrieves maimai DX player data including comboStatus (FC/AP), ratings, characters, and more.

No game client or arcade hardware required.

## Install

```bash
pip install httpx cryptography
```

Place the `.pyd` file in your project directory.

## Quick Start

```python
import asyncio
import maimai_score

async def main():
    data = await maimai_score.fetch("SGWCMAID...")

    print(data["player_name"])   # player name
    print(data["rating"])        # rating

    # comboStatus: {(musicId, level): status}  1=FC 2=FC+ 3=AP 4=AP+
    for (mid, lv), cs in data["combo_status"].items():
        label = {1: "FC", 2: "FC+", 3: "AP", 4: "AP+"}[cs]
        print(f"musicId={mid} level={lv} {label}")

asyncio.run(main())
```

## API

| Function | SGWCMAID | Returns |
|----------|:---:|---------|
| `fetch(sgwcmaid)` | Yes | Full player data |
| `fetch_combo_only(sgwcmaid)` | Yes | `{(mid,lv): comboStatus}` |
| `fetch_scores_only(sgwcmaid)` | Yes | Score list with comboStatus |
| `fetch_scores_hash(uid_encrypted)` | No | Score list without comboStatus |

See `USAGE.md` for full API documentation.

## Response Structure

```python
{
    "user_id": 13196854,
    "player_name": "Player",
    "rating": 13920,
    "play_count": 284,

    "scores": [
        {"musicId": 44, "level": 3, "achievement": 756000,
         "comboStatus": 0, "deluxscoreMax": 540},
    ],

    "combo_status": {(44, 3): 1, (587, 2): 2},  # 1=FC 2=FC+ 3=AP 4=AP+

    "characters": [
        {"id": 101, "level": 141, "awakening": 3},
    ],

    "b35": [{"musicId": 11624, "level": 2, "achievement": 1005812}],
    "b15": [...],

    "extend": {"selectMusicId": 11386, "selectDifficultyId": 2, ...}
}
```

## Requirements

- Python 3.11+
- httpx
- cryptography

## License

Proprietary — All rights reserved. Unauthorized distribution prohibited.
