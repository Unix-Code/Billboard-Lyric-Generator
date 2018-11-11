from app import app
from flask import render_template, flash, redirect, url_for, request
from app.forms import Params



curVideoData = []*5
thread = Thread()
curVideoData = None
temp = None
user = None

@app.route('/')
def index():
    eventlet.monkey_patch()
    global curVideoData, thread
    form = Params()

    if curVideoData:
        return render_template('theonlyhtmlfileweneed.html', title='Song Flong', form=form, videoData=curVideoData[1:])
    else:
        temp = [VideoData(None, title="Call Me Maybe", final='static/demo/video1.mp4', artist='Carly Rae Jepsen', art='https://upload.wikimedia.org/wikipedia/en/thumb/a/ad/Carly_Rae_Jepsen_-_Call_Me_Maybe.png/220px-Carly_Rae_Jepsen_-_Call_Me_Maybe.png'),
        VideoData(None, title="Harder", final='static/demo/video2.mp4', artist='Tiesto & Amp', art='https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Ti%C3%ABsto_and_KSHMR_Harder.jpg/220px-Ti%C3%ABsto_and_KSHMR_Harder.jpg'),
        VideoData(None, title="Hot N Cold", final='static/demo/video3.mp4', artist='Katy Perry', art='https://upload.wikimedia.org/wikipedia/en/thumb/b/b9/Hot_N_Cold_%28Official_Single_Cover%29_by_Katy_Perry.png/220px-Hot_N_Cold_%28Official_Single_Cover%29_by_Katy_Perry.png'),
        VideoData(None, title="On The Floor", final='static/demo/video4.mp4', artist='Jennifer Lopez Feat. Pitbull', art='https://upload.wikimedia.org/wikipedia/en/thumb/9/91/On_the_Floor.png/220px-On_the_Floor.png'),
        VideoData(None, title="Sexy And I Know It", final='static/demo/video5.mp4', artist='LMFAO', art='https://upload.wikimedia.org/wikipedia/en/thumb/7/76/Sexy_and_I_Know_It_-_Single.png/220px-Sexy_and_I_Know_It_-_Single.png'),
        VideoData(None, title="placeholder", final='static/demo/video6.mp4', artist='placeholder', art=None)]
        return render_template('theonlyhtmlfileweneed.html', title='Song Flong', form=form, videoData=temp)

def ack():
    print('message was received!')

def remove_temp(user):
	parent = os.getcwd() + "\\app\\static\\" + user.uuid
	output = os.getcwd() + "\\app\\static\\" + user.uuid + "\\output"
	temp = os.getcwd() + "\\app\\static\\" + user.uuid + "\\tmp"
	for filename in os.listdir(output):
		os.remove(filename)
	for filename in os.listdir(temp):
		os.remove(filename)
	os.rmdir(temp)
	os.rmdir(output)
	os.rmdir(parent)

@socketio.on('connect', namespace='/test')
def test_connect():
        global user
        user = User(request.sid)
        emit('connection made', {'msg': 'connected'})
	

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
	global user
	remove_temp(user)

@socketio.on('send search', namespace='/test')
def test_message(message):
	emit('data created',{'msg': 'ready'}, callback=ack)
	global user
	user.ytURL = message['data']
	print(user.uuid)
	print(user.ytURL)
	global temp
	#print(message['data']);
	payload = []
	thread = Search(user)
	thread.start()
	thread.join()
	#print(user)
	#print(user.data)
	for file in user.data:
		#print(file)
		data = {
			'title': file.title,
			'file': file.final,
			'art': file.art,
			'artist': file.artist
		}
		payload.append(data)
	temp = payload

@socketio.on('get data', namespace='/test')
def get_data():
	global temp, user
	print('done')
	emit('send data', {'content': temp}, room=user.sid)