CREATE TABLE "Works"(
    "work_id" VARCHAR(10) PRIMARY KEY NOT NULL,
    "title" NVARCHAR(255) NOT NULL,
    "director" NVARCHAR(100) NOT NULL,
    "type" NVARCHAR(15) NOT NULL,
    "year" SMALLINT NOT NULL,
    "genre_1" NVARCHAR(30) NOT NULL,
    "genre_2" NVARCHAR(30),
    "genre_3" NVARCHAR(30),
);

CREATE TABLE "Quotes"(
    "quote_id" INT PRIMARY KEY IDENTITY(1,1), -- IDENTITY(1,1) IS SAME AS AUTOINCREMENT
    "quote" NVARCHAR(500) NOT NULL,
    "character" NVARCHAR(100) NOT NULL,
    "season" SMALLINT,
    "episode" SMALLINT,
    "timestamp" TIME NOT NULL,
    "work_id" VARCHAR(10) NOT NULL
    FOREIGN KEY("work_id") REFERENCES "Works"("work_id") ON DELETE CASCADE
);