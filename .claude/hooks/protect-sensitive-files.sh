#!/bin/bash
# Prevent accidental edits to sensitive files
# Called by PreToolUse hook on Edit|Write

INPUT="$1"

# Block edits to .env files
if echo "$INPUT" | grep -qE '\.env($|\.)'; then
  echo "BLOCKED: Cannot edit .env files directly. Use .env.example as a template."
  exit 2
fi

# Block edits to private/ directory content (except README)
if echo "$INPUT" | grep -qE 'private/' && ! echo "$INPUT" | grep -qE 'private/README\.md'; then
  echo "BLOCKED: Cannot edit files in private/ directory. This directory is for local sensitive data only."
  exit 2
fi

exit 0
