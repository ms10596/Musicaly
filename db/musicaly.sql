CREATE TABLE IF NOT EXISTS `Artist` (
  `id`      int,
  `name`    VARCHAR,
  `dob`     date,
  `band_id` int,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Song` (
  `id`             int,
  `name`           VARCHAR,
  `release_date`   date,
  `lyrics`         VARCHAR,
  `length`         time,
  `artist_song_id` int,
  `band_song_id`   int,
  `album_id`       int,
  `genre_song_id`  int,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Band` (
  `id`             int,
  `name`           VARCHAR,
  `band_artist_id` int,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Album` (
  `id`            int,
  `title`         VARCHAR,
  `band_id`       int,
  `songs_no`      int,
  `album_song_id` int,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Playlist` (
  `id`               int,
  `name`             VARCHAR,
  `description`      VARCHAR,
  `playlist_song_id` int,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Artist_Song` (
  `id`        int,
  `artist_id` int,
  `song_id`   int,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Genre` (
  `id`   int,
  `Name` VARCHAR,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Band_Song` (
  `id`      int,
  `band_id` int,
  `song_id` int,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Genre_Song` (
  `id`       int,
  `genre_id` int,
  `song_id`  int,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Playlist_Song` (
  `id`          int,
  `playlist_id` int,
  `song_id`     int,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Band_Artist` (
  `id`        int,
  `band_id`   int,
  `artist_id` int,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Album_Song` (
  `id`       int,
  `song_id`  int,
  `album_id` int,
  PRIMARY KEY (`id`)
);
