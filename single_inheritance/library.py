class Library:
    def count_total_books(self):
        return 100
    
class DepartmentLibrary (Library):
    def count_books(self):
        return 30

books = DepartmentLibrary()

print (f"{books.count_total_books()} total books in the library")

print (f"{books.count_books()} books in the department library")




