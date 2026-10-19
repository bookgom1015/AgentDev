from openai import OpenAI
import rich

client = OpenAI()

default_model = "gpt-5-mini"

# chat.completions API를 사용한 스트리밍 응답 함수
def stream_chat_completion(prompt, model):
    stream = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )
    for chunk in stream: # 응답 청크를 하나씩 처리
        content = chunk.choices[0].delta.content
        if content is not None:
            print(content, end="")
    
# 새로운 리스폰스 API를 상요ㅛ한 스트리밍 함수(컨텍스트 매니저로 스트림 관리)        
def stream_resonse(prompt, model):
    with client.responses.stream(model=model, input=prompt) as stream:
        for event in stream: # 스트림에서 발생하는 각 이벤트 처리
            if "output_text" in event.type: # 텍스트 출력 이벤트인 경우
                rich.print(event)
    rich.print(stream.get_final_response()) # 최종 응답 출력
    
if __name__ == "__main__":
    stream_chat_completion("스트리밍이 뭔가요?", default_model)
    stream_resonse("점심 메뉴 추천해주세요.", default_model)
    