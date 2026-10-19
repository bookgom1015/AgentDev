import asyncio
import os

from openai import AsyncOpenAI

# 비동기 클라이언트 생성
openai_client = AsyncOpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# await를 상요해 비동기적으로 API 응답을 기다림
async def call_async_openai(prompt: str, model: str = "gpt-5-mini") -> str:
    response = await openai_client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

async def main():
    print("동시에 API 호출하기")
    prompt = "비동기 프로그래밍에 대해 두세 문장으로 설명해주세요."
    # 비동기 함수 호출 시 코루틴 객체 반환(실행은 아직 안 됨)
    openai_task = call_async_openai(prompt)
    print("대기 중...")
    # 호출을 병렬로 실행하고 완료될 때까지 대기
    openai_response = await asyncio.gather(openai_task)
    print(f"OpenAI 응답: {openai_response}")
    
if __name__ == "__main__":
    asyncio.run(main()) # 비동기 메인 함수를 이벤트 루프에서 실행