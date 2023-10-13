# TODO Найдите количество книг, которое можно разместить на дискете

disk_mb = 1.44
page_count = 100
number_of_lines = 50
number_of_characters = 25
bite = 4

number_of_book = number_of_characters * number_of_lines * page_count

bite_in_book = number_of_book * bite

size_disk = int (disk_mb * 1024 * 1024)

number_of_books_disk = size_disk // bite_in_book

print("Количество книг, помещающихся на дискету:", number_of_books_disk)
