class Settings():
    """Клас для зберігання налаштувань програми ImageToGcode."""

    def __init__(self):
        """Ініціалізує налаштування програми."""
        # max_Z=5, koef=4 pix/mm, ris=1, z_safe=0.5, feed_z=1000

        # Параметри для станка
        self.W_size = 0
        self.H_size = 0
        self.z_safe = 1
        self.feed_z = 1000
        self.depth_Z = 5


        # В програму вносяться координати величина яких >= filtr_z
        self.filtr_z = 0

        # Параметри для зображення
        self.koef = 1

        # Параметри для виводу обробленого зображення
        self.ris = 1
