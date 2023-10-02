SELECT album.Title from Album album
JOIN Artist artist ON album.ArtistId = artist.ArtistId
WHERE artist.Name = 'Marvin Gaye';

SELECT DISTINCT playlist.Name FROM Playlist playlist
JOIN PlaylistTrack playtrack ON playlist.PlaylistId = playtrack.PlaylistId
JOIN Track track ON playtrack.TrackId = track.TrackId
JOIN Genre genre ON track.GenreId = genre.GenreId
WHERE genre.Name = 'Rock';

DROP INDEX [IFK_PlaylistTrackTrackId];
DROP INDEX [IFK_TrackGenreId];

CREATE INDEX playlisttrack_playlist on PlaylistTrack(PlaylistId);
CREATE INDEX playlisttrack_track on PlaylistTrack(TrackId);
CREATE INDEX track_genre on Track(GenreId);
CREATE INDEX genre_name on Genre(Name);