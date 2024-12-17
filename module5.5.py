from time import sleep
class User:
   def __init__(self,nickname, password, age):
       self.nickname=nickname
       self.password=password
       self.age=age
   def __str__(self):
       return self.nickname
class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode= adult_mode
class UrTube:
    def __init__(self):
       self.users= []
       self.videos = []
       self.current_user = None
    def log_in (self,nickname, password):
         for user in self.users:
            if user.nickname == nickname and user.password==password:
               self.current_user = user
    def register(self,nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь: {nickname} уже существует")
                break
        else:
            uuser=User(nickname, password, age)
            self.users.append(uuser)
            self.current_user = uuser
    def log_out(self):
        self.current_user = None
    def add(self, *videos):
        for video in videos:
            if video in  self.videos:
                continue
            else:
                self.videos.append(video)
    def get_videos(self,key_word):
        love_key=key_word.lower()
        key_number=[]
        for video in self.videos:
            if love_key in video.title.lower():
                key_number.append(video.title)
        return key_number
    def watch_video(self,title):
        if not self.current_user:
            print(f"Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode == True and self.current_user.age <18:
                    print(f"Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                for i in range(video.duration):
                    sleep(1)
                    video.time_now+=1
                    print(video.time_now,end = " ")# пробелами
                video.time_now = 0
                print("Конец видео")
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# Добавление видео
ur.add(v1, v2)
# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')