# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/Tokocrypto96/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/Tokocrypto96/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

Engine catur Python untuk kompetisi [make.fun — tiny-chess-01](https://make.fun/bounty/tiny-chess-01): bangun engine catur terkuat dalam ≤ 4 KB Python.

## Cara kerja

- Papan 0x88, skor inkremental dengan piece-square tables (Michniewski).
- Pencarian: iterative deepening + alpha-beta + PVS, transposition table,
  null-move pruning, LMR, killer/history move ordering, quiescence search.
- Budget 200.000 node per langkah, deterministik (tanpa jam, tanpa acak).
- Berkomunikasi dengan harness lewat `MAKEFUN_ENV_URL` (`/game`, `/move`).

## Ukuran

`main.py` (4.033 byte) adalah payload lzma dari source engine (7,3 KB)
yang di-unpack saat jalan — cara yang sama seperti baseline house
(sunfish 4k, 3.649 byte, juga lzma payload + unpacker, lihat
`competition.yaml` kit). Semua logika tetap Python stdlib saja.

## Lisensi

MIT — lihat `LICENSE`.
