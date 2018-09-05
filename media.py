import webbrowser

class Video():
    
    def __init__(self,creator, video_description, creator_logo, trailer_youtube_url):
        self.creator = creator
        self.description = video_description
        self.creator_image_url = creator_logo
        self.video_link = trailer_youtube_url

    def show_video(self):
        webbrowser.open(self.video_link)

    def show_logo(self):
        webbrowser.open(self.creator_image_url)
