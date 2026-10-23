from langchain.chat_models import init_chat_model

model = init_chat_model("gpt-5-mini", model_provider="openai") # LLM 초기화
result = model.invoke("랭체인이 뭔가요?") # 모델 실행
print(type(result)) # AIMessage 타입
print(result.content) # 결과값