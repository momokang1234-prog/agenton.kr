---
id: "development_agenton_kr"
workspace_name: "agenton.kr"
category: "development"
sync_governance:
  primary_track: "Track 1 (Git-Only)"
  media_policy: "Git-LFS"
  cloud_exclude: true
  git_remote_required: true
registered_at: "2026-11-02"
---

# agenton.kr 에이전트 헌장 (Agent Charter)

본 문서는 에이전트온(AgentOn)의 공식 웹사이트 프로젝트(`agenton.kr`)를 관리하고 개발하는 모든 AI 에이전트가 절대적으로 준수해야 하는 최상위 운영 헌장입니다.

## 1. 동기화 및 인프라 거버넌스 (Sync & Deployment Governance)
- **Track 1 (Git-Only) 원칙**: 본 워크스페이스는 오직 GitHub 원격 저장소(`origin`)와 Vercel 프로덕션 파이프라인을 통해서만 코드와 정적 에셋을 배포합니다. 클라우드 드라이브(rclone 등) 실시간 동기화 대상에서 전면 제외됩니다.
- **도메인 연동 아키텍처**: 비즈니스 기획, 마케팅 캠페인 전략, 칼럼 원고 및 포트폴리오 기획 자산은 `/Users/ganghyeon-ug/develop/workspaces/domain/agenton-marketing-team` 워크스페이스에서 관장하며, 본 `development/agenton.kr` 워크스페이스는 이를 웹 표준 프로덕션 코드로 구현 및 서빙하는 프론트엔드/배포 전담 레이어입니다.

## 2. 법적 및 사업자 정보 단일 진실 공급원 (Business Entity SSOT)
웹사이트의 모든 페이지(`index.html`, `privacy.html`, `terms.html`) 및 메타데이터에서 사업자 정보를 표기할 때는 아래의 실물 사업자등록증 기준 SSOT 정보를 100% 정확하게 사용해야 합니다.
- **상호명**: `에이전트온 (AgentOn)`
  - **[절대 금지]**: 에이전트온은 개인사업자이므로 어떠한 경우에도 `주식회사 에이전트온` 또는 `(주)에이전트온`과 같은 법인 사칭/오표기를 사용해서는 안 됩니다.
- **대표자**: `강현욱`
- **사업자등록번호**: `233-62-00821`
- **공식 도메인**: `https://agenton.kr`
- **공식 연락처**:
  - 비즈니스 도입 및 개인정보 보호 문의: `daviidkang@gmail.com`
  - 글로벌 채용 및 파트너십 문의: `daviidkang2@gmail.com`

## 3. 디자인 및 엔지니어링 표준 (Design & Code Standards)
- **Zero-Emoji 원칙**: 공식 문서, 소스 코드, HTML UI 전반에 걸쳐 유니코드 이모지(Emoji) 사용을 전면 금지합니다. 모든 시각적 표식은 정교한 인라인 SVG 아이콘(Lucide 규격) 또는 구조화된 영문/국문 상태 배지(`[ACTIVE]`, `[PASS]`, `[VERIFIED]`)로만 구현합니다.
- **타이포그래피 및 테마**: Pretendard 웹폰트를 기본 서체로 채택하며, 모노톤 다크 글래스모피즘(Monotone Dark Glassmorphism)과 고대비 에디토리얼 레이아웃을 결합하여 엔터프라이즈 엔지니어링 스튜디오의 신뢰감을 전달합니다.
- **무결성 자동 검증**: 모든 코드 변경 후에는 반드시 `python3 scripts/verify_site.py`를 실행하여 SSOT 일치 여부, 금지어(법인 오표기) 포함 여부, 이모지 0건 여부를 물리적으로 검증해야 합니다.
