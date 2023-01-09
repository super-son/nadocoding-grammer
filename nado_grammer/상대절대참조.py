import pygame

#상대경로를 받으면 절대경로를 반환해주는 역할!
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#사용예제
background = pygame.image.load(r"C:\Users\hj144\Desktop\Coding\Python\pygame\nado_project\images\background.png")
#여기에 접목시키면
background = pygame.image.load(resource_path(r"C:\Users\hj144\Desktop\Coding\Python\pygame\nado_project\images\background.png"))
print("hi") # 일단은 요론 느낌인듯