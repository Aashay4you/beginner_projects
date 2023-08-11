# #Robo_speaker (project1)
# import os
# if __name__ == '__main__':
#     print("Welcome to Robo_speaker created by aashay(09/08/23")
#     while True:
#         x=input("Enter what you want me to pronounce:")
#         if x== "q":
#             break
#         command=f"google_speech {x}"
#         os.system(command)
#
import win32com.client as wincom

# you can insert gaps in the narration by adding sleep calls
# import time

speak = wincom.Dispatch("SAPI.SpVoice")

text = input("Enter what you want to pronounce:")
speak.Speak(text)

# # 3 second sleep
# time.sleep(3)
#
# text = "This text is read after 3 seconds"
# speak.Speak(text)
