#!/usr/bin/python3
import database
import logger

print(logger.star(),logger.level(0),logger.sep(),logger.msg('Database Creation'),end='\r')
try:
    database.initDB()
    print(logger.tick(),logger.level(1),logger.sep(),logger.msg('Database Creation'),end='\n')
except:
    print(logger.cross(),logger.level(2),logger.sep(),logger.msg('Database Creation'),end='\n')