import sqlite3

def read_table_posts():
    with sqlite3.connect('/home/jod/crawlers/folha_de_sao_paulo/posts.db') as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM posts""")
        rows = cursor.fetchall()
        rows = [dict(post) for post in rows if len(post["title"]) != 0]
        return rows

if __name__ == "__main__":
    posts_data = read_table_posts()
    print(posts_data)