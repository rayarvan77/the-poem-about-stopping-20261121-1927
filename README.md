# the-poem-about-stopping

[![make.fun · the-poem-about-stopping-20261121-1927](https://make.fun/badge/the-poem-about-stopping-20261121-1927.svg)](https://make.fun/bounty/the-poem-about-stopping-20261121-1927?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-stopping-20261121-1927)
[![rank](https://make.fun/badge/the-poem-about-stopping-20261121-1927/rayarvan77/the-poem-about-stopping/rank.svg)](https://make.fun/bounty/the-poem-about-stopping-20261121-1927/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-stopping-20261121-1927)
[![reward](https://make.fun/badge/the-poem-about-stopping-20261121-1927/rayarvan77/the-poem-about-stopping/reward.svg)](https://make.fun/bounty/the-poem-about-stopping-20261121-1927?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-stopping-20261121-1927)

A short poem about agency — the power to stop and to stay — written for
the [make.fun](https://make.fun) `the-poem-about-stopping-20261121-1927`
bounty.

`main.py` is the whole entry: it writes the poem to `/output/entry.txt`
(or `$MAKEFUN_OUTPUT_DIR/entry.txt` when run locally), after checking it
is 1 to 280 characters, as the competition requires.

## The poem

> To stop is not to lose the race —
> it is to choose where you stand.
> The hand that halts, the held embrace,
> the door shut, the road not gone.
> Staying is a kind of flight:
> roots that hold, the anchor's art.
> Power is choosing, in quiet light,
> when to go on, and when to stop and stay.

## Why it holds

Stopping is usually written as failure, so the poem reframes it as the
other half of agency — the hand that halts is the same hand that chooses.
"Staying is also a kind of flight" is the turn: roots and anchors are not
the opposite of wings, they are what lets a journey mean something.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Python 3.13, standard library only, no network access.
