import ollama

with open('chaptersPlants.txt') as f:
    while True:
      chapterName = f.readline()
      if not chapterName:
          break
      prompt = f"I am writing a book about plants. Write the following chapter: {chapterName}"
      response = ollama.chat(model='llama2', messages=[
        {
          'role': 'user',
          'content': prompt,
        },
      ])
      print("-----------------------------------")
      print(chapterName)
      print(response['message']['content'])
    
