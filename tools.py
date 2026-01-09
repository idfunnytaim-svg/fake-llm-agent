# 대전, 강릉일 때 입력이 수정되게 하고 있습니다.
def fake_tool():
  return "result"

def get_weather(location):
  if location == "seoul":
    return "sunny"
  elif location == "daejeon":
    return "gloomy"
  elif location == "gangneoung":
    return "rainy"
  return "unknown"
