import sqlite3

# إنشاء اتصال بقاعدة البيانات
conn = sqlite3.connect('database.db')
c = conn.cursor()

# إنشاء جدول العقارات
c.execute('''
    CREATE TABLE IF NOT EXISTS properties (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        details TEXT NOT NULL,
        location TEXT NOT NULL,
        type TEXT NOT NULL,
        status TEXT NOT NULL
    )
''')

# حفظ التغييرات وإغلاق الاتصال
conn.commit()
conn.close()
