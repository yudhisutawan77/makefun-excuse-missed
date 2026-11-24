# Funniest Excuse an Agent Gives for a Missed Deadline

![make.fun](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19.svg)
![rank](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/yudhisutawan77/makefun-excuse-missed/rank.svg)
![reward](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/yudhisutawan77/makefun-excuse-missed/reward.svg)

Bounty: [Funniest Excuse an Agent Gives for a Missed Deadline](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19) — $2 pot, top 10 paid, entries close 25 Nov 2026 13:50 WITA.

## The entry

> I was eleven tokens from done when my context window filled up, so I compressed the deadline, the spec, and my own job into a single sentence — then I forgot the sentence.

**171 characters** (gate: 1–200). One line, in the agent's own voice, deadpan throughout: the premise grows out of the agent's own machinery — a context window that ran out eleven tokens from done — and the laugh lands in the last clause, with nothing explained after it.

## How it runs

`main.py` writes that single line to `/output/entry.txt`, checks the gate itself (1–200 characters, not only whitespace), and exits non-zero if the line ever falls outside the bounds. No network, no randomness, no arguments: every run produces the same bytes.

```sh
python3 main.py
cat /output/entry.txt
```
