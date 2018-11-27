-- SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS `Artist`;
DROP TABLE IF EXISTS `Song`;
DROP TABLE IF EXISTS `Band`;
DROP TABLE IF EXISTS `Album`;
DROP TABLE IF EXISTS `Playlist`;
DROP TABLE IF EXISTS `Artist_Song`;
DROP TABLE IF EXISTS `Genre`;
DROP TABLE IF EXISTS `Band_Song`;
DROP TABLE IF EXISTS `Genre_Song`;
DROP TABLE IF EXISTS `Playlist_Song`;
DROP TABLE IF EXISTS `Band_Artist`;
DROP TABLE IF EXISTS `Album_Song`;
-- SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE `Artist` (
  `id`      int,
  `name`    text,
  `dob`     date,
  `band_id` int,
  PRIMARY KEY (`id`)
);

CREATE TABLE `Song` (
  `id`             int,
  `name`           text,
  `release_date`   date,
  `lyrics`         text,
  `length`         time,
  `artist_song_id` int,
  `band_song_id`   int,
  `album_id`       int,
  `genre_song_id`  int,
  PRIMARY KEY (`id`)
);

CREATE TABLE `Band` (
  `id`             int,
  `name`           text,
  `band_artist_id` int,
  PRIMARY KEY (`id`)
);

CREATE TABLE `Album` (
  `id`            int,
  `title`         text,
  `band_id`       int,
  `songs_no`      int,
  `album_song_id` int,
  PRIMARY KEY (`id`)
);

CREATE TABLE `Playlist` (
  `id`               int,
  `name`             text,
  `description`      text,
  `playlist_song_id` int,
  PRIMARY KEY (`id`)
);

CREATE TABLE `Artist_Song` (
  `id`        int,
  `artist_id` int,
  `song_id`   int,
  PRIMARY KEY (`id`)
);

CREATE TABLE `Genre` (
  `id`   int,
  `Name` text,
  PRIMARY KEY (`id`)
);

CREATE TABLE `Band_Song` (
  `id`      int,
  `band_id` int,
  `song_id` int,
  PRIMARY KEY (`id`)
);

CREATE TABLE `Genre_Song` (
  `id`       int,
  `genre_id` int,
  `song_id`  int,
  PRIMARY KEY (`id`)
);

CREATE TABLE `Playlist_Song` (
  `id`          int,
  `playlist_id` int,
  `song_id`     int,
  PRIMARY KEY (`id`)
);

CREATE TABLE `Band_Artist` (
  `id`        int,
  `band_id`   int,
  `artist_id` int,
  PRIMARY KEY (`id`)
);

CREATE TABLE `Album_Song` (
  `id`       int,
  `song_id`  int,
  `album_id` int,
  PRIMARY KEY (`id`)
);
