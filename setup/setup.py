class Setup:

    # ФПС
    FPS = 60

    # Ширина и высота окна для оконного режима
    screen_width = 1024
    screen_height = 768

    # Скорость движения площадки за мышью, по горизонтали
    # Выше значение = быстрей перемещение
    speed_player = 64

    # Коррекция угла отбоя шара
    angle_correction = 360

    # Начальная скорость движения шара
    speed_ball_x = 0
    speed_ball_y = 0
    ball_acceleration = 9.8

    # Гашение скорости при вертикальном отскоке
    correct_up = 0.8

    # Модификатор ускорения в зависимости от энергии
    # Больше - больше энергии при отскоке
    multiple_energy = 100

    # Максимальная энергия для отскока
    max_energy_player = 32

    # Каждые X очков добавляется ещё один корабль пришельцев
    # Далее будет каждые adding_nlo * adding_nlo_multiply
    start_count_nlo = 2
    adding_nlo = 4
    adding_nlo_multiply = 3

    # Количество звёзд по фону
    stars = 300

    # Цвета
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
