# 에이전트온 (AgentOn) 공식 웹사이트 (`agenton.kr`)

반복되는 마케팅·채용·운영을 검증된 AI 시스템으로 대체하는 엔지니어링 스튜디오 **에이전트온 (AgentOn)**의 공식 웹사이트 레포지토리입니다.

---

## 1. 사업자 및 도메인 SSOT 정보

- **상호명**: 에이전트온 (AgentOn) *(개인사업자이므로 법인 표기 엄격 금지)*
- **대표자**: 강현욱
- **사업자등록번호**: `233-62-00821`
- **공식 도메인**: `https://agenton.kr`
- **비즈니스 및 개인정보 보호 문의**: `daviidkang@gmail.com`
- **글로벌 채용 및 파트너십 문의**: `daviidkang2@gmail.com`

---

## 2. 디렉토리 구조

```text
agenton.kr/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # GitHub Actions 무결성 검증 및 Vercel 배포 파이프라인
├── public/
│   ├── index.html             # 공식 메인 랜딩 페이지 & 인터랙티브 라이브 데모
│   ├── privacy.html           # 공식 개인정보처리방침 (Meta 비즈니스/앱 검수 규격 준수)
│   └── terms.html             # 공식 서비스 이용약관
├── scripts/
│   └── verify_site.py         # SSOT, 금지어(법인 오표기), Zero-Emoji 물리 검증 스크립트
├── .gitignore
├── .vercelignore
├── GEMINI.md                  # 워크스페이스 에이전트 헌장 (Track 1 Git-Only)
├── package.json
├── vercel.json                # Clean URLs (/privacy, /terms) 및 보안 헤더 설정
└── README.md
```

---

## 3. 로컬 실행 및 무결성 검증

### 무결성 검증 실행
모든 파일이 SSOT 사업자 정보를 포함하고 있는지, 법인 오표기 및 이모지가 0건인지 검증합니다.
```bash
python3 scripts/verify_site.py
# 또는
npm run verify
```

### 로컬 웹 서버 구동
```bash
npm run serve
# 브라우저에서 http://localhost:3000 접속
```

---

## 4. Vercel 배포 및 도메인(`agenton.kr`) 연결 가이드

1. GitHub 레포지토리에 `main` 브랜치를 푸시하면 `.github/workflows/ci-cd.yml`이 자동 실행되어 `verify_site.py` 무결성 검사를 수행합니다.
2. Vercel 대시보드에서 본 GitHub 레포지토리를 Import 하거나, GitHub Secrets에 `VERCEL_TOKEN`, `VERCEL_ORG_ID`, `VERCEL_PROJECT_ID`를 등록하여 자동 배포합니다.
3. Vercel Project Settings -> **Domains** 메뉴에서 `agenton.kr` 및 `www.agenton.kr` 도메인을 추가하고 안내된 DNS 레코드(A 레코드 `76.76.21.21`, CNAME `cname.vercel-dns.com`)를 도메인 등록기관에 설정합니다.
