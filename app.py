from flask import Flask, render_template, request

app = Flask(__name__)

# List of videos stored with names and Google Drive URLs
videos = [
    { "name": "Hunter Vantar", "url": "https://drive.google.com/file/d/1gAcd5hBQ7a4a38tS27dZgGb3FfQQ-RtX/view?usp=sharing" },
    { "name": "Manasilaayo", "url": "https://drive.google.com/file/d/1qOg6uXqv9gf0bYF6xPwsEbk8vrFDJT2A/view?usp=sharing" },
    { "name": "Matta", "url": "https://drive.google.com/file/d/1eO37gKELn4lFPiHfX1qhVDtRtc7rbrB0/view?usp=sharing" },
    { "name": "Spark", "url": "https://drive.google.com/file/d/1el6WCVtGxDBCKD5tHPJB1TpthbxIANPD/view?usp=sharing" }
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['video_name'].lower()

    # Find the video based on the search query
    found_video = next((video for video in videos if search_query in video["name"].lower()), None)

    if found_video:
        # Modify the Google Drive link to allow embedding
        embed_url = found_video["url"].replace("/view", "/preview")
        return render_template('index.html', video_url=embed_url, video_name=found_video["name"])
    else:
        return render_template('index.html', error="Video Not Found !")


if __name__ == '__main__':
    app.run(debug=True)
