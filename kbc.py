from gtts import gTTS
import os
import pygame
language = 'en'

pygame.mixer.init()
pygame.init()

ques=[["Which god is also known as \'Gauri Nandan\'?",
        "Agni","Indra","Hanuman","Ganesha",
        "Ganesha"],

      ["What does not grow on tree according to a popular Hindi saying",
       "Money","Flowers","Leaves","Fruits",
       "Money"],

      ["Which city is known as the Pink City of India?",
       "Banglore","Maysore","Jaipur","Kochi",
       "Jaipur"],

      ["Who wrote India's National Anthem?",
       "Rabindranath Tagore","Lal Bahadur Shastri","Chetan Bhagat","RK Narayan",
       "Rabindranath Tagore"],

      ["Current Railway Minister of India is",
       "Mamta Banarjee","Ram Vilash","Ashwini Vaishnaw","Piyush Goyal",
       "Ashwini Vaishnaw"],

      ["How many major religions are there in India?",
       "6","7","8","9",
       "6"],

      ["When is the National Hindi Diwas celebrated?",
       "13 September","14 September","14 July","15 August",
       "14 September"],

      ["How many states are there in India?",
       "28","29","30","31",
       "28"],

      ["Where is India Gate located?",
       "Agra","Punjab","Mumbai","New Delhi",
       "New Delhi"],

      ["Who wrote Vande Mataram?",
       "Sarat Chandra Chattopadhyay","Rabindranath Tagore","Bankim Chandra Chatterjee","Ishwar Chandra Vidyasagar",
       "Bankim Chandra Chatterjee"],

      ["Which one of the following places is famous for the Great Vishnu Temple?",
       "Bordubar, Indonesia","Bamiyan, Afghanistan","Panja Sahib, Pakistan","Ankorvat, Cambodia",
       "Ankorvat, Cambodia"],

      ["Where is the largest Buddhist Monastery in India located?",
       "Sarnath, Uttar Pradesh","Tawang, Arunachal Pradesh","Dharmashala, Himachal Pradesh","Gangtok, Sikkim",
       "Tawang, Arunachal Pradesh"],

      ["Which Indian monument was originally built as a victory tower to commemorate the defeat of the Khan of Khambhat?",
       "Qutub Minar","India Gate","Charminar","Vijay Stambha",
       "Vijay Stambha"]]

money=["5,000","10,000","20,000","40,000","80,000","160,000","320,000","640,000","1,250,000","2,500,000","5,000,000","1 Crore","5 Crore"]

cash=0
cash_price=0
print("Let's Start".center(50))

for i in range(len(ques)):
  s1=f"\nQuestion {i+1} for Rs. {money[i]}\n"
  myobj = gTTS(text=s1, lang=language, slow=False)
  myobj.save(f"s1.mp3")
  pygame.mixer.music.load('s1.mp3')
  pygame.mixer.music.play(100)
  print(f"\nQuestion {i+1} for Rs. {money[i]}\n")
  s2=f"{i+1}. {ques[i][0]}"
  myobj = gTTS(text=s2, lang=language, slow=False)
  myobj.save(f"s2.mp3")
  pygame.mixer.music.load('s2.mp3')
  print(f"{i+1}. {ques[i][0]}")

  s=set([ques[i][1],ques[i][2],ques[i][3],ques[i][4]])
  A,B,C,D=s
  s3=f"A. {A}\nB. {B}"
  myobj = gTTS(text=s3, lang=language, slow=False)
  myobj.save(f"s3.mp3")
  pygame.mixer.music.load('s3.mp3')
  pygame.mixer.music.play(100)
  print(f"A. {A}\nB. {B}")
  s4=f"C. {C}\nD. {D}"
  myobj = gTTS(text=s4, lang=language, slow=False)
  myobj.save(f"s4.mp3")
  pygame.mixer.music.load('s4.mp3')
  print(f"C. {C}\nD. {D}")

  choice=input()

  if((choice =='A' or choice == 'a') and A == ques[i][5]) or ((choice =='B' or choice == 'b') and B == ques[i][5]) or ((choice =='C' or choice == 'c') and C == ques[i][5]) or ((choice =='D' or choice == 'd') and D == ques[i][5]):
    s5="Congratulation Right Aswer!"
    myobj = gTTS(text=s5, lang=language, slow=False)
    myobj.save(f"s5.mp3")
    pygame.mixer.music.load('s5.mp3')
    print("\nCongratulation Right Aswer!")
    cash=money[i]
    if cash == "10,000":
      cash_price = "10,000"
      s6="You win Rs. 10,000"
      myobj = gTTS(text=s6, lang=language, slow=False)
      myobj.save(f"s6.mp3")
      pygame.mixer.music.load('s6.mp3')
      print(f"\nYou win Rs. {cash}")
    elif cash == "320,000":
      cash_price = "320,000"
      s7="You win Rs. 320,000"
      myobj = gTTS(text=s7, lang=language, slow=False)
      myobj.save(f"s7.mp3")
      pygame.mixer.music.load('s7.mp3')
      print(f"\nYou win Rs. {cash}")
    elif cash == "1 Crore":
      cash_price = "1 Crore"
      s8="You win Rs. 1 Crore"
      myobj = gTTS(text=s8, lang=language, slow=False)
      myobj.save(f"s8.mp3")
      pygame.mixer.music.load('s8.mp3')
      print(f"\nYou win Rs. {cash}")
    elif cash == "5 Crore":
      s9="You win Rs. 5 Crore"
      myobj = gTTS(text=s9, lang=language, slow=False)
      myobj.save(f"s9.mp3")
      pygame.mixer.music.load('s9.mp3')
      print(f"\nYou win Rs. {cash}")
      cash_price = "5 Crore" 
  else:
    if(cash_price!="5 Crore"):
      s10="Sorry Wrong Answer"
      myobj = gTTS(text=s10, lang=language, slow=False)
      myobj.save(f"s10.mp3")
      pygame.mixer.music.load('s10.mp3')
      print("\nSorry Wrong Answer")
    break

  

  