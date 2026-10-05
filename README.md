# 🚀 My AI Tools (`my-ai-tools`)

생산성을 극대화하기 위한 AI 프롬프트 라이브러리 및 브라우저 기반 경량 유틸리티 도구 모음입니다.

---

## 📁 디렉터리 구조 (Directory Structure)

```text
my-ai-tools/
├── .github/
│   └── ISSUE_TEMPLATE/
│       └── prompt_issue_template.md  # 프롬프트 제안/이슈 템플릿
├── docs/                             # 웹 대시보드 및 도구
│   ├── index.html                    # 메인 대시보드
│   ├── tools/
│   │   ├── json-formatter.html       # JSON 포맷터 & 검증기
│   │   └── text-diff.html            # 텍스트 비교 도구
│   └── assets/
│       └── .gitkeep
├── prompts/                          # AI 프롬프트 라이브러리
│   ├── coding/
│   │   ├── refactoring.md            # 클린 코드 & 리팩토링 프롬프트
│   │   └── code-review.md            # PR 코드 리뷰 프롬프트
│   ├── writing/
│   │   └── summarizer.md             # 비즈니스 핵심 요약 프롬프트
│   └── templates/
│       └── prompt-template.md        # 표준 프롬프트 작성 서식
├── CHANGELOG.md                      # 변경 이력 기록
├── LICENSE                           # MIT License
├── README.md                         # 저장소 소개 및 문서
└── build_structure.py                # 초기 구조 자동 생성 스크립트
```

---

## 🛠️ 웹 도구 목록 (Web Tools)

`docs/index.html`을 브라우저에서 열면 로컬에서 바로 사용할 수 있는 대시보드가 제공됩니다.

- **[JSON Formatter](docs/tools/json-formatter.html)**: 들여쓰기 정렬, 압축(Minify), 문법 검증 기능
- **[Text Diff Checker](docs/tools/text-diff.html)**: 원본과 수정본의 라인별 차이점 비교

---

## 💡 프롬프트 라이브러리 (Prompt Library)

- **Coding**
  - [`refactoring.md`](prompts/coding/refactoring.md): 동작 변경 없이 가독성/확장성을 개선하는 리팩토링
  - [`code-review.md`](prompts/coding/code-review.md): 보안, 성능, 예외 처리를 검토하는 PR 코드 리뷰
- **Writing**
  - [`summarizer.md`](prompts/writing/summarizer.md): 핵심 위주로 명료하게 재구성하는 요약기
- **Templates**
  - [`prompt-template.md`](prompts/templates/prompt-template.md): 새로운 프롬프트를 작성할 때 사용하는 표준 서식

---

## 📄 라이선스 (License)

이 프로젝트는 [MIT License](LICENSE)에 따라 배포됩니다.
