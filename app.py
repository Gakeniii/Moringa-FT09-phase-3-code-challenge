from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    if not(author_name and magazine_name and magazine_category and article_title and article_content):
        print("All fields are required. Please try again.")
        return
    
    author = Author(None, name=author_name)
    magazine = Magazine(name=magazine_name, category=magazine_category)
    article = Article(author=author, magazine=magazine, title=article_title)

    try:
        author.save()
        magazine.save()
        article.save()
    except Exception as e:
        print(f"An error occured: {str(e)}")
        return
    
    # Display results
    print("\nMagazines:")
    for magazine in Magazine.get_all():
        print(Magazine(magazine["id"], magazine["name"], magazine["category"]))

    print("\nAuthors:")
    for author in Author.get_all():
        print(Author(author["id"], author["name"]))

    print("\nArticles:")
    for article in Article.get_all():
        print(Article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]))

    # # Connect to the database
    # conn = get_db_connection()
    # cursor = conn.cursor()


    # '''
    #     The following is just for testing purposes, 
    #     you can modify it to meet the requirements of your implmentation.
    # '''

    # # Create an author
    # cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
    # author_id = cursor.lastrowid # Use this to fetch the id of the newly created author

    # # Create a magazine
    # cursor.execute('INSERT INTO magazines (name, category) VALUES (?,?)', (magazine_name, magazine_category))
    # magazine_id = cursor.lastrowid # Use this to fetch the id of the newly created magazine

    # # Create an article
    # cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
    #                (article_title, article_content, author_id, magazine_id))

    # conn.commit()

    # # Query the database for inserted records. 
    # # The following fetch functionality should probably be in their respective models

    # cursor.execute('SELECT * FROM magazines')
    # magazines = cursor.fetchall()

    # cursor.execute('SELECT * FROM authors')
    # authors = cursor.fetchall()

    # cursor.execute('SELECT * FROM articles')
    # articles = cursor.fetchall()

    # conn.close()



if __name__ == "__main__":
    main()
