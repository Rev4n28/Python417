from dz0806_parser import Parser


def main():
    #  Сайт 1
    pars = Parser("https://www.ixbt.com/live/", "news.txt")

    #  Сайт 2
    # pars = Parser("https://www.mariinsky.ru/", "performances.csv")
    #  Сайт 3
    # pars = Parser("https://planetavto.ru/catalog/avtokhimiya-dlya-kuzova/", "store.json")

    pars.run()


if __name__ == "__main__":
    main()
