from openai import OpenAI

client = OpenAI()

# OpenAI의 gpt-5-mini 모델을 사용하여 응답 생성
def chatbot_response(user_message: str):
    result = client.responses.create(model="gpt-5-mini", input=user_message)
    return result

if __name__ == "__main__":
    try:
        # 사용자의 메세지를 입력받고 응답을 출력합니다    
        while True:
            # 사용자에게 메세지 입력받기
            user_message = input("메세지: ")
            # 'exit' 입력 시 대화 종료
            if user_message.lower() == "exit":
                print("대화를 종료합니다.")
                break
            
            # 챗봇 응답받아오기
            result = chatbot_response(user_message)
            print("챗봇: " + result.output_text)
    except KeyboardInterrupt as e:
        print("대화를 종료합니다.")