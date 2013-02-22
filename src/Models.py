'''
Created on Feb 21, 2013

@author: vaibhavsaini
'''
from sqlalchemy.schema import Column, Sequence
from sqlalchemy.types import *
import Base

class Post(Base):
    '''
    classdocs
    '''
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    acceptedAnswerId = Column(Integer)
    parentId = Column(Integer),
    creationDate = Column(DateTime)
    score = Column(Integer)
    viewCount = Column(Integer)
    body = Column(Text)
    ownerUserId = Column(Integer)
    ownerDisplayName = Column(String(100)) 
    lastEditorUserId = Column(Integer)
    lastEditorDisplayName = Column(String(100))
    lastEditDate = Column(DateTime)
    lastActivityDate = Column(DateTime)
    title = Column(String(2000))
    tags = Column(String(100))
    answerCount = Column(Integer)
    commentCount = Column(Integer)
    favouriteCount = Column(Integer)
    closedDate = Column(DateTime)
    communityOwnedDate = Column(DateTime)

class Tag_Post_Map(Base):
    __tablename__ = 'tag_post_map'
    id = Column(Integer, Sequence('tag_post_map_id_seq') ,primary_key=True)
    post_id = Column(Integer)
    tag = Column(String(50))
    acceptedAnswerId = Column(Integer)
    parentId = Column(Integer),
    creationDate = Column(DateTime)
    score = Column(Integer)
    viewCount = Column(Integer)
    body = Column(Text)
    ownerUserId = Column(Integer)
    ownerDisplayName = Column(String(100)) 
    lastEditorUserId = Column(Integer)
    lastEditorDisplayName = Column(String(100))
    lastEditDate = Column(DateTime)
    lastActivityDate = Column(DateTime)
    title = Column(String(2000))
    tags = Column(String(100))
    answerCount = Column(Integer)
    commentCount = Column(Integer)
    favouriteCount = Column(Integer)
    closedDate = Column(DateTime)
    communityOwnedDate = Column(DateTime)
    java = Column(Boolean)
    python= Column(Boolean)
    cSharp = Column(Boolean)
    cPP = Column(Boolean)
    php = Column(Boolean)
    c = Column(Boolean)
    ruby = Column(Boolean)
    ruby_on_rails = Column(Boolean)
    javascript = Column(Boolean)
    jquery = Column(Boolean)
    asp_dot_net = Column(Boolean)
    objective_c = Column(Boolean)
    sql = Column(Boolean)
    xml = Column(Boolean)
    perl = Column(Boolean)
    cocoa = Column(Boolean)
    delphi = Column(Boolean)
    node_dot_js = Column(Boolean)
    scala = Column(Boolean)
    visual_cPP = Column(Boolean)
    