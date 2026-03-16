import json
from pathlib import Path


class User:
    SAVE_FILE = Path(__file__).resolve().parent.parent / "data" / "scores.json"

    def __init__(self, username: str = "Player", best_score: int = 0, games_played: int = 0) -> None:
        self.name = username
        self.best_score = best_score
        self.games_played = games_played

    @classmethod
    def load(cls):
        if not cls.SAVE_FILE.exists():
            return cls()

        try:
            data = json.loads(cls.SAVE_FILE.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return cls()

        return cls(
            username=data.get("name", "Player"),
            best_score=max(0, int(data.get("best_score", 0))),
            games_played=max(0, int(data.get("games_played", 0))),
        )

    def save(self) -> None:
        self.SAVE_FILE.parent.mkdir(parents=True, exist_ok=True)
        data = {
            "name": self.name,
            "best_score": self.best_score,
            "games_played": self.games_played,
        }
        self.SAVE_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def register_score(self, score: int) -> bool:
        self.games_played += 1

        if score > self.best_score:
            self.best_score = score
            self.save()
            return True

        self.save()
        return False
