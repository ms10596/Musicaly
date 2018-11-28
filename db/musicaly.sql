CREATE TABLE IF NOT EXISTS `Artist` (
  `id`      int AUTO_INCREMENT,
  `name`    VARCHAR,
  `dob`     date,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Song` (
  `id`             int AUTO_INCREMENT,
  `name`           VARCHAR,
  `release_date`   date,
  `lyrics`         VARCHAR,
  `length`         time,
  `album`          VARCHAR,
  `artist_id`      int,
  `artist_type`    VARCHAR,
  `ft_id`          int,
  `ft_type`        VARCHAR,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Band` (
  `id`             int AUTO_INCREMENT,
  `name`           VARCHAR,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Album` (
  `id`            int AUTO_INCREMENT,
  `title`         VARCHAR,
  `songs_no`      int,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Playlist` (
  `id`               int AUTO_INCREMENT,
  `name`             VARCHAR,
  `description`      VARCHAR,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Genre` (
  `id`   int AUTO_INCREMENT,
  `Name` VARCHAR,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Genre_Song` (
  `id`       int AUTO_INCREMENT,
  `genre_id` int,
  `song_id`  int,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Playlist_Song` (
  `id`          int AUTO_INCREMENT,
  `playlist_id` int,
  `song_id`     int,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Band_Artist` (
  `id`        int AUTO_INCREMENT,
  `band_id`   int,
  `artist_id` int,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Album_Song` (
  `id`       int AUTO_INCREMENT,
  `song_id`  int,
  `album_id` int,
  PRIMARY KEY (`id`)
);
