# 프롬프트 템플릿 표준 서식 (Standard Prompt Template)

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
