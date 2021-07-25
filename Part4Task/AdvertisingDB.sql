create table advertiser_db
(
	id integer
		constraint advertiser_db_pk
			primary key autoincrement,
	name varchar(50) not null,
	views integer default 0 check ( views >= 0 ),
	clicks integer default 0 check ( clicks >= 0 )
);


create unique index advertiser_db_id_uindex
	on advertiser_db (id);


create table ad_db
(
    id integer
        constraint ad_db_pk
            primary key autoincrement,
    title varchar(50) not null,
    img_url varchar(50) not null,
    link text not null,
    advertiser_id integer references advertiser_db(id),
    views integer default 0 check ( views >= 0 ),
    clicks integer default 0 check ( clicks >= 0 )
);

create unique index ad_db_id_uindex
    on ad_db(id);


-- test db
insert into advertiser_db(name) VALUES ("name1");
insert into advertiser_db(name) VALUES ("name2");
insert into ad_db(title, img_url, link, advertiser_id) VALUES ("title1", "img-url1", "link1", 1);
insert into ad_db(title, img_url, link, advertiser_id) VALUES ("title2", "img-url2", "link2", 2);

