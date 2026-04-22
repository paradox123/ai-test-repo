---
name: onboarding-smoke
description: Minimal smoke test for cloned skill repos. USE WHEN clone or skill setup should be verified after onboarding.
---

# Onboarding Smoke Skill

## Goal
Verify that the skill exists after clone and can be executed.

## Run
`python3 scripts/smoke_check.py --out ./onboarding-runs/smoke`

## Success Criteria
- Exit code `0`
- File `smoke-result.json` is written
- Field `status` is `ok`
