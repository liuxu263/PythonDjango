# coding:utf-8

from ..models.user1 import User


# filter() 过滤查询对象。
# exclude() 排除满足条件的对象
# annotate() 为查询集添加注解或者聚合内容
# order_by() 对查询集进行排序
# reverse() 反向排序
# distinct() 对查询集去重
# values() 返回包含对象具体值的字典的QuerySet
# values_list() 与values()类似，只是返回的是元组而不是字典。
# dates() 根据日期获取查询集
# datetimes() 根据时间获取查询集
# none() 创建空的查询集
# all() 获取所有的对象
# union() 并集
# intersection() 交集
# difference() 差集
# select_related() 附带查询关联对象，利用缓存提高效率
# prefetch_related() 预先查询，提高效率
# defer() 不加载指定字段，也就是排除一些列的数据
# only() 只加载指定的字段，仅选择需要的字段
# using() 选择数据库
# select_for_update() 锁住选择的对象，直到事务结束。
# raw() 接收一个原始的SQL查询
# get() 获取单个对象
# create() 创建对象，无需save()
# get_or_create() 查询对象，如果没有找到就新建对象
# update_or_create() 更新对象，如果没有找到就创建对象
# bulk_create() 批量创建对象
# bulk_update() 批量更新对象
# count() 统计对象的个数
# in_bulk() 根据主键值的列表，批量返回对象
# iterator() 获取包含对象的迭代器
# latest() 获取最近的对象
# earliest() 获取最早的对象
# first() 获取第一个对象
# last() 获取最后一个对象
# aggregate() 聚合操作
# exists() 判断queryset中是否有对象
# update() 更新对象
# delete() 删除对象
# as_manager() 获取管理器
# explain() 对数据库操作的解释性信息

def select():
    """
    :return:class
    """
    # data = User.objects.all()
    # data = User.objects.get(username='lx001')
    # data = User.objects.get(pk=1)
    # data = User.objects.filter(id=1)
    # return data
    pass


def insert():
    """
    :return:class / None
    """
    # mode1
    # data = User.objects.create(user_id='00000004',
    #                            password='123123',
    #                            username='lx005',
    #                            email='1308460167@qq.com',
    #                            create_time='1625105410000')
    # return data
    # mode2
    # User(user_id='00000008',
    #      password='123123',
    #      username='lx008',
    #      email='1308460167@qq.com',
    #      create_time='1625105410000').save()
    pass


def update():
    """
    :return:None / int
    """
    # mode1
    # user = User.objects.get(username='lx002')
    # user.username = 'lx009'
    # user.save()
    # mode2
    # data = User.objects.filter(username='lx004').update(username='lx005')
    # return data
    pass


def delete():
    """
    :return:tuple
    """
    # mode1
    # data = User.objects.get(id=102).delete()
    # mode2
    # data = User.objects.filter(id=103).delete(
    # return data
    pass
