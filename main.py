from agent import LlmAgent

def do_stash():
  print("git stash")

if __name__ == "__main__":
  agent = LlmAgent()
  reply = agent.handle("hong", "weather은 어떄?")
  print("응답:", reply)