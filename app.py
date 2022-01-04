import google_searcher2 as gs
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/analyze')
def sentiment():
	if request.method == 'GET':
		term = request.args.get('term')
		analysis = gs.Analysis(term)
		analysis.run()
		return jsonify({"Term": term, "Sentiment": analysis.sentiment, "Subjectivity": analysis.subjectivity})
	else:
		return('USE GET REQUEST PLZ')

if __name__ == '__main__':
	app.run(debug=True)
