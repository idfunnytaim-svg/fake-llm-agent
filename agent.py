from tools import get_weather


class LlmAgent:
  def handle(self, user, message):
    if "weather" in message:
      weather = get_weather("seoul")
      return f"{user} is '{weather}'"
    # 아주 단순한 LLM 흉내
    return f"{user}님, '{message}' 잘 받았습니다."