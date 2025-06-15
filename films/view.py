def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output

        return wrap

    return wrapper


class UserInterface:
    @add_title("Ввод пользовательских данных")
    def wait_user_answer(self):
        # print(" Ввод пользовательских данных ".center(50, "="))
        print("1 - добавление фильма"
              "\n2 - каталог фильмов"
              "\n3 - просмотр определённого фильма"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        print("Действие с фильмами:")
        user_answer = input("Выберите вариант действия: ")
        # print("=" * 50)
        return user_answer

    @add_title("Создание статьи:")
    def add_user_film(self):
        dict_film = {
            "- название фильма": None,
            "- жанр": None,
            "- режиссёр": None,
            "- год выпуска": None,
            "- длительность": None,
            "- студия": None,
            "- актёры": None,
        }
        # print(" Создание статьи: ".center(50, "="))
        for key in dict_film:
            dict_film[key] = input(f"Введите {key}: ")
        # print("=" * 50)
        return dict_film

    @add_title("Список фильмов:")
    def show_all_films(self, articles):
        # print(" Список статей ".center(50, "="))
        for ind, article in enumerate(articles, 1):
            print(f"{ind}. {article}")
        # print("=" * 50)

    @add_title('Ввод названия фильма:')
    def get_user_film(self):
        return input('Введите название фильма: ')

    @add_title("Просмотр фильма:")
    def show_single_film(self, film):
        for key in film:
            print(f"{key} фильма - {film[key]}")

    @add_title("Сообщение об ошибке:")
    def show_incorrect_title_error(self, user_title):
        print(f"Фильм {user_title} не существует")

    @add_title("Удаление фильма")
    def remove_single_film(self, film):
        print(f"Фильм {film} - был удален.")

    @add_title("Сообщение об ошибке:")
    def show_incorrect_answer_error(self, answer):
        print(f"Варианта {answer} не существует")

