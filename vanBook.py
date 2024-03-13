import ollama

with open('chaptersVan.txt') as f:
    while True:
      chapterName = f.readline()
      if not chapterName:
          break
      prompt = f"I am writing a book about converting a van to live in. Write the following chapter: {chapterName}"
      response = ollama.chat(model='llama2', messages=[
        {
          'role': 'user',
          'content': prompt,
        },
      ])
      print("-----------------------------------")
      print(chapterName)
      print(response['message']['content'])
    
