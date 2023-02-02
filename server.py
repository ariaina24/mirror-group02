import web
web.config.debug = True

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        db = web.database(
            dbn='mysql',
            host='tmp-insi.rktmb.org',
            port=3306,
            user='insigroup00',
            pw='insigroup00',
            db='project00',
        )
        a2=db.select('Album', limit=10)
        a3=db.select('Artist', limit=10)
        grs=db.select('Genre', limit=10)
        cstm=db.select('Customer', limit=10)
        playList=db.select('Playlist', limit=10)
        employe=db.select('Employee', limit=10)
        result = '<html><head><title>test</title>'
        result += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">'
        result += '</head>'
        result += '<table class="container table table-border" border= "1">'
        result += '<tr class="bg-primary text-white text-center"><th>Id Artist</th><th>Artists</th><th>Genres</th><th>Customer</th><th>Employee</th><th>Playlists</th><th>Albums</th></tr>'
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
            for playlist in playList:
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
