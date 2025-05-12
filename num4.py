from typing import List, Dict, Optional

class MusicGroup:

    # Атрибуты класса
    total_groups = 0
    available_genres = ["Rock", "Pop", "Jazz", "Hip-Hop", "Electronic"]

    def __init__(self, group_name: str, foundation_year: int, artist_list: List[str],
                 music_style: str, discography_count: int = 0) -> None:
       
        self.group_name = group_name
        self.foundation_year = foundation_year
        self.artist_list = artist_list
        self.music_style = music_style
        self.discography_count = discography_count
        self.currently_active = True

        MusicGroup.total_groups += 1

    def __str__(self) -> str:
        """Строковое представление группы"""
        activity_status = "активна" if self.currently_active else "неактивна"
        return (f"Группа '{self.group_name}' ({self.music_style}), основана в {self.foundation_year}. "
                f"Состав: {', '.join(self.artist_list)}. Статус: {activity_status}")

    def add_artist(self, new_artist: str) -> None:
        """Добавляет нового участника в группу"""
        self.artist_list.append(new_artist)
        print(f"{new_artist} присоединился к группе {self.group_name}")

    def record_album(self) -> None:
        """Увеличивает счетчик выпущенных альбомов"""
        self.discography_count += 1
        print(f"{self.group_name} выпустила новый альбом! Всего альбомов: {self.discography_count}")

    def break_up(self) -> None:
        """Деактивирует группу"""
        self.currently_active = False
        print(f"Группа {self.group_name} прекратила существование")

    def calculate_years_active(self, current_year: int) -> int:
        """Вычисляет сколько лет группа существует"""
        if current_year < self.foundation_year:
            raise ValueError("Текущий год не может быть меньше года основания")
        return current_year - self.foundation_year

    @classmethod
    def get_genre_data(cls) -> Dict[str, int]:
        """Возвращает информациб о жанрах в виде словаря"""
        return {style: index + 1 for index, style in enumerate(cls.available_genres)}


fab_four = MusicGroup("The Beatles", 1960, ["John Lennon", "Paul McCartney","George Harrison", "Ringo Starr"], "Rock", 12)

floyd = MusicGroup("Pink Floyd", 1965, ["Roger Waters", "David Gilmour","Nick Mason", "Richard Wright"], "Progressive Rock", 15)

print(fab_four)
print(floyd)

fab_four.add_artist("Billy Preston")
floyd.record_album()

print(f"\nГруппа {fab_four.group_name} существует {fab_four.calculate_years_active(2025)} лет")
print(f"Всего групп создано: {MusicGroup.total_groups}")
print(f"Доступные жанры: {MusicGroup.available_genres}")

floyd.break_up()
print(floyd)