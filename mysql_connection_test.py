import mysql.connector, datetime

connection = mysql.connector.connect(host="localhost",
                                     port="3306",
                                     database="summarizer",
                                     user="root",
                                     password="Gisprog_1")

def main():
    cursor = connection.cursor()

    selectQuery = "SELECT * FROM USER"

    cursor.execute(selectQuery)
    rows=cursor.fetchall()

    print(f"Number of rows retrieved from user table: {cursor.rowcount}")
    print()

    for row in rows:
        print(f"user_id:    {row[0]}")
        print(f"username:   {row[1]}")
        print(f"password:   {row[2]}")
        print()

    selectQuery = \
    "SELECT * FROM summary JOIN user ON summary.user_id = user.user_id \
    WHERE user.user_id = 1"

    cursor.execute(selectQuery)
    rows=cursor.fetchall()

    print(f"Number of rows retrieved from summary table: {cursor.rowcount}")
    print()

    for row in rows:
        print(f"summary_id:     {row[0]}")
        print(f"date_created:   {row[1]}")
        print(f"article_text:   {row[2]}")
        print(f"article_url:    {row[3]}")
        print(f"summary_text:   {row[4]}")
        print(f"summary_length: {row[5]}")
        print(f"user_id: {row[6]}")
        print()

    #selectQuery = "INSERT INTO user VALUES (4, 'pwhite', 'password04');"

    #cursor.execute(selectQuery)
    #connection.commit()

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
