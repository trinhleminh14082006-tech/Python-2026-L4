# ================= CẤU TRÚC DỮ LIỆU BAN ĐẦU =================
students_list = []  # Danh sách chứa tất cả sinh viên
courses_list = []   # Danh sách chứa tất cả môn học
marks_dict = {}     # Từ điển chứa điểm số: { ma_mon: { ma_sv: diem } }

# ================= CÁC HÀM NHẬP DỮ LIỆU (INPUT) =================

# 1. Hàm nhập số lượng và thông tin sinh viên: ID, Tên, Ngày sinh
def input_students():
    num_students = int(input("Nhập số lượng sinh viên trong lớp: "))
    for i in range(num_students):
        print(f"\n--- Nhập sinh viên thứ {i+1} ---")
        student_id = input("Mã sinh viên (ID): ")
        name = input("Tên sinh viên: ")
        dob = input("Ngày sinh (DoB): ")
        
        # Gom thông tin thành 1 từ điển rồi thêm vào danh sách tổng
        student = {"id": student_id, "name": name, "dob": dob}
        students_list.append(student)

# 2. Hàm nhập số lượng và thông tin môn học: ID, Tên môn
def input_courses():
    num_courses = int(input("Nhập số lượng môn học: "))
    for i in range(num_courses):
        print(f"\n--- Nhập môn học thứ {i+1} ---")
        course_id = input("Mã môn học (ID): ")
        name = input("Tên môn học: ")
        
        course = {"id": course_id, "name": name}
        courses_list.append(course)

# 3. Hàm chọn một môn học và nhập điểm cho từng sinh viên trong môn đó
def input_marks():
    if not courses_list or not students_list:
        print("⚠️ Vui lòng nhập danh sách môn học và sinh viên trước!")
        return

    print("\n--- Danh sách mã môn học hiện có ---")
    for c in courses_list:
        print(f"- {c['id']}: {c['name']}")
        
    course_id = input("Chọn mã môn học muốn nhập điểm: ")
    
    # Khởi tạo vùng chứa điểm cho môn học này nếu chưa có
    if course_id not in marks_dict:
        marks_dict[course_id] = {}
        
    print(f"\n--- Tiến hành nhập điểm cho môn {course_id} ---")
    for s in students_list:
        mark = float(input(f"Nhập điểm cho sinh viên {s['name']} (ID: {s['id']}): "))
        marks_dict[course_id][s['id']] = mark

# ================= CÁC HÀM HIỂN THỊ (LISTING) =================

# 4. Hàm liệt kê danh sách môn học
def list_courses():
    if not courses_list:
        print("⚠️ Danh sách môn học trống!")
        return
    print("\n=== DANH SÁCH MÔN HỌC ===")
    for c in courses_list:
        print(f"ID: {c['id']} | Tên môn: {c['name']}")

# 5. Hàm liệt kê danh sách sinh viên
def list_students():
    if not students_list:
        print("⚠️ Danh sách sinh viên trống!")
        return
    print("\n=== DANH SÁCH SINH VIÊN ===")
    for s in students_list:
        print(f"ID: {s['id']} | Tên: {s['name']} | Ngày sinh: {s['dob']}")

# 6. Hàm hiển thị bảng điểm của một môn học cụ thể
def show_marks_for_course():
    course_id = input("Nhập mã môn học muốn xem điểm: ")
    if course_id not in marks_dict:
        print("⚠️ Môn học này chưa được nhập điểm!")
        return
        
    print(f"\n=== BẢNG ĐIỂM MÔN HỌC: {course_id} ===")
    for s in students_list:
        diem = marks_dict[course_id].get(s['id'], "Chưa có")
        print(f"Sinh viên: {s['name']} (ID: {s['id']}) -> Điểm: {diem}")

# ================= MENU ĐIỀU KHIỂN CHÍNH =================

def main():
    while True:
        print("\n================ SYSTEM MENU ================")
        print("1. Nhập danh sách sinh viên")
        print("2. Nhập danh sách môn học")
        print("3. Nhập điểm môn học")
        print("4. Liệt kê danh sách sinh viên")
        print("5. Liệt kê danh sách môn học")
        print("6. Xem điểm theo môn học")
        print("0. Thoát chương trình")
        
        choice = input("Mời bạn chọn chức năng (0-6): ")
        
        if choice == "1": input_students()
        elif choice == "2": input_courses()
        elif choice == "3": input_marks()
        elif choice == "4": list_students()
        elif choice == "5": list_courses()
        elif choice == "6": show_marks_for_course()
        elif choice == "0": 
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!")

if __name__ == "__main__":
    main()
