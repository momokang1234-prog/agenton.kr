# [AgentOn 공식 웹사이트 (agenton.kr)] 세션 마무리 요약 보고서

> **세션 ID:** `819082f8-e0b5-4901-b085-2f5301802eae`  
> **일시:** `2026-11-02 17:00:00 KST`  
> **상태:** `COMPLETED (100% PASS)`  
> **신규 구축 워크스페이스:** `/Users/ganghyeon-ug/develop/workspaces/development/agenton.kr`  
> **GitHub 원격 리포지토리:** `https://github.com/momokang1234-prog/agenton.kr` (`main` 브랜치)  
> **라이브 프로덕션 도메인:** `https://agenton.kr` (`308` -> `https://www.agenton.kr` HTTP/2 `200 OK`)

---

## 1. 세션 핵심 목표 및 범위 (Goal & Criteria)

- **초기 목표:**
  - 에이전트온(AgentOn)의 비즈니스 실체(메타 광고 슬랙 제어 자동화, 호주 STODJA 그룹 독점 채용 대행, 매장 백오피스·정산 대사 자동화)를 전수 파악하여 `agenton.kr` 공식 웹사이트 구축 및 Vercel 배포 전략 컨설팅 수행.
- **추가/확장 요구사항:**
  1. `development` 카테고리 산하에 `agenton.kr` 신규 워크스페이스 생성 및 L2 공식 원장 등재.
  2. GitHub 원격 리포지토리(`momokang1234-prog/agenton.kr`) 생성 및 GitHub Actions CI/CD 파이프라인 세팅.
  3. Vercel 프로젝트 연동 및 커스텀 도메인(`agenton.kr`, `www.agenton.kr`) 무료 SSL 발급·연결 완결.
- **최종 달성도:**
  - **100% 완수** (웹사이트·법적 고지 페이지 구축, CI/CD 자동 검증 통과, Vercel 배포 및 `https://agenton.kr` 실서버 HTTPS 200 응답 가동 확인, 독립 QA 서브에이전트 `functional-qa-v2` Sign-off 승인 완료).

---

## 2. 핵심 아키텍처 및 기술적 결정 사항 (Key Architectural Decisions)

1. **호주 광고 봇(`meta-ads-lite`)과 공식 웹사이트(`agenton.kr`)의 독립 워크스페이스 분리 아키텍처**
   - 실시간 가동 중인 호주 STODJA 메타 광고 슬랙 봇 서버(`meta-ads-lite`)에 홈페이지 디자인/콘텐츠 수정 배포가 영향을 주지 않도록, `development/agenton.kr`을 독립된 Track 1 (Git-Only) 워크스페이스 및 독립 GitHub/Vercel 프로젝트로 분리 구축함.
2. **B2B 리드 전환 및 플랫폼(Meta/구글/포털) 심사 동시 충족 하이브리드 설계**
   - 단순 소개 페이지를 넘어, 방문자가 브라우저에서 직접 클릭해 볼 수 있는 **3종 인터랙티브 라이브 데모 샌드박스(Slack Boost Controller / Multimodal HR Verifier / Ledger Reconciliation)**를 메인 페이지(`public/index.html`)에 탑재하여 기술력을 즉시 증명함.
   - Meta 비즈니스 인증 및 앱 검수 필수 요건인 개인정보처리방침(`/privacy`)과 서비스 이용약관(`/terms`)을 Clean URLs 리라이트(`vercel.json`)와 함께 구축하고, 개인사업자 SSOT 정보(`상호: 에이전트온 (AgentOn) | 대표자: 강현욱 | 사업자등록번호: 233-62-00821`)를 정확히 표기하여 법인 오표기 리스크를 원천 차단함.
3. **결정론적 CI/CD 무결성 게이트(`scripts/verify_site.py` + `.github/workflows/ci-cd.yml`)**
   - 코드 푸시마다 필수 라우트 파일 존재 여부, 사업자 SSOT 문자열 포함 여부, 법인 오표기(`주식회사`, `(주)`) 0건, 유니코드 이모지 0건(Zero-Emoji)을 자동 검사하도록 CI/CD 파이프라인을 구축함.
4. **도메인 라우팅 표준화 (`agenton.kr` 308 Redirect -> `www.agenton.kr` Production)**
   - Vercel 권장 아키텍처에 따라 `www.agenton.kr`을 CNAME 기반 글로벌 엣지 CDN Production 엔드포인트로 설정하고, Apex 도메인(`agenton.kr`)은 `308 Permanent Redirect`로 즉시 연결되도록 구성하여 접속 속도와 안정성을 극대화함.

---

## 3. 물리적 구현 및 변경 자산 맵 (Implemented Assets)

