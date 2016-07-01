#from hello import db,Role,User
from app import db,create_app
from app.models import User,Role,Permission


#创建角色和用户
admin_role = Role(name='admin')
mod_role = Role(name='Moderator')
user_role = Role(name='User')
user_john = User(username='john',role=admin_role)
user_susan = User(username='susan',role=mod_role)
user_david = User(username='david',role=user_role)

def createDB():
    '''创建表'''
    app = create_app('default')
    app_context = app.app_context()
    app_context.push()
    db.create_all()

def dropDB():
    '''删除表'''
    db.drop_all()

def insertData():
    '''插入行'''


    '''
    #将对象添加到会话中
    db.session.add_all([admin_role,mod_role,user_role,user_john,user_susan,user_david])
    #提交会话
    db.session.commit()

    db.session.add(admin_role)
    db.session.add(mod_role)
    db.session.add(user_role)
    db.session.add(user_john)
    db.session.add(user_susan)
    db.session.add(user_david)
    '''

def searchData():
   #print(Role.query.all())
   #print(User.query.all())
   print(str(User.query.filter_by(role=user_role).all()))
   #print(User.query.filter_by(role=user_role).all())
   print(str(User.query.filter_by(role=user_role)))
   #user_role1 = Role.query.filter_by(name='User').first()
   #print(user_role1)
   #print(user_role.users)

#createDB()
#dropDB()
#insertData()
#searchData()

roles = {
    'User': (Permission.FOLLOW | Permission.COMMENT | Permission.WRITE_ARTICLES),
    'Moderator': (Permission.FOLLOW | Permission.COMMENT | Permission.WRITE_ARTICLES | Permission.MODERATE_COMMENTS, False),
    'Administrator': (0xff, False)
}

for r in roles:
    print(r)
    role = Role.query.filter_by(name=r).first()
    print(role)