"""
Flask API 示例：用于接收技能库同步数据。
请设置环境变量 SKILL_STORE_API_KEY；未设置时拒绝 API 写操作。
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import json, os
from datetime import datetime

app = Flask(__name__)
CORS(app)
SKILLS_FILE = os.environ.get("SKILLS_FILE", "skills_store.json")
API_KEY = os.environ.get("SKILL_STORE_API_KEY")

def verify_api_key():
    if not API_KEY:
        return False
    auth = request.headers.get("Authorization", "")
    return auth.startswith("Bearer ") and auth[7:] == API_KEY


def load_skills():
    if os.path.exists(SKILLS_FILE):
        with open(SKILLS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"skills": [], "total": 0, "updated_at": None}


def save_skills(data):
    data["updated_at"] = datetime.now().isoformat()
    with open(SKILLS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


@app.route("/api/skills", methods=["GET"])
def get_skills():
    data = load_skills()
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 50, type=int)
    items = data.get("skills", [])
    page = max(page, 1)
    per_page = max(per_page, 1)
    start = (page - 1) * per_page
    return jsonify({"skills": items[start:start + per_page], "total": len(items), "page": page, "per_page": per_page})


@app.route("/api/skills", methods=["POST"])
def add_skills():
    if not verify_api_key():
        return jsonify({"error": "Unauthorized; configure SKILL_STORE_API_KEY"}), 401
    payload = request.get_json(silent=True) or {}
    items = payload.get("skills", [])
    data = load_skills()
    data["skills"].extend(items)
    data["total"] = len(data["skills"])
    save_skills(data)
    return jsonify({"success": True, "added": len(items), "total": data["total"]})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
