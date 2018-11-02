# sql-operate.py 

## 数据表变量

### 公寓 apartment

* 编号 apartment_id
* 名称 apartment_name
* 地址 apartment_dir
* 层数 floor

### 楼层 floor

* 编号 floor_id
* 层号 floor_num
* 寝室数 room_count

### 寝室 room

* 编号 id
* 室号 room_id
* 入住学生数 student_count
* 面向 face
* 朝向 orientatin

### 学生 student

* 学号 student_num
* 名字 name
* 性别 gender
* 入住日期 stay_time

### 班级 class

* 班号 class_num
* 班名 class_name
* 专业 profession
* 年级 grade

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

### 财产管理 apartment_manage

* 编号 id
* 名称 name
* 价值 value

### 来访登记 visit_register

* 身份证号 id
* 名字 name
* 单位 location
* 来访时间 visit_time
* 离开时间 quit_time

## 主要sql操作函数

* search
* room_allocation
* information_search
* property_manage
* outside_man
* cargo