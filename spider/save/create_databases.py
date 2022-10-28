# coding: utf8
""" 
@File: create_databases.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/27 19:21
"""

from connect_mysql import ConnectMySQL


class CreateDatabases(ConnectMySQL):
    """创建数据表"""

    def __init__(self):
        super(CreateDatabases, self).__init__()
        self.connect = self.mysql()
        self.curous = self.connect.cursor()
        
    def create_tables(self, create_msg):
        """
        创建数据表方法封装
        :param create_msg: 创建数据库的sql语句 
        :return: 
        """
        try:
            self.curous.execute(query=create_msg)
        except Exception as error:
            self.curous.close()
            self.connect.close()
            return error
        self.curous.close()
        self.connect.commit()
        self.connect.close()

    def c_tb_director_info(self):
        sql_msg = "create table if not exists tb_director_info (" \
                     "id int(11) not null primary key auto_increment comment 'id'," \
                     "name varchar(50) not null unique comment '导演姓名'," \
                     "sex int(1) not null comment '导演性别: 0-男, 1-女'," \
                     "introduction varchar(255) comment '导演介绍'," \
                     "link varchar(255) not null comment '导演详情链接'," \
                     "create_time datetime default current_timestamp comment '字段创建时间'," \
                     "modify_time datetime default current_timestamp on update current_timestamp comment '字段修改时间'," \
                     "is_delete boolean default false comment '是否逻辑删除'" \
                     ") charset utf8mb4;"
        self.create_tables(create_msg=sql_msg)
    
    def c_tb_player_info(self):
        sql_msg = "create table if not exists tb_player_info (" \
                  "id int(11) not null primary key auto_increment comment 'id'," \
                  "name varchar(50) not null unique comment '演员姓名'," \
                  "introduction varchar(255) not null comment '演员介绍'," \
                  "link varchar(255) not null comment '演员详情链接'," \
                  "create_time datetime default current_timestamp comment '字段创建时间'," \
                  "modify_time datetime default current_timestamp on update current_timestamp comment '字段修改时间'," \
                  "is_delete boolean default false comment '是否逻辑删除'" \
                  ") charset utf8mb4;"
        self.create_tables(create_msg=sql_msg)
        
    def c_tb_movies_info(self):
        pass
        sql_msg = "create table if not exists tb_movies_info (" \
                  "id int(11) not null primary key auto_increment comment 'id'," \
                  "name varchar(50) not null unique comment '电影名称'," \
                  "director_id int(11) not null comment '导演id'," \
                  "foreign key (director_id) references tb_director_info (id)," \
                  "assistant_director varchar(255) comment '副导演; 多个副导演使用,分隔'," \
                  "screenwriter varchar(255) not null comment '电影编剧; 多个编剧使用,分隔'," \
                  "player_master_id int(11) not null comment '电影主演'," \
                  "foreign key (player_master_id) references tb_player_info (id)," \
                  "player varchar(100) not null comment '电影演员; 多个演员使用,分隔'," \
                  "first_play varchar(10) not null comment '电影首映时间'," \
                  "type varchar(30) not null comment '电影类型; 多个类型使用,分隔'," \
                  "country varchar(10) not null comment '制片国家; 多个国家使用,分隔'," \
                  "length float not null comment '电影时长'," \
                  "introduction varchar(255) default null comment '电影介绍'," \
                  "link varchar(255) not null comment '电影url'," \
                  "create_time datetime default current_timestamp comment '字段创建时间'," \
                  "modify_time datetime default current_timestamp on update current_timestamp comment '字段修改时间'," \
                  "is_delete boolean default false comment '是否逻辑删除'" \
                  ") charset utf8mb4;"
        self.create_tables(create_msg=sql_msg)

if __name__ == '__main__':
    CreateDatabases().c_tb_director_info()
    CreateDatabases().c_tb_player_info()
    CreateDatabases().c_tb_movies_info()



