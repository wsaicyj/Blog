from hello import db,Role,User


#创建角色和用户
admin_role = Role(name='admin')
mod_role = Role(name='Moderator')
user_role = Role(name='User')
user_john = User(username='john',role=admin_role)
user_susan = User(username='susan',role=mod_role)
user_david = User(username='david',role=user_role)

def createDB():
    db.create_all()

def insertData():
    '''插入行'''


    #将对象添加到会话中
    db.session.add_all([admin_role,mod_role,user_role,user_john,user_susan,user_david])
    #提交会话
    db.session.commit()
    '''
    db.session.add(admin_role)
    db.session.add(mod_role)
    db.session.add(user_role)
    db.session.add(user_john)
    db.session.add(user_susan)
    db.session.add(user_david)
    '''

def searchData():
   print(Role.query.all())
   print(User.query.all())
   #print(User.query.filter_by(role=user_role).all())
   print(str(User.query.filter_by(role=user_role)))

#insertData()
searchData()

