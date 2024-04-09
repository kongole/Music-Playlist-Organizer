songs = ['Mamou', 'Maby', 'Africa', 'Eau Bénite', 'Mere Superieure', 'Zadio', 'OK Madame', 'Beyanga', 'Lisanga Ya Bambanda', 'Pauline', 'Ebale Ya Zaire', 'Francine', 'Bina na Ngai na Respect', 'Afida Na Ngai', 'Sorozo', 'Francine', 'Monie', 'Mfumbe', 'Liyanzi Ekoti Ngai Na Motema', 'Moziki', 'Nalembi Nalembi', 'Libala Ya Madeleine', 'Pesa Position', 'Editha', 'Echauffement 1 & 2', 'Cielo', 'Merengue', 'Yeba Buana', 'Mimi Et Mimi', 'Pamphile', 'Marie-Josée', 'Kamikaze', 'Lina', 'Fongola', 'La Reine De Sabah', 'Ida', 'Nati Congo', 'Canta Moçambique', 'Dembela', 'BB 69', 'N\'Zoto Souvenir', 'Mokili', 'Mwana Wabi', 'On Entre OK, On Sort KO', 'Mamu', 'Nakomitunaka', 'Sala Keba', 'Doris Iloko', 'Liwa Ya Somo', 'Chouchouna']
playlist = songs
print("Curent Playlsist:", playlist)

playlist_size = len(playlist)
print(playlist_size)

artist = "tpok jazz"
print("Artist:", artist.title())

currently_playing = songs[0].title()
print(f"{'The song currently playing is :'} {currently_playing} by {artist.upper()}")

songs.pop()

songs.append("Mario")
print("Updated Playlist:", songs)



