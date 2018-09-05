import media
import fresh_tomatoes

fix_this_build_that = media.Video("Brad Rodriguez",
                              "Fix This Build That Woodworking Workshop Tour - Jan 2018",
                              "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                              "https://youtu.be/mquWDnCbysc")

wood_whisperer = media.Video("Mark Spagnolo",
                              "2017 Wood Whisperer Shop Tour",
                              "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                              "https://youtu.be/48qxudcYPrU")

jay_bates = media.Video("Jay Bates",
                              "2 Car Garage Woodshop - Shop Tour 2015",
                              "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                              "https://youtu.be/lxdVJl3nmXo")

frank_howarth = media.Video("Frank Howarth",
                              "The Woodshop Tour",
                              "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                              "https://youtu.be/XmDAInbnPYQ")

april_wilkerson = media.Video("April Wilkerson",
                              "2016 Shop Tour",
                              "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                              "https://youtu.be/_5YjjUbyKnU")

crafted_workshop = media.Video("Johnny Brooke",
                              "Shop Tour 2018, All of My Woodworking and Metalworking Tools!",
                              "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                              "https://youtu.be/wsV4xfxjehs")

aryVideos = [fix_this_build_that,wood_whisperer,jay_bates,frank_howarth,april_wilkerson,crafted_workshop]

fresh_tomatoes.open_movies_page(aryVideos)

