#!/usr/bin/env bash
# Chat completion through FastAIToken with plain HTTP.
#
#   export FASTAITOKEN_API_KEY=sk-...
#   export FASTAITOKEN_BASE_URL=...   # copy from the FastAIToken console, e.g. ending in /v1
#   bash examples/curl/chat.sh
set -euo pipefail

: "${FASTAITOKEN_API_KEY:?Set FASTAITOKEN_API_KEY}"
: "${FASTAITOKEN_BASE_URL:?Set FASTAITOKEN_BASE_URL}"
MODEL="${FASTAITOKEN_MODEL:-gpt-5.5}"

curl -sS "${FASTAITOKEN_BASE_URL%/}/chat/completions" \
  -H "Authorization: Bearer ${FASTAITOKEN_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "{\"model\": \"${MODEL}\", \"messages\": [{\"role\": \"user\", \"content\": \"Hello!\"}]}"
echo
