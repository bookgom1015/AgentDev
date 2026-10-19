from openai import OpenAI

client = OpenAI(); # OpenAI 클라이언트 초기화

# 입력된 프롬프트에 데한 AI 응답을 받아오는 함수
def get_responses(prompt, model="gpt-5-mini"):
    response = client.responses.create(
        model=model, # 사용할 모델 지정
        tools=[{"type": "web_search_preview"}], # 웹 검색 도구 활성화
        input=prompt # 사용자 입력 전달
    )
    return response.output_text # 텍스트 응답만 반환

# 스크립트가 직접 실행될 때 실행
if __name__ == "__main__":
    prompt = """https://platform.openai.com/docs/api-reference/response/create 를 읽어서 리스폰스 API에 대해 요약 정리해주세요."""
    
    output = get_responses(prompt)
    print(output)