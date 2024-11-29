# α���룺�û���¼
def user_login(username, password):
    user = database.query("SELECT * FROM users WHERE username = ?", username)
    if user and user.password == password:
        return {"status": "success", "token": generate_token(user)}
    else:
        return {"status": "fail", "message": "Invalid credentials"}

# α���룺��������
def generate_token(user):
    return jwt.encode({"user_id": user.id}, SECRET_KEY, algorithm="HS256")

# α���룺��ӷ��յ�
def add_risk_point(risk_data):
    if validate_risk_data(risk_data):
        database.insert("INSERT INTO risk_points (field, value) VALUES (?, ?)", risk_data)
        return {"status": "success"}
    else:
        return {"status": "fail", "message": "Invalid risk data"}
    
# α���룺��֤��������
def validate_risk_data(risk_data):
    # ��֤�߼�
    return True  # �� False

# α���룺��������
def relate_data(data_id, related_data):
    database.update("UPDATE data SET related_data = ? WHERE id = ?", related_data, data_id)
    return {"status": "success"}

# α���룺���ɷ�����������
def generate_risk_report(risk_data):
    report = generate_report_template()
    report.add_section("Risk Analysis", risk_data)
    return report.generate_pdf()

