# Personal Portfolio - Industrial Automation Engineer

Website chuyên nghiệp được xây dựng bằng FastAPI, Python và Tailwind CSS dành cho kỹ sư tự động hóa công nghiệp.

## ✨ Tính năng
- 🏠 **Home Page** - Giới thiệu bản thân, slogan và chuyên môn chuyên sâu về AMR, cảm biến công nghiệp, giao tiếp công nghiệp và PLC
- 🎓 **Education** - Lịch sử học tập và bằng cấp dạng timeline
- 💼 **Career** - Quá trình làm việc và các dự án đã thực hiện
- 📰 **News** - Tin tức và xu hướng công nghiệp tự động hóa
- 📞 **Contact** - Thông tin liên hệ và form gửi tin nhắn

## 🚀 Công nghệ sử dụng
- **Backend**: FastAPI (Python)
- **Frontend**: Tailwind CSS 3, Jinja2 Templates
- **Database**: SQLAlchemy (sẵn sàng cho tương lai)
- **Icons**: Font Awesome 4.7
- **Server**: Uvicorn

## 📦 Cài đặt
```bash
# Clone repository
git clone https://github.com/Sivuu/Curriculum-Vitae.git
cd Curriculum-Vitae

# Cài đặt dependencies
pip install -r requirements.txt

# Chạy ứng dụng
python main.py
```

Mở trình duyệt truy cập: `http://localhost:8000`

## 🏗️ Cấu trúc project
```
Curriculum-Vitae/
├── main.py              # FastAPI application
├── requirements.txt     # Dependencies
├── app/
│   ├── templates/       # Jinja2 HTML templates
│   │   ├── base.html    # Base layout
│   │   ├── index.html   # Home page
│   │   ├── education.html
│   │   ├── career.html
│   │   ├── news.html
│   │   └── contact.html
│   └── static/          # Static files (css, js, images)
└── README.md
```

## 🔮 Tương lai phát triển
- [ ] Admin panel quản lý nội dung
- [ ] CSDL SQLite/PostgreSQL để quản lý tin tức, sự nghiệp
- [ ] Dashboard thống kê
- [ ] Blog hệ thống
- [ ] Tải lên hình ảnh và file
- [ ] Form liên hệ gửi email
- [ ] SEO tối ưu

## 📝 Ghi chú
Website đã được thiết kế theo chuẩn hiện đại, responsive trên mọi thiết bị, giao diện chuyên nghiệp phù hợp với ngành công nghiệp tự động hóa. Cấu trúc code được tổ chức rõ ràng dễ dàng để mở rộng và tùy chỉnh sau này.