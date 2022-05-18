def seto(x):
  text = []
  for i in range(1, x+1):
      if i % 3 == 0:
          text.append('Frontend')
      elif i % 5 == 0:
          text.append('Backend')
      elif i % 3 == 0 and i % 5 == 0:
          text.append("FrontendBackend")
      else:
          text.append(str(i))
  return text
def main():
    print(', '.join(seto(50)))
main()