CREATE TABLE user (
    username varchar(64) PRIMARY KEY,
    password varchar(64) NOT NULL,
    email varchar(256),
    fname varchar(64),
    lname varchar(64),
    bio varchar(1000),
    gender varchar(16)
);

CREATE TABLE channel (
    name varchar(64) PRIMARY KEY,
    chiefadmin varchar(64) NOT NULL,
    FOREIGN KEY (chiefadmin) REFERENCES user(username)
);

CREATE TABLE pmbox (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    user1 varchar(64) NOT NULL,
    user2 varchar(64) NOT NULL,
    FOREIGN KEY (user1) REFERENCES user(username),
    FOREIGN KEY (user2) REFERENCES user(username)
);

CREATE TABLE message (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    text varchar(1000),
    channel varchar(64) NOT NULL,
    timestamp varchar(32) NOT NULL,
    sender varchar(64) NOT NULL,
    FOREIGN KEY (channel) REFERENCES channel(name),
    FOREIGN KEY (sender) REFERENCES user(username)
);

CREATE TABLE private_message (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    text varchar(1000),
    pmbox int NOT NULL,
    timestamp varchar(32) NOT NULL,
    sender varchar(64) NOT NULL,
    FOREIGN KEY (pmbox) REFERENCES pmbox(id),
    FOREIGN KEY (sender) REFERENCES user(username)
);

CREATE TABLE subscribers (
    username varchar(64) PRIMARY KEY,
    channelname varchar(64) NOT NULL,
    FOREIGN KEY (username) REFERENCES user(username),
    FOREIGN KEY (channelname) REFERENCES channel(name)
);

CREATE TABLE admin (
    username varchar(64) PRIMARY KEY,
    channelname varchar(64) NOT NULL,
    FOREIGN KEY (username) REFERENCES user(username),
    FOREIGN KEY (channelname) REFERENCES channel(name)
);

CREATE TABLE blacklist (
    username varchar(64) PRIMARY KEY,
    channelname varchar(64) NOT NULL,
    expiretime varchar(32),
    FOREIGN KEY (username) REFERENCES user(username),
    FOREIGN KEY (channelname) REFERENCES channel(name)
);