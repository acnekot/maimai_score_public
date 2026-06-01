# maimai_score — Usage

## Install

```bash
pip install httpx cryptography
```

Place the `.pyd` file in your project directory.

```python
import maimai_score  # auto-loads .pyd
```

Source `.py` not required for distribution.

## API

### fetch(sgwcmaid, proxy=None)

Full player data including comboStatus.

```python
import asyncio
import maimai_score

async def main():
    data = await maimai_score.fetch("SGWCMAID...")

    print(data["player_name"])
    print(data["rating"])
    print(data["play_count"])

    # comboStatus: {(musicId, level): status}  1=FC 2=FC+ 3=AP 4=AP+
    for (mid, lv), cs in data["combo_status"].items():
        label = {1: "FC", 2: "FC+", 3: "AP", 4: "AP+"}.get(cs, "?")
        print(f"musicId={mid} level={lv} {label}")

    for s in data["scores"]:
        print(f"mid={s['musicId']} lv={s['level']} ach={s['achievement']} cs={s['comboStatus']}")

    for c in data["characters"]:
        print(f"id={c['id']} level={c['level']} awakening={c['awakening']}")

    for b in data["b35"]:
        print(f"mid={b['musicId']} lv={b['level']} ach={b['achievement']}")

asyncio.run(main())
```

### fetch_combo_only(sgwcmaid, proxy=None)

ComboStatus map only.

```python
combos = await maimai_score.fetch_combo_only("SGWCMAID...")
# → {(44, 3): 1, (109, 2): 1, (587, 2): 2, ...}
# 1=FC 2=FC+ 3=AP 4=AP+
```

### fetch_scores_only(sgwcmaid, proxy=None)

Score list only.

```python
scores = await maimai_score.fetch_scores_only("SGWCMAID...")
# → [{"musicId": 44, "level": 3, "achievement": 756000, "comboStatus": 0, "deluxscoreMax": 540}, ...]
```

### fetch_scores_hash(uid_encrypted, proxy=None)

Basic scores without comboStatus. No SGWCMAID needed.

```python
scores = await maimai_score.fetch_scores_hash(uid_encrypted)
# → [{"musicId": 44, "level": 3, "achievement": 756000, "deluxscoreMax": 540}, ...]
```

## Response Structure

```python
{
    "user_id": 13196854,
    "player_name": "Player",
    "rating": 13920,
    "icon_id": 458025,
    "trophy_id": 0,
    "nameplate_id": 0,
    "last_play_date": "1970-01-01 00:00:00",
    "play_count": 284,
    "combo_count": 0,

    "scores": [
        {
            "musicId": 44,
            "level": 3,
            "achievement": 756000,
            "comboStatus": 0,
            "deluxscoreMax": 540,
        },
        ...
    ],

    "combo_status": {
        (44, 3): 1,        # 1=FC, 2=FC+, 3=AP, 4=AP+
        (587, 2): 2,
        ...
    },

    "characters": [
        {"id": 101, "level": 141, "awakening": 3},
        ...
    ],

    "b35": [
        {"musicId": 11624, "level": 2, "achievement": 1005812, "romVersion": 23003},
        ...
    ],
    "b15": [...],
    "extend": {"selectMusicId": 11386, "selectDifficultyId": 2, ...}
}
```

## Build

```bash
pip install cython
python setup.py build_ext --inplace
# → maimai_score.cp311-win_amd64.pyd
```
