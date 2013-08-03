'''
Created on 31/07/2013

@author: luke

IDoes the ISBN-13 have any meaning imbedded in the numbers?
    The five parts of an ISBN are as follows:
    1. The current ISBN-13 will be prefixed by "978"
    2. Group or country identifier which identifies a national or geographic grouping of publishers;
    3. Publisher identifier which identifies a particular publisher within a group;
    4. Title identifier which identifies a particular title or edition of a title;
    5. Check digit is the single digit at the end of the ISBN which validates the ISBN.
'''
import random
import unittest
from library_catalog import Book, Library

class TestBook(unittest.TestCase):
    """
    A book should have a title, an ISBN, an author, a genre
    """
    _book      = Book(title="Book Tests", isbn="0000111125433",
                           author="Book Writer", genre="Educational",)
    _class_vars= vars(_book)
    
#    def testInit(self):
#        """
#        On creation a book should have a title,
#        an ISBN, an author, and a genre
#        """
        

    def testTitle(self):
        def set_title(title):
            self._book.title    = title
        """
        A book should have a title when it is created;
        the title of a book should not be able to change
        as this would imply a new book has been created
        """
        
        title       = '_title'
        # ensure book has a title
        self.assertIn(title,self._class_vars)
        self.assertNotEqual(self._class_vars[title],'','Expected legitimate title')
        # test if setting title fails
        with self.assertRaises(AttributeError):
            set_title('should_fail')
        self.assertEqual("Book Tests",self._book.title)
        
    def testISBN(self):
        def set_isbn(num):
            self._book.isbn     = num
        def bad_impl():
            Book("title","123456789","author","genre")
        """
        An ISBN number is 13 numbers long
        A book should have an ISBN when created
        the ISBN of a book should not be able to change
        """
        isbn        = '_isbn'
        isbn_num    = "0000111125433"
        self.assertIn(isbn,self._class_vars)
        self.assertEqual(self._class_vars[isbn],isbn_num)
        self.assertEqual(len(self._class_vars[isbn]),13)
        # ISBN should be 13 chars long
        with self.assertRaises(AttributeError):
            bad_impl()
            set_isbn('someNumber')
        self.assertEqual("0000111125433",self._book.isbn)
        
    def testAuthor(self):
        def set_author(author):
            self._book.author   = author
        """
        A book should have an author upon creation
        the author of a book should not be able to change
        """
        author      = '_author'
        self.assertIn(author,self._class_vars)
        self.assertNotEqual(self._class_vars[author],'')
        with self.assertRaises(AttributeError):
            set_author('fail')
        self.assertEqual("Book Writer",self._book.author)
        
    def testGenre(self):
        def set_genre(x):
            self._book.genre = x
        self.assertEqual("Educational",self._book.genre)
        with self.assertRaises(AttributeError):
            set_genre('fail')
        
class TestLibrary(unittest.TestCase):        
    """
    A library should have a listing of all books the library owns;
    the books available for hire; the books that are currently being
    hired; the ability to check in and check out books; the ability
    to add/remove books from the library permanently.
    """
    gen_isbn    = lambda size: "".join([str(random.randint(0,9)) for _ in range(size)])
    _library    = Library()
    __books     = [
                   Book("book_two",gen_isbn(13),"author_two","genre_two"),
                   Book("book_three",gen_isbn(13),"author_three","genre_three"),
                   Book("book_four",gen_isbn(13),"author_four","genre_four"),
                   Book("book_five",gen_isbn(13),"author_five","genre_five"),
                   Book("book_six",gen_isbn(13),"author_six","genre_six"),
                   Book("book_seven",gen_isbn(13),"author_seven","genre_seven"),
                   ]
    
    def testAddBooks(self):
        """
        should be able to add books to library catalog. Should only accept
        books; should return True to indicate success
        """
        self.assertRaises(TypeError,self._library.add_books("NOT A BOOK LOLOLOLOL"))
        self.assertTrue(self._library.add_books(book for book in self.__books))
        
                
    
    
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()