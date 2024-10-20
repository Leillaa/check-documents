Приложение конвертирует файлы с различными расширениями в питоновский объект (список).

Для запуска необходимо:

1) Затем устанавливаем Tesseract и копируем путь до exe файла в файл constants.py, и заменяем константу PATH_TO_TESSERACT.
Сcылка на Tesseract - https://github.com/UB-Mannheim/tesseract/wiki

2) Также нужно скачать Poppler и скопировать путь до содержимого папки bin в константу POPPLER_PATH.
Ccылка на Poppler - https://github.com/oschwartz10612/poppler-windows/releases/

3) Установить зависимости из файла requirements.txt
pip install -r requirements.txt

4) Указать путь до файла, который вы хотите конверировать в текст, в главной функции get_text в файлу main.py

В основной папке уже есть несколько простейших файлов для тестирования.
