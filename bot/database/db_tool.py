from math import isnan

from . import get_session

from .unit_of_work import AlchemyUnitOfWork


class DBTool:
    session = get_session()
    uow = AlchemyUnitOfWork(session)


    @classmethod
    def get(cls, *args, **kwargs):
        """Get first by args and kwargs"""
        return cls.session.query(cls).filter(*args).filter_by(**kwargs).first()


    @classmethod
    def filter(cls, *args, **kwargs):
        """Filter all by args and kwargs"""
        return cls.session.query(cls).filter(*args).filter_by(**kwargs).all()


    @classmethod
    def all(cls):
        """Returns all objs"""
        return cls.session.query(cls).all()


    @classmethod
    def len(cls):
        return cls.session.query(cls).count()


    @classmethod
    def new(cls, **kwargs):
        """Creates new row in DB"""
        with cls.uow:
            new = cls(**kwargs)

            cls.uow.session.add(new)

            cls.uow.commit()

            cls.uow.session.refresh(new)
            cls.uow.session.expunge(new)
        
            return new


    def save(self):
        """Update self"""
        self.session.commit()


    @classmethod
    def delete_first(cls, **kwargs):
        """Delete first by kwargs"""
        with cls.uow as u:
            obj = cls.session.query(cls).filter_by(**kwargs).first()
            cls.session.delete(obj)
            cls.session.commit()

    
    def delete(self):
        """Delete self"""
        self.session.delete(self)
        self.session.commit()


    @classmethod
    def delete_all(cls, **kwargs):
        """Delete all by kwargs"""
        with cls.uow as u:
            u.session.query(cls).filter_by(**kwargs).delete()
            u.commit()


    def as_dict(self):
        """Returns self info as dist"""
        return {c.name: getattr(self, c.name) if not (isinstance(getattr(self, c.name), float) and isnan(getattr(self, c.name))) else None for c in self.__table__.columns}
