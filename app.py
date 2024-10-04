from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# تعريف التطبيق
app = Flask(__name__)

# وظيفة للحصول على قائمة الطلبات من قاعدة البيانات
def get_properties(status=None, location=None):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    query = 'SELECT * FROM properties WHERE 1=1'
    params = []

    # تصفية حسب الحالة
    if status:
        query += ' AND status = ?'
        params.append(status)

    # تصفية حسب الموقع
    if location:
        query += ' AND location = ?'
        params.append(location)

    c.execute(query, params)
    properties = c.fetchall()
    conn.close()
    return properties

# وظيفة لتحديث حالة العقار
def update_property_status(property_id, status):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('UPDATE properties SET status = ? WHERE id = ?', (status, property_id))
    conn.commit()
    conn.close()

# صفحة لوحة التحكم
@app.route('/')
def admin_panel():
    # الحصول على العقارات المعلقة والمرتبطة بالقاهرة والجيزة
    pending_properties = get_properties(status='معلق')
    cairo_properties = get_properties(location='القاهرة')
    giza_properties = get_properties(location='الجيزة')
    return render_template('admin.html', 
                           pending_properties=pending_properties, 
                           cairo_properties=cairo_properties, 
                           giza_properties=giza_properties)

# معالجة طلبات الموافقة أو الرفض
@app.route('/update_status/<int:property_id>/<status>')
def update_status(property_id, status):
    update_property_status(property_id, status)
    return redirect(url_for('admin_panel'))

if __name__ == '__main__':
    app.run(debug=True)