| 구분 | 물리적 파일 절대 경로 | 역할 및 설명 |
| :--- | :--- | :--- |
| **에이전트 헌장** | [`GEMINI.md`](file:///Users/ganghyeon-ug/develop/workspaces/development/agenton.kr/GEMINI.md) | Track 1 (Git-Only) 동기화 규칙, 마케팅 도메인 연동, Zero-Emoji 및 SSOT 사업자 표기 원칙 정의 |
| **메인 웹사이트** | [`public/index.html`](file:///Users/ganghyeon-ug/develop/workspaces/development/agenton.kr/public/index.html) | Pretendard 타이포그래피, 모노톤 다크 글래스모피즘, 3대 솔루션, 인터랙티브 데모 샌드박스, 케이스 스터디, 문의 폼, 공식 푸터 |
| **개인정보처리방침** | [`public/privacy.html`](file:///Users/ganghyeon-ug/develop/workspaces/development/agenton.kr/public/privacy.html) | 개인정보 보호법 및 Meta 플랫폼 정책 준수 개인정보처리방침 (`/privacy`) |
| **서비스 이용약관** | [`public/terms.html`](file:///Users/ganghyeon-ug/develop/workspaces/development/agenton.kr/public/terms.html) | 에이전트온 공식 서비스 이용약관 (`/terms`) |
| **Vercel 설정** | [`vercel.json`](file:///Users/ganghyeon-ug/develop/workspaces/development/agenton.kr/vercel.json) | `/`, `/privacy`, `/terms` Clean URLs Rewrites 및 보안 헤더 정의 |
| **무결성 검증기** | [`scripts/verify_site.py`](file:///Users/ganghyeon-ug/develop/workspaces/development/agenton.kr/scripts/verify_site.py) | 라우트 파일, SSOT 토큰, 법인 오표기 금지어, Zero-Emoji 자동 검증 스크립트 |
| **CI/CD 워크플로우** | [`.github/workflows/ci-cd.yml`](file:///Users/ganghyeon-ug/develop/workspaces/development/agenton.kr/.github/workflows/ci-cd.yml) | GitHub Actions 기반 사이트 무결성 검증 및 조건부 Vercel 배포 자동화 |
| **프로젝트 문서** | [`README.md`](file:///Users/ganghyeon-ug/develop/workspaces/development/agenton.kr/README.md) | 아키텍처 개요, 로컬 실행/검증 명령어, Vercel 도메인 DNS 가이드 |
| **L2 공식 원장** | [`workspace_track_ledger.json`](file:///Users/ganghyeon-ug/develop/main_memory/develop/_memory/workspace_track_ledger.json) | `development_agenton_kr` 워크스페이스 공식 등재 (`total_count: 73`) |
| **L2 마크다운 원장** | [`L2_workspace_track_ledger.md`](file:///Users/ganghyeon-ug/develop/main_memory/develop/_memory/L2_rules/L2_workspace_track_ledger.md) | `development` 섹션 내 `agenton.kr` Track 1 등록 |

---

## 4. 검증 및 테스트 실측 결과 (Verification & Test Results)

1. **사이트 무결성 및 SSOT/Zero-Emoji 검증 (`verify_site.py`)**
   - 실행 명령어: `python3 /Users/ganghyeon-ug/develop/workspaces/development/agenton.kr/scripts/verify_site.py`
   - 결과: **`[PASS] All AgentOn site integrity checks passed.` (Exit Code: `0`)**
2. **GitHub Actions CI/CD 실행 검증**
   - 워크플로우: `AgentOn Site Integrity & Vercel CD` (Run ID: `41407128514`)
   - 결과: **`completed / success` (14초 소요)**
3. **라이브 도메인(`https://agenton.kr`) 및 SSL 인증서 실측 검증**
   - 실행 명령어: `curl -I -L -s https://agenton.kr`
   - 결과:
     - `https://agenton.kr` -> `HTTP/2 308` (`location: https://www.agenton.kr/`, `server: Vercel`)
     - `https://www.agenton.kr/` -> **`HTTP/2 200 OK`** (SSL 인증서 정상 적용 완료)
4. **독립 QA 서브에이전트(`functional-qa-v2`) 교차 검증**
   - 전수 파일 무결성, 로컬 HTTP 엔드포인트(`/`, `/privacy.html`, `/terms.html`) 200 응답, 원격 리포지토리 및 L2 원장 정합성 감사 결과 **최종 `PASS` 승인**.

---

## 5. 잔여 과제 및 후속 단계 (Next Steps & Backlog)

1. **[TASK-01] `domain/agenton-marketing-team` 칼럼 및 포트폴리오 콘텐츠 증분 게시**
   - 마케팅 워크스페이스(`domain/agenton-marketing-team/01_Website_Portfolio_Columns`)에서 작성되는 인사이트 칼럼 및 신규 자동화 구축 사례를 `agenton.kr`의 Case Studies & Columns 섹션에 주기적으로 업데이트하고 `git push`로 자동 배포.
2. **[TASK-02] 외부 플랫폼(Meta 비즈니스 관리자, 채용 포털 등) 공식 웹사이트 URL 등록**
   - Meta 비즈니스 정보 및 앱 설정에 공식 웹사이트(`https://agenton.kr`), 개인정보처리방침(`https://agenton.kr/privacy`), 서비스 약관(`https://agenton.kr/terms`) URL을 등록하여 심사 및 인증에 활용.
3. **[TASK-03] 필요 시 서브도메인(`ads.agenton.kr` 등) 확장 연결**
   - 향후 슬랙/메타 광고 봇이나 채용 포털을 `agenton.kr` 하위 서브도메인으로 통합할 경우 Vercel Domains 설정에서 CNAME 레코드만 추가하여 즉시 연동.
