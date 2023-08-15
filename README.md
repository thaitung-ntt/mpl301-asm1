# Test Grade Calculator

Test Grade calculator là phần mềm chấm điểm học sinh, cho phép:
* Nhập file câu trả lời của các học sinh thuộc 1 lớp, mỗi học sinh thuộc 1 dòng.
* Đếm số dòng đúng định dạng, số dòng không đúng định dạng, report các dòng không đúng.
* Với các dòng đúng định dạng, tính và report mean, max, min, range và median.
* Lưu điểm của các học sinh vào 1 file định dạng txt.

## Cài đặt thư viện cần thiết:
```
pip install numpy
pip install pandas
```

## Chạy chương trình:
`python lastname_firstname_grade_the_exams.py`

Sau đó nhập tên file chứa điểm của học sinh. Ví dụ với file **file1.txt** ta chỉ nhập **file1**.

## Định dạng của file nhập vào:
* File có định dạng txt.
* Mỗi hàng chứa mã ID của học sinh, theo sau là câu trả lời của 25 câu hỏi, cách nhau bởi dấu phẩy. 
* ID: Ký tự N, theo sau là 8 ký tự số.
* Câu học sinh không trả lời thì để trống.
Ví dụ: N12345678,B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D

## Định dạng của file xuất ra:
* File có định dạng txt.
* Mỗi hàng chứa ID và điểm của học sinh.
Ví dụ: N00000001,59

## Github
[Github](https://github.com/thaitung-ntt/mpl301-asm1.git)

## License
Test Grade Calculator là phần mềm miễn phí, bạn có thể sử dụng và chỉnh sửa cho mục đích cá nhân và thương mại.