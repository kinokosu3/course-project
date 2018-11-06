# exists.py

## 验证数据是否在数据库内

# 其他为功能数据库操作

# sqlcreate.py 

## 数据表变量

### 系统管理 user
* 账号 username
* 密码 password
### 公寓 apartment

* 编号 apartment_id
* 名称 apartment_name 主键
* 地址 apartment_dir
* 层数 floor

### 楼层 floor

* 编号 floor_id
* 层号 floor_num
* 寝室数 room_count
* 公寓名 apartment_name

### 寝室 room

* 编号 id
* 室号 room_id
* 入住学生数 student_count
* 面向 face
* 朝向 orientatin
* 楼层 floor_num
* 公寓名 apartment_name

### 学生 student

* 学号 student_num
* 名字 name
* 性别 gender
* 入住日期 stay_time
* 宿舍号 room_id
* 班别 class_num
* 院系 department_name
* 公寓楼号 apartment_name

### 班级 class

* 班号 class_num
* 班名 class_name
* 专业 profession
* 年级 grade
* 院系 department_name

### 院系 department

* 系号 department_num
* 系名 department_name
* 系主任 department_leader

### 货物登记 cargo_register

* 编号 id
* 货物号 cargo_id
* 时间日期 time
* 来源 origin
* 去处 direction
* 负责人 duty_man
* 公寓楼号 apartment_name

### 财产管理 apartment_manage

* 编号 id
* 名称 name
* 价值 value
* 公寓楼号 apartment_name

### 来访登记 visit_register

* 身份证号 id
* 名字 name
* 单位 location
* 来访时间 visit_time
* 离开时间 quit_time
* 公寓楼号 apartment_name
