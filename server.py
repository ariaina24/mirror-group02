import web
from database import Db

web.config.debug = False

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        d = Db()
        db = d.getDb()
        a2=db.select('Album', limit=8)
        a3=db.select('Artist', limit=8)
        grs=db.select('Genre', limit=8)
        cstm=db.select('Customer', limit=8)
        playList=db.select('Playlist', limit=8)
        employe=db.select('Employee', limit=8)
        invc=db.select('Invoice', limit=8)
        invcline=db.select('InvoiceLine', limit=8)
        mdtype=db.select('MediaType', limit=8)
        playlistTrack=db.select('PlaylistTrack', limit=8)
        track=db.select('Track', limit=8)
        result = '<html><head><title>Test Groupe 02</title>'
        result += '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">'
        result += '</head>'
        result += '<nav class="navbar navbar-expand-lg navbar-light bg-light rounded " >'
        result += '<div class="container-fluid justify-content-md-center">'
        result += '<ul class="navbar-nav">'
        result += '<li class="nav-item"><a class="nav-link active" aria-current="page" href="#">Home</a></li>'
        result += '<li class="nav-item"><a class="nav-link" aria-current="page" href="#">Album</a></li>'
        result += '<li class="nav-item"><a class="nav-link" href="#">Artist</a></li>'
        result += '<li class="nav-item"><a class="nav-link" href="#">Liste de genre</a></li>'
        result += '<li class="nav-item"><a class="nav-link" href="#">Employee</a></li>'
        result += '<li class="nav-item"><a class="nav-link" href="#">Invoice</a></li>'
        result += '<li class="nav-item"><a class="nav-link" href="#">InvoiceLine</a></li>'
        result += '<li class="nav-item"><a class="nav-link" href="#">MediaType</a></li>'
        result += '<li class="nav-item"><a class="nav-link" href="#">Playlist</a></li>'
        result += '</ul>'
        result += '</div>'
        result += '</nav>'
        result += '<table class="container-fluid table table-border" border= "1">'
        result += '<tr class="bg-primary text-white text-center"><th>Id Artist</th><th>Artists</th><th>Genres</th><th>Customer</th><th>Employee</th><th>Invoice</th><th>InvoiceLine</th><th>MediaType</th><th>Playlists</th><th>Playlists Tracks</th><th>Albums</th></tr>'
        for a in a2:
            result += '<tr>'
            for artist in a3:
                result += '<td class="bg-dark text-white text-center">' + str(a.ArtistId) + '</td>'
                result += '<td>' +artist.Name+'</td>' 
                break 
            for genre in grs:
                result += '<td>' +genre.Name+'</td>'
                break
            for customer in cstm:
                result += '<td>' +customer.FirstName+'</td>' 
                break
            for employee in employe:
                result += '<td>' +employee.LastName+'</td>'
                break
            for invoice in invc:
                result += '<td>' +invoice.BillingCity+'</td>' 
                break
            for invoiceLine in invcline:
                result += '<td>' +invoice.BillingCity+'</td>' 
                break
            for MediaType in mdtype:
                result += '<td>' +MediaType.Name+'</td>' 
                break
            for playlist in playList:
                result += '<td>' +playlist.Name+'</td>'
                break
            for playlist_track in playlistTrack:
                result += '<td>' +playlist.Name+'</td>'
                break
            result += '<td>' +a.Title+'</td>'
            result += '</tr>'
        result += '</table>'
        result += '</body></html>'
        return result

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
