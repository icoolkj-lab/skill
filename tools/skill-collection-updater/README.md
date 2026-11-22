# Legacy Skill Store Updater

This is the repository's earlier standalone crawler/synchronizer. It is separate from the current GitHub Actions synchronization pipeline and retained for manual use.

## Run

- Windows one-shot: run `run_once.bat`.
- Windows daemon: run `start_daemon.bat`.
- CLI: `python main.py --once` or `python main.py --daemon`.
- Install dependencies: `python -m pip install -r requirements.txt`.

Data and logs are stored inside this directory (`data/` and `logs/`) instead of the repository-wide data directory.

## Note

The default API integration is disabled/placeholder configuration. Review endpoint and credentials before enabling. The active GitHub Actions sync scripts remain under the repository's `.github/workflows/` and `scripts/`.
