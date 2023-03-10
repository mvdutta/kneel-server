CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` VARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);
CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carats` DECIMAL(5,2) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);
CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` TEXT NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);
CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL,
    `style_id` INTEGER NOT NULL,
    `timestamp` TIMESTAMP NOT NULL,
    FOREIGN KEY(`metal_id`) REFERENCES `Metals`(`id`),
	FOREIGN KEY(`size_id`) REFERENCES `Sizes`(`id`), 
    FOREIGN KEY(`style_id`) REFERENCES `Styles`(`id`)
);

INSERT INTO `Metals` VALUES (null, "Sterling Silver", 11.50);
INSERT INTO `Metals` VALUES (null, "14K Gold", 250.20);
INSERT INTO `Metals` VALUES (null, "24K Gold", 1258);
INSERT INTO `Metals` VALUES (null, "Platinum", 795.45);
INSERT INTO `Metals` VALUES (null, "Palladium", 1254);

INSERT INTO `Sizes` VALUES (null, 0.5, 405);
INSERT INTO `Sizes` VALUES (null, 0.75, 782);
INSERT INTO `Sizes` VALUES (null, 1, 1470);
INSERT INTO `Sizes` VALUES (null, 1.5, 1997);
INSERT INTO `Sizes` VALUES (null, 2, 3638);

INSERT INTO `Styles` VALUES (null, "Classic", 500);
INSERT INTO `Styles` VALUES (null, "Modern", 710);
INSERT INTO `Styles` VALUES (null, "Vintage", 960);

INSERT INTO `Orders` VALUES (null, 3, 2, 1, "2022-12-05");
INSERT INTO `Orders` VALUES (null, 2, 1, 2, "2022-11-21");
INSERT INTO `Orders` VALUES (null, 4, 4, 3, "2022-11-22");


SELECT
    o.id,
    o.metal_id,
    o.size_id,
    o.style_id,
    o.timestamp
FROM Orders o

SELECT
    o.id,
    o.metal_id,
    o.size_id,
    o.style_id,
    o.timestamp,
    st.style,
    st.price,
    m.metal,
    m.price,
    si.carats,
    si.price
FROM Orders o
JOIN Styles st
    ON o.style_id = st.id
JOIN Metals m
    ON o.metal_id = m.id
JOIN Sizes si
    ON o.size_id = si.id