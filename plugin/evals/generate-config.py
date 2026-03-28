#!/usr/bin/env python3
"""Generate promptfooconfig.yaml from all skills' evals.json files."""

import json
import glob
import yaml
from pathlib import Path

ROOT = Path(__file__).parent.parent
SKILLS_DIR = ROOT / "skills"


def build_config():
    tests = []

    eval_files = sorted(glob.glob(str(SKILLS_DIR / "*/evals/evals.json")))
    for eval_file in eval_files:
        eval_path = Path(eval_file)
        skill_dir = eval_path.parent.parent
        skill_name = skill_dir.name
        skill_md = skill_dir / "SKILL.md"

        if skill_name == "_template" or not skill_md.exists():
            continue

        with open(eval_file) as f:
            data = json.load(f)

        # Build relative path from evals/ dir to skill SKILL.md
        skill_rel = f"file://../skills/{skill_name}/SKILL.md"

        for case in data.get("evals", []):
            assertions = []
            for assertion_text in case.get("assertions", []):
                assertions.append({
                    "type": "llm-rubric",
                    "value": assertion_text,
                })

            test = {
                "description": f"{skill_name} eval {case['id']}",
                "vars": {
                    "skill_content": skill_rel,
                    "prompt": case["prompt"],
                },
                "assert": assertions,
            }
            tests.append(test)

    config = {
        "description": "Stellenium DC Skills evaluation suite",
        "prompts": ["file://prompt.json"],
        "providers": [
            {
                "id": "anthropic:messages:claude-sonnet-4-20250514",
                "config": {
                    "temperature": 0.0,
                    "max_tokens": 8192,
                },
            }
        ],
        "defaultTest": {
            "options": {
                "provider": "anthropic:messages:claude-sonnet-4-20250514",
            },
        },
        "tests": tests,
    }

    out_path = ROOT / "evals" / "promptfooconfig.yaml"
    with open(out_path, "w") as f:
        yaml.dump(config, f, default_flow_style=False, sort_keys=False, width=120)

    print(f"Generated {out_path} with {len(tests)} test cases from {len(eval_files) - 1} skills")


if __name__ == "__main__":
    build_config()
