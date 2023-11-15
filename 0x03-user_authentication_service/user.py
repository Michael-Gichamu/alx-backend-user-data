#!/usr/bin/env python3
"""
Contains SQLAlchemy model User for database table users.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base() 


class User(Base):
    """
    Defines Attributes for Column of users
    table

    Args:
        Base (class): derivatives to describe the actual database.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
