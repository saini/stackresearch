'''
Created on Feb 21, 2013

@author: vaibhavsaini
'''
from sqlalchemy.schema import Column, Sequence
from sqlalchemy.types import *
from Base import *

class Post(Base):
    '''
    classdocs
    '''
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    postTypeId = Column(Integer)
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
    
    def getVars(self):
        return vars(self)
    
    def __repr__(self):
        return "<Post (%d)>" % (self.id)

class Tag_Post_Map(Base):
    __tablename__ = 'tag_post_map2'
    id = Column(Integer, Sequence('tag_post_map_id_seq') ,primary_key=True)
    post_id = Column(Integer)
    postTypeId = Column(Integer)
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


class Tag_Post_Answer(Base):
    __tablename__ = 'tag_post_answer_map'
    id = Column(Integer, Sequence('tag_post_map_id_seq') ,primary_key=True)
    post_id = Column(Integer)
    postTypeId = Column(Integer)
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
    a_parentId = Column(Integer)
    a_creationDate = Column(DateTime)
    a_score = Column(Integer)
    a_viewCount = Column(Integer)
    a_body = Column(Text)
    a_ownerUserId = Column(Integer)
    a_OwnerDisplayName = Column(String)
    a_LastEditorUserId = Column(Integer)
    a_LastEditDate = Column(DateTime)
    a_LastEditorDisplayName = Column(String)
    a_LastActivityDate = Column(DateTime)
    a_Title = Column(String)
    a_CommentCount = Column(Integer)
    a_FavouriteCount = Column(Integer)
    a_ClosedDate = Column(DateTime)
    a_CommunityOwnedDate = Column(DateTime)


class Dummy (Base):
    __tablename__ = 'abc'
    id= Column (Integer, Sequence('dummy_id_seq'),primary_key=True)
    name = Column (String(50))
    score = Column(Integer)


class Dummy2 (Base):
    __tablename__ = 'pqr'
    id= Column (Integer, Sequence('dummy_id_seq'),primary_key=True)
    dumId = Column(Integer)
    name = Column (String(50))
    score = Column(Integer)
    