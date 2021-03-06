import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" type="text/css" href="css/main.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style>
        body {
            background: url('bg2.jpg') no-repeat;
            background-size:cover;
            
            
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
            transition: all 0.5s linear;
            color:#F0F5C1;
            
        }
        .movie-tile img{
            border: 2px solid white;
	    box-shadow: 3px 3px hsla(38,67%,0%,0.3);
	    -webkit-transition: all 120ms ease-out;
            -moz-transition: all 120ms ease-out;
            -o-transition: all 120ms ease-out;
            -ms-transition: all 120ms ease-out;
            transition: all 120ms ease-out;    
        }
        .movie-tile h4 {
            letter-spacing:2px;
        }
        .movie-tile:hover {
            -moz-transform: scale(1.25);
            -o-transform: scale(1.25);
            -webkit-transform: scale(1.25);
            transform: scale(1.25);
            cursor: pointer;
        }
        .heading {
            padding-top:20px;
            padding-bottom:20px;
            
            text-alignment:center;
            
        }
        .heading a{
            font-size:25px;
            font-family:Arial;
            letter-spacing:8px;
            text-decoration:none;
            text-transform: uppercase;
            color:#F0F5C1;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        footer {
            margin-top:50px;
            padding: 6px 0px;
            background-color:rgba(0, 0, 0,0.2);
        }
        .rights {color:white;}
        .disclaimer {color:white;}
        .my-footer{
            font-size:10px;
        }

    
    </style>
    
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Main Page Content -->
    <div class="container-fluid text-center">
        <div class="heading">
            <a href="#">Fresh Tomatoes Movie Trailers</a>
        </div>
    </div>
    <div class="container">
        {movie_tiles}
    </div>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <footer class="my-footer">
        <div class="container content text-center">
            <div class="rights">copyright &copy; 2018 Ramesh Vegoti</div>
            <div class="rights">licensed under <a href="http://creativecommons.org/licenses/by/4.0/" target="_blank">CC BY 4.0</a></div>
            <div class="rights">background image by <a href="https://www.shutterstock.com" target="_blank">shutterstock</a>, licensed under <a href="http://creativecommons.org/licenses/by-nc-sa/2.0/deed.en" target="_blank">CC BY-NC-SA 2.0</a></div>
            <div>&bull; &bull; &bull;</div>
            <div class="disclaimer">All webpages appearing in this work are fictitious and for demostration purposes only. Any resemblance to real websites, living or dead, is purely coincidental.</div>
        </div>  
    </footer>
    
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-3 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="175" height="275">
    <h4>{movie_title}</h4>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=1) # open in a new tab, if possible
