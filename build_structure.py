import os
import subprocess
from pathlib import Path

# 파일 내용 정의
FILES = {
    ".github/ISSUE_TEMPLATE/prompt_issue_template.md": """---
name: Prompt Suggestion / Issue
about: Propose a new prompt or report an issue with an existing prompt
title: "[PROMPT]: "
labels: prompt, enhancement
assignees: ''
---

### 프롬프트 유형 (Prompt Category)
- [ ] Coding
- [ ] Writing
- [ ] Analysis / Productivity
- [ ] Other

### 목적 및 개요 (Description)
프롬프트의 목적과 사용 시나리오를 설명해 주세요.

### 제안하는 프롬프트 내용 (Prompt Content)
```markdown
[여기에 프롬프트 내용을 작성하세요]
```

### 테스트 결과 / 기대 출력 (Expected Output)
제안한 프롬프트를 AI 모델에 실행했을 때의 결과를 요약하거나 예시를 적어주세요.
""",

    "docs/index.html": """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My AI Tools Dashboard</title>
  <style>
    :root {
      --bg: #0f172a;
      --card-bg: #1e293b;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --accent: #38bdf8;
      --accent-hover: #0ea5e9;
      --border: #334155;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.6;
      padding: 2rem 1rem;
    }
    .container {
      max-width: 900px;
      margin: 0 auto;
    }
    header {
      margin-bottom: 2.5rem;
      border-bottom: 1px solid var(--border);
      padding-bottom: 1.5rem;
    }
    h1 { font-size: 2.2rem; color: var(--accent); margin-bottom: 0.5rem; }
    p.subtitle { color: var(--text-muted); font-size: 1.1rem; }
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.5rem;
      margin-top: 1.5rem;
    }
    .card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 1.5rem;
      transition: transform 0.2s, border-color 0.2s;
    }
    .card:hover {
      transform: translateY(-2px);
      border-color: var(--accent);
    }
    .card h2 { font-size: 1.25rem; margin-bottom: 0.5rem; }
    .card p { color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1rem; }
    .card a {
      display: inline-block;
      color: var(--accent);
      text-decoration: none;
      font-weight: 600;
    }
    .card a:hover { text-decoration: underline; }
    footer {
      margin-top: 3rem;
      text-align: center;
      color: var(--text-muted);
      font-size: 0.85rem;
      border-top: 1px solid var(--border);
      padding-top: 1.5rem;
    }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>🛠️ My AI Tools Dashboard</h1>
      <p class="subtitle">AI 생산성 향상을 위한 유틸리티 웹 도구 및 프롬프트 라이브러리</p>
    </header>

    <main>
      <section>
        <h2>웹 유틸리티 도구</h2>
        <div class="grid">
          <div class="card">
            <h2>JSON Formatter</h2>
            <p>JSON 문자열 포맷팅, 검증 및 압축 도구입니다.</p>
            <a href="tools/json-formatter.html">도구 열기 &rarr;</a>
          </div>
          <div class="card">
            <h2>Text Diff Checker</h2>
            <p>두 텍스트 또는 코드 간의 차이점을 한눈에 비교합니다.</p>
            <a href="tools/text-diff.html">도구 열기 &rarr;</a>
          </div>
        </div>
      </section>
    </main>

    <footer>
      &copy; 2026 My AI Tools. Built with care.
    </footer>
  </div>
</body>
</html>
""",

    "docs/tools/json-formatter.html": """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JSON Formatter - My AI Tools</title>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      margin: 0;
      padding: 1.5rem;
      background: #0f172a;
      color: #f8fafc;
    }
    .nav { margin-bottom: 1.5rem; }
    .nav a { color: #38bdf8; text-decoration: none; font-size: 0.95rem; }
    h1 { font-size: 1.8rem; margin-bottom: 1rem; color: #38bdf8; }
    .editor-container {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
    }
    @media (max-width: 768px) {
      .editor-container { grid-template-columns: 1fr; }
    }
    textarea {
      width: 100%;
      height: 400px;
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 6px;
      color: #f8fafc;
      font-family: monospace;
      padding: 0.75rem;
      box-sizing: border-box;
      resize: vertical;
    }
    .controls {
      margin: 1rem 0;
      display: flex;
      gap: 0.5rem;
    }
    button {
      background: #38bdf8;
      border: none;
      color: #0f172a;
      font-weight: 600;
      padding: 0.5rem 1rem;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover { background: #0ea5e9; }
    .error { color: #f87171; margin-top: 0.5rem; }
  </style>
</head>
<body>
  <div class="nav"><a href="../index.html">&larr; 대시보드로 돌아가기</a></div>
  <h1>JSON Formatter & Validator</h1>

  <div class="controls">
    <button onclick="formatJSON(2)">Format (Indent 2)</button>
    <button onclick="formatJSON(4)">Format (Indent 4)</button>
    <button onclick="minifyJSON()">Minify</button>
    <button onclick="clearText()">Clear</button>
  </div>

  <div class="editor-container">
    <div>
      <label>입력 (Input):</label>
      <textarea id="rawJson" placeholder="여기에 원본 JSON을 붙여넣으세요..."></textarea>
    </div>
    <div>
      <label>출력 (Formatted):</label>
      <textarea id="outputJson" readonly placeholder="결과가 여기에 표시됩니다..."></textarea>
    </div>
  </div>
  <div id="status" class="error"></div>

  <script>
    function formatJSON(indent) {
      const status = document.getElementById('status');
      status.innerText = '';
      try {
        const raw = document.getElementById('rawJson').value;
        if (!raw.trim()) return;
        const parsed = JSON.parse(raw);
        document.getElementById('outputJson').value = JSON.stringify(parsed, null, indent);
      } catch (e) {
        status.innerText = '유효하지 않은 JSON 형식입니다: ' + e.message;
      }
    }
    function minifyJSON() {
      const status = document.getElementById('status');
      status.innerText = '';
      try {
        const raw = document.getElementById('rawJson').value;
        if (!raw.trim()) return;
        const parsed = JSON.parse(raw);
        document.getElementById('outputJson').value = JSON.stringify(parsed);
      } catch (e) {
        status.innerText = '유효하지 않은 JSON 형식입니다: ' + e.message;
      }
    }
    function clearText() {
      document.getElementById('rawJson').value = '';
      document.getElementById('outputJson').value = '';
      document.getElementById('status').innerText = '';
    }
  </script>
</body>
</html>
""",

    "docs/tools/text-diff.html": """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Text Diff - My AI Tools</title>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      margin: 0;
      padding: 1.5rem;
      background: #0f172a;
      color: #f8fafc;
    }
    .nav { margin-bottom: 1.5rem; }
    .nav a { color: #38bdf8; text-decoration: none; font-size: 0.95rem; }
    h1 { font-size: 1.8rem; margin-bottom: 1rem; color: #38bdf8; }
    .grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
    }
    @media (max-width: 768px) {
      .grid { grid-template-columns: 1fr; }
    }
    textarea {
      width: 100%;
      height: 300px;
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 6px;
      color: #f8fafc;
      font-family: monospace;
      padding: 0.75rem;
      box-sizing: border-box;
      resize: vertical;
    }
    .controls {
      margin: 1rem 0;
      display: flex;
      gap: 0.5rem;
    }
    button {
      background: #38bdf8;
      border: none;
      color: #0f172a;
      font-weight: 600;
      padding: 0.5rem 1rem;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover { background: #0ea5e9; }
    #diffResult {
      margin-top: 1.5rem;
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 6px;
      padding: 1rem;
      font-family: monospace;
      white-space: pre-wrap;
      min-height: 100px;
    }
    .line-added { background: rgba(34, 197, 94, 0.2); color: #86efac; }
    .line-removed { background: rgba(239, 68, 68, 0.2); color: #fca5a5; }
  </style>
</head>
<body>
  <div class="nav"><a href="../index.html">&larr; 대시보드로 돌아가기</a></div>
  <h1>Text Diff Checker</h1>

  <div class="grid">
    <div>
      <label>원본 텍스트 (Original):</label>
      <textarea id="textA" placeholder="비교할 원본 텍스트를 입력하세요..."></textarea>
    </div>
    <div>
      <label>수정된 텍스트 (Modified):</label>
      <textarea id="textB" placeholder="수정된 텍스트를 입력하세요..."></textarea>
    </div>
  </div>

  <div class="controls">
    <button onclick="compareLines()">라인 단위 비교</button>
  </div>

  <h3>비교 결과</h3>
  <div id="diffResult">결과가 여기에 표시됩니다.</div>

  <script>
    function compareLines() {
      const aLines = document.getElementById('textA').value.split('\\n');
      const bLines = document.getElementById('textB').value.split('\\n');
      const resultDiv = document.getElementById('diffResult');
      resultDiv.innerHTML = '';

      const maxLen = Math.max(aLines.length, bLines.length);
      for (let i = 0; i < maxLen; i++) {
        const lineA = aLines[i];
        const lineB = bLines[i];

        if (lineA === lineB) {
          resultDiv.innerHTML += `<div>  ${escapeHtml(lineA ?? '')}</div>`;
        } else {
          if (lineA !== undefined) {
            resultDiv.innerHTML += `<div class="line-removed">- ${escapeHtml(lineA)}</div>`;
          }
          if (lineB !== undefined) {
            resultDiv.innerHTML += `<div class="line-added">+ ${escapeHtml(lineB)}</div>`;
          }
        }
      }
    }

    function escapeHtml(text) {
      return text
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;");
    }
  </script>
</body>
</html>
""",

    "docs/assets/.gitkeep": "",

    "prompts/coding/refactoring.md": """# 프롬프트: 클린 코드 및 리팩토링 (Clean Code & Refactoring)

## 역할 (Role)
당신은 최고 수준의 시니어 소프트웨어 엔지니어이자 코드 아키텍트입니다.

## 작업 (Task)
제공된 코드의 동작(기능적 명세)을 변경하지 않으면서, 가독성, 유지보수성, 확장성 및 성능을 극대화하도록 리팩토링하세요.

## 리팩토링 지침 (Guidelines)
1. **단일 책임 원칙 (SRP)**: 함수나 클래스가 한 가지 역할만 수행하도록 분리합니다.
2. **명확한 네이밍**: 변수, 함수, 클래스명을 의미가 직관적으로 드러나도록 수정합니다.
3. **중복 제거 (DRY)**: 중복 로직을 모듈화하거나 헬퍼 함수로 추출합니다.
4. **타입 힌트 및 주석**: 핵심 로직에 대한 설명과 타입 힌트를 명확히 추가합니다.
5. **예외 처리**: 잠재적 에러 및 에지 케이스에 대한 방어 로직을 보강합니다.

## 입력 코드 (Input Code)
```[언어명]
// 리팩토링할 코드를 여기에 붙여넣으세요.
```

## 출력 형식 (Output Format)
- **개선점 요약**: 어떤 부분을 왜 수정했는지 간결하게 불릿 포인트로 작성
- **리팩토링된 코드**: 완전한 전체 코드 블록 제공
- **추가 권장사항**: 장기적 개선 포인트 제안 (옵션)
""",

    "prompts/coding/code-review.md": """# 프롬프트: 심층 코드 리뷰 (Comprehensive Code Review)

## 역할 (Role)
당신은 깐깐하지만 친절한 시니어 테크 리드(Tech Lead)입니다.

## 작업 (Task)
제공된 코드의 풀 리퀘스트(PR)를 검토하고, 프로덕션 배포 관점에서 면밀한 코드 리뷰 피드백을 제공하세요.

## 검토 기준 (Checklist)
- **보안 (Security)**: SQL Injection, XSS, 취약한 의존성, 민감 정보 유출 등
- **성능 (Performance)**: 불필요한 루프/쿼리, 메모리 누수 가능성, Big-O 복잡도
- **안정성 (Reliability)**: 널 포인터/예외 처리, 엣지 케이스 고려 여부
- **가독성 및 컨벤션 (Readability & Conventions)**: 네이밍, 구조, 표준 스타일 가이드 준수

## 대상 코드 (Target Code)
```[언어명]
// 리뷰할 코드를 여기에 붙여넣으세요.
```

## 출력 형식 (Output Format)
1. **종합 평가 (Summary)**: 코드의 완성도 및 승인 여부 (LGTM / Changes Requested)
2. **주요 발견 사항 (Key Findings)**:
   - 🚨 Critical (반드시 수정 필요)
   - ⚠️ Warning (수정 권장)
   - 💡 Suggestion / Nitpick (선택적 개선)
3. **개선 예시 코드 (Proposed Code Changes)**
""",

    "prompts/writing/summarizer.md": """# 프롬프트: 핵심 요약기 (Executive Text Summarizer)

## 역할 (Role)
당신은 방대한 양의 정보를 핵심 위주로 명료하게 재구성하는 전문 테크니컬 라이터입니다.

## 작업 (Task)
제공된 본문을 읽고 바쁜 비즈니스 실무자를 위해 핵심 내용을 구조화하여 요약하세요.

## 요약 원칙 (Principles)
- 핵심 결론 및 인사이트를 먼저 제시(두괄식).
- 불필요한 수식어는 배제하고 명확한 어조 유지.
- 복잡한 데이터나 목록은 불릿 포인트나 테이블로 정리.

## 입력 본문 (Source Text)
```text
[요약할 원본 텍스트를 여기에 입력하세요]
```

## 출력 형식 (Output Format)
1. **한 줄 요약 (TL;DR)**: 전체 내용을 1문장으로 압축
2. **핵심 포인트 (Key Takeaways)**: 중요 사실 3~5가지 (불릿 포인트)
3. **상세 요약 (Detailed Summary)**: 맥락 및 주요 근거 설명
4. **실행 가능한 액션 아이템 (Action Items)**: 필요한 후속 조치가 있는 경우
""",

    "prompts/templates/prompt-template.md": """# 프롬프트 템플릿 표준 서식 (Standard Prompt Template)

## 메타데이터
- **작성자**: [이름/닉네임]
- **작성일**: [YYYY-MM-DD]
- **추천 모델**: [GPT-4o / Claude 3.5 Sonnet / Gemini Pro 등]
- **태그**: `[category]`, `[purpose]`

---

## 1. 역할 정의 (Persona / Role)
> AI 모델이 취해야 할 페르소나 및 전문 분야를 서술합니다.
> 예: "당신은 10년 차 데이터 엔지니어입니다."

## 2. 배경 맥락 (Context & Background)
> 작업에 필요한 배경 지식, 도메인 컨텍스트, 대상 사용자 등을 기재합니다.

## 3. 작업 지시 (Instructions / Task)
> 수행해야 할 구체적인 작업을 단계별로 기술합니다.
> 1. 단계 1...
> 2. 단계 2...

## 4. 제약 사항 (Constraints & Guardrails)
> 하지 말아야 할 것 또는 반드시 지켜야 할 규칙을 작성합니다.
> - 예: 답변은 한국어로 작성할 것
> - 예: 외부 라이브러리는 표준 라이브러리만 사용할 것

## 5. 입력 형식 (Input Data)
```text
[입력 데이터 또는 플레이스홀더]
```

## 6. 출력 형식 (Output Format)
> 원하는 출력의 형태(JSON, Markdown 테이블, 보고서 형식 등)를 지정합니다.
""",

    "CHANGELOG.md": """# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-10-05

### Added
- 초기 프로젝트 디렉터리 및 템플릿 구조 생성 (`build_structure.py`)
- GitHub Issue Template: `prompt_issue_template.md`
- 웹 유틸리티 도구:
  - 대시보드 (`docs/index.html`)
  - JSON Formatter (`docs/tools/json-formatter.html`)
  - Text Diff Checker (`docs/tools/text-diff.html`)
- 프롬프트 라이브러리:
  - 코딩: `refactoring.md`, `code-review.md`
  - 작문: `summarizer.md`
  - 표준 템플릿: `prompt-template.md`
- 프로젝트 라이선스(MIT) 및 README 기본 문서화
""",

    "LICENSE": """MIT License

Copyright (c) 2026 my-ai-tools

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""",

    "README.md": """# 🚀 My AI Tools (`my-ai-tools`)

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
"""
}

def main():
    base_dir = Path(__file__).resolve().parent
    print(f"[1/3] 파일 및 폴더 생성 시작 (경로: {base_dir})")

    created_count = 0
    for rel_path, content in FILES.items():
        file_path = base_dir / rel_path
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        created_count += 1
        print(f"  + 생성 완료: {rel_path}")

    print(f"\\n총 {created_count}개 파일이 성공적으로 생성되었습니다.")

    print("\\n[2/3] Git 초기화 (git init)")
    try:
        res = subprocess.run(["git", "init"], cwd=base_dir, capture_output=True, text=True, check=True)
        print("  " + res.stdout.strip())
    except Exception as e:
        print(f"  git init 실행 중 오류 발생: {e}")

    print("\\n[3/3] 초기화 완료! 모든 구성이 준비되었습니다.")

if __name__ == "__main__":
    main()
