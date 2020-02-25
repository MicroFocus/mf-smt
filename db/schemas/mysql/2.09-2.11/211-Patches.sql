ALTER TABLE Patches MODIFY COLUMN DESCRIPTION  VARCHAR(1024) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL;
ALTER TABLE Clients MODIFY COLUMN NAMESPACE  VARCHAR(300) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '';
ALTER TABLE Clients MODIFY COLUMN  DESCRIPTION  VARCHAR(500) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '';
ALTER TABLE Patches MODIFY COLUMN  SUMMARY  VARCHAR(512) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL;
ALTER TABLE PatchRefs MODIFY COLUMN TITLE VARCHAR(256) CHARACTER SET utf8 COLLATE utf8_general_ci;

