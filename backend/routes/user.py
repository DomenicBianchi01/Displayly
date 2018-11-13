import falcon
import mysql.connector

class UserRoutes(object):
	def on_get(self, req, res):
		res.status = falcon.HTTP_200  # This is the default status
		res.body = ('This is me, Falcon, serving a resource!')
		mydb.close()

	def on_post_register(self, req, res):
		if 'username' not in req.params or 'password' not in req.params or 'question' not in req.params or 'answer' not in req.params:
			res.body = '{"error":"Username, password, security question and answer are required."}'
			res.status = falcon.HTTP_400
		else:
			db = mysql.connector.connect(host="localhost", user="root", password="de5ign", port="3306")
			cursor = db.cursor()
			sql = "INSERT INTO Users (Email, Password, SecurityQuestion, SecurityAnswer) VALUES (%s, %s, %s, %s)"
			cursor.execute(sql, (req.params['username'], req.params['password'], req.params['question'], req.params['answer']))
			db.commit()
			res.status = falcon.HTTP_200

	def on_post_login(self, req, res):
		res.status = falcon.HTTP_200
