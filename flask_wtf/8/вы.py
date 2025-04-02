hrom flask import Flask, url_for


app = Flask(__name__)


@app.route('/carousel')
def show_slide():
    url_1 = url_for('static', filename='img/1.png')
    url_2 = url_for('static', filename='img/2.png')
    url_3 = url_for('static', filename='img/3.png')



    html = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" 
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
          crossorigin="anonymous">
    <title>Привет, Яндекс!</title>
  </head>
  <body>
    <div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="{url_1}" class="d-block w-100" alt="Mars Landscape 1">
        </div>
        <div class="carousel-item">
          <img src="{url_2}" class="d-block w-100" alt="Mars Landscape 2">
        </div>
        <div class="carousel-item">
          <img src="{url_3}" class="d-block w-100" alt="Mars Landscape 3">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleSlidesOnly" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleSlidesOnly" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" 
            integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" 
            crossorigin="anonymous"></script>
  </body>
</html>"""

    return html


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
