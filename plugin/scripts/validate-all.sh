#!/usr/bin/env bash
# scripts/validate-all.sh -- Lightweight YAML frontmatter validation for skills
# Checks: SKILL.md exists, has 'name' and 'description' fields, name matches directory
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS_DIR="$REPO_ROOT/skills"
ERRORS=0
CHECKED=0

# Helper function: extract YAML field value from SKILL.md
# Usage: get_yaml_field <file> <field_name>
get_yaml_field() {
  local file="$1"
  local field="$2"
  # Extract value between first --- and second ---
  sed -n '/^---$/,/^---$/p' "$file" | grep "^$field:" | head -1 | cut -d: -f2- | xargs
}

# Iterate all skill directories
for skill_dir in "$SKILLS_DIR"/*/; do
  [ -d "$skill_dir" ] || continue
  dir_name="$(basename "$skill_dir")"

  # Skip _template directory
  if [ "$dir_name" = "_template" ]; then
    continue
  fi

  skill_file="$skill_dir/SKILL.md"
  if [ ! -f "$skill_file" ]; then
    echo "FAIL [$dir_name]: SKILL.md not found"
    ERRORS=$((ERRORS + 1))
    continue
  fi

  CHECKED=$((CHECKED + 1))

  # Check for 'name' field
  name_value=$(get_yaml_field "$skill_file" "name")
  if [ -z "$name_value" ]; then
    echo "FAIL [$dir_name]: missing or empty 'name' field in frontmatter"
    ERRORS=$((ERRORS + 1))
  fi

  # Check for 'description' field
  desc_value=$(get_yaml_field "$skill_file" "description")
  if [ -z "$desc_value" ]; then
    echo "FAIL [$dir_name]: missing or empty 'description' field in frontmatter"
    ERRORS=$((ERRORS + 1))
  fi

  # Check that name matches directory name
  if [ -n "$name_value" ] && [ "$name_value" != "$dir_name" ]; then
    echo "FAIL [$dir_name]: 'name' field ('$name_value') does not match directory name"
    ERRORS=$((ERRORS + 1))
  fi
done

# Exit logic
if [ "$CHECKED" -eq 0 ]; then
  echo "NO SKILLS FOUND -- nothing to validate"
  exit 0
fi

if [ "$ERRORS" -gt 0 ]; then
  echo ""
  echo "VALIDATION FAILED: $ERRORS error(s) in $CHECKED skill(s)"
  exit 1
fi

echo "ALL CHECKS PASSED ($CHECKED skill(s) validated)"
