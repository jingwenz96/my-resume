from flask_script import Manager
from resume import app, db, Professor, Course

manager = Manager(app)

@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    professor1 = Professor(name='Wang,Jiannan', department='MISY')
    professor2 = Professor(name='Sharma,Pratyush Nidhi', department='MISY')
    professor3 = Professor(name='White,Matthew N', department='ECON')
    professor4 = Professor(name='Spotts,Robert Earl', department='MISY')
    course1 = Course(number="MISY330",title='Database Design and Implementation', description='Covers the design and implementation of enterprise databases in the business environment. A networked setting and its effect on database management will be emphasized', professor=professor2)
    course2 = Course(number="MISY350",title='Business Application Development II', description='Covers concepts related to client side development, including cascading style sheets and JavaScript.', professor=professor1)
    course3 = Course(number="ECON301",title='Quantitative Microeconomic Theory', description='Uses calculus to study price determination and income distribution in a market economy; and the behavior of firms and industry under conditions of pure and imperfect competition.',professor=professor3)
    course4 = Course(number="MISY225",title='Introduction to Programming Business Applications', description='Use of higher level contemporary computing languages to structure Prototyping applications of systems.',professor=professor4)
    db.session.add(professor1)
    db.session.add(professor2)
    db.session.add(professor3)
    db.session.add(professor4)
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.add(course4)
    db.session.commit()

if __name__ == "__main__":
    manager.run()
