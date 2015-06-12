Lunch
=====

Random lunch scheduler. Right now, it's super simple and just reads results from a Google form, generates random lunch groups and informs them via email. However, it brought up an interesting problem.

Suppose you have n items, each of which has a subset of d features. Consolidate the items into groups of size k such that all items in a group have at least one feature in common. The goal is to maximize the number of groups. Also we would like multiple near-optimal solutions since we want to ensure that the same items are not grouped together in future runs of the algorithm.

There are n! ways of forming groups of size k. The search space is too large to use a brute force solution and check which of all the possible disitributions are feasible. Possibly an NP-hard problem, but there might be a good approximation algorithm.

Uses:
- [yagmail](https://github.com/kootenpv/yagmail)
- [gspread](https://github.com/burnash/gspread)

Sample `config.json` and private key are provided. Remove the `_hidden` from `config.json_hidden`. Get the private key from Google Developers Console. Follow the gspread instructions.

This is not setup such that you can clone and use this easily. There's some setup on Google Forms also required.
