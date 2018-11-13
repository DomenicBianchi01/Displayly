import falcon
import json
import bcrypt
import mysql.connector

class UserRoutes(object):
	def on_get(self, req, res):
		res.status = falcon.HTTP_200  # This is the default status
		res.body = ('This is me, Falcon, serving a resource!')
		mydb.close()

	def on_post_register(self, req, res):
		raw_json = req.bounded_stream.read()
		data = raw_json.decode('utf8').replace("'", '"')
		body = json.loads(data)
		if 'username' not in body or 'password' not in body or 'question' not in body or 'answer' not in body:
			res.body = '{"error":"Username, password, security question and answer are required."}'
			res.status = falcon.HTTP_400
		else:
			db = mysql.connector.connect(host="localhost", user="root", password="de5ign", port="3306", db="displayly")
			cursor = db.cursor()
			sql = "INSERT INTO Users (Email, Password, SecurityQuestion, SecurityAnswer) VALUES (%s, %s, %s, %s)"
			hashedPassword = bcrypt.hashpw(body['password'], bcrypt.gensalt())
			hashedQuestion = bcrypt.hashpw(body['answer'], bcrypt.gensalt())
			hashedAnswer = bcrypt.hashpw(body['answer'], bcrypt.gensalt())
			cursor.execute(sql, (body['username'], hashedPassword, hashedQuestion, hashedAnswer))
			db.commit()
			res.status = falcon.HTTP_200

	def on_post_login(self, req, res):
		res.status = falcon.HTTP_200
