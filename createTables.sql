drop table if exists public.badge;
create table public.badge(id varchar(255) not null primary key, guest_id varchar(255) not null, guest_firstname varchar(255) not null, guest_lastname varchar(255) not null,
        guest_company varchar(255), host_firstname varchar(255) not null, host_lastname varchar(255) not null, badge_status varchar(255), badge_url varchar(255), creation_date timestamp not null, picture_url varchar(255));
drop table if exists public.packagingreviews;
create table public.packagingreviews(
            id varchar(255) not null primary key, 
            ParticipantName varchar(255) not null, 
            ParticipantEmail varchar(255) not null, 
            BrandEvaluated varchar(255) not null,
            GripReview varchar(255), 
            PlugReview varchar(255) not null, 
            PortabilityReview varchar(255) not null, 
            Freetext varchar(255), 
            image_url varchar(255), 
            creation_date timestamp not null) ;
