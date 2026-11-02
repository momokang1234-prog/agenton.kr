#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AgentOn (agenton.kr) 공식 웹사이트 무결성 검증 스크립트.
1. 필수 파일(public/index.html, public/privacy.html, public/terms.html, vercel.json) 존재 및 비어있지 않음 확인
2. 사업자등록번호(233-62-00821), 상호명(에이전트온), 대표자(강현욱) SSOT 문자열 포함 확인
3. 잘못된 법인 오표기('주식회사 에이전트온', '(주)에이전트온', '㈜에이전트온') 0건 검증
4. Zero-Emoji 원칙 준수 여부 (유니코드 이모지 0건) 검증
"""

import json
import re
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    ROOT_DIR / "public" / "index.html",
    ROOT_DIR / "public" / "privacy.html",
    ROOT_DIR / "public" / "terms.html",
    ROOT_DIR / "vercel.json",
]

HTML_FILES = [
    ROOT_DIR / "public" / "index.html",
    ROOT_DIR / "public" / "privacy.html",
    ROOT_DIR / "public" / "terms.html",
]

REQUIRED_SSOT_TOKENS = [
    "233-62-00821",
    "에이전트온",
    "강현욱",
    "daviidkang@gmail.com",
]

FORBIDDEN_CORPORATE_TERMS = [
    "주식회사 에이전트온",
    "주식회사에이전트온",
    "(주)에이전트온",
    "(주) 에이전트온",
    "㈜에이전트온",
    "㈜ 에이전트온",
]

# 유니코드 이모지 블록 정규식 (Zero-Emoji 검증용)
EMOJI_PATTERN = re.compile(
    "["
    "\U0001F300-\U0001F5FF"
    "\U0001F600-\U0001F64F"
    "\U0001F680-\U0001F6FF"
    "\U0001F700-\U0001F77F"
    "\U0001F780-\U0001F7FF"
    "\U0001F800-\U0001F8FF"
    "\U0001F900-\U0001F9FF"
    "\U0001FA00-\U0001FA6F"
    "\U0001FA70-\U0001FAFF"
    "\U00002702-\U000027B0"
    "]+",
    flags=re.UNICODE,
)


def main() -> int:
    errors = []

    # 1. 필수 파일 존재 및 크기 검증
    for file_path in REQUIRED_FILES:
        if not file_path.exists():
            errors.append(f"[MISSING] 필수 파일이 존재하지 않습니다: {file_path}")
        elif file_path.stat().st_size == 0:
            errors.append(f"[EMPTY] 파일이 비어 있습니다: {file_path}")

    if errors:
        for err in errors:
            print(err, file=sys.stderr)
        return 1

    # 2. vercel.json 구문 및 라우팅 검증
    vercel_path = ROOT_DIR / "vercel.json"
    try:
        vercel_data = json.loads(vercel_path.read_text(encoding="utf-8"))
        rewrites = vercel_data.get("rewrites", [])
        sources = {item.get("source") for item in rewrites}
        for req_route in ("/", "/privacy", "/terms"):
            if req_route not in sources:
                errors.append(f"[VERCEL] vercel.json에 필수 rewrite 경로가 누락되었습니다: {req_route}")
    except Exception as exc:
        errors.append(f"[VERCEL] vercel.json 파싱 실패: {exc}")

    # 3. HTML 파일별 SSOT, 법인 오표기, Zero-Emoji 검사
    for html_path in HTML_FILES:
        content = html_path.read_text(encoding="utf-8")
        rel_name = html_path.relative_to(ROOT_DIR)

        for token in REQUIRED_SSOT_TOKENS:
            if token not in content:
                errors.append(f"[SSOT] {rel_name} 파일에 필수 사업자 정보 '{token}'이(가) 누락되었습니다.")

        for forbidden in FORBIDDEN_CORPORATE_TERMS:
            if forbidden in content:
                errors.append(f"[FORBIDDEN] {rel_name} 파일에 금지된 법인 오표기 '{forbidden}'이(가) 포함되어 있습니다.")

        emoji_matches = EMOJI_PATTERN.findall(content)
        if emoji_matches:
            errors.append(f"[EMOJI] {rel_name} 파일에서 이모지가 검출되었습니다 (Zero-Emoji 위반): {emoji_matches}")

    if errors:
        for err in errors:
            print(err, file=sys.stderr)
        return 1

    print("[PASS] All AgentOn site integrity checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
