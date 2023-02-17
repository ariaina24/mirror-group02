import web
from navbar import Navbar
from database import Db

web.config.debug = True

urls = (
    '/', 'index',
    '/artist', 'Artist',
    '/genre', 'Genre',
    '/employee', 'Employee',
    '/invoice', 'Invoice',
    '/album', 'Album',
    '/invoiceLine', 'InvoiceLine',
    '/customer', 'Customer',
    '/playlist', 'Playlist',
    '/playlistTrack', 'PlaylistTrack'
)

class PlaylistTrack:
    def GET(self):
        navbar = Navbar()
        navbar_html = navbar.get_navbar()
        d = Db()
        db = d.getDb()
        a2=db.select('Album', limit=8)
        playlistTrack=db.select('PlaylistTrack', limit=8)
        result = navbar_html
        result += '<div class="container">'
        result += '<table class="table table-striped text-center w-75 m-auto">'
        result += '<thead class="bg-primary text-white">'
        result += '<tr>'
        result += '<th>Playlist Track</th>'
        result += '</tr>'
        result += '</thead>'
        result += '<tbody>'
        for a in a2:
            result += '<tr>'
            for playlist_track in playlistTrack:
                result += '<td>' +playlist.Name+'</td>'
                break
        result += '</tr>'
        result += '</table>'
        result += '</div>'
        result += '</body></html>'
        return result

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
