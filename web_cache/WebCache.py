from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, and_, update, Table

Base = declarative_base()

class WebCache():
    def __init__(self,cache_db="cache.db"):
        self.engine = create_engine('sqlite:///' + cache_db, echo=False)
        Base.metadata.create_all(self.engine)
        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()

    def add_page(self,url,source):
        if (self.get_page(url) == None):
            page = CachedPage(url=url,source=source)
            self.session.add(page)
            self.session.commit()

    def get_page(self,url):
        page = self.session.query(CachedPage).filter(CachedPage.url.like(url)).first()
        return page

class CachedPage(Base):
    __tablename__ = 'cached_page'
    id = Column(Integer, primary_key=True)
    url = Column(String(250), nullable=False)
    source = Column(String(convert_unicode=True), nullable=False)