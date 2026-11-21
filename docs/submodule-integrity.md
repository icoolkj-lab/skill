# Git Submodule Integrity Notes

## Current issue

The repository tree contains Git submodule entries (mode `160000`) but no root `.gitmodules` file. A normal clone therefore leaves these directories uninitialized, and Git's checkout cleanup may emit warnings such as `No url found for submodule path ...`.

## Verified references

The recorded commit SHA was checked against the source repository's commit API for the following entries:

| Path | Source repository | Recorded commit |
|---|---|---|
| `skills/NanoBanana-PPT-Skills` | `https://github.com/op7418/NanoBanana-PPT-Skills` | `0c18b9abde04ad42f4f62c7e9ead346b7bb39260` |
| `skills/ai-drawio` | `https://github.com/GBSOSS/ai-drawio` | `16621c06d202bd25c60cf9d00f8a3cd702bdb7d6` |
| `skills/baoyu-skills` | `https://github.com/JimLiu/baoyu-skills` | `6cbf0f4e524a75a2392c7e37f6fe8686c408fdbe` |
| `skills/jiamu-skills` | `https://github.com/isjiamu/jiamu-skills` | `032882531d0b6fecfd05d71e6e4d48fd47a7fbed` |

## Unresolved

- `skills/anything-to-notebooklm/anything-to-notebooklm`
  - Recorded commit: `965051880b73873bb73d849eb6d6edd0c3eef20f03`
  - The source repository for this exact gitlink commit has not been verified.
  - Do not invent a submodule URL or replace the gitlink until its origin is confirmed.

## Resolution options

1. Recover the original `.gitmodules` / upstream source metadata and verify every commit.
2. If a source is confirmed, restore `.gitmodules` and test `git submodule update --init --recursive`.
3. Alternatively, vendor each package at its exact recorded commit after reviewing its license and required binary assets; preserve provenance and checksums.

This is a repository integrity issue, not a completed cleanup. Keep all gitlinks until their origins and intended distribution model are verified.
